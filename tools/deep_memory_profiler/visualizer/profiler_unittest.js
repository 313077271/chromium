// Copyright 2013 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

/**
 * Test whether given model is valid.
 * @param {Object} model
 * @return {boolean} Model is valid or not.
 */
var modelIsValid = function(model) {
  // Model object must contain 'name' and 'id'.
  if (!('name' in model) || !('id' in model))
   return false;

  // Model object cant contain 'children' and 'size' together.
  if ('children' in model && 'size' in model ||
    !('children' in model) && !('size' in model))
    return false;

  // Model object must contain 'subs' and 'template' both or neither.
  if ('subs' in model && !('template' in model) ||
    !('subs' in model) && 'template' in model)
    return false;

  // If model contains children, every child also must be valid.
  if ('children' in model) {
    return model.children.reduce(function(previous, current) {
      return previous && modelIsValid(current);
    }, true);
  }

  return true;
};

// Test title format is file-name:function-name.
test('profiler:parseTemplate_', function() {
  stop();
  $.getJSON('data/sample.json', function(data) {
    start();
    var profiler = new Profiler(data);
    var models = profiler.parseTemplate_();
    equal(models.length, data.snapshots.length);
    models.forEach(function(model) {
      ok(modelIsValid(model));
    });
    inspect(models, 'models generated by profile:\n');
  });
});
