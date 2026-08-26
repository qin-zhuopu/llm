# Source: https://opendatalab.org.cn/

> 抓取日期: 2026-08-26

---

<!DOCTYPE html>
<html lang="en" translate="no">
  <head>
<base href="/datasets/">
    <base href="/" />
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="https://webpub.shlab.tech/dps/opendatalab-web/xlab_v5.2103/xlab.svg" />
    <link rel="dns-prefetch preconnect" href="https://webpub.shlab.tech">
    <link rel="dns-prefetch preconnect" href="https://static.openxlab.org.cn">
    <link rel="dns-prefetch preconnect" href="https://at.alicdn.com">
    <link rel="dns-prefetch preconnect" href="https://cdn-static.openxlab.org.cn">
    <link rel="dns-prefetch preconnect" href="https://oss.openmmlab.com">
    <meta name="viewport" content="width=device-width, initial-scale=1.0 maximum-scale=1.0" />
    <title>OpenDataLab  å¼é¢AIå¤§æ¨¡åæ¶ä»£çå¼æ¾æ°æ®å¹³å°</title>
    <script type="module" crossorigin src="https://webpub.shlab.tech/dps/opendatalab-web/xlab_v5.2103/assets/index-cccb28a0.js"></script>
    <link rel="modulepreload" crossorigin href="https://webpub.shlab.tech/dps/opendatalab-web/xlab_v5.2103/assets/react-vendor-d21adf7d.js">
    <link rel="modulepreload" crossorigin href="https://webpub.shlab.tech/dps/opendatalab-web/xlab_v5.2103/assets/library-b141523a.js">
    <link rel="modulepreload" crossorigin href="https://webpub.shlab.tech/dps/opendatalab-web/xlab_v5.2103/assets/xlab-header-62e8bff9.js">
    <link rel="stylesheet" href="https://webpub.shlab.tech/dps/opendatalab-web/xlab_v5.2103/assets/xlab-header-b3b33b77.css">
    <link rel="stylesheet" href="https://webpub.shlab.tech/dps/opendatalab-web/xlab_v5.2103/assets/index-e9820dcc.css">
  </head>
  <body>
    <div id="root"></div>
    
    <script>
      if (window.opener) {
          const Dom = document.querySelector('div')
          function queryURLParameter(str) {
              var reg = /([^?&=]+)=([^?&=]+)/g,
                  obj = {}
              str.replace(reg, function () {
                  obj[arguments[1]] = arguments[2]
              })
              return obj
          }
          let query = queryURLParameter(window.location.href)
          // TIPï¼ githubUploadç±äºè·³è½¬çåæ/datasets?.code=,ï¼æ¥å£æ²¡æå¤çæææåredirecté»è¾ï¼å¯å¤æ­åæ
          const isGithubUploadJumpFrom = query?.method === 'githubUpload' || window?.location.href?.includes('?code=');
          console.log('postMessage', isGithubUploadJumpFrom, query, document?.referrer, query?.method)
          if(isGithubUploadJumpFrom) {
              window.opener.postMessage(query,'*')
              window.opener = null
              window.close()
          }

      }
  </script>
  </body>
</html>
