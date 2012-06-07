// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "base/win/scoped_handle.h"

#include <map>
#include <set>

#include "base/debug/alias.h"
#include "base/lazy_instance.h"
#include "base/synchronization/lock.h"
#include "base/win/windows_version.h"

namespace {

struct Info {
  const void* owner;
  const void* pc1;
  const void* pc2;
  DWORD thread_id;
};
typedef std::map<HANDLE, Info> HandleMap;

base::LazyInstance<HandleMap>::Leaky g_handle_map = LAZY_INSTANCE_INITIALIZER;
base::LazyInstance<std::set<const void*> >::Leaky g_owner_set =
    LAZY_INSTANCE_INITIALIZER;
base::LazyInstance<base::Lock>::Leaky g_lock = LAZY_INSTANCE_INITIALIZER;

}  // namespace

namespace base {
namespace win {

// Static.
void VerifierTraits::StartTracking(HANDLE handle, const void* owner,
                                   const void* pc1, const void* pc2) {
  if (OSInfo::GetInstance()->version() > VERSION_XP)
    return;

  // Grab the thread id before the lock.
  DWORD thread_id = GetCurrentThreadId();

  AutoLock lock(g_lock.Get());

  if (handle == INVALID_HANDLE_VALUE) {
    // Cannot track this handle.
    g_owner_set.Get().insert(owner);
    return;
  }

  Info handle_info = { owner, pc1, pc2, thread_id };
  std::pair<HANDLE, Info> item(handle, handle_info);
  std::pair<HandleMap::iterator, bool> result = g_handle_map.Get().insert(item);
  if (!result.second) {
    Info other = result.first->second;
    debug::Alias(&other);
    CHECK(false);
  }
}

// Static.
void VerifierTraits::StopTracking(HANDLE handle, const void* owner,
                                  const void* pc1, const void* pc2) {
  if (OSInfo::GetInstance()->version() > VERSION_XP)
    return;

  AutoLock lock(g_lock.Get());
  HandleMap::iterator i = g_handle_map.Get().find(handle);
  if (i == g_handle_map.Get().end()) {
    std::set<const void*>::iterator j = g_owner_set.Get().find(owner);
    if (j != g_owner_set.Get().end()) {
      g_owner_set.Get().erase(j);
      return;
    }
    CHECK(false);
  }

  Info other = i->second;
  if (other.owner != owner) {
    debug::Alias(&other);
    CHECK(false);
  }

  g_handle_map.Get().erase(i);
}

}  // namespace win
}  // namespace base
