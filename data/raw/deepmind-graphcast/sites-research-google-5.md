# Source: https://sites.research.google/floodforecasting/?utm_source=&utm_medium=&utm_campaign=&utm_content=

> 抓取日期: 2026-08-26

---

<!doctype html>
<html lang="en">
<head>
<meta charSet="utf-8" />
<meta name="viewport" content="width=device-width" />
<title>Flood Forecasting: AI for Information &amp; Alerts - Google Research</title>
<link rel="canonical" href="https://sites.research.google/floodforecasting/" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="true" />
<link rel="preconnect" href="https://storage.googleapis.com" crossOrigin="true" />
<meta name="description" content="Discover how Google's Flood Hub provides users with locally relevant flood forecasting, information and alerting up to 7 days in advance using AI." />
<meta property="og:type" content="website" />
<meta property="og:site_name" content="Flood Forecasting: AI for Information &amp; Alerts - Google Research" />
<meta property="og:url" content="https://sites.research.google/floodforecasting/" />
<meta property="og:title" content="Flood Forecasting: AI for Information &amp; Alerts - Google Research" />
<meta property="og:description" content="Discover how Google's Flood Hub provides users with locally relevant flood forecasting, information and alerting up to 7 days in advance using AI." />
<meta property="og:image" content="https://lh3.googleusercontent.com/nn9MuoHnRZC1PPy_0w8mbdwJvpfCgwuvG-GQMpNnx4OdRp30PeqKOI_QPwjK3rzmXbTwKczAjZwPLXFtfS6JfIWK-kI-_BvtIqKHYQ=w2880-e365-pa-nu" />
<meta property="twitter:card" content="summary" />
<meta property="twitter:site" content="GoogleAI" />
<meta property="twitter:title" content="Flood Forecasting: AI for Information &amp; Alerts - Google Research" />
<meta property="twitter:description" content="Discover how Google's Flood Hub provides users with locally relevant flood forecasting, information and alerting up to 7 days in advance using AI." />
<meta property="twitter:image" content="https://lh3.googleusercontent.com/nn9MuoHnRZC1PPy_0w8mbdwJvpfCgwuvG-GQMpNnx4OdRp30PeqKOI_QPwjK3rzmXbTwKczAjZwPLXFtfS6JfIWK-kI-_BvtIqKHYQ=w2880-e365-pa-nu" />
<link rel="icon" href="https://research.google/static/images/favicon-6da5620880159634213e197fafca1dde0272153be3e4590818533fab8d040770.ico" />
<script async src="https://www.googletagmanager.com/gtag/js?id=G-CLR36F4B6Z"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag() {
dataLayer.push(arguments);
}
gtag('js', new Date());
gtag('config', 'G-CLR36F4B6Z');
</script>
<link href="https://fonts.googleapis.com/css?family=Google+Sans+Display:300,400,500,600,700|Google+Sans:300,400,500,600,700|Google+Sans+Text:300,400,500,600,700&amp;display=swap" rel="preload" as="style" onload="this.onload=null;this.rel='stylesheet'" />
<link rel="stylesheet" href="/assets/slug.WxSJaVwC.css" />
<script type="module" src="/assets/main.BUxWUSNG.min.js"></script>
</head>
<body>
<div class="_frame_81bt0_1">
<div id="root" role="main">
<div class="_frame_bpa2b_1 _frame:with-navItems_bpa2b_9">
<div class="_frame_epqtt_1 _fullbleed_epqtt_11"><relate-mobile-nav>
<nav>
<div class="_container_bpa2b_14">
<div class="_logo_bpa2b_34 _logoHiddenMobile_bpa2b_34"><a href="https://research.google" title="Google Research"><svg role="img" aria-hidden="true" aria-label="Google Research logo" xmlns="http://www.w3.org/2000/svg" width="170.58" height="24">
<title>Google Research</title>
<g fill="#5F6368">
<path d="M82 1.79h5.61c2.74 0 5.15 2.02 5.15 4.9 0 2.35-1.75 4.25-3.93 4.71l-.05.07 4.62 6.69v.09h-2.5l-4.44-6.67h-2.35v6.67H82V1.79zm5.52 7.82c1.63 0 3.08-1.2 3.08-2.92 0-1.31-1.06-2.87-2.94-2.87h-3.54v5.79h3.4zM93.97 12.62c0-3.27 2.14-6 5.56-6 3.36 0 5.47 2.37 5.47 6 0 .16-.02.39-.02.39h-8.85c.07 2.53 2.02 3.68 3.63 3.68 1.56 0 2.53-.9 3.17-2.02l1.89.92c-.87 1.66-2.62 3.04-5.15 3.04-3.3-.01-5.7-2.54-5.7-6.01zm5.52-4.07c-1.63 0-2.85 1.1-3.2 2.71h6.46c-.06-.98-.77-2.71-3.26-2.71zM106.09 15.4l1.89-.8c.6 1.45 1.79 2.14 2.94 2.14 1.45 0 2.37-.74 2.37-1.47 0-.71-.44-1.29-2.18-1.72l-1.66-.41c-1.31-.34-3.04-1.17-3.04-3.1 0-2.25 2.12-3.4 4.46-3.4 1.82 0 3.7.9 4.39 2.62l-1.89.78c-.48-1.06-1.63-1.52-2.67-1.52-.92 0-2.14.51-2.14 1.43 0 .71.53 1.08 1.82 1.38l1.7.44c2.32.55 3.36 1.82 3.36 3.38 0 1.88-1.82 3.5-4.53 3.5-2.57-.03-4.2-1.61-4.82-3.25zM116.52 12.62c0-3.27 2.14-6 5.56-6 3.36 0 5.47 2.37 5.47 6 0 .16-.02.39-.02.39h-8.85c.07 2.53 2.02 3.68 3.63 3.68 1.56 0 2.53-.9 3.17-2.02l1.89.92c-.87 1.66-2.62 3.04-5.15 3.04-3.31-.01-5.7-2.54-5.7-6.01zm5.52-4.07c-1.63 0-2.85 1.1-3.2 2.71h6.46c-.07-.98-.78-2.71-3.26-2.71zM138.65 11.31v6.94h-2.02v-1.56h-.09c-.62.94-1.75 1.93-3.5 1.93-2.46 0-4.37-1.66-4.37-3.86 0-2.46 2.07-3.82 4.85-3.82 1.59 0 2.67.44 3.1.69v-.48c0-1.56-1.47-2.64-2.92-2.64-1.2 0-2.09.44-2.8 1.5l-1.86-1.17c.99-1.4 2.53-2.21 4.55-2.21 3.15-.01 5.06 1.78 5.06 4.68zm-2.03 2.12s-1.01-.78-2.76-.78c-1.79 0-3.01.99-3.01 2.16 0 1.22 1.26 1.93 2.34 1.93 1.71 0 3.43-1.47 3.43-3.31zM141 18.26V6.99h2.02v1.84h.09c.46-1.29 2.12-2.16 3.29-2.16.69 0 1.15.09 1.56.28L147.32 9c-.32-.12-.71-.16-1.24-.16-1.59 0-2.97 1.49-2.97 3.22v6.21H141zM148.15 12.62c0-3.43 2.41-6 5.79-6 2.69 0 4.25 1.59 4.94 3.24l-1.93.81c-.55-1.33-1.59-2.12-3.15-2.12-1.79 0-3.54 1.63-3.54 4.07s1.75 4.07 3.54 4.07c1.56 0 2.71-.8 3.26-2.12l1.89.81c-.69 1.66-2.32 3.24-5.01 3.24-3.38 0-5.79-2.6-5.79-6zM162.72 6.99l-.09 1.56h.09c.6-1.03 2.02-1.93 3.56-1.93 3.01 0 4.3 1.91 4.3 4.55v7.08h-2.12v-6.76c0-2.21-1.22-2.94-2.69-2.94-1.84 0-3.06 1.84-3.06 3.56v6.14h-2.12V1.79h2.12v5.2z"></path>
</g>
<path fill="#4285F4" d="M9.49 18.62C4.33 18.62 0 14.44 0 9.31 0 4.18 4.33 0 9.49 0c2.85 0 4.88 1.11 6.41 2.57l-1.8 1.79C13 3.34 11.52 2.54 9.49 2.54c-3.76 0-6.71 3.02-6.71 6.77 0 3.75 2.94 6.77 6.71 6.77 2.44 0 3.83-.98 4.72-1.86.73-.73 1.21-1.77 1.39-3.2H9.49V8.47h8.6c.09.45.14 1 .14 1.59 0 1.91-.53 4.27-2.21 5.95-1.65 1.7-3.75 2.61-6.53 2.61z"></path>
<path fill="#EA4335" d="M31.52 12.62c0 3.45-2.67 5.99-5.93 5.99s-5.93-2.54-5.93-5.99c0-3.47 2.67-5.99 5.93-5.99s5.93 2.52 5.93 5.99zm-2.6 0c0-2.16-1.55-3.63-3.34-3.63s-3.34 1.48-3.34 3.63c0 2.13 1.55 3.63 3.34 3.63s3.34-1.49 3.34-3.63z"></path>
<path fill="#FBBC04" d="M44.83 12.62c0 3.45-2.66 5.99-5.93 5.99-3.27 0-5.93-2.54-5.93-5.99 0-3.47 2.66-5.99 5.93-5.99 3.26 0 5.93 2.52 5.93 5.99zm-2.6 0c0-2.16-1.55-3.63-3.34-3.63-1.79 0-3.34 1.48-3.34 3.63 0 2.13 1.55 3.63 3.34 3.63 1.79.01 3.34-1.49 3.34-3.63z"></path>
<path fill="#4285F4" d="M57.8 6.99v10.76c0 4.43-2.62 6.24-5.72 6.24-2.92 0-4.68-1.95-5.34-3.54l2.3-.95c.41.98 1.41 2.13 3.03 2.13 1.98 0 3.22-1.23 3.22-3.52v-.86h-.09c-.59.73-1.73 1.36-3.17 1.36-3.01 0-5.77-2.61-5.77-5.97 0-3.38 2.76-6.02 5.77-6.02 1.44 0 2.58.64 3.17 1.34h.09v-.97h2.51zm-2.33 5.66c0-2.11-1.41-3.66-3.22-3.66-1.82 0-3.35 1.54-3.35 3.66 0 2.09 1.53 3.61 3.35 3.61 1.81 0 3.22-1.52 3.22-3.61z"></path>
<path fill="#34A853" d="M62.43.64v17.62h-2.65V.64h2.65z"></path>
<path fill="#EA4335" d="M72.83 14.6l2.05 1.36c-.66.98-2.26 2.66-5.02 2.66-3.42 0-5.89-2.63-5.89-5.99 0-3.56 2.49-5.99 5.6-5.99 3.12 0 4.65 2.47 5.15 3.81l.28.68-8.05 3.32c.62 1.2 1.57 1.82 2.92 1.82 1.34-.01 2.28-.67 2.96-1.67zm-6.31-2.16l5.38-2.22c-.3-.75-1.19-1.27-2.24-1.27-1.34 0-3.21 1.18-3.14 3.49z"></path>
</svg></a></div>
<div class="_siteName_bpa2b_52 _siteNameDesktop_bpa2b_76"><a href="/floodforecasting/">Flood Forecasting</a></div>
<div class="_siteNameMobile_bpa2b_82">
<div><a href="/floodforecasting/" class="_siteName_bpa2b_52">Flood Forecasting</a></div>
</div>
<div class="_navItems_bpa2b_93"><a href="#Intro" class>
<div class="_frame_13anx_99 _body_13anx_63 _body_13anx_63">About</div>
</a><a href="#solution" class>
<div class="_frame_13anx_99 _body_13anx_63 _body_13anx_63">Flood Hub</div>
</a><a href="#alerts" class>
<div class="_frame_13anx_99 _body_13anx_63 _body_13anx_63">Alerts</div>
</a><a href="#how" class>
<div class="_frame_13anx_99 _body_13anx_63 _body_13anx_63">How it works</div>
</a><a href="#floods_publications" class>
<div class="_frame_13anx_99 _body_13anx_63 _body_13anx_63">Publications</div>
</a><a href="#floods_faq" class>
<div class="_frame_13anx_99 _body_13anx_63 _body_13anx_63">FAQ</div>
</a></div>
</div>
<div class="_mobileNav_bpa2b_184">
<div class="_navItems_bpa2b_93"><a href="#Intro" class>
<div class="_frame_13anx_99 _body_13anx_63 _body_13anx_63">About</div>
</a><a href="#solution" class>
<div class="_frame_13anx_99 _body_13anx_63 _body_13anx_63">Flood Hub</div>
</a><a href="#alerts" class>
<div class="_frame_13anx_99 _body_13anx_63 _body_13anx_63">Alerts</div>
</a><a href="#how" class>
<div class="_frame_13anx_99 _body_13anx_63 _body_13anx_63">How it works</div>
</a><a href="#floods_publications" class>
<div class="_frame_13anx_99 _body_13anx_63 _body_13anx_63">Publications</div>
</a><a href="#floods_faq" class>
<div class="_frame_13anx_99 _body_13anx_63 _body_13anx_63">FAQ</div>
</a></div>
</div>
</nav>
</relate-mobile-nav></div>
</div>
<div class="_frame_1jr7w_1">
<div class="_container_1xa7h_1 _containerFullbleedMobile_1xa7h_62">
<div class="_item_1xa7h_67" style="--grid-item-start: 1; --grid-item-end: 12;">
<div class="_container_1jr7w_30">
<div class="_copyGroup_1jr7w_86">
<h1 class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _display_13anx_86 _heading1_13anx_1">Flood Forecasting</div>
</h1>
<div class="_frame_13anx_99 _desktop_1jr7w_15 _heading3_13anx_32"></div>
<div class="_frame_13anx_99 _mobile_1jr7w_25 _body_13anx_63 _bodyLarge_13anx_71"></div>
<div class="_buttonGroup_1jr7w_106"><a href="https://www.nature.com/articles/s41586-024-07145-1" target="_blank" class="_container_12nlj_1 _mediumEmphasis_12nlj_27">
<div class="_frame_13anx_99 _body_13anx_63 _body_13anx_63">Paper</div>
</a><a href="https://blog.google/technology/ai/google-ai-global-flood-forecasting/" target="_blank" class="_container_12nlj_1 _mediumEmphasis_12nlj_27">
<div class="_frame_13anx_99 _body_13anx_63 _body_13anx_63">Blog</div>
</a><a href="https://sites.research.google/floods/l/0/0/3" target="_blank" class="_container_12nlj_1 _mediumEmphasis_12nlj_27">
<div class="_frame_13anx_99 _body_13anx_63 _body_13anx_63">Flood Hub</div>
</a></div>
</div>
<div class="_backgroundDesktop_1jr7w_57"><video playsInline muted disablePictureInPicture disableRemotePlayback loop autoPlay>
<source type="video/mp4" src="https://storage.googleapis.com/googwebreview.appspot.com/grow-ext-cloud-images-uploads/ryzlk7wp5wkm-TCvIvxy20gZFkHwZFRZPR-0796ccd7260b3aab797b5306dbea3503-Floods-1_4089266B.mp4" />
</video></div>
<div class="_backgroundMobile_1jr7w_58"><video playsInline muted disablePictureInPicture disableRemotePlayback loop autoPlay>
<source type="video/mp4" src="https://storage.googleapis.com/googwebreview.appspot.com/grow-ext-cloud-images-uploads/ryzlk7wp5wkm-TCvIvxy20gZFkHwZFRZPR-0796ccd7260b3aab797b5306dbea3503-Floods-1_4089266B.mp4" />
</video></div>
</div>
</div>
</div>
</div>
<div class="_container_3mwgq_1"></div>
<div id="Intro" class="_container_1xa7h_1">
<div class="_item_1xa7h_67" style="--grid-item-start: 2; --grid-item-end: 11;">
<div class="_container_or7p1_1">
<div class="_frame_13anx_99 _container_1r2da_1 _body_13anx_63 _bodyLarge_13anx_71">
<h3 size="3" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading3_13anx_32">Using AI to make critical flood forecasting information universally accessible</div>
</h3>
<p>Every year, floods cause thousands of fatalities worldwide,âdisrupt the lives of millions, and cause significant financial damages. As part of our efforts to advance AI to address the climate crisis and help communities affected, Google Research has developedÂ <a target="_blank" href="https://www.nature.com/articles/s41586-024-07145-1"><u>AI models to forecast floods</u></a>. Our system combines two AI models that process diverse publicly available data sources: the Hydrologic Model forecasts the amount of water flowing in a river, and the Inundation Model predicts what areas will be affected and how high the water level will be. This way, we can alert people in areas that are about to be impacted up to 7 days before disaster strikes. By warning organizations and people, we hope to empower them to act, limiting damage and loss of life. We work closely with governments, the UN, and NGOs to implement and distribute flood alerts. After many years of intense research and development, our technology is now scalable and covers dozens of countries, and in the future, we aspire to cover all areas affected by floods globally.
</p>
</div>
</div>
</div>
</div>
<div class="_container_3mwgq_1"></div>
<div class="_container_1xa7h_1">
<div class="_item_1xa7h_67" style="--grid-item-start: 2; --grid-item-end: 11;">
<div class="_container_or7p1_1">
<figure class="_frame_1wolg_15 _frameFullbleedMobile_1wolg_15">
<div class="_imageContainer_1wolg_10"><rds-click-video src="https://storage.googleapis.com/googwebreview.appspot.com/grow-ext-cloud-images-uploads/ryzlk7wp5wkm-KF23MBGbXTxiscxvcL8TI-55eb925c019c507af5c077b3925e6bac-What_is_the_Google_FloodHub__EBFDD859.mp4"><img src="https://lh3.googleusercontent.com/BJo5WOaFmhQicrfTPT2VgbHQrPWiGROdyqGYxTZyR9BtPeMxbu7lcKnGYgdU8A_BmkqXvAxvBkx_msPcfZ27kddeVh_kTDhszkWok_20=w2880-e365-pa-nu" loading="lazy" alt /></rds-click-video></div>
</figure>
<div class="_frame_13anx_99 _container_1r2da_1 _body_13anx_63 _bodyLarge_13anx_71">
<h3 size="3" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading3_13anx_32"></div>
</h3>
<p></p>
</div>
</div>
</div>
</div>
<div id="solution" class="_container_1xa7h_1 _withPadding_or7p1_31">
<div class="_item_1xa7h_67" style="--grid-item-start: 2; --grid-item-end: 11;">
<div class="_container_or7p1_1">
<div class="_frame_13anx_99 _container_1r2da_1 _body_13anx_63 _bodyLarge_13anx_71">
<h3 size="3" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading3_13anx_32">Flood Hub for Governments and Organizations</div>
</h3>
<p>The <a target="_blank" href="https://sites.research.google/floods/l/0/0/3"><u>Flood Hub</u></a> provides users with locally relevant flood data and flood forecasts up to 7 days in advance so they can take timely action. It is a visual, easy-to-use resource that displays local riverine flood maps and water trends and gives real-time flood forecasts and alerts based on Google's AI models and global data sources. The <a target="_blank" href="https://sites.research.google/floods/l/0/0/3"><u>Flood Hub</u></a> is designed to meet the needs of governments, local aid organizations, and people directly at risk. All information is free of charge, publicly available, and can be shared over social networks. Forecasts are updated daily.</p>
<p>Flood Hub currently covers river basins in over 80 countries worldwide, providing critical flood forecasting for over 1,800 sites and, covering a population of 460M peopleÂ </p><img src="https://lh3.googleusercontent.com/tFhh2FDUqHVntvYPqdostsRC8UMCtnjNxFKxjAYbUZ54yEurICVzh7YQso9Z3artKx_srlCeCD3k-7pc_B1QiFTTzGi8hlZUmC5D97w=w2880-e365-pa-nu" loading="lazy" alt />
<p><a target="_blank" href="https://sites.research.google/floods/l/0/0/3">Flood Hub</a> currently covers river basins across over 80 countries worldwide, providing critical flood forecasting for over 1800 sites and covering a population of 460M people.
</p>
</div>
</div>
</div>
</div>
<div id="alerts" class="_container_1xa7h_1">
<div class="_item_1xa7h_67" style="--grid-item-start: 2; --grid-item-end: 11;">
<div class="_container_or7p1_1">
<div class="_frame_13anx_99 _container_1r2da_1 _body_13anx_63 _bodyLarge_13anx_71">
<h3 size="3" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading3_13anx_32">Alerts on Google Search and Google Maps and notifications</div>
</h3>
<p>We publish our forecasts via alerts on Google Search, Maps, and Android notifications to help more people access flood information. </p>
<p>
</p>
</div>
</div>
</div>
</div>
<div class="_container_3mwgq_1"></div>
<div id="how" class="_container_1xa7h_1 _withPadding_or7p1_31">
<div class="_item_1xa7h_67" style="--grid-item-start: 2; --grid-item-end: 11;">
<div class="_container_or7p1_1">
<figure class="_frame_1wolg_15 _frameFullbleedMobile_1wolg_15">
<div class="_imageContainer_1wolg_10"><video playsInline muted disablePictureInPicture disableRemotePlayback loop autoPlay>
<source type="video/mp4" src="https://storage.googleapis.com/googwebreview.appspot.com/grow-ext-cloud-images-uploads/ryzlk7wp5wkm-3pZ1SxDZJuCZm8o0qIW21J-8f8c49e60670adb8aaa11a087760dcea-Floods_mock_highres4K_B5345757.mp4" />
</video></div>
</figure>
<div class="_frame_13anx_99 _container_1r2da_1 _body_13anx_63 _bodyLarge_13anx_71">
<h3 size="3" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading3_13anx_32">How it works</div>
</h3>
<p>The Hydrologic Model identifies whether a river is expected to flood by processing publicly available data sources, such as precipitation and other weather and basin data, and outputs a forecast for the water level in the river in the following days. The Inundation Model simulates the behavior of the water as it moves across the floodplain based on the hydrology forecast and satellite imagery. This allows us to know which areas are going to be affected and how high we expect the water level to be. </p><img src="https://lh3.googleusercontent.com/VwOZ_d7eQlUYxc44HLpyQ6Sbyq1JcbqHa3LNwMsEqt1X-B3W5kzdf18dzEWsW0UZ94HVvQN0hKvXezj3TGCZy1d2ji7Deg0px2BklcY=w2880-e365-pa-nu" loading="lazy" alt />
<p><b>Our groundbreaking AI model combines these two models to achieve unprecedented accuracy:</b></p>
<ul>
<li>
<p>Provides more actionable and accurate forecasts (when compared to the state-of-the-art, widely-used globally-available model, <a target="_blank" href="https://www.globalfloods.eu/"><u>GloFAS</u></a>) to empower governments, relief organizations, and citizens to take relevant actions and save lives.</p>
</li>
<li>
<p>Can evaluate whether a riverâs water level will rise or fall and by how much up to 7 days in advance, and depending on data availability, generates maps that showcase which specific areas are expected to flood.</p>
</li>
<li>
<p>Is trained on a wide variety of publicly available global weather products, <a target="_blank" href="https://en.wikipedia.org/wiki/Stream_gauge"><u>river gauge</u></a> measurements and satellite imagery.Â Â </p>
</li>
<li>
<p>Can be applied to locations for which we have river gauge data, and more importantly, can infer from data-rich to data-scarce locations, enabling us to provide coverage in many low and medium-income countries (LMIC).</p>
</li>
</ul>
<p></p>
</div>
</div>
</div>
</div>
<div class="_container_3mwgq_1 _filled_3mwgq_10"></div>
<div class="_filled_1mg00_1">
<div class="_mobileHeader_1mg00_5">
<h3 size="3" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading3_13anx_32">Discover more</div>
</h3>
<p></p>
</div>
<div class="_frame_z883j_84"><bds-carousel controls><bds-carousel-slide>
<div class="_slide_z883j_150 _marginSlide_z883j_165"></div>
</bds-carousel-slide><bds-carousel-slide>
<div class="_slide_z883j_150 _firstSlide_z883j_175">
<h3 size="3" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading3_13anx_32">Discover more</div>
</h3>
<p></p>
</div>
</bds-carousel-slide><bds-carousel-slide>
<div class="_slide_z883j_150 _roundedLeftSlide_z883j_192">
<figure class="_frame_1wolg_15">
<div class="_imageContainer_1wolg_10"><img src="https://lh3.googleusercontent.com/D2Gce7iygAoOVQTDXl-puEdsG77siHQfcEaIYspCBZfrgfYRjtzoFOGnc9MKZzkuxdSC1LIIh7F27Z5LZdpZDyT2nWgqmHaVtP2qvw=w2880-e365-pa-nu" loading="lazy" alt /></div>
<figcaption class="_caption_1wolg_19">
<div class="_frame_13anx_99 _caption_13anx_55">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47"><a target="_blank" href="https://www.youtube.com/watch?v=ET04pDj-RvM&amp;t=3s">How AI is Improving Global Access to Reliable Flood Forecasts</a></div>
</h4>
<p>
</p>
</div>
</figcaption>
</figure>
</div>
</bds-carousel-slide><bds-carousel-slide>
<div class="_slide_z883j_150">
<figure class="_frame_1wolg_15">
<div class="_imageContainer_1wolg_10"><img src="https://lh3.googleusercontent.com/ybW2H5yx07QWm0GRZ9U0OBfRSAqAjIJqoHdD21tAontuc3XknIQEFzfypGPS2T6oU2vDq0-7GkuUBklKU-XBm80l8ldZo54qf2cXIjQ=w2880-e365-pa-nu" loading="lazy" alt /></div>
<figcaption class="_caption_1wolg_19">
<div class="_frame_13anx_99 _caption_13anx_55">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47"><a target="_blank" href="https://research.google/blog/using-ai-to-expand-global-access-to-reliable-flood-forecasts/">Using AI to expand global access to reliable flood forecasts</a></div>
</h4>
<p></p>
</div>
</figcaption>
</figure>
</div>
</bds-carousel-slide><bds-carousel-slide>
<div class="_slide_z883j_150">
<figure class="_frame_1wolg_15">
<div class="_imageContainer_1wolg_10"><img src="https://lh3.googleusercontent.com/IcfLlyjQ0c6TnCWyoj7X0I5-l7SvdaxuJW8ZGBifikyU-GDIB7l14TXI11zvkFSu0ofzjZ-m-lA1wDqWJgEDL2cypVUJdmDihhNniWu6=w2880-e365-pa-nu" loading="lazy" alt /></div>
<figcaption class="_caption_1wolg_19">
<div class="_frame_13anx_99 _caption_13anx_55">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47"><a target="_blank" href="https://blog.google/technology/ai/google-ai-global-flood-forecasting/">How we are using AI for reliable flood forecasting at a global scale</a></div>
</h4>
<p></p>
</div>
</figcaption>
</figure>
</div>
</bds-carousel-slide><bds-carousel-slide>
<div class="_slide_z883j_150">
<figure class="_frame_1wolg_15">
<div class="_imageContainer_1wolg_10"><img src="https://lh3.googleusercontent.com/atFKXp9a__9t9cUn3NszKwhdlt6LrRDKjUmm_xA0s1WsBKfNkER5IuQs66EQ72SZrwcn4qQKSMKS0RPHqDuJpetgf8DZ6g36nbK54BI=w2880-e365-pa-nu" loading="lazy" alt /></div>
<figcaption class="_caption_1wolg_19">
<div class="_frame_13anx_99 _caption_13anx_55">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47"><a target="_blank" href="https://blog.google/outreach-initiatives/sustainability/4-flood-forecasting-collaboration-case-studies-show-how-ai-can-help-communities-in-need/">How AI flood forecasting can help communities in need</a></div>
</h4>
<p></p>
</div>
</figcaption>
</figure>
</div>
</bds-carousel-slide><bds-carousel-slide>
<div class="_slide_z883j_150">
<figure class="_frame_1wolg_15">
<div class="_imageContainer_1wolg_10"><img src="https://lh3.googleusercontent.com/qY3Yb44xmq6kSpRRIJgUuOrvnRIaJ8ZwAvMDZOH9B7oFvEGoLfnYZfJRUDscg0_hmIHwFsMog7hC7Pgj-5Uc5fXlX1EU5WqFPftqPA=w2880-e365-pa-nu" loading="lazy" alt /></div>
<figcaption class="_caption_1wolg_19">
<div class="_frame_13anx_99 _caption_13anx_55">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">BBC: <a target="_blank" href="https://www.bbc.com/news/business-67748255">'We want to let people know before floods hit them'</a></div>
</h4>
<p></p>
</div>
</figcaption>
</figure>
</div>
</bds-carousel-slide><bds-carousel-slide>
<div class="_slide_z883j_150">
<figure class="_frame_1wolg_15">
<div class="_imageContainer_1wolg_10"><img src="https://lh3.googleusercontent.com/0iiuxwIRdvTf2KVYMeVBa3ljL1sgfmrMf41p-lB-8c6Q_JE8B7D4fgV7XOrdlo4ZNGTVsHOoIYEeM_HvD_mHKjXRYre1NAKeqUBkEYr4=w2880-e365-pa-nu" loading="lazy" alt /></div>
<figcaption class="_caption_1wolg_19">
<div class="_frame_13anx_99 _caption_13anx_55">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">Bloomberg:Â <a target="_blank" href="https://sponsored.bloomberg.com/article/google-sustainability/How-AI-Is-Helping-Communities-Anticipate-Floods">How AI Is Helping Communities Anticipate Floods</a></div>
</h4>
<p></p>
</div>
</figcaption>
</figure>
</div>
</bds-carousel-slide><bds-carousel-slide>
<div class="_slide_z883j_150">
<figure class="_frame_1wolg_15">
<div class="_imageContainer_1wolg_10"><img src="https://lh3.googleusercontent.com/TPYSjK0Ef0BXnbXpSX5bL1uJjjegop8J4WHPZo-tMVnLhPZ31lyWUbFOmVjeW-3BVPTbppES2v1zPIWUQefNUny7RRxDG96p7VDthw=w2880-e365-pa-nu" loading="lazy" alt /></div>
<figcaption class="_caption_1wolg_19">
<div class="_frame_13anx_99 _caption_13anx_55">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">Blog: <a target="_blank" href="https://blog.google/outreach-initiatives/sustainability/flood-hub-ai-flood-forecasting-more-countries/"><u>Helping more people stay safe with flood forecasting</u></a></div>
</h4>
<p></p>
</div>
</figcaption>
</figure>
</div>
</bds-carousel-slide><bds-carousel-slide>
<div class="_slide_z883j_150">
<figure class="_frame_1wolg_15">
<div class="_imageContainer_1wolg_10"><img src="https://lh3.googleusercontent.com/mKaFJHfp_ltzFMQGIoFS33qsvi-t3U5VhQ7nqltNTZeLz1UeCKrmkgHuXnak83eqNSYku0V6Q4dKabkZQfD0QehnkQESC8LACvA-_LUT=w2880-e365-pa-nu" loading="lazy" alt /></div>
<figcaption class="_caption_1wolg_19">
<div class="_frame_13anx_99 _caption_13anx_55">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">Blog: <a target="_blank" href="https://blog.google/outreach-initiatives/sustainability/environmental-impact-report-2023/"><u>Our 2023 Environmental Report</u></a></div>
</h4>
<p></p>
</div>
</figcaption>
</figure>
</div>
</bds-carousel-slide><bds-carousel-slide>
<div class="_slide_z883j_150">
<figure class="_frame_1wolg_15">
<div class="_imageContainer_1wolg_10"><img src="https://lh3.googleusercontent.com/sBAd7isIc15sHLCxWKZj_bGELUyah8iOGMj_KfAegDXmwEletLrcEUKGXBKuA2f8L1lIjXcnrIwI_3fj9JoocXwrn4UbGJFiqAg9eR4=w2880-e365-pa-nu" loading="lazy" alt /></div>
<figcaption class="_caption_1wolg_19">
<div class="_frame_13anx_99 _caption_13anx_55">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">Blog: <a target="_blank" href="https://blog.google/outreach-initiatives/sustainability/early-warning-system-wmo-google/"><u>How Google is supporting the WMOâs early warning system</u></a></div>
</h4>
<p></p>
</div>
</figcaption>
</figure>
</div>
</bds-carousel-slide><bds-carousel-slide>
<div class="_slide_z883j_150">
<figure class="_frame_1wolg_15">
<div class="_imageContainer_1wolg_10"><img src="https://lh3.googleusercontent.com/guxyl2-9nWUM-ENFCzPWZLL1IFPE5vQUwHl5s0KaQD-rJgPgTf5sfE47zMMBqFZNCQyGQ9vtJQDs4pD_OtPOYxPeJz5gQauLt8jAAvic=w2880-e365-pa-nu" loading="lazy" alt /></div>
<figcaption class="_caption_1wolg_19">
<div class="_frame_13anx_99 _caption_13anx_55">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">Axios <a target="_blank" href="https://www.axios.com/2023/05/22/googles-ai-flood-forecast"><u>Google's AI-enabled flood forecasting goes global</u></a> (US)</div>
</h4>
<p></p>
</div>
</figcaption>
</figure>
</div>
</bds-carousel-slide><bds-carousel-slide>
<div class="_slide_z883j_150">
<figure class="_frame_1wolg_15">
<div class="_imageContainer_1wolg_10"><img src="https://lh3.googleusercontent.com/A1xIKxN1M4E5zt3X5ijj40YCTnX4ybrRgY972DN9eg3Eg3LlG5eEQWLyvr_HDk6jMvgN0DA9U9rs7GoZpC_pz1SWb4oL7FurwHL8rN8=w2880-e365-pa-nu" loading="lazy" alt /></div>
<figcaption class="_caption_1wolg_19">
<div class="_frame_13anx_99 _caption_13anx_55">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">El EspaÃ±ol <a target="_blank" href="https://www.elespanol.com/elandroidelibre/noticias-y-novedades/20230521/ia-ayuda-personas-usos-google-sin-enteres/736176592_0.html"><u>Cuando la IA ayuda a las personas: 7 usos que Google le da sin que te enteres</u></a> (Spain)</div>
</h4>
<p></p>
</div>
</figcaption>
</figure>
</div>
</bds-carousel-slide><bds-carousel-slide>
<div class="_slide_z883j_150">
<figure class="_frame_1wolg_15">
<div class="_imageContainer_1wolg_10"><img src="https://lh3.googleusercontent.com/bmogwFF1yiX-Agw-Z7oHapFkxOdOeNIE6_FmAubk-MOq0i-EhzB7URGZOmSXLJhm6KoO5vc1ulZIOM3dz5jrFUYp8ctvYxRKOY1x1g=w2880-e365-pa-nu" loading="lazy" alt /></div>
<figcaption class="_caption_1wolg_19">
<div class="_frame_13anx_99 _caption_13anx_55">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">Computer Bild <a target="_blank" href="https://www.computerbild.de/artikel/cb-News-Internet-Google-FloodHub-fuer-ueber-80-Laender-Hochwasservorhersage-per-KI-35815777.html"><u>Google FloodHub fÃ¼r Ã¼ber 80 LÃ¤nder: Hochwasservorhersage per KI - COMPUTER BILD</u></a> (Germany)</div>
</h4>
<p></p>
</div>
</figcaption>
</figure>
</div>
</bds-carousel-slide><bds-carousel-slide>
<div class="_slide_z883j_150">
<figure class="_frame_1wolg_15">
<div class="_imageContainer_1wolg_10"><img src="https://lh3.googleusercontent.com/Ihcp2IV6ZbzT3Wx33Lc-QL1rDPhgirufZ4RbVvttQwjd7pBoz2-Zxc5ymQp-RvK0N9io5P2Rfg5v2255kINRX5Sh1QVzcH2Fkeq00cE=w2880-e365-pa-nu" loading="lazy" alt /></div>
<figcaption class="_caption_1wolg_19">
<div class="_frame_13anx_99 _caption_13anx_55">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">BFM <a target="_blank" href="https://www.bfmtv.com/tech/google/google-va-desormais-alerter-les-francais-en-cas-de-risque-d-inondation_AN-202305220572.html"><u>Google va dÃ©sormais alerter les FranÃ§ais en cas de risque d'inondation</u></a>Â (France)</div>
</h4>
<p></p>
</div>
</figcaption>
</figure>
</div>
</bds-carousel-slide><bds-carousel-slide>
<div class="_slide_z883j_150">
<figure class="_frame_1wolg_15">
<div class="_imageContainer_1wolg_10"><img src="https://lh3.googleusercontent.com/YPCqbT7NapCpOZJt56tI3wg4cDl-XgjwPM_HdI2I8tf0Tno143V0wMurG88rBFLp4AaoJxMl0j7lDrt8cAzJjye_wiFgky3JgmwPmRdr=w2880-e365-pa-nu" loading="lazy" alt /></div>
<figcaption class="_caption_1wolg_19">
<div class="_frame_13anx_99 _caption_13anx_55">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">Blog: <a target="_blank" href="https://ai.googleblog.com/2023/04/directing-ml-toward-natural-hazard.html"><u>Directing ML toward natural hazard mitigation through collaboration</u></a> </div>
</h4>
<p></p>
</div>
</figcaption>
</figure>
</div>
</bds-carousel-slide><bds-carousel-slide>
<div class="_slide_z883j_150">
<figure class="_frame_1wolg_15">
<div class="_imageContainer_1wolg_10"><img src="https://lh3.googleusercontent.com/qjCUC1YicOr6-jO0vQU7l-ypwjNw0mVHVwO_3R8OGL53JWENbvG-hjwbysxzgbVGsIyneukdSZ2sRJ6jTCjbtMgjn0u2TPa4O_OXU14=w2880-e365-pa-nu" loading="lazy" alt /></div>
<figcaption class="_caption_1wolg_19">
<div class="_frame_13anx_99 _caption_13anx_55">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">Video: <a target="_blank" href="https://www.youtube.com/watch?v=Klu3zlbUy0Y&amp;app=desktop"><u>How to get started with the Google Flood Hub</u></a> </div>
</h4>
<p></p>
</div>
</figcaption>
</figure>
</div>
</bds-carousel-slide><bds-carousel-slide>
<div class="_slide_z883j_150">
<figure class="_frame_1wolg_15">
<div class="_imageContainer_1wolg_10"><img src="https://lh3.googleusercontent.com/ubVfI3M5piZZOnVZc8EB4E_RbVqzrv6gCfuv2mH80lm5cWIYncRwKAl-b9JbVxLCFKt9Ykj8NdNu-wcoisQ9g_NEhX-3Ds5TUPSqHg=w2880-e365-pa-nu" loading="lazy" alt /></div>
<figcaption class="_caption_1wolg_19">
<div class="_frame_13anx_99 _caption_13anx_55">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">Wired:Â <a target="_blank" href="https://www.wired.com/story/google-ai-wildfire-flood-tracking/">Google expands floods and wildfire tracking to more countries</a></div>
</h4>
<p></p>
</div>
</figcaption>
</figure>
</div>
</bds-carousel-slide><bds-carousel-slide>
<div class="_slide_z883j_150">
<figure class="_frame_1wolg_15">
<div class="_imageContainer_1wolg_10"><img src="https://lh3.googleusercontent.com/a7p2HJpaimQozktSJEXrH2tJmucAEkHfp4zfUbAI38Non-4Q1_zYQGXVJd-Uo3WGTcXAxGjFuPVdOtgIDzYn7ZBxIdpZpBzlTwiWOxM=w2880-e365-pa-nu" loading="lazy" alt /></div>
<figcaption class="_caption_1wolg_19">
<div class="_frame_13anx_99 _caption_13anx_55">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">The Verge:Â <a target="_blank" href="https://www.theverge.com/2022/11/2/23434777/google-wildfire-flood-tracking-expands-floodhub-app">Google expands flood and wildfire tracking</a></div>
</h4>
<p></p>
</div>
</figcaption>
</figure>
</div>
</bds-carousel-slide><bds-carousel-slide>
<div class="_slide_z883j_150 _roundedRightSlide_z883j_203">
<figure class="_frame_1wolg_15">
<div class="_imageContainer_1wolg_10"><img src="https://lh3.googleusercontent.com/ASF2kHGpX1xDWRW0d1Hf4P-VV6JTXwXXuqufYUjt-Yo3OR_a_kIdfR-r6MfcWVNOGMHiYRPD23WdezBRa6THFI1D8E5ZluVc0hDifQ=w2880-e365-pa-nu" loading="lazy" alt /></div>
<figcaption class="_caption_1wolg_19">
<div class="_frame_13anx_99 _caption_13anx_55">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">Blog: <a target="_blank" href="https://blog.google/outreach-initiatives/sustainability/cop27-adaptation-efforts/"><u>How we're using AI to help address the climate crisis</u></a>Â </div>
</h4>
<p></p>
</div>
</figcaption>
</figure>
</div>
</bds-carousel-slide><bds-carousel-slide>
<div class="_slide_z883j_150 _marginSlide_z883j_165"></div>
</bds-carousel-slide></bds-carousel></div>
</div>
<div class="_container_3mwgq_1 _filled_3mwgq_10"></div>
<div class="_container_3mwgq_1"></div>
<div id="floods_publications" class="_container_1xa7h_1">
<div class="_item_1xa7h_67" style="--grid-item-start: 1; --grid-item-end: 12;">
<div class="_container_or7p1_1">
<div class="_frame_13anx_99 _container_1r2da_1 _body_13anx_63 _body_13anx_63">
<h3 size="3" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading3_13anx_32">Publications</div>
</h3>
<p><u></u><a target="_blank" href="https://www.nature.com/articles/s41586-024-07145-1"><u>Global prediction of extreme floods in ungauged watersheds</u></a>, Grey Nearing, Deborah Cohen, Vusumuzi Dube, Martin Gauch, Oren Gilon, Shaun Harrigan, Avinatan Hassidim, Daniel Klotz, Frederik Kratzert, Asher Metzger, Sella Nevo, Florian Pappenberger, Christel Prudhomme, Guy Shalev, Shlomo Shenzis, Tadele Yednkachw Tekalign, Dana Weitzner &amp; Yossi Matias. <i>Nature, March 2024.</i></p>
<p><a target="_blank" href="https://www.nature.com/articles/s41597-023-01975-w"><u>Caravan - A Global Community Dataset for Large-sample Hydrology</u></a>, Frederik Kratzert, Grey Nearing, Nans Addor, Tyler Erickson, Martin Gauch, Oren Gilon, Lukas Gudmundsson, Avinatan Hassidim, Daniel Klotz, Sella Nevo, Guy Shalev &amp; Yossi Matias.<i> Scientific Data, 2023.</i></p>
<p><u></u><a target="_blank" href="https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2022WR033918"><u>In Defense of Metrics: Metrics Sufficiently Encode Typical Human Preferences Regarding Hydrological Model Performance</u></a>, Martin Gauch, Frederik Kratzert, Oren Gilon, Hoshin Gupta, Juliane Mai, Grey Nearing, Bryan Tolson, Sepp Hochreiter, Daniel Klotz. <i>Water Resources Research, May 2023.</i></p>
<p><a target="_blank" href="https://hess.copernicus.org/articles/26/5493/2022/"><u>Technical Note: Data assimilation and autoregression for using near-real-time streamflow observations in long short-term memory networks</u></a>, Grey Nearing, Daniel Klotz, Jonathan Frame, Martin Gauch, Oren Gilon, Frederik Kratzert, Alden Keefe Sampson, Guy Shalev, and Sella Nevo. <i>Hydrology and Earth Systems Science (HESS), 2022.</i></p>
<p><a target="_blank" href="https://hess.copernicus.org/articles/26/3377/2022/hess-26-3377-2022.html"><u>Deep learning rainfall-runoff predictions of extreme events</u></a>, Jonathan Frame, Frederik Kratzert, Daniel Klotz, Martin Gauch, Guy Shalev, Oren Gilon, Logan Qualls, Hoshin Gupta, and Grey S. Nearing. <i>Hydrology and Earth Systems Science (HESS), 2022.</i></p>
<p><a target="_blank" href="https://hess.copernicus.org/articles/26/4013/2022/"><u>Flood forecasting with machine learning models in an operational framework</u></a> Sella Nevo, Efrat Morin, Adi Gerzi Rosenthal, Asher Metzger, Chen Barshai, Dana Weitzner, Dafi Voloshin, Frederik Kratzert, Gal Elidan, Gideon Dror, Gregory Begelman, Grey Nearing, Guy Shalev, Hila Noga, Ira Shavitt, Liora Yuklea, Moriah Royz, Niv Giladi, Nofar Peled Levi, Ofir Reich, Oren Gilon, Ronnie Maor, Shahar Timnat, Tal Shechter, Vladimir Anisimov, Yotam Gigi, Yuval Levin, Zach Moshe, Zvika Ben-Haim, Avinatan Hassidim, and Yossi Matias. <i>Hydrology and Earth Systems Science (HESS), 2022.</i></p>
<p><a target="_blank" href="https://arxiv.org/abs/2204.10323"><u>Accelerating Physics Simulations with TPUs: An Inundation Modeling Example</u></a>, Damien Pierce, R. Lily Hu, Yusef Shafi, Anudhyan Boral, Vladimir Anisimov, Sella Nevo, Yi-fan Chen. <i>International Journal of High Performance Computing Applications (IJHPCA), 2022.</i></p>
<p><a target="_blank" href="https://hess.copernicus.org/articles/23/5089/2019/"><u>Towards learning universal, regional, and local hydrological behaviors via machine learning applied to large-sample datasets</u></a>, Frederik Kratzert, Daniel Klotz, Guy Shalev, GÃ¼nter Klambauer, Sepp Hochreiter, and Grey Nearing,<i> Hess, 2019</i></p>
<p><a target="_blank" href="https://arxiv.org/abs/1901.09583"><u>ML for Flood Forecasting at Scale</u></a>,Â  Sella Nevo, Vova Anisimov, Gal Elidan, Ran El-Yaniv, Pete Giencke, Yotam Gigi, Avinatan Hassidim, Zach Moshe, Mor Schlesinger, Guy Shalev, Ajai Tirumali, Ami Wiesel, Oleg Zlydenko, Yossi Matias, <i>Jan 2018</i></p>
</div>
</div>
</div>
</div>
<div class="_container_3mwgq_1"></div>
<div trigger-together>
<div id="floods_faq" class="_container_1xa7h_1">
<div class="_item_1xa7h_67" style="--grid-item-start: 1; --grid-item-end: 12;">
<div class="_container_55vns_1" style="--stack-gap: 28px;">
<div>
<h2 size="2" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading2_13anx_17">FAQs</div>
</h2>
</div>
<div>
<details class="_details_1heq1_6" style="--inview-delay: 0.2s">
<summary>
<div>
<div class="_frame_13anx_99 _body_13anx_63 _bodyLarge_13anx_71">Why is Google doing this?</div>
</div><svg aria-hidden="true" width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M11.115 23.1152L18 16.2452L24.885 23.1152L27 21.0002L18 12.0002L9 21.0002L11.115 23.1152Z" fill="#174EA6"></path>
</svg>
</summary>
<div class="_detailsAnswer_1heq1_58">
<div class="_frame_13anx_99 _container_1r2da_1 _body_13anx_63 _body_13anx_63">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">At Google, weâre investing in technologies that can help communities prepare for and respond to climate-related disasters and threats. As part of our <a target="_blank" href="https://crisisresponse.google/forecasting-and-alerts/"><u>Crisis Response</u></a> efforts, we're working to bring trusted information to people in critical moments to keep them safe and informed. To do so, we rely on the research and development of our AI-powered technologies and longstanding partnerships with frontline emergency workers and organizations. Our goal with this program is to provide accurate and actionable flood alerts covering all affected by floods globally. </div>
</h4>
<p>
</p>
<p>
</p>
</div>
</div>
</details>
<details class="_details_1heq1_6" style="--inview-delay: 0.4s">
<summary>
<div>
<div class="_frame_13anx_99 _body_13anx_63 _bodyLarge_13anx_71">What is not covered?</div>
</div><svg aria-hidden="true" width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M11.115 23.1152L18 16.2452L24.885 23.1152L27 21.0002L18 12.0002L9 21.0002L11.115 23.1152Z" fill="#174EA6"></path>
</svg>
</summary>
<div class="_detailsAnswer_1heq1_58">
<div class="_frame_13anx_99 _container_1r2da_1 _body_13anx_63 _body_13anx_63">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">We currently focus only on riverine floods, as opposed to flash and coastal floods. We also do not generate flood maps for urban areas.</div>
</h4>
<p></p>
</div>
</div>
</details>
<details class="_details_1heq1_6" style="--inview-delay: 0.6000000000000001s">
<summary>
<div>
<div class="_frame_13anx_99 _body_13anx_63 _bodyLarge_13anx_71">What is unique about Googleâs models?</div>
</div><svg aria-hidden="true" width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M11.115 23.1152L18 16.2452L24.885 23.1152L27 21.0002L18 12.0002L9 21.0002L11.115 23.1152Z" fill="#174EA6"></path>
</svg>
</summary>
<div class="_detailsAnswer_1heq1_58">
<div class="_frame_13anx_99 _container_1r2da_1 _body_13anx_63 _body_13anx_63">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">The Google hydrology model is the first operational model that uses machine learning to generate improved hydrology forecasts in more locations globally.</div>
</h4>
<p></p>
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">The Google inundation maps model is one of the few flood models that generate maps that allow to identify which villages or areas are going to be flooded given a specific hydrology forecast.</div>
</h4>
<p>
</p>
</div>
</div>
</details>
<details class="_details_1heq1_6" style="--inview-delay: 0.8s">
<summary>
<div>
<div class="_frame_13anx_99 _body_13anx_63 _bodyLarge_13anx_71">How often are forecasts updated?</div>
</div><svg aria-hidden="true" width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M11.115 23.1152L18 16.2452L24.885 23.1152L27 21.0002L18 12.0002L9 21.0002L11.115 23.1152Z" fill="#174EA6"></path>
</svg>
</summary>
<div class="_detailsAnswer_1heq1_58">
<div class="_frame_13anx_99 _container_1r2da_1 _body_13anx_63 _body_13anx_63">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">Forecasts are updated daily based on the most up-to-date meteorological data available. The forecasts are also in daily resolution.</div>
</h4>
<p></p>
</div>
</div>
</details>
<details class="_details_1heq1_6" style="--inview-delay: 1s">
<summary>
<div>
<div class="_frame_13anx_99 _body_13anx_63 _bodyLarge_13anx_71">What is the data source for the models?</div>
</div><svg aria-hidden="true" width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M11.115 23.1152L18 16.2452L24.885 23.1152L27 21.0002L18 12.0002L9 21.0002L11.115 23.1152Z" fill="#174EA6"></path>
</svg>
</summary>
<div class="_detailsAnswer_1heq1_58">
<div class="_frame_13anx_99 _container_1r2da_1 _body_13anx_63 _body_13anx_63">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">We do not use any of the countries' proprietary data, but a variety of weather products, including <a target="_blank" href="https://www.ecmwf.int/en/forecasts"><u>ECMWF forecasts</u></a>, <a target="_blank" href="https://climatedataguide.ucar.edu/climate-data/cpc-unified-gauge-based-analysis-global-daily-precipitation"><u>CPC rain gauge measurements</u></a>,<u> </u><a target="_blank" href="https://gpm.nasa.gov/data/imerg"><u>IMERG precipitation</u></a><u> </u>and Copernicus Sentinel-1 satellites of the European Space Agency. Sentinel-1 is a C-band SAR satellite. We then use our algorithms to calculate the flooded area based on the SAR image.</div>
</h4>
<p></p>
</div>
</div>
</details>
<details class="_details_1heq1_6" style="--inview-delay: 1.2000000000000002s">
<summary>
<div>
<div class="_frame_13anx_99 _body_13anx_63 _bodyLarge_13anx_71">Why arenât forecasts available in my region?</div>
</div><svg aria-hidden="true" width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M11.115 23.1152L18 16.2452L24.885 23.1152L27 21.0002L18 12.0002L9 21.0002L11.115 23.1152Z" fill="#174EA6"></path>
</svg>
</summary>
<div class="_detailsAnswer_1heq1_58">
<div class="_frame_13anx_99 _container_1r2da_1 _body_13anx_63 _body_13anx_63">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">We are working on gradually rolling out forecasts in more regions. Google only approves the release of data and forecasts in locations that have been thoroughly evaluated and are deemed to be of sufficient quality. We are continuously evaluating new locations and improving the quality of our forecasts as necessary to launch flood forecasts in more areas of the world.</div>
</h4>
<p></p>
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">The availability of local historical discharge records dramatically improves model quality. If you would like to contribute discharge data to facilitate coverage in your area, please consider looking at the <a target="_blank" href="https://github.com/kratzert/Caravan"><u>Caravan project</u></a>, which facilitates publishing streamflow data, combined with meteorological forcing data and catchment attributes.</div>
</h4>
<p></p>
</div>
</div>
</details>
<details class="_details_1heq1_6" style="--inview-delay: 1.4000000000000001s">
<summary>
<div>
<div class="_frame_13anx_99 _body_13anx_63 _bodyLarge_13anx_71">What models are used by the system?</div>
</div><svg aria-hidden="true" width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M11.115 23.1152L18 16.2452L24.885 23.1152L27 21.0002L18 12.0002L9 21.0002L11.115 23.1152Z" fill="#174EA6"></path>
</svg>
</summary>
<div class="_detailsAnswer_1heq1_58">
<div class="_frame_13anx_99 _container_1r2da_1 _body_13anx_63 _body_13anx_63">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">As is common in riverine flood forecasting systems, there are two types of models involved in producing these alerts: a hydrologic model that calculates the one-dimensional flow in the river, and an inundation model that uses the flow to calculate a flood map.</div>
</h4>
<p>
</p>
</div>
</div>
</details>
<details class="_details_1heq1_6" style="--inview-delay: 1.6s">
<summary>
<div>
<div class="_frame_13anx_99 _body_13anx_63 _bodyLarge_13anx_71">What input data is used by the system?</div>
</div><svg aria-hidden="true" width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M11.115 23.1152L18 16.2452L24.885 23.1152L27 21.0002L18 12.0002L9 21.0002L11.115 23.1152Z" fill="#174EA6"></path>
</svg>
</summary>
<div class="_detailsAnswer_1heq1_58">
<div class="_frame_13anx_99 _container_1r2da_1 _body_13anx_63 _body_13anx_63">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">The model uses different sets of features in different parts of the model, namely the hindcast LSTM (the part of the model that summarizes the past until the point of the issued forecast) and the forecast LSTM.</div>
</h4>
<ul>
<li>
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">Input features to the hindcast portion of the model are <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.cpc.globalprecip.html">CPC precipitation</a>, <a target="_blank" href="https://gpm.nasa.gov/data/imerg">IMERG precipitation</a>, ECMWF IFS nowcasts, including precipitation, temperature, and other surface (single-level) variables.</div>
</h4>
</li>
<li>
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">Input features to the forecast portion of the model are various <a target="_blank" href="https://www.ecmwf.int/en/forecasts/datasets/set-i">ECMWF IFS-HRES bands</a> from the most recently issued IFS forecast, including precipitation, temperature, solar radiation, windspeed, and surface pressure.</div>
</h4>
</li>
<li>
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">Additionally, both parts of the model (hindcast and forecast) use static geophysical attributes derived from <a target="_blank" href="https://www.hydrosheds.org/hydroatlas">HydroATLAS</a>, alongside climate indices derived from long-term records from <a target="_blank" href="https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-land?tab=overview">ERA5-Land</a>.</div>
</h4>
</li>
</ul>
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">More meteorological data products will be added to the model to improve the prediction quality (see for example <a target="_blank" href="https://hess.copernicus.org/articles/25/2685/2021/hess-25-2685-2021.html">this publication</a> for details on the effect of using multiple forcing products).</div>
</h4>
<p>
</p>
</div>
</div>
</details>
<details class="_details_1heq1_6" style="--inview-delay: 1.8s">
<summary>
<div>
<div class="_frame_13anx_99 _body_13anx_63 _bodyLarge_13anx_71">Where can I get a historical record of your forecasts?</div>
</div><svg aria-hidden="true" width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M11.115 23.1152L18 16.2452L24.885 23.1152L27 21.0002L18 12.0002L9 21.0002L11.115 23.1152Z" fill="#174EA6"></path>
</svg>
</summary>
<div class="_detailsAnswer_1heq1_58">
<div class="_frame_13anx_99 _container_1r2da_1 _body_13anx_63 _body_13anx_63">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">We archive most of our forecasts in a publicly available dataset, see documentation <a target="_blank" href="https://docs.google.com/document/d/e/2PACX-1vSqZ53gvCDXGIoH8xVRD6C_7QynuIuwepQq5a7BfbrnQ8mmk5lcKQmCy3pI5Ki2rsLc6vv8D5x5a4_P/pub">here</a>.</div>
</h4>
<p>
</p>
</div>
</div>
</details>
<details class="_details_1heq1_6" style="--inview-delay: 2s">
<summary>
<div>
<div class="_frame_13anx_99 _body_13anx_63 _bodyLarge_13anx_71">Why do some places show flood maps while others donât?</div>
</div><svg aria-hidden="true" width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M11.115 23.1152L18 16.2452L24.885 23.1152L27 21.0002L18 12.0002L9 21.0002L11.115 23.1152Z" fill="#174EA6"></path>
</svg>
</summary>
<div class="_detailsAnswer_1heq1_58">
<div class="_frame_13anx_99 _container_1r2da_1 _body_13anx_63 _body_13anx_63">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">We evaluate the hydrologic and inundation models separately. In some regions, we see that our hydrologic models are very accurate when compared to ground truth information, but the inundation models do not show clear and regular inundation patterns. In these regions we decide to only share the hydrologic information.</div>
</h4>
<p>
</p>
</div>
</div>
</details>
<details class="_details_1heq1_6" style="--inview-delay: 2.2s">
<summary>
<div>
<div class="_frame_13anx_99 _body_13anx_63 _bodyLarge_13anx_71">How does Google deal with dams on rivers? </div>
</div><svg aria-hidden="true" width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M11.115 23.1152L18 16.2452L24.885 23.1152L27 21.0002L18 12.0002L9 21.0002L11.115 23.1152Z" fill="#174EA6"></path>
</svg>
</summary>
<div class="_detailsAnswer_1heq1_58">
<div class="_frame_13anx_99 _container_1r2da_1 _body_13anx_63 _body_13anx_63">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">Since our flood forecasting models are based on machine learning algorithms (as opposed to classic physics-based models), our models can incorporate dam behavior implicitly (i.e. we donât need to explicitly code that in). Weâve seen very good performance of our models including in basins that are heavily instrumented and affected by dams.Â </div>
</h4>
<p></p>
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">We are also working towards more explicit incorporation of dams, and also using our models to provide recommendations for dam management. This is currently in pilot research phase (in collaboration with the Indian government), and may become a service we provide in the future.</div>
</h4>
<p>
</p>
</div>
</div>
</details>
<details class="_details_1heq1_6" style="--inview-delay: 2.4000000000000004s">
<summary>
<div>
<div class="_frame_13anx_99 _body_13anx_63 _bodyLarge_13anx_71">How was the benchmarking done for Google models against GloFAS?</div>
</div><svg aria-hidden="true" width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M11.115 23.1152L18 16.2452L24.885 23.1152L27 21.0002L18 12.0002L9 21.0002L11.115 23.1152Z" fill="#174EA6"></path>
</svg>
</summary>
<div class="_detailsAnswer_1heq1_58">
<div class="_frame_13anx_99 _container_1r2da_1 _body_13anx_63 _body_13anx_63">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">The benchmarking was done in collaboration with the GloFAS team itself. It involved testing the accuracy of our models relative to their models on all points in the world where we have gauge measurements (and therefore can know what the âcorrect predictionâ is). We are currently working on submitting these results, together with GloFAS, to Nature.
</div>
</h4>
<p></p>
</div>
</div>
</details>
<details class="_details_1heq1_6" style="--inview-delay: 2.6s">
<summary>
<div>
<div class="_frame_13anx_99 _body_13anx_63 _bodyLarge_13anx_71">If a country wishes to provide historical or real-time gauge data, how will this improve accuracy? Which data is needed?</div>
</div><svg aria-hidden="true" width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M11.115 23.1152L18 16.2452L24.885 23.1152L27 21.0002L18 12.0002L9 21.0002L11.115 23.1152Z" fill="#174EA6"></path>
</svg>
</summary>
<div class="_detailsAnswer_1heq1_58">
<div class="_frame_13anx_99 _container_1r2da_1 _body_13anx_63 _body_13anx_63">
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">If a country provides historical or real-time data we can use this to further train (or âcalibrateâ) the model, leading to a significant improvement in prediction quality at the location of the data (could even be 10% in NSE scores or more), and a more modest improvement in other locations. In the future we will also be able to incorporate real-time data as an input to the model, which will provide an even larger improvement in accuracy.</div>
</h4>
<p></p>
<h4 size="4" class="_heading_1mjz1_1">
<div class="_frame_13anx_99 _heading4_13anx_47">The data needed is discharge measurements at a daily resolution or better (e.g. hourly), with timestamps and the location of the gauge.</div>
</h4>
<p></p>
</div>
</div>
</details>
</div>
</div>
</div>
</div>
</div>
<div class="_container_3mwgq_1 _desktopOnly_3mwgq_28"></div>
</div>
</div>
<link href="https://www.gstatic.com/glue/cookienotificationbar/cookienotificationbar.min.css" rel="stylesheet" />
<script src="https://www.gstatic.com/glue/cookienotificationbar/cookienotificationbar.min.js" data-glue-cookie-notification-bar-category="2B" data-glue-cookie-notification-bar-site-id="sites.research.google"></script>
</body>
</html>
