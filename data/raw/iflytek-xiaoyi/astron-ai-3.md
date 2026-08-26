# Source: https://astron.ai/

> 抓取日期: 2026-08-26

---

<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/agent-icon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>
      Astron | AI Agent Platform for Autonomous Agents &amp; Workflow Automation
    </title>
    <meta
      name="description"
      content="Astron is an AI agent platform for building, deploying, and managing autonomous agents. Astron Agent offers cloud-based agent deployment, while Astron Workflow lets you build custom agent workflows with zero-code flexibility."
    />
    <meta
      name="keywords"
      content="Astron, Astron Agent, Astron Workflow, AI agent platform, autonomous agents, agent workflow builder, RAG pipeline, cross-system automation, no-code AI agent, enterprise AI agent, agentic AI, multi-agent system, self deployment,  AI agent builder, AI agent orchestration, workflow automation platform, LLM agent deployment, MaaS model foundation, RPA automation, AI tool plugins, agent-as-a-service, cloud AI agent platform, build your own AI agent, MCP, voice and virtual human agents, production-grade AI agents"
    />
    <meta
      property="og:title"
      content="Astron | AI Agent Platform for Autonomous Agents &amp; Workflow Automation"
    />
    <meta
      property="og:description"
      content="Build, deploy, and manage autonomous agents with Astron Agent and Astron Workflow. Zero-code flexibility, scalable operations, real work."
    />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://astron.ai/" />
    <meta name="twitter:card" content="summary" />
    <meta
      name="twitter:title"
      content="Astron | AI Agent Platform for Autonomous Agents &amp; Workflow Automation"
    />
    <meta
      name="twitter:description"
      content="Build, deploy, and manage autonomous agents with Astron Agent and Astron Workflow. Zero-code flexibility, scalable operations, real work."
    />
    <link rel="canonical" href="https://astron.ai/" />
    <!-- <%- ssoScript %> -->
    <script type="module" crossorigin src="/assets/index-CJQpyVoF.js"></script>
    <link rel="stylesheet" crossorigin href="/assets/index-gC2lNhMo.css">
  </head>

  <body>
    <div id="root"></div>
    <script>
      const RELOAD_FLAG = '__VITE_PRELOAD_FIXED_AT__';
      let reloading = false;

      function safeReload() {
        if (reloading) return;
        reloading = true;

        const now = Date.now();
        const last = Number(sessionStorage.getItem(RELOAD_FLAG) || '0');
        if (now - last < 5000) return; // 5s ååªè§¦åä¸æ¬¡ï¼é²æ+é²æ­»å¾ªç¯
        sessionStorage.setItem(RELOAD_FLAG, String(now));

        // ç¼å­ç ´åï¼è¿½å æ¶é´æ³åæ°ï¼é¿ååæ¬¡è¯·æ±æ§ chunk
        const url = new URL(window.location.href);
        url.searchParams.set('v', String(now));

        // ä¸ä¸å¸§æ¿æ¢å·æ°ï¼é¿åäº§çåå²è®°å½å¹¶å°½éåå°éªç
        requestAnimationFrame(() => {
          window.location.replace(url.toString());
        });
      }

      function suppressAndReload(e) {
        console.log('suppressAndReload error:', e);
        e?.preventDefault?.();
        e?.stopPropagation?.();
        e?.stopImmediatePropagation?.();
        !window?.location?.origin?.includes('localhost') && safeReload();
      }

      // ä¸å±äºä»¶ï¼Vite é¢å è½½å¤±è´¥
      window.addEventListener('vite:preloadError', suppressAndReload, true);

      // ä¸äºæµè§å¨/åºæ¯ä¸çæ¨¡åå¯¼å¥å¤±è´¥éè¯¯
      window.addEventListener(
        'error',
        e => {
          const msg = e?.message || '';
          if (
            msg.includes('Failed to fetch dynamically imported module') ||
            msg.includes('Importing a module script failed')
          ) {
            suppressAndReload(e);
          }
        },
        true
      );

      // Promise æç»å½¢æçå¨æ import å¤±è´¥
      window.addEventListener('unhandledrejection', e => {
        const msg = String(e?.reason?.message || e?.reason || '');
        if (msg.includes('Failed to fetch dynamically imported module')) {
          suppressAndReload(e);
        }
      });
    </script>

    <!-- itmçæ§ -->
    <!-- <script>
      (function (w, d, s, l, i) {
        w[l] = w[l] || [];
        w[l].push({ 'itm.start': new Date().getTime(), event: 'itm.js' });
        var f = d.getElementsByTagName(s)[0],
          j = d.createElement(s),
          dl = l != 'ITM_dataLayer' ? '&l=' + l : '';
        j.async = true;
        j.src = 'https://dt.xfyun.cn/itm.js/?id=' + i + dl;
        f.parentNode.insertBefore(j, f);
      })(window, document, 'script', 'ITM_dataLayer', 'ITM-5ad5f3a8');
    </script> -->

    <!-- åç¹æä»¶ -->
    <!-- <script>
      (function (w, d, s) {
        var l = 'IFlyCollector',
          f = d.getElementsByTagName(s)[0],
          j = d.createElement(s),
          w = window;
        w[l] = {};
        var c = w[l];
        c._o = function (a) {
          return function () {
            (c._e = c._e || []).push([a, arguments]);
          };
        };
        var e = [
          'init',
          'onEvent',
          'bindUser',
          'unbindUser',
          'updateCustomConfig',
        ];
        for (var i = 0; i < e.length; i++) {
          c[e[i]] = c._o.call(null, e[i]);
        }
        j.async = true;
        j.src = 'https://idatalogconf.iflysec.com/entry.js?sdk_ver=1.4.2';
        f.parentNode.insertBefore(j, f);
      })(window, document, 'script');
    </script> -->

    <!-- åç¹æä»¶åå§å -->
    <!-- <script>
      window.onload = function () {
        IFlyCollector.init({
          appId: '150b4dfebe',
          host: window.location.host,
          debug: window.location.protocol !== 'https:',
        });
        IFlyCollector.setAppVersion('1.4.0');
      };
    </script> -->

    <!-- ç­åå¾ -->
    <!-- <script type="text/javascript">
      (function (c, l, a, r, i, t, y) {
        c[a] =
          c[a] ||
          function () {
            (c[a].q = c[a].q || []).push(arguments);
          };
        t = l.createElement(r);
        t.async = 1;
        t.src = 'https://www.clarity.ms/tag/' + i;
        y = l.getElementsByTagName(r)[0];
        y.parentNode.insertBefore(t, y);
      })(window, document, 'clarity', 'script', 's4vy9shdgs');
    </script> -->

    <!-- æéªæä»¶ -->
    <!-- <script src="https://static.geetest.com/g5/gd.js" async></script> -->

    <!-- AIUI è¯­é³äº¤äº SDK å¨è¿å¥è¯­é³æ¨¡å¼åæéå è½½ -->

    <!-- Google tag (gtag.js) -->
    <script
      async
      src="https://www.googletagmanager.com/gtag/js?id=G-71YF9HXM5B"
    ></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag() {
        dataLayer.push(arguments);
      }
      gtag('js', new Date());

      gtag('config', 'G-71YF9HXM5B');
    </script>
  </body>
</html>
