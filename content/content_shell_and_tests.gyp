# Copyright 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    'chromium_code': 1,  # Use higher warning level.
  },
  'target_defaults': {
    'conditions': [
      # TODO(jschuh): Remove this after crbug.com/173851 gets fixed.
      ['OS=="win" and target_arch=="x64"', {
        'msvs_settings': {
          'VCCLCompilerTool': {
            'AdditionalOptions': ['/bigobj'],
          },
        },
      }],
    ],
  },
  'targets': [
    {
      'target_name': 'test_support_content_tmp',
      'type': 'static_library',
      'dependencies': [
        '../net/net.gyp:net_test_support',
        '../skia/skia.gyp:skia',
        '../testing/gmock.gyp:gmock',
        '../testing/gtest.gyp:gtest',
        '../ui/events/events.gyp:events',
        '../ui/gfx/gfx.gyp:gfx',
        '../ui/ui.gyp:keycode_converter',
        '../ui/ui.gyp:ui',
        '../ui/ui.gyp:ui_resources',
        '../ui/ui.gyp:ui_test_support',
        '../url/url.gyp:url_lib',
        'content.gyp:content_app_both',
        'content.gyp:content_browser',
        'content.gyp:content_common',
      ],
      'include_dirs': [
        '..',
      ],
      'sources': [
        'public/test/browser_test_base.cc',
        'public/test/browser_test_base.h',
        'public/test/browser_test.h',
        'public/test/browser_test_utils.cc',
        'public/test/browser_test_utils.h',
        'public/test/content_test_suite_base.cc',
        'public/test/content_test_suite_base.h',
        'public/test/download_test_observer.cc',
        'public/test/download_test_observer.h',
        'public/test/fake_speech_recognition_manager.cc',
        'public/test/fake_speech_recognition_manager.h',
        'public/test/js_injection_ready_observer.h',
        'public/test/layouttest_support.h',
        'public/test/mock_download_item.cc',
        'public/test/mock_download_item.h',
        'public/test/mock_download_manager.cc',
        'public/test/mock_download_manager.h',
        'public/test/mock_notification_observer.cc',
        'public/test/mock_notification_observer.h',
        'public/test/mock_render_process_host.cc',
        'public/test/mock_render_process_host.h',
        'public/test/mock_render_thread.cc',
        'public/test/mock_render_thread.h',
        'public/test/mock_resource_context.cc',
        'public/test/mock_resource_context.h',
        'public/test/nested_message_pump_android.cc',
        'public/test/nested_message_pump_android.h',
        'public/test/render_view_fake_resources_test.cc',
        'public/test/render_view_fake_resources_test.h',
        'public/test/render_view_test.cc',
        'public/test/render_view_test.h',
        'public/test/render_widget_test.cc',
        'public/test/render_widget_test.h',
        'public/test/sandbox_file_system_test_helper.cc',
        'public/test/sandbox_file_system_test_helper.h',
        'public/test/test_browser_context.cc',
        'public/test/test_browser_context.h',
        'public/test/test_browser_thread.cc',
        'public/test/test_browser_thread.h',
        'public/test/test_browser_thread_bundle.cc',
        'public/test/test_browser_thread_bundle.h',
        'public/test/test_content_client_initializer.cc',
        'public/test/test_content_client_initializer.h',
        'public/test/test_file_error_injector.cc',
        'public/test/test_file_error_injector.h',
        'public/test/test_file_system_backend.cc',
        'public/test/test_file_system_backend.h',
        'public/test/test_file_system_context.cc',
        'public/test/test_file_system_context.h',
        'public/test/test_file_system_options.cc',
        'public/test/test_file_system_options.h',
        'public/test/test_launcher.cc',
        'public/test/test_launcher.h',
        'public/test/test_navigation_observer.cc',
        'public/test/test_navigation_observer.h',
        'public/test/test_notification_tracker.cc',
        'public/test/test_notification_tracker.h',
        'public/test/test_renderer_host.cc',
        'public/test/test_renderer_host.h',
        'public/test/test_utils.cc',
        'public/test/test_utils.h',
        'public/test/unittest_test_suite.cc',
        'public/test/unittest_test_suite.h',
        'public/test/web_contents_tester.cc',
        'public/test/web_contents_tester.h',
        'app/startup_helper_win.cc',
        # TODO(phajdan.jr): All of those files should live in content/test (if
        # they're only used by content) or content/public/test (if they're used
        # by other embedders).
        'browser/download/mock_download_file.cc',
        'browser/download/mock_download_file.h',
        'browser/geolocation/fake_access_token_store.cc',
        'browser/geolocation/fake_access_token_store.h',
        'browser/geolocation/mock_location_arbitrator.cc',
        'browser/geolocation/mock_location_arbitrator.h',
        'browser/geolocation/mock_location_provider.cc',
        'browser/geolocation/mock_location_provider.h',
        'browser/renderer_host/compositing_iosurface_shader_programs_mac.cc',
        'browser/renderer_host/compositing_iosurface_shader_programs_mac.h',
        'browser/renderer_host/compositing_iosurface_transformer_mac.cc',
        'browser/renderer_host/compositing_iosurface_transformer_mac.h',
        'browser/renderer_host/media/mock_media_observer.cc',
        'browser/renderer_host/media/mock_media_observer.h',
        'browser/renderer_host/test_backing_store.cc',
        'browser/renderer_host/test_backing_store.h',
        'browser/renderer_host/test_render_view_host.cc',
        'browser/renderer_host/test_render_view_host.h',
        'gpu/gpu_idirect3d9_mock_win.cc',
        'gpu/gpu_idirect3d9_mock_win.h',
        'test/content_test_suite.cc',
        'test/content_test_suite.h',
        'test/layouttest_support.cc',
        'test/mock_keyboard.cc',
        'test/mock_keyboard.h',
        'test/mock_keyboard_driver_win.cc',
        'test/mock_keyboard_driver_win.h',
        'test/mock_render_process.cc',
        'test/mock_render_process.h',
        'test/mock_webclipboard_impl.cc',
        'test/mock_webclipboard_impl.h',
        'test/mock_webframeclient.h',
        'test/mock_weburlloader.cc',
        'test/mock_weburlloader.h',
        'test/net/url_request_abort_on_end_job.cc',
        'test/net/url_request_abort_on_end_job.h',
        'test/net/url_request_failed_job.cc',
        'test/net/url_request_failed_job.h',
        'test/net/url_request_mock_http_job.cc',
        'test/net/url_request_mock_http_job.h',
        'test/net/url_request_prepackaged_interceptor.cc',
        'test/net/url_request_prepackaged_interceptor.h',
        'test/net/url_request_slow_download_job.cc',
        'test/net/url_request_slow_download_job.h',
        'test/ppapi_unittest.cc',
        'test/ppapi_unittest.h',
        'test/test_content_browser_client.cc',
        'test/test_content_browser_client.h',
        'test/test_content_client.cc',
        'test/test_content_client.h',
        'test/test_media_stream_client.cc',
        'test/test_media_stream_client.h',
        'test/test_render_view_host_factory.cc',
        'test/test_render_view_host_factory.h',
        'test/test_video_frame_provider.cc',
        'test/test_video_frame_provider.h',
        'test/test_web_contents.cc',
        'test/test_web_contents.h',
        'test/test_web_contents_view.cc',
        'test/test_web_contents_view.h',
        'test/test_webkit_platform_support.cc',
        'test/test_webkit_platform_support.h',
        'test/web_gesture_curve_mock.cc',
        'test/web_gesture_curve_mock.h',
        'test/web_layer_tree_view_impl_for_testing.cc',
        'test/web_layer_tree_view_impl_for_testing.h',
        'test/webkit_support.cc',
        'test/webkit_support.h',
        'test/webkit_support_glue.cc',
        'test/weburl_loader_mock.cc',
        'test/weburl_loader_mock.h',
        'test/weburl_loader_mock_factory.cc',
        'test/weburl_loader_mock_factory.h',

        # TODO(phajdan.jr): Those files should be moved to webkit
        # test support target.
        '../webkit/browser/appcache/appcache_test_helper.cc',
        '../webkit/browser/appcache/appcache_test_helper.h',
      ],
      'conditions': [
        ['OS == "ios"', {
          'sources/': [
            # iOS only needs a small portion of content; exclude all the
            # implementation, and re-include what is used.
            ['exclude', '\\.(cc|mm)$'],
            ['include', '_ios\\.(cc|mm)$'],
            ['include', '^public/test/content_test_suite_base\\.cc$'],
            ['include', '^public/test/mock_notification_observer\\.cc$'],
            ['include', '^public/test/mock_resource_context\\.cc$'],
            ['include', '^public/test/test_browser_thread\\.cc$'],
            ['include', '^public/test/test_content_client_initializer\\.cc$'],
            ['include', '^public/test/test_notification_tracker\\.cc$'],
            ['include', '^public/test/test_utils\\.cc$'],
            ['include', '^public/test/unittest_test_suite\\.cc$'],
            ['include', '^test/content_test_suite\\.cc$'],
            ['include', '^test/test_content_browser_client\\.cc$'],
            ['include', '^test/test_content_client\\.cc$'],
          ],
        }, {  # OS != "ios"
          'conditions': [
            ['OS=="mac"', {
              'copies': [{
                'destination': '<(SHARED_INTERMEDIATE_DIR)/webkit',
                'files': [
                  'shell/resources/missingImage.png',
                  'shell/resources/textAreaResizeCorner.png',
                ],
              }],
            }],
          ],
          'dependencies': [
            'content.gyp:content_child',
            'content.gyp:content_gpu',
            'content.gyp:content_ppapi_plugin',
            'content.gyp:content_renderer',
            'content.gyp:content_utility',
            'content.gyp:content_worker',
            '../media/media.gyp:media',
            '../ppapi/ppapi_internal.gyp:ppapi_host',
            '../ppapi/ppapi_internal.gyp:ppapi_proxy',
            '../ppapi/ppapi_internal.gyp:ppapi_shared',
            '../ppapi/ppapi_internal.gyp:ppapi_unittest_shared',
            '../third_party/WebKit/public/blink.gyp:blink',
            '../third_party/WebKit/public/blink_test_runner.gyp:blink_test_runner',
            '../ui/surface/surface.gyp:surface',
            '../webkit/common/gpu/webkit_gpu.gyp:webkit_gpu',
            '../webkit/common/user_agent/webkit_user_agent.gyp:user_agent',
            '../webkit/glue/webkit_glue.gyp:glue',
            '../webkit/glue/webkit_glue.gyp:glue_child',
            '../webkit/renderer/compositor_bindings/compositor_bindings.gyp:webkit_compositor_support',
            '../webkit/renderer/webkit_renderer.gyp:webkit_renderer',
            '../webkit/storage_browser.gyp:webkit_storage_browser',
            '../webkit/storage_common.gyp:webkit_storage_common',
          ],
        }],
        ['OS == "win" or toolkit_uses_gtk == 1', {
          'dependencies': [
            '../sandbox/sandbox.gyp:sandbox',
          ],
        }],
        ['enable_webrtc==1', {
          'sources': [
            'renderer/media/mock_media_stream_dependency_factory.cc',
            'renderer/media/mock_media_stream_dependency_factory.h',
            'renderer/media/mock_media_stream_dispatcher.cc',
            'renderer/media/mock_media_stream_dispatcher.h',
            'renderer/media/mock_media_stream_registry.cc',
            'renderer/media/mock_media_stream_registry.h',
            'renderer/media/mock_peer_connection_impl.cc',
            'renderer/media/mock_peer_connection_impl.h',
            'renderer/media/mock_web_rtc_peer_connection_handler_client.cc',
            'renderer/media/mock_web_rtc_peer_connection_handler_client.h',
            'test/webrtc_audio_device_test.cc',
            'test/webrtc_audio_device_test.h',
          ],
          'dependencies': [
            '../third_party/libjingle/libjingle.gyp:libjingle_webrtc',
            '../third_party/libjingle/libjingle.gyp:libpeerconnection',
            '../third_party/webrtc/modules/modules.gyp:audio_device',
            '../third_party/webrtc/modules/modules.gyp:video_capture_module',
          ],
        }],
        ['toolkit_uses_gtk == 1', {
          'dependencies': [
            '../build/linux/system.gyp:gtk',
          ],
        }],
        ['use_glib == 1', {
          'dependencies': [
            '../build/linux/system.gyp:glib',
          ],
        }],
        ['use_aura==1', {
          'dependencies': [
            '../ui/aura/aura.gyp:aura_test_support',
            '../ui/compositor/compositor.gyp:compositor',
          ],
        }],
        ['OS=="win"', {
          'dependencies': [
            '../third_party/iaccessible2/iaccessible2.gyp:iaccessible2',
          ],
        }],
        ['OS!="android" and OS!="ios"', {
          'dependencies': [
            '../third_party/libvpx/libvpx.gyp:libvpx',
          ],
        }],
        ['OS=="android"', {
          'dependencies': [
            '../ui/ui.gyp:shell_dialogs',
            'test_support_content_jni_headers_tmp',
          ],
        }],
      ],
    },
  ],
  'conditions': [
    ['OS!="ios"', {
      'targets': [
        {
          'target_name': 'content_webkit_unit_test_support_tmp',
          'type': 'static_library',
          'dependencies': [
            'test_support_content_tmp',
          ],
          'include_dirs': [
            '..',
          ],
          'sources': [
            'test/webkit_unit_test_support.cc',
            'test/webkit_unit_test_support.h',
          ],
        },
      ],
    }],
    ['OS == "android"', {
      'targets': [
        {
          'target_name': 'test_support_content_jni_headers_tmp',
          'type': 'none',
          'sources': [
            'public/test/android/javatests/src/org/chromium/content/browser/test/NestedSystemMessageHandler.java',
          ],
          'direct_dependent_settings': {
            'include_dirs': [
              '<(SHARED_INTERMEDIATE_DIR)/content/public/test',
            ],
          },
          'variables': {
            'jni_gen_package': 'content/public/test',
          },
          'includes': [ '../build/jni_generator.gypi' ],
        },
      ],
    }],
  ],
}
