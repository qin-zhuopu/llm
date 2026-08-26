# Source: https://ataru.qidian.com/noah/125876280

> 抓取日期: 2026-08-26

---

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=no, viewport-fit=cover">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="format-detection" content="telephone=no">
    <meta http-equiv="Cache-Control" content="no-store"/>
    <meta http-equiv="Pragma" content="no-cache"/>
    <meta http-equiv="Expires" content="0"/>
    <script>
        var _nativeDispatchEvent = window.dispatchEvent.bind(window);

        // 起点客户端通知 WebView：当前是否为悬浮窗口（支持 add/removeEventListener 监听）
        window.QD_WEBVIEW_FLOATING_WINDOW_CHANGE_EVENT = 'qd:webview-floating-window-change';
        window.__qd_floating_window__ = false;

        function _createQdCustomEvent(eventName, detail) {
          if (typeof window.CustomEvent === 'function') {
            return new window.CustomEvent(eventName, { detail: detail });
          }
          var event = document.createEvent('CustomEvent');
          event.initCustomEvent(eventName, false, false, detail);
          return event;
        }

        function _toBoolean(val) {
          return val === 1 || val === '1' || val === true || val === 'true';
        }

        // 客户端调用：window.setFloatingWindow(value)
        // value 仅支持 1 / '1' / true / 'true' 视为 true，其余视为 false
        window.setFloatingWindow = function (value) {
          var isFloatingWindow = _toBoolean(value);
          var detail = {
            isFloatingWindow: isFloatingWindow,
            timestamp: Date.now(),
            source: 'qidian-client',
          };

          window.__qd_floating_window__ = isFloatingWindow;

          _nativeDispatchEvent(
            _createQdCustomEvent(window.QD_WEBVIEW_FLOATING_WINDOW_CHANGE_EVENT, detail)
          );
        };

        window.addEventListener(window.QD_WEBVIEW_FLOATING_WINDOW_CHANGE_EVENT, function (e) {
          console.log('QD_WEBVIEW_FLOATING_WINDOW_CHANGE_EVENT', e.detail.isFloatingWindow);
          window.__qd_floating_window__ = e.detail.isFloatingWindow;
        }, { once: true })

        function _getQuery(str){
          return new URLSearchParams(window.location.search).get(str) || '0';
        }

        function _toggleDarkMode(theme){
          if (theme === '2') {
            document.documentElement.classList.add('dark-mode')
          } else {
            document.documentElement.classList.remove('dark-mode')
          }
        }

        function _getTheme(val) {
          var theme = '1' // 1 为日间模式， 2 为夜间模式
          if (val) {
            theme = val
          } else {
            var qdBg = _getQuery('_qdbg')
            if (qdBg !== '0') {
              theme = qdBg
            } else {
              theme = navigator.userAgent.indexOf('QDNightStyle_2') > -1 ? '2' : '1'
            }
          }
          return theme
        }

        function _isDarkTheme() {
          return document.documentElement.classList.contains('dark-mode')
        }

        function _initDarkMode() {
          var theme = _getTheme()
          _toggleDarkMode(theme)
        }

        _initDarkMode()

        // 给客户端调用的方法
        window.qdSetTheme = function qdSetTheme(val) {
          if (_getQuery('_isappbg') === '1') return;
          console.log('qdSetTheme', val)
          var themeValue = "" + val;
          var url = new URL(window.location.href);
          url.searchParams.set('_qdbg', themeValue);
          window.history.replaceState(null, '', url.toString());

          // 自定义逻辑
          if (window._onQdSetTheme && typeof window._onQdSetTheme === 'function') {
            window._onQdSetTheme(themeValue)
          } else {
            window.location.reload();
          }
        }
    </script>
    <link rel="preload" href="https://webfontsource.yuewen.com/api/v1/yfont/font.ttf?base64=0&font=YuewenFont-Regular&text=1234567890" as="font" type="font/ttf" crossorigin>
    <style>
      @charset "UTF-8";
      @font-face {
        font-family: Yuewen Font;
        font-display: swap;
        src: url("https://webfontsource.yuewen.com/api/v1/yfont/font.ttf?base64=0&font=YuewenFont-Regular&text=1234567890");
      }
    </style>
    
      <link rel="preconnect" href="https://noah2-1252317822.file.myqcloud.com"></link>
    
      <link rel="preconnect" href="https://qidian.gtimg.com"></link>
    
      <link rel="preconnect" href="https://noahqd.yuewen.com"></link>
    
    
        <title>角逐IP之光</title>
    
      
      <link rel="preload" as="script" href="//noah2-1252317822.file.myqcloud.com/npm/@noah-nqd/site-config@2.5.3/dist/index.js"></link>
    
    
      
        
        <link rel="preload" as="script" href="//noah2-1252317822.file.myqcloud.com/npm/@noah-nqd/task-v2@0.2.10/dist/index.js"></link>
      
        
        <link rel="preload" as="script" href="//noah2-1252317822.file.myqcloud.com/npm/@noah-common/guide-download@0.0.54/dist/index.js"></link>
      
        
        <link rel="preload" as="script" href="//noah2-1252317822.file.myqcloud.com/npm/@noah-nqd/img-handler@0.1.9/dist/index.js"></link>
      
        
        <link rel="preload" as="script" href="//noah2-1252317822.file.myqcloud.com/npm/@noah-common/top-prompt@0.0.23/dist/index.js"></link>
      
        
        <link rel="preload" as="script" href="//noah2-1252317822.file.myqcloud.com/npm/@noah-nqd/task-v2@0.2.10/dist/index.js"></link>
      
        
        <link rel="preload" as="script" href="//noah2-1252317822.file.myqcloud.com/npm/@noah-nqd/navbar-viewmode@0.0.25/dist/index.js"></link>
      
        
        <link rel="preload" as="script" href="//noah2-1252317822.file.myqcloud.com/npm/@noah-nqd/task-v2@0.2.10/dist/index.js"></link>
      
        
        <link rel="preload" as="script" href="//noah2-1252317822.file.myqcloud.com/npm/@noah-nqd/task-v2@0.2.10/dist/index.js"></link>
      
        
        <link rel="preload" as="script" href="//noah2-1252317822.file.myqcloud.com/npm/@noah-nqd/widget-hotspot@0.0.2/dist/index.js"></link>
      
        
        <link rel="preload" as="script" href="//noah2-1252317822.file.myqcloud.com/npm/@noah-nqd/template-2025-yw10@0.3.1/dist/index.js"></link>
      
        
        <link rel="preload" as="script" href="//noah2-1252317822.file.myqcloud.com/npm/@noah-common/nested-time@0.0.12/dist/index.js"></link>
      
        
        <link rel="preload" as="script" href="//noah2-1252317822.file.myqcloud.com/npm/@noah-nqd/nqd-logo-box@0.0.14/dist/index.js"></link>
      
        
        <link rel="preload" as="script" href="//noah2-1252317822.file.myqcloud.com/npm/@noah-nqd/plugin-app@0.1.1/dist/index.js"></link>
      
        
        <link rel="preload" as="script" href="//noah2-1252317822.file.myqcloud.com/npm/@noah-common/share@0.9.1/dist/index.js"></link>
      
        
        <link rel="preload" as="script" href="//noah2-1252317822.file.myqcloud.com/npm/@noah-nqd/yfont@0.0.18/dist/index.js"></link>
      
        
        <link rel="preload" as="script" href="//noah2-1252317822.file.myqcloud.com/npm/@noah-common/style@0.4.2/dist/index.js"></link>
      
    
    <!-- tam -->

    
    <style>
      .v-spinner {
        width: 48px;
        height: 48px;
        border: 5px solid currentColor;
        border-bottom-color: transparent;
        border-radius: 50%;
        display: inline-block;
        box-sizing: border-box;
        animation: s-rotation 0.6s linear infinite;
      }
      @keyframes s-rotation {
        0% {transform: rotate(0deg);}
        100% {transform: rotate(360deg);}
      }
    </style>
  <link href="https://yuxstacdn.yuewen.com/noah/css/noah.7c3e9629.css" rel="stylesheet"></head>
  <!--tam report -->
  
    <script>
      
        
          window.__GALILEO_ID__ = 'SDK-d50db4bf681711a544c7'
        
        
        
        
        
      
    </script>
  
  <body id="body">
    <noscript>We're sorry but noah doesn't work properly without JavaScript enabled. Please enable it to continue.</noscript>
    
      <script>
        // 使用函数包裹， 避免全局变量污染
        function qdSiteInit() {
          var query = new URLSearchParams(window.location.search);
          var errorQuery = query.get("error") || '';
          var isInApp = /qdreader/i.test(navigator.userAgent);
          if (!isInApp) return;
          var androidVersion = '7.9.450'
          var androidVersionCode = '1827'
          var iosVersion = '5.9.450'
          var iosVersionCode = '721'
          
          if (/harmonyos/i.test(navigator.userAgent)) {
            // 鸿蒙系统的UA里包含harmonyos字段， 但目前鸿蒙系统的版本较低， 不支持jsbridge， 先直接过滤掉
            return;
          }

          // ios ua UA: Mozilla/5.0 (iPhone; CPU iPhone OS 18_6_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/QDReaderiOS/5.9.442/715/QDReaderAppstore/QDNightStyle_2/QDShowNativeLoading/getTabHeight_92
          // android UA: UA: Mozilla/5.0 (Linux; Android 16; 25019PNF3C Build/BP2A.250605.031.A3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/145.0.7632.79 Mobile Safari/537.36 QDJSSDK/1.0  QDNightStyle_1  QDReaderAndroid/7.9.446/1806/1002140/Xiaomi/getTabHeight_89

          function compareVersion(v1, v2) {
            var arr1 = v1.split('.');
            var arr2 = v2.split('.');
            var len = Math.max(arr1.length, arr2.length);
            for (var i = 0; i < len; i++) {
              var num1 = parseInt(arr1[i]) || 0;
              var num2 = parseInt(arr2[i]) || 0;
              if (num1 !== num2) return num1 - num2;
            }
            return 0;
          }

          var ua = navigator.userAgent;
          var match = ua.match(/(QDReaderAndroid|QDReaderiOS)\/([\d\.]+)\/(\d+)/);
          if (!match) return;
          
          var platform = match[1];
          var currentVersion = match[2];
          var currentVersionCode = parseInt(match[3]);
          var requiredVersion = platform === 'QDReaderAndroid' ? androidVersion : iosVersion;
          var requiredVersionCode = parseInt(platform === 'QDReaderAndroid' ? androidVersionCode : iosVersionCode);
          var verDiff = compareVersion(currentVersion, requiredVersion);
          
          if (verDiff < 0 || (verDiff === 0 && currentVersionCode < requiredVersionCode)) {
            return;
          }

          var errorActionURL = "QDReader://app/showWebViewErrorView";
          var hideLoading = "QDReader://app/hiddenWebViewLoading";
          var decodedQuery;
          try {
            decodedQuery = decodeURIComponent(errorQuery);
          } catch (e) {
            decodedQuery = errorQuery;
          }
          var errorActionWithQuery =
            errorActionURL +
            (errorQuery
              ? "?query=" + encodeURIComponent(decodedQuery)
              : "");
          var timeout = 15000; // 弱网超时时长（ms），超时后调用客户端错误视图
          var callJSBridge = function (actionURL) {
            var iframe = document.createElement("iframe");
            iframe.style.display = "none";
            iframe.src = actionURL;
            document.body.appendChild(iframe);
            setTimeout(function () {
              document.body.removeChild(iframe);
            }, 100);
          };
          window.__call_js_bridge__ = callJSBridge;
          window.__error_action_with_query__ = errorActionWithQuery;

          callJSBridge(hideLoading);
          window.__qd_timeout_error_timer__ = setTimeout(function () {
            callJSBridge(errorActionWithQuery);
          }, timeout);
        }

        try {
          qdSiteInit();
        } catch (e) {
          console.error('调用客户端接口失败', e);
        }
      </script>
    
    <div id="app"></div>
    <!-- built files will be auto injected -->
    <script>
      window.__init_data__ = { siteId: 16384, siteName: "nqd", ajaxApi: "/act/noah/index", staticUrl: "noah2-1252317822.file.myqcloud.com", env: "ol", query: {} };
      window.staticDomain = "https://yuxstacdn.yuewen.com/noah/";
      
        window.__noah_ajax_resp={"code":0,"data":{"actConf":{"actId":125876280,"activityStatus":0,"basePopupInfo":[{"popTitle":"敬请期待","disable":true,"closeButton":"我知道了","active":false,"popDesc":"活动还未开始哦～","status":true,"scene":"活动未开始"},{"popTitle":"你来晚啦","disable":true,"closeButton":"我知道了","active":false,"popDesc":"下次再来参加活动吧～","status":true,"scene":"活动已结束"},{"popTitle":"提示","disable":true,"closeButton":"我知道了","active":false,"popDesc":"换个姿势，再试一次？","status":true,"scene":"请求数据失败"},{"popTitle":"换个姿势","disable":false,"closeButton":"去参加","active":false,"popDesc":"去APP参加活动吧","status":true,"scene":"站外引导"},{"popTitle":"提示","disable":true,"closeButton":"立即升级","active":false,"popDesc":"当前版本不支持哦~","status":true,"scene":"版本升级提示"}],"baseToastStyle":{"btn":{"borderColor":"#000","bgColor":"#E5353E","color":"#fff","borderRadius":200,"borderWidth":0,"angel":0},"base":{"maskColor":"rgba(0,0,0,.75)","textColor":"rgba(0,0,0,.65)"}},"conf":{"hidePublishButton":false,"desktopAdapt":false,"retainPopup":{"imgUrl":"\u002F\u002Fbossaudioandcomic-1252317822.image.myqcloud.com\u002Factivity\u002Fdocument\u002F8919de199c988b28b349325cffe90f1d.png","rightText":"继续留下","visible":0,"leftText":"狠心离开","title":"弹窗标题","content":"弹窗描述文案，说明当前状态；至多不超过两行。"},"offlineConfig":{"act":{"harmony":"","isActionComponentsAppOnly":true,"btnText":"去活动中心","useBackground":0,"backgroundImage":"","android":"","linkType":0,"text":"活动已下线，去看看别的活动","ios":"","textColor":"#BCBCBC","url":"QDReader:\u002F\u002Fapp\u002Factscenter?query={\"tabId\":0,\"tagId\":0}"},"pages":[{"harmony":"","isActionComponentsAppOnly":true,"btnText":"去活动中心","useBackground":0,"backgroundImage":"","android":"","followActConfig":true,"ios":"","pageId":30501,"pagePath":"index","textColor":"#BCBCBC","pageName":"阅文十周年","url":"QDReader:\u002F\u002Fapp\u002Factscenter?query={\"tabId\":0,\"tagId\":0}","linkType":0,"text":"活动已下线，去看看别的活动","isPage":true},{"harmony":"","isActionComponentsAppOnly":true,"btnText":"去活动中心","useBackground":0,"backgroundImage":"","android":"","followActConfig":true,"ios":"","pageId":30995,"pagePath":"role","textColor":"#BCBCBC","pageName":"角色详情页","url":"QDReader:\u002F\u002Fapp\u002Factscenter?query={\"tabId\":0,\"tagId\":0}","linkType":0,"text":"活动已下线，去看看别的活动","isPage":true},{"harmony":"","isActionComponentsAppOnly":true,"btnText":"去活动中心","useBackground":0,"backgroundImage":"","android":"","followActConfig":true,"ios":"","pageId":30996,"pagePath":"30996","textColor":"#BCBCBC","pageName":"公共抽奖页","url":"QDReader:\u002F\u002Fapp\u002Factscenter?query={\"tabId\":0,\"tagId\":0}","linkType":0,"text":"活动已下线，去看看别的活动","isPage":true}]},"__noah_nodejs_flag__":"Y","__noah_enable_gray_actId__":"*","techConfig":{"useIndexCacheWhenJump":false}},"currentTime":1787782799,"defaultPageInfo":[{"img":"https:\u002F\u002Fimgservices-1252317822.image.myqcloud.com\u002Fimage\u002F20200102\u002Fojuts8u8qd.png","btnText":"去看看","background":{"bgColor":"rgba(0, 0, 0, 0)","bgImage":"","type":1},"textColor":"rgba(0, 0, 0, 0.45)","jumpUrl":"","scene":"活动已结束","desc":"你来晚啦，活动已经结束了","jump":false},{"img":"https:\u002F\u002Fimgservices-1252317822.image.myqcloud.com\u002Fimage\u002F20200102\u002Fvtmiexu62d.png","btnText":"刷新","background":{"bgColor":"rgba(0, 0, 0, 0)","bgImage":"","type":1},"textColor":"rgba(0, 0, 0, 0.45)","scene":"发生错误","desc":"Error Code:"},{"img":"https:\u002F\u002Fimgservices-1252317822.image.myqcloud.com\u002Fimage\u002F20200102\u002F6omqbkzu55.png","btnText":"去看看","background":{"bgColor":"rgba(0, 0, 0, 0)","bgImage":"","type":1},"textColor":"rgba(0, 0, 0, 0.45)","jumpUrl":"","scene":"不符合条件","desc":"暂无资格，去看看别的活动吧〜","jump":false}],"devConf":{"frontJs":"\u002F\u002Fnoah2-1252317822.file.myqcloud.com\u002Fnpm\u002F@noah-nqd\u002Fsite-config@2.5.3\u002Fdist\u002Findex.js","jsUrl":"\u002F\u002Fnoah2-1252317822.file.myqcloud.com\u002Fnpm\u002F@noah-nqd\u002Fsite-config@2.5.3\u002Fdist\u002Findex.js","hooks":[]},"endTime":1793462399,"inlinePage":{"address":{"language":{"data":{},"type":1},"configType":2,"btn":{"color":"#fff","bgColor":"#029fe8"}},"data":[{"displayColumn":[{"name":"姓名","key":"name","status":0},{"name":"手机号码","key":"phone","status":0},{"name":"联系地址","key":"address","status":0},{"name":"QQ号码","key":"qq","status":1},{"name":"微信号码","key":"wechat","status":1}],"active":true,"scene":"联系地址"},{"displayColumn":[{"name":"所获奖品","key":"getPrize","status":0},{"name":"获得时间","key":"getTime","status":0}],"active":false,"scene":"我的奖品"}],"checkList":["name","phone","address","getPrize","getTime"],"list":{"txt":{"normalColor":"#000000","highLightColor":"#F96A0E"},"language":{"data":{},"type":1},"configType":2}},"startTime":1757347200},"configData":[{"dataJson":{"overallRankBanner":{"actionUrl":"","position":10,"bannerImg":""},"headConf":{"smallPrizeImg":"\u002F\u002Fnoahqd.yuewen.com\u002Fimage\u002F8b38ad836c884a958c68b36c1a34abe8.png","outHeadImg":"\u002F\u002Fnoahqd.yuewen.com\u002Fimage\u002F9f667b11f02240938f8955e04c0e9cc9.png","prizeImg":"\u002F\u002Fnoahqd.yuewen.com\u002Fimage\u002F34df960530ba4e9db78e9c4a1c8ab948.png"},"emptyLotteryText":"抽一抽，好运马上到手～","drawboxId":"478266","platformLinks":{"qq":"https:\u002F\u002Fiyuedu.reader.qq.com\u002Fevent\u002Fact25023943\u002Findex.html#\u002F","xhs":"https:\u002F\u002Ffe.xiaohongshu.com\u002Fditto\u002Fvincent\u002Fa7c28c5875d0489187675499607a91c3?naviHidden=yes&fullscreen=true&source=tiaozhuan","qd":"","wb":"https:\u002F\u002Fm.weibo.cn\u002Fc\u002Fwbox?id=l331zrkexk&cid=1258"},"tickerClearWarning":{"text":"召唤券将于9月17日12:00清零，请尽快使用","ts":"1757995200000"}},"id":168,"name":"activity-act2025-yuewen-10th-anniversary","site":16384}],"pageInfo":{"components":[{"componentSelect":{"componentId":478237,"componentListId":1603,"componentName":"@noah-nqd\u002Ftask-v2","displayComponentName":"起点任务组件v2","displayVersion":"0.2.10","hash":"125876280:dd75a4ca61744bc68d176a00d0de2c33","isStatic":1,"parentComponentId":478235,"siteStr":"sub","version":"0.2.10"},"config":{"_onList":[{"name":"响应页面刷新","value":"ON_PAGE_REFRESH"}],"_vtag":{"name":"","id":""},"qd_creator":1,"_cnode":"543bc99f","_emitList":[{"name":"刷新页面","value":"EMIT_PAGE_REFRESH"}],"isValid":true,"userConf":{"mode":0,"autoGetReward":false,"noapp":false,"enableRefresh":true,"customStates":"","previewState":-1,"col_name":"","customTexts":[]},"isEnableRisk":true,"states":[{"val":-1,"src":"\u002F\u002Fnoahqd.yuewen.com\u002Fimage\u002F92258d667d75416c8967f54944505dd4.png","hotspots":[{"tasks":[{"name":""}]}]},{"val":0,"src":"\u002F\u002Fnoahqd.yuewen.com\u002Fimage\u002Fca6894f0269b42bdb9da948b7e9d3940.png","hotspots":[{"tasks":[{"name":"task\u002Fv2-award"},{"data":{"text":"领取成功"},"name":"msg-toast"}]}]},{"val":1,"src":"\u002F\u002Fnoahqd.yuewen.com\u002Fimage\u002F60a7049f67b5451d9c2078c027b24077.png","hotspots":[]}],"riskId":"3164"}},{"componentSelect":{"category":"guide-download","componentId":469806,"componentListId":296,"componentName":"@noah-common\u002Fguide-download","displayComponentName":"下载引导","displayVersion":"0.0.54","hash":"125876280:fd73dacc166540048639e56786d4cb06","isStatic":1,"parentComponentId":0,"siteStr":"main","version":"0.0.54"},"config":{"_globalEmitEvent":{"EMIT_SWITCH_BOOKS":{"name":"切换书本","value":"EMIT_SWITCH_BOOKS"},"EMIT_PAGE_REFRESH":{"name":"刷新页面","value":"EMIT_PAGE_REFRESH"},"EMIT_AFTER_BUY":{"name":"购买完成","value":"EMIT_AFTER_BUY"}},"btnText":"立即打开","_emitList":[{"name":"刷新页面","value":"EMIT_PAGE_REFRESH"},{"name":"切换书本","value":"EMIT_SWITCH_BOOKS"},{"name":"购买完成","value":"EMIT_AFTER_BUY"}],"isValid":true,"icon":"https:\u002F\u002Fnoahqd.yuewen.com\u002Factivity\u002Fdocument\u002Fd82c2324417d4b56b3591d6df0e2354e.png","showConfig":0,"title":"起点读书","imgClickAfter":"","textColor":"#000000","content":"下载APP，新用户免费看","_onList":[{"name":"响应页面刷新","value":"ON_PAGE_REFRESH"},{"name":"响应切换书本","value":"ON_SWITCH_BOOKS"},{"name":"响应购买完成","value":"ON_AFTER_BUY"}],"baseStyle":{"bgColor":"#FFFFFF","bgImage":"","type":1},"imgClickBefore":"","_globalOnEvent":{"ON_PAGE_REFRESH":{"name":"响应页面刷新","value":"ON_PAGE_REFRESH"},"ON_SWITCH_BOOKS":{"name":"响应切换书本","value":"ON_SWITCH_BOOKS"},"ON_AFTER_BUY":{"name":"响应购买完成","value":"ON_AFTER_BUY"}},"showType":0,"btn":{"borderColor":"rgba(0, 0, 0, 0)","bgColor":"#E5353E","color":"#FFFFFF","borderRadius":40,"borderWidth":0,"text":{"normal":"","disabled":""},"bgImage":{"normal":"","disabled":""},"angel":0,"type":1,"fontStyle":"","font":""},"status":true}},{"componentSelect":{"componentId":478432,"componentListId":1489,"componentName":"@noah-nqd\u002Fimg-handler","displayComponentName":"交互图片","displayVersion":"0.1.9","hash":"125876280:fab1ec3e1624479f81c2335a3a8d9ad5","isStatic":1,"parentComponentId":478431,"siteStr":"sub","version":"0.1.9"},"config":{"_cnode":"a638d587","isValid":true,"userConf":{"app":true,"cssName":"","businessValue":"","report":false,"login":false,"businessType":0},"imgConf":{"fitSize":false,"src":"\u002F\u002Fnoahqd.yuewen.com\u002Fimage\u002F8615b36ff9e84dbc99e7de326cc8778a.png","thumb":"","mb":0,"lazy":false,"custom":false,"width":750,"progressive":false,"hotspots":[{"tasks":[{"data":{"newWindow":true,"link":"https:\u002F\u002Fh5.if.qidian.com\u002Fnew\u002Fbaida\u002F?_viewmode=0&activityId=125876280&componentId=111","replace":false},"name":"link-custom"}]}],"preload":true,"height":160}}},{"componentSelect":{"category":"top-prompt","componentId":469807,"componentListId":81,"componentName":"@noah-common\u002Ftop-prompt","displayComponentName":"顶部提示条","displayVersion":"0.0.23","hash":"125876280:d8bae5e3f7c8493ca57ba1c5108640fe","isStatic":1,"parentComponentId":0,"siteStr":"main","version":"0.0.24"},"config":{}},{"componentSelect":{"componentId":478402,"componentListId":1603,"componentName":"@noah-nqd\u002Ftask-v2","displayComponentName":"起点任务组件v2","displayVersion":"0.2.10","hash":"125876280:5d051b49bb3343eea5d2976184e82753","isStatic":1,"parentComponentId":478235,"siteStr":"sub","version":"0.2.10"},"config":{"_onList":[{"name":"响应页面刷新","value":"ON_PAGE_REFRESH"}],"_vtag":{"name":"","id":""},"qd_creator":1,"_cnode":"543bc99f","_emitList":[{"name":"刷新页面","value":"EMIT_PAGE_REFRESH"}],"isValid":true,"userConf":{"mode":0,"autoGetReward":false,"noapp":false,"enableRefresh":true,"customStates":"","previewState":-1,"col_name":"","customTexts":[]},"isEnableRisk":true,"states":[{"val":-1,"src":"\u002F\u002Fnoahqd.yuewen.com\u002Fimage\u002F1c60459572994969a3502ad68f59f6fd.png","hotspots":[{"tasks":[{"data":{"autoReport":true,"imageUrl":"","title":"","bitmapUrl":"","url":"","desc":""},"name":"app-share"}]}]},{"val":0,"src":"\u002F\u002Fnoahqd.yuewen.com\u002Fimage\u002F7aae786400274514a3c34ed9d776f04c.png","hotspots":[{"tasks":[{"name":"task\u002Fv2-award"},{"data":{"text":"领取成功"},"name":"msg-toast"}]}]},{"val":1,"src":"\u002F\u002Fnoahqd.yuewen.com\u002Fimage\u002Fcb3f2164bf904610806b75cf179157db.png","hotspots":[]}],"riskId":"3164"}},{"componentSelect":{"componentId":478261,"componentListId":1488,"componentName":"@noah-nqd\u002Fnavbar-viewmode","displayComponentName":"沉浸式导航","displayVersion":"0.0.25","hash":"125876280:fa2c587690db47e298e98a326e1f7f34","isStatic":1,"parentComponentId":0,"siteStr":"sub","version":"0.0.25"},"config":{"iconLeft":[{"src":"\u002F\u002Fnoahqd.yuewen.com\u002Fnqd\u002Fimage\u002F7a204039cdb24915a3bd57165cc509b0.png","hotspot":[]}],"iconRight":[],"_cnode":"bbf6d350","isValid":true,"styles":{"padding":28,"top":98,"size":60,"innerPadding":4,"gap":0,"appendBody":true,"zIndex":8}}},{"componentSelect":{"componentId":478404,"componentListId":1603,"componentName":"@noah-nqd\u002Ftask-v2","displayComponentName":"起点任务组件v2","displayVersion":"0.2.10","hash":"125876280:2898a44d63ff49c08f440034f8ed75c0","isStatic":1,"parentComponentId":478235,"siteStr":"sub","version":"0.2.10"},"config":{"_onList":[{"name":"响应页面刷新","value":"ON_PAGE_REFRESH"}],"_vtag":{"name":"","id":""},"qd_creator":1,"_cnode":"543bc99f","_emitList":[{"name":"刷新页面","value":"EMIT_PAGE_REFRESH"}],"isValid":true,"userConf":{"mode":0,"autoGetReward":false,"noapp":false,"enableRefresh":true,"customStates":"","previewState":-1,"col_name":"","customTexts":[]},"isEnableRisk":true,"states":[{"val":-1,"src":"\u002F\u002Fnoahqd.yuewen.com\u002Fimage\u002Ffb30bb078c9542189e5c0b4d3d624e29.png","hotspots":[{"tasks":[{"data":{"id":"bookshelf","params":{},"bindValue":false},"name":"link-open-quick"}]}]},{"val":0,"src":"\u002F\u002Fnoahqd.yuewen.com\u002Fimage\u002F845323812e2a440eae55b71214e1653e.png","hotspots":[{"tasks":[{"name":"task\u002Fv2-award"},{"data":{"text":"领取成功"},"name":"msg-toast"}]}]},{"val":1,"src":"\u002F\u002Fnoahqd.yuewen.com\u002Fimage\u002F5a0e29aee50e4ae2914985521f77e800.png","hotspots":[]}],"riskId":"3164"}},{"componentSelect":{"componentId":478405,"componentListId":1603,"componentName":"@noah-nqd\u002Ftask-v2","displayComponentName":"起点任务组件v2","displayVersion":"0.2.10","hash":"125876280:5b242998ab474798aebbefef418a0992","isStatic":1,"parentComponentId":478235,"siteStr":"sub","version":"0.2.10"},"config":{"_onList":[{"name":"响应页面刷新","value":"ON_PAGE_REFRESH"}],"_vtag":{"name":"","id":""},"qd_creator":1,"_cnode":"543bc99f","_emitList":[{"name":"刷新页面","value":"EMIT_PAGE_REFRESH"}],"isValid":true,"userConf":{"mode":0,"autoGetReward":false,"noapp":false,"enableRefresh":true,"customStates":"","previewState":-1,"col_name":"","customTexts":[]},"isEnableRisk":true,"states":[{"val":-1,"src":"\u002F\u002Fnoahqd.yuewen.com\u002Fimage\u002F54feeb33503a415a802d62bbcf9a1b7d.png","hotspots":[{"tasks":[{"data":{"id":"bookshelf","params":{},"bindValue":false},"name":"link-open-quick"}]}]},{"val":0,"src":"\u002F\u002Fnoahqd.yuewen.com\u002Fimage\u002F7b54f96dd7cf44f8beb15797c9c5d6e7.png","hotspots":[{"tasks":[{"name":"task\u002Fv2-award"},{"data":{"text":"领取成功"},"name":"msg-toast"}]}]},{"val":1,"src":"\u002F\u002Fnoahqd.yuewen.com\u002Fimage\u002Fbb75666bc2994c6cb5ac09420ca82a7a.png","hotspots":[]}],"riskId":"3164"}},{"componentSelect":{"componentId":478670,"componentListId":2045,"componentName":"@noah-nqd\u002Fwidget-hotspot","displayComponentName":"悬浮热区","displayVersion":"0.0.2","hash":"125876280:5aa6207309c14b899af8427a88dc43c1","isStatic":1,"parentComponentId":0,"siteStr":"sub","version":"0.0.2"},"config":{"stylesheet":{"frame":{"r":"","b":"","pos":"","w":"350","x":"300","h":"100","y":"1000","z":"1"}},"qd_creator":1,"_cnode":"dcdb0304","isValid":true,"actions":[]}},{"componentSelect":{"componentId":478235,"componentListId":2039,"componentName":"@noah-nqd\u002Ftemplate-2025-yw10","displayComponentName":"2025 - 阅文十周年","displayVersion":"0.3.1","hash":"125876280:ef56403930154255851d8d5121e2a555","isStatic":1,"parentComponentId":0,"siteStr":"sub","version":"0.3.1"},"config":{"_onList":[{"name":"响应页面刷新","value":"ON_PAGE_REFRESH"}],"slots":{"default":[{"componentId":478237},{"componentId":478402},{"componentId":478404},{"componentId":478405},{"componentId":478431}]},"_cnode":"de8e12a2","_emitList":[{"name":"刷新页面","value":"EMIT_PAGE_REFRESH"}],"isValid":true,"rankPageSize":500,"previewHeader":"\u002F\u002Fnoahqd.yuewen.com\u002Fimage\u002F449a673da76c49a689d4767f3ecd6fb5.png"}},{"componentSelect":{"category":"nested","componentId":478431,"componentListId":178,"componentName":"@noah-common\u002Fnested-time","displayComponentName":"定时组件","displayVersion":"0.0.12","hash":"125876280:18ae0968083e436bb5fe5a2f372adc06","isStatic":1,"parentComponentId":478235,"siteStr":"main","version":"0.0.12"},"config":{"slots":{"default":[{"componentId":478432}]},"background":{"bgColor__bg":"rgba(0, 0, 0, 0)","bgImage":"","type":1},"isValid":true,"startTime":"2025-09-19 12:00:00","endTime":"2025-09-30 12:00:00"}},{"componentSelect":{"componentId":478238,"componentListId":1516,"componentName":"@noah-nqd\u002Fnqd-logo-box","displayComponentName":"起点 logo 组件","displayVersion":"0.0.14","hash":"125876280:5bce39248f6c41eea09dbdffef437e57","isStatic":1,"parentComponentId":0,"siteStr":"sub","version":"0.0.14"},"config":{"color":"rgba(0, 0, 0, 0.1)","_cnode":"30f0607b","background":{"bgColor":"","bgImage":"","type":1},"isValid":true,"marginBottom":232,"paddingTop":32,"ratio":1}},{"componentSelect":{"componentId":478447,"componentListId":1701,"componentName":"@noah-nqd\u002Fplugin-app","displayComponentName":"App扩展","displayVersion":"0.1.1","hash":"125876280:78db47f35577433e989c961840cccf40","isStatic":1,"parentComponentId":0,"siteStr":"sub","version":"0.1.1"},"config":{"appConf":{"noKeyBounce":false,"noViewBounce":true,"reloadOnFocus":false,"noExitGesture":false},"_onList":[{"name":"响应页面刷新","value":"ON_PAGE_REFRESH"}],"_cnode":"9928b2a3","_emitList":[{"name":"刷新页面","value":"EMIT_PAGE_REFRESH"}],"isValid":true,"webConf":{"vqq":false,"ddlAn":""}}},{"componentSelect":{"category":"share","componentId":478233,"componentListId":82,"componentName":"@noah-common\u002Fshare","displayComponentName":"分享","displayVersion":"0.9.1","hash":"125876280:b3c4abfcf30f47599e23641e53b07a92","isStatic":0,"parentComponentId":0,"siteStr":"main","version":"0.9.1"},"config":{"supportPlatforms":["wechat","workwechat","qq","app"],"_globalEmitEvent":{"EMIT_SWITCH_BOOKS":{"name":"切换书本","value":"EMIT_SWITCH_BOOKS"},"EMIT_PAGE_REFRESH":{"name":"刷新页面","value":"EMIT_PAGE_REFRESH"},"EMIT_AFTER_BUY":{"name":"购买完成","value":"EMIT_AFTER_BUY"}},"actionChecker":{"query":"#{A24005}"},"visible":true,"_emitList":[{"name":"刷新页面","value":"EMIT_PAGE_REFRESH"},{"name":"切换书本","value":"EMIT_SWITCH_BOOKS"},{"name":"购买完成","value":"EMIT_AFTER_BUY"}],"module":1,"isValid":true,"actionList":[24005],"sharePrize":false,"actioner":[{"isReal":0,"_uniqueId":"efaa4d8a-3274-4682-bae5-6e1988ddd0b3","query":"#{A24005}","count":1,"addressStatus":0,"prizeId":24005}],"title":"角逐IP之光！召唤你心中的角色","onceShare":false,"url":"","imgUrl":"\u002F\u002Fnoahqd.yuewen.com\u002Fimage\u002F56a8ada4ad94433eae2c16aa696118b0.png","_onList":[{"name":"响应页面刷新","value":"ON_PAGE_REFRESH"},{"name":"响应切换书本","value":"ON_SWITCH_BOOKS"},{"name":"响应购买完成","value":"ON_AFTER_BUY"}],"_globalOnEvent":{"ON_PAGE_REFRESH":{"name":"响应页面刷新","value":"ON_PAGE_REFRESH"},"ON_SWITCH_BOOKS":{"name":"响应切换书本","value":"ON_SWITCH_BOOKS"},"ON_AFTER_BUY":{"name":"响应购买完成","value":"ON_AFTER_BUY"}},"iconUrl":"\u002F\u002Fnoahqd.yuewen.com\u002Factivity\u002Fdocument\u002F960fa05b6630f7188fb27abdefe98b6c.png","desc":"每日抽锦鲤，赢3C礼包，iPhone17、Switch2等豪礼"}},{"componentSelect":{"componentId":478234,"componentListId":1668,"componentName":"@noah-nqd\u002Fyfont","displayComponentName":"字体加载器","displayVersion":"0.0.18","hash":"125876280:9414f9fb5da2489085d498f9a2222757","isStatic":1,"parentComponentId":0,"siteStr":"sub","version":"0.0.18"},"config":{"fonts":[{"text":"1234567890x","family":"Roboto","preload":false,"font":"RobotoCondensed-Bold"},{"text":"1234567890.万亿TOP","family":"YuewenFont","preload":false,"font":"YuewenFont-Regular"},{"text":"做任务得召唤券角色明细搜索","family":"HYQiHei","preload":false,"font":"HYQH-90S"}],"isValid":true}},{"componentSelect":{"category":"style","componentId":478448,"componentListId":97,"componentName":"@noah-common\u002Fstyle","displayComponentName":"覆盖样式","displayVersion":"0.4.2","hash":"125876280:94f5a081a1cb4a2aa5bfcdd030e48641","isStatic":1,"parentComponentId":0,"siteStr":"main","version":"0.4.2"},"config":{"pageStyle":"html {\n    background: rgba(255, 238, 193, 1);\n}\n\n.component-noah-nqd-creator-ui {\n    position: fixed;\n    background: rgba(255, 238, 193, 1);\n    top: 0;\n    left: 0;\n    width: 100vh;\n    height: 100vh;\n    z-index: -1;\n}\n\n.activity-head {\n    position: relative;\n    z-index: 1;\n}\n\n.prize .a-icon-pz {\n    right: -.39rem !important;\n}\n\n.component-noah-nqd-template-2025-yw10 .role-card .desc {\n    font-size: .22rem;\n}","isValid":true}}],"currentTime":1787782799,"endTime":1793462399,"id":30501,"isIndex":1,"pageConf":{"eventList":"[]","keywords":"","bgColor":"","innerTitle":"","cloudTalk":[],"theme":"","langs":[],"newBgStyle":{"bgColor":"rgba(255, 238, 193, 1)","bgImage":"","type":1},"desc":""},"pageList":[{"end_time":1793462399,"id":30501,"order_id":0,"page_name":"角逐IP之光","page_path":"index","start_time":1757347200},{"end_time":1762099200,"id":30995,"order_id":1,"page_name":"角色详情页","page_path":"role","start_time":1757347200},{"end_time":1762099200,"id":30996,"order_id":1,"page_name":"公共抽奖页","page_path":"30996","start_time":1757347200}],"pageName":"角逐IP之光","pagePath":"index","pageStatus":0,"startTime":1757347200},"siteInfo":{"siteId":16384},"userInfo":{"avatar":"","businessInfo":{"isLogin":false},"encodeGuid":"","guid":0,"isLogin":false,"nickname":"","userId":0}},"msg":"success"};
      
      
        window.__noah_ajax_code=200;
      
    </script>
    
    
    <script>
      (function () {
        function dateFormat(options) {
          var format = options.format;
          var t = new Date(options.time);
          var tf = dateFormat.toFormatNum;
          return format.replace(/yyyy|mm|dd|hh|ii|ss/g, function (a) {
            switch (a) {
              case 'yyyy':
                return tf(t.getFullYear());
              case 'mm':
                return tf(t.getMonth() + 1);
              case 'dd':
                return tf(t.getDate());
              case 'hh':
                return tf(t.getHours());
              case 'ii':
                return tf(t.getMinutes());
              case 'ss':
                return tf(t.getSeconds());
            }
          });
        }

        dateFormat.toFormatNum = function (num) {
          return (num < 10 ? '0' : '') + num;
        };

        function getEnvPrefix() {
          var host = location.host;
          var env = /local/.test(host) ? 'dev' : /dev/.test(host) ? 'dev' : /oa/.test(host) || /pt/.test(host) ? 'oa' : /pre/.test(host) || /sim/.test(host) ? 'pre' : '';
          return env;
        }

        function getReportUrl() {
          var prefix = getEnvPrefix();
          var url = (prefix === 'pre' ? '' : prefix) + 'activity.qidian.com/qreport';
          return "//".concat(url);
        }

        // 获取各平台数据上报的地址
        function getReportSiteUrl(sitename) {
          var url = '';
          var site = window.__init_data__.siteName

          if (site !== sitename) {
            return url;
          }

          var prefix = getEnvPrefix();

          switch (site) {
            case 'webnovel':
              url = "//".concat(prefix, "activity.webnovel.com/report");
              break;
            case 'chereads':
              url = "//".concat(prefix, "activity.chereads.com/report");
              break;
            default:
              break;
          }

          return url;
        }

        function createSender(url) {
          if (navigator.sendBeacon) {
            navigator.sendBeacon(url, '');
          } else {
            var img = new Image();

            img.onload = img.onerror = function () {
              img = null;
            };

            img.src = url;
          }
        }

        function Report(urlArray) {
          var _this = this;

          this.urlArray = urlArray || [];
          this.params = {};

          var report = function report() {
            var params = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : {};

            if (_this.urlArray.length < 0) {
              return;
            }

            var paramsCopy = {}
            for (var i in _this.params) {
              if (_this.params.hasOwnProperty(i)) {
                  paramsCopy[i] = _this.params[i];
              }
            }

            for (var key in paramsCopy) {
              if (typeof paramsCopy[key] === 'function') {
                paramsCopy[key] = paramsCopy[key]();
              }
            }

            var paramsString = '';

            var paramData = {};
            // 合并
            for (var i in params) {
              if (params.hasOwnProperty(i)) {
                  paramsCopy[i] = params[i];
              }
            }

            // 创建
            for (var i in paramsCopy) {
              if (paramsCopy.hasOwnProperty(i)) {
                  paramData[i] = paramsCopy[i];
              }
            }

            Object.keys(paramData).forEach(function (key) {
              paramsString += key + '=' + encodeURIComponent(paramData[key]) + '&';
            }); // 去除最后一个&

            paramsString = paramsString.substring(0, paramsString.length - 1); // 上报

            _this.urlArray.forEach(function (url) {
              if (url) {
                createSender("".concat(url, "?").concat(paramsString));
              }
            });
          };

          report.init = function () {
            var params = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : {};
            _this.params = params;
          };

          return report;
        }

        function getCookie (name) {
          var v = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)')
          return v ? v[2] : ''
        }

        function getQimei() {
          return  getCookie('qimei') || getCookie('qrsn') || ''
        }

        function getQimei36() {
          return qimei36 = getCookie('qimei36') || getCookie('qrsn_new') || getCookie('qrsn') || ''
        }
        
        function searchParse(querystring) {
          var result = {};
          if (querystring) {
            var query = querystring.slice(1).split('&');
            query.forEach(function (kv) {
                var kvPair = kv.split('=');
                var key = kvPair[0];
                var val = decodeURIComponent(kvPair[1]);
                if (result.hasOwnProperty(key)) {
                    if (Array.isArray(result[key])) {
                        result[key].push(val);
                    } else {
                        result[key] = [result[key]];
                        result[key].push(val);
                    }
                } else {
                    result[key] = val;
                }
            });
          }
          return result;
        }

        // 海外
        var isWebnovel = window.__init_data__.siteName === 'webnovel';
        var isChereads = window.__init_data__.siteName === 'chereads';
        var isToonscroll = window.__init_data__.siteName === 'toonscroll';

        var isMQQReader = window.__init_data__.siteName === 'mqq';
        var report = new Report(isWebnovel ? [getReportSiteUrl('webnovel')] : isChereads ? [getReportSiteUrl('chereads')] : [getReportUrl()]);
        var hrefParts = location.pathname.split('/');
        var query = searchParse(location.search);
        /* 公共参数 */ 
        window.noah_mp_platform = query._mp || '';
        window.noah_platform = "";

        var from =  query.noahFrom || query.from || query.f || -1
        var noqimei = query.noqimei || ''
        var index = hrefParts.indexOf('noah')
        window.__act_id__ = (index + 1 >= hrefParts.length || index === -1) ? '' : hrefParts[index + 1]
        window.__path_id__ = (index + 2 >= hrefParts.length || index === -1) ? '' : hrefParts[index + 2]
        window.__csrf_tkn__ = getCookie('_csrfToken')
        // 手Q 针对 ios 下的 sendBeacon，特殊处理
        if(isMQQReader){
          var inQQ = navigator.userAgent.indexOf('MQQBrowser') > -1 || navigator.userAgent.indexOf('QQ') > -1;
          var isApple = /(iPhone|iPad|iPod|iOS)/i.test(window.navigator.userAgent);
          if (inQQ && isApple) {
            window.navigator.sendBeacon = null;
          }
        }
        var reportParam = {
          path: 'qdactivity',
          activityid: window.__act_id__,
          userid: '',
          guid: getCookie('ywGuid') || getCookie('ywguid') || getCookie('uid') || '',
          version: 2,
          platform: '',
          appid: query.appId || query.appid || 0,
          areaid: query.areaId || query.areaid || 0,
          from: from,
        }
        if (noqimei === '') {
          reportParam.qimei = getQimei()
          reportParam.qimei36 = getQimei36();
        }
        report.init(reportParam);
        report({
          p1: 5,
          logtime: dateFormat({
            format: 'yyyy-mm-dd hh:ii:ss',
            time: Date.now()
          })
        });
      })()
    </script>
    <!-- ejs start -->
    
    
    
    
    
    
    
    
    
    
      <script type="text/javascript" src="https://yuxstacdn.yuewen.com/noah/js/core.22115b95.js"></script><script type="text/javascript" src="https://yuxstacdn.yuewen.com/noah/js/chunk-vendors.66c54c2d.js"></script><script type="text/javascript" src="https://yuxstacdn.yuewen.com/noah/js/noah.91fadbac.js"></script></body>
  <!-- ejs end -->
</html>