// Copyright 2013 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// Message definition file, included multiple times, hence no include guard.

#include "base/strings/string16.h"
#include "content/common/service_worker_types.h"
#include "ipc/ipc_message_macros.h"
#include "ipc/ipc_param_traits.h"
#include "third_party/WebKit/public/platform/WebServiceWorkerError.h"
#include "url/gurl.h"

IPC_STRUCT_TRAITS_BEGIN(content::ServiceWorkerFetchRequest)
  IPC_STRUCT_TRAITS_MEMBER(url)
  IPC_STRUCT_TRAITS_MEMBER(method)
  IPC_STRUCT_TRAITS_MEMBER(headers)
IPC_STRUCT_TRAITS_END()

#undef IPC_MESSAGE_EXPORT
#define IPC_MESSAGE_EXPORT CONTENT_EXPORT

#define IPC_MESSAGE_START ServiceWorkerMsgStart

IPC_ENUM_TRAITS(blink::WebServiceWorkerError::ErrorType)

// Messages sent from the child process to the browser.

IPC_MESSAGE_CONTROL4(ServiceWorkerHostMsg_RegisterServiceWorker,
                     int32 /* thread_id */,
                     int32 /* request_id */,
                     GURL /* scope */,
                     GURL /* script_url */)

IPC_MESSAGE_CONTROL3(ServiceWorkerHostMsg_UnregisterServiceWorker,
                     int32 /* thread_id */,
                     int32 /* request_id */,
                     GURL /* scope (url pattern) */)

// Messages sent from the browser to the child process.

// Response to ServiceWorkerMsg_RegisterServiceWorker
IPC_MESSAGE_CONTROL3(ServiceWorkerMsg_ServiceWorkerRegistered,
                     int32 /* thread_id */,
                     int32 /* request_id */,
                     int64 /* service_worker_id */)

// Response to ServiceWorkerMsg_UnregisterServiceWorker
IPC_MESSAGE_CONTROL2(ServiceWorkerMsg_ServiceWorkerUnregistered,
                     int32 /* thread_id */,
                     int32 /* request_id */)

// Sent when any kind of registration error occurs during a
// RegisterServiceWorker / UnregisterServiceWorker handler above.
IPC_MESSAGE_CONTROL4(ServiceWorkerMsg_ServiceWorkerRegistrationError,
                     int32 /* thread_id */,
                     int32 /* request_id */,
                     blink::WebServiceWorkerError::ErrorType /* code */,
                     base::string16 /* message */)

// Informs the browser of a new ServiceWorkerProvider in the child process,
// |provider_id| is unique within its child process.
IPC_MESSAGE_CONTROL1(ServiceWorkerHostMsg_ProviderCreated,
                     int /* provider_id */)

// Informs the browser of a ServiceWorkerProvider being destroyed.
IPC_MESSAGE_CONTROL1(ServiceWorkerHostMsg_ProviderDestroyed,
                     int /* provider_id */)

// For EmbeddedWorker related messages -------------------------------------

// Browser -> Renderer message to create a new embedded worker context.
IPC_MESSAGE_CONTROL3(EmbeddedWorkerMsg_StartWorker,
                     int /* embedded_worker_id */,
                     int64 /* service_worker_version_id */,
                     GURL /* script_url */)

// Browser -> Renderer message to stop (terminate) the embedded worker.
IPC_MESSAGE_CONTROL1(EmbeddedWorkerMsg_StopWorker,
                     int /* embedded_worker_id */)

// Renderer -> Browser message to indicate that the worker is started.
IPC_MESSAGE_CONTROL2(EmbeddedWorkerHostMsg_WorkerStarted,
                     int /* thread_id */,
                     int /* embedded_worker_id */)

// Renderer -> Browser message to indicate that the worker is stopped.
IPC_MESSAGE_CONTROL1(EmbeddedWorkerHostMsg_WorkerStopped,
                     int /* embedded_worker_id */)

// ---------------------------------------------------------------------------
// For EmbeddedWorkerContext related messages, which are directly sent from
// browser to the worker thread in the child process. We use a new message class
// for this for easier cross-thread message dispatching.

#undef IPC_MESSAGE_START
#define IPC_MESSAGE_START EmbeddedWorkerContextMsgStart

IPC_MESSAGE_CONTROL3(EmbeddedWorkerContextMsg_FetchEvent,
                     int /* thread_id */,
                     int /* embedded_worker_id */,
                     content::ServiceWorkerFetchRequest)
