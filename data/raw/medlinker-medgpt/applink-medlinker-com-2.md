# Source: https://applink.medlinker.com/medgpt/

> 抓取日期: 2026-08-26

---

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta
      name="viewport"
      content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover"
    />
    <title>前往未来医生</title>

    <style>
      html,
      body {
        margin: 0;
        padding: 0;
        width: 100%;
        height: 100%;
        font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
          Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
        background: #009944;
      }

      #root {
        display: flex;
        height: 100%;
        width: 100%;
        overflow: hidden;
        flex-direction: column;
        align-items: center;
        position: relative;
        background: url('./images/img.jpg?v=2');
        background-size: cover;
        background-repeat: no-repeat;
        background-position-x: center;
      }

      #img {
        text-align: center;
      }

      #openAppButton {
        background-color: transparent;
        width: 100%;
        height: 48px;
        border-radius: 8px;
        color: #fff;
        font-size: 16px;
        outline: none;
        border: none;
      }

      #footerBtn {
        width: 80vw;
        position: absolute;
        background: #009944;
        border: 2px solid #fff;
        border-radius: 100px;
        top: 85%;
      }

      #footerBtn-wx {
        position: absolute;
        left: 0;
        top: 0;
        width: 287px;
        z-index: 98;
        display: none;
        /* margin-top: 16px; */
      }

      #wx-mask {
        position: fixed;
        z-index: 999;
        left: 0;
        right: 0;
        top: 0;
        bottom: 0;
        display: none;
        background-color: rgba(0, 0, 0, 0.75);
      }
    </style>
  </head>
  <body>
    <div id="root">
      <div id="footerBtn">
        <button id="openAppButton" onclick="openApp()">下载未来医生</button>
        <div id="footerBtn-wx"></div>
      </div>

      <div id="wx-mask" onclick="closeMask()">
        <img
          src="./images/img-guide@2x.png"
          style="width: 286px; height: 136px; position: absolute; top: 12px; right: 16px"
        />
      </div>
    </div>

    <script src="/libs/axios.min.js"></script>
    <script src="/libs/QDTracker.umd.js"></script>
    <script>
      QDTracker.init({
        appkey:
          window.location.origin.indexOf('-qa') >= 0 ? '0WEB06DVFFRPBYOR' : '0WEB06DVE7ZXMCJJ', //域名对应的appkey
        options: {
          encrypt_mode: 'close', // default - base64加密 ｜ close - 不加密 ｜ aes - aes加密 （依赖额外aes加密包，需要优先加载。方法如下方备注）
          enable_compression: false, // 上报前压缩
          track_interval: 0, // 上报间隔
          batch_max_time: 1, // 批量上报合并
          url: 'https://report1.tmc.qidian.qq.com',
          // 全埋点配置初始化
          // 1. 页面全埋点
          preventAutoTrack: false, // 用于控制页面浏览事件（$pageview）和页面关闭事件（$pageclose）是否自动上报；false表示自动上报，true表示阻止自动上报，默认为false
          pagestay: false, // 用于控制页面停留事件（$pageview）是否自动上报；ture表示进行上报，false表示阻止自动上报，默认false

          // 2. 点击全埋点（v6.2新增）
          heatmap: {
            clickmap: 'default', // 用于控制元素点击事件（$WebClick）是否自动上报；default 表示自动上报，'not_collect'表示阻止自动上报，默认为'not_collect'
            // 以下为配置默认采集点击事件的节点
            collect_tags: {
              DIV: {
                max_level: 1, // 默认是 1，即只支持叶子 div。可配置范围是 [1, 2, 3]，非该范围配置值，会被当作 1 处理。
              },
              LI: true,
              IMG: true,
              SPAN: {
                max_level: 1,
              },
              // ... 其他标签
            },
            // 手动在节点上，对需要进行点击采集的节点进行打标签采集点击          // 例子：<el-button anotherprop>anotherprop</el-button>
            track_attr: [],

            // 内嵌iframe内部的节点，是否需要收集点击事件
            iframeEnable: false, // false表示不开启，true表示开启，默认为false；没有特殊要求建议不开启，以提高性能

            singlePage: true,
          },
        },
      });
    </script>
    <script src="https://res2.wx.qq.com/open/js/jweixin-1.6.0.js"></script>
    <script>
      var search = window.location.search;
      if (search.indexOf('debug') >= 0 || search.indexOf('-qa') >= 0) {
        var script = document.createElement('script');
        script.src = '/libs/vconsole.min.js';
        script.onload = function () {
          var vConsole = new window.VConsole();
        };
        document.head.appendChild(script);
      }
    </script>
    <script>
      function isIOS() {
        return /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
      }

      function isAndroid() {
        return /android/i.test(navigator.userAgent);
      }

      function isWechat() {
        return navigator.userAgent.toLowerCase().indexOf('micromessenger') !== -1;
      }

      function getAppEl(appid, extra) {
        return (
          '<wx-open-launch-app id="launch-btn" appid="' +
          appid +
          '" extinfo="' +
          extra +
          '">' +
          '<script type="text/wxtag-template">' +
          '<style>.btn { font-size: 16px;color: #fff;outline:none;border:none; padding: 12px; background-color: rgba(0, 81, 235, 1);width: 287px;height: 48px;background: transparent;border-radius: 8px; }</style>' +
          '<button class="btn"></button>' +
          '<\/script>' +
          '</wx-open-launch-app>'
        );
      }

      function initWx() {
        document.querySelector('#footerBtn-wx').innerHTML = getAppEl('wx4d9bdbd26ae999a6', '/');
        axios
          .post(
            'https://medgptv2.medlinker.com/api/medgpt/expert/platform/wechat/config/jsapi/appid',
            {
              url: location.href,
              appid: 'wx8514142bf6d3f7c4',
            },
          )
          .then(function (res) {
            wx.config({
              appId: 'wx8514142bf6d3f7c4',
              debug: false,
              timestamp: res.data.data.timestamp,
              nonceStr: res.data.data.nonce_str,
              signature: res.data.data.signature,
              jsApiList: [
                'onMenuShareAppMessage',
                'onMenuShareTimeline',
                'onMenuShareQQ',
                'onMenuShareQZone',
                'updateAppMessageShareData',
                'updateTimelineShareData',
              ],
              openTagList: ['wx-open-launch-app'], // 获取开放标签权限
            });

            wx.ready(() => {
              const _shareConfig = {
                title: `未来医生-名医决策，家庭健康`,
                desc: '随时在线，为您服务',
                link: location.href.split('#')[0],
                imgUrl: window.location.origin + '/medgpt/images/logo-new.png',
                success: function () {},
              };

              wx.onMenuShareTimeline(_shareConfig);
              // @ts-ignore
              wx.onMenuShareAppMessage(_shareConfig);
              // @ts-ignore
              wx.onMenuShareQQ(_shareConfig);
              // @ts-ignore
              wx.onMenuShareQZone(_shareConfig);
              // @ts-ignore
              wx.updateAppMessageShareData(_shareConfig);
              // @ts-ignore
              wx.updateTimelineShareData(_shareConfig);
            });
          });

        var btn = document.getElementById('launch-btn');
        btn.addEventListener('ready', function (e) {
          document.querySelector('#footerBtn-wx').style.display = 'block';
        });
        btn.addEventListener('launch', function (e) {
          console.log('success');
        });
        btn.addEventListener('error', function (e) {
          console.error(e.detail);

          if (e.detail.errMsg === 'launch:fail') {
            if (isIOS()) {
              window.location.href = 'https://apps.apple.com/cn/app/id6737268204';
              document.getElementById('wx-mask').style.display = 'block';
              return;
            } else {
              window.location.href = 'https://sj.qq.com/appdetail/com.medlinker.medgptandroid';
            }
          } else {
            document.getElementById('wx-mask').style.display = 'block';
          }
        });
      }

      function openApp() {
        if (isWechat()) {
          document.getElementById('wx-mask').style.display = 'block';
          return;
        }

        // ios有universal link，如果能打开这个页面说明没安装
        if (isIOS()) {
          window.location.href = 'https://apps.apple.com/cn/app/id6737268204';
          return;
        } else {
          var arr = location.href.split('/');
          var appName = arr[3];
          var link = arr[4];
          window.location.href = 'medgpt://' + link;
        }

        // 检测是否成功打开APP
        function checkOpenApp() {
          var startTime = Date.now();
          var checkInterval = setInterval(function () {
            if (Date.now() - startTime > 2000) {
              clearInterval(checkInterval);

              // ios有universal link
              if (isIOS()) {
                // 超过2秒未打开APP，跳转到应用商店
                window.location.href = 'https://apps.apple.com/cn/app/id6737268204';
              } else {
                window.location.href = 'https://sj.qq.com/appdetail/com.medlinker.medgptandroid';
              }
            }
          }, 100);
        }

        checkOpenApp();
      }

      function closeMask() {
        document.getElementById('wx-mask').style.display = 'none';
      }

      if (isWechat()) {
        initWx();
      }
      // 替换图片的时候需注意图片上按钮位置的宽高比
      function btnPositionTop() {
        const root = document.getElementById('root');
        const rw = root.scrollWidth;
        const rh = root.scrollHeight;
        const rate = 2160 / 4094;
        const btn = document.getElementById('footerBtn');
        if ((rw / rh) >= 0.53) {
          root.style.backgroundSize = 'contain';
          btn.style.width = (rh * rate) * 0.8 + 'px';
          btn.style.top = rh * 0.85 + 'px';
        } else {
          root.style.backgroundSize = 'cover';
          btn.style.width = rw * 0.8 + 'px';
          btn.style.top = rh * 0.85 + 'px';
        }
      }
      btnPositionTop();
      window.onresize = function () {
        btnPositionTop();
      };
    </script>
  </body>
</html>
