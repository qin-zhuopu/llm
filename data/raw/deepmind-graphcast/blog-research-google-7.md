# Source: https://blog.research.google/2023/11/metnet-3-state-of-art-neural-weather.html?utm_source=&utm_medium=&utm_campaign=&utm_content=

> 抓取日期: 2026-08-26

---





<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8" />
    
        
<meta name="description" content="Posted by Samier Merchant, Google Research, and Nal Kalchbrenner, Google DeepMind Forecasting weather variables such as precipitation, temperature,..."><meta name="keywords" content="Machine Learning"><link rel="canonical" href="https://research.google/blog/metnet-3-a-state-of-the-art-neural-weather-model-available-in-google-products/" /><meta property="og:title" content="MetNet-3: A state-of-the-art neural weather model available in Google products"><meta property="og:url" content="https://research.google/blog/metnet-3-a-state-of-the-art-neural-weather-model-available-in-google-products/"><meta property="og:description" content="Posted by Samier Merchant, Google Research, and Nal Kalchbrenner, Google DeepMind Forecasting weather variables such as precipitation, temperature,..."><meta property="og:image" content="https://storage.googleapis.com/gweb-research2023-media/original_images/e667f855aee9e830a1c1f9a30b9fdd24-metnethero1.gif"><meta property="og:image:secure_url" content="https://storage.googleapis.com/gweb-research2023-media/original_images/e667f855aee9e830a1c1f9a30b9fdd24-metnethero1.gif"><meta property="og:type" content="Website">

    
    
    <title>MetNet-3: A state-of-the-art neural weather model available in Google products</title>
    
    <meta name="description" content="Posted by Samier Merchant, Google Research, and Nal Kalchbrenner, Google DeepMind Forecasting weather variables such as precipitation, temperature,..." />
    
    <meta name="viewport" content="width=device-width, initial-scale=1 viewport-fit=cover"/>

    
    

    <link rel="icon" type="image/png" href="https://www.gstatic.com/images/branding/googleg_gradient/1x/googleg_gradient_standard_20dp.png">

    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preload"
        href="https://fonts.googleapis.com/css2?family=Google+Sans+Flex:opsz,wght@6..144,1..1000&family=Product+Sans&display=swap"
        as="style">
    <link rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Google+Sans+Flex:opsz,wght@6..144,1..1000&family=Product+Sans&display=swap">
    <link rel="preload"
        href="https://fonts.googleapis.com/css2?family=Product+Sans&family=Google+Sans+Display:ital@0;1&family=Google+Sans:ital,wght@0,400;0,500;0,700;1,400;1,500;1,700&family=Google+Sans+Text:ital,wght@0,400;0,500;0,700;1,400;1,500;1,700&display=swap"
        as="style">
    <link rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Product+Sans&family=Google+Sans+Display:ital@0;1&family=Google+Sans:ital,wght@0,400;0,500;0,700;1,400;1,500;1,700&family=Google+Sans+Text:ital,wght@0,400;0,500;0,700;1,400;1,500;1,700&display=swap">
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&display=swap" rel="stylesheet">
    <link rel="preload" href="https://fonts.googleapis.com/css2?family=Google+Symbols:opsz,wght,FILL,GRAD,ROND@48,100..300,0..1,0,100&display=swap" as="style" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Symbols:opsz,wght,FILL,GRAD,ROND@48,100..300,0..1,0,100&display=swap">

    
    <link href="https://www.gstatic.com/glue/cookienotificationbar/cookienotificationbar.min.css" rel="stylesheet" />
    <link href="https://www.gstatic.com/glue/v27_1/glue-material.min.css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="/gr/static/css/googleresearch.css?id=1df8cfd093ef74378ad52e9df6e91ef9">
    
    
    

    
    
      <script id="analyticsScript" data-blog-publish-date="20231101"
          data-blog-word-count="1875">
        window.dataLayer = window.dataLayer || [];
        const blogData = document.querySelector('#analyticsScript')

        dataLayer.push({
          publishDate: blogData?.dataset.blogPublishDate,
          wordCount: blogData?.dataset.blogWordCount,
        });
      </script>
    

    <!-- Google Tag Manager -->
    <script>
      window.dataLayer = window.dataLayer || [];
      function glueCookieNotificationBarLoaded() {
        (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
        new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
        j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
        'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
        })(window,document,'script','dataLayer','GTM-K8QBZ7Q');
      }
    </script>
    <!-- End Google Tag Manager -->
</head>

<body class=" js-google-tag-wrapper" data-gt-page-path="https://research.google/blog/metnet-3-a-state-of-the-art-neural-weather-model-available-in-google-products/" data-env="production">
    
    <div class="button-group skip-link">
      <a href="#page-content" class="glue-button glue-button--high-emphasis">Skip to main content</a>
    </div>
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-K8QBZ7Q"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <!-- End Google Tag Manager (noscript) -->
    
    
      




  
    
    
      
        
  <site-nav>
    <header class="site-navigation-isolation header glue-header glue-header--no-cta deepai-header js-header js-site-navigation">
      <div class="header-container">
        <div class="header__background mobile tablet"></div>
        
          <div class="header flyout__desktop-container">
            
              
                
<nav class="header flyout desktop"
    data-section="Research"
    aria-labelledby="Research">
  <div class="flyout__container grid">
    
    <div class="flyout__intro">
      <div>
        <h2 class="headline-6">Explore our many areas of focus</h2>
        
      </div>
      
        <div class="button-group button-group--compact">
          <div class="button-group__buttons">
            
              



  
  
    <a href="/research-areas/"
      
      
       class="glue-button glue-button--medium-emphasis cta-small"
      
      
        data-gtm-event="nav_select"
        data-event-nav-type="subheader"
        data-event-nav-name="Research - Explore all research areas"
      
      
      >
      <div class="button__label">
        
          Explore all research areas
        
      </div>
    </a>
  


            
          </div>
        </div>
      
    </div>

    
    <div class="flyout__content-desktop">
      <div class="flyout__subnav subnav subnav--3-column">
        
          <div class="subnav__column">
            <div class="subnav__content">
              
                <div class="subnav__header">
                  
                    <div class="cta-small">Applied AI &amp; sciences</div>
                  
                  
                </div>
              

              
              
                <div class="subnav__links">
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/google-earth-ai/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/earth_AI_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="earth_AI_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Earth AI</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/health-ai/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/health_AI_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="health_AI_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Health AI</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/science-ai/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/science_AI_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="science_AI_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Science AI</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/sustainability-crisis-resilience/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/sustainability_crisis_resilience_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="sustainability_crisis_resilience_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Sustainability &amp; crisis resilience</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                </div>
              

              
              
            </div>
          </div>
        
          <div class="subnav__column">
            <div class="subnav__content">
              
                <div class="subnav__header">
                  
                    <div class="cta-small">Foundational ML &amp; algorithms</div>
                  
                  
                </div>
              

              
              
                <div class="subnav__links">
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/algorithms-and-theory/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/algorithms_theory_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="algorithms_theory_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Algorithms &amp; theory</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/information-retrieval/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/information_retrieval_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="information_retrieval_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Information retrieval</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/machine-intelligence/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/machine_intelligence_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="machine_intelligence_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Machine intelligence</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/machine-perception/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/machine_perception_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="machine_perception_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Machine perception</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/natural-language-processing/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/NLP_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="NLP_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Natural language processing</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                </div>
              

              
              
            </div>
          </div>
        
          <div class="subnav__column">
            <div class="subnav__content">
              
                <div class="subnav__header">
                  
                    <div class="cta-small">People, systems &amp; quantum AI</div>
                  
                  
                </div>
              

              
              
                <div class="subnav__links">
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/human-computer-interaction-and-visualization/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/human_computer_interaction_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="human_computer_interaction_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Human-computer interaction and visualization</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/networking/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/networking_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="networking_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Networking</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/quantum-computing/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/quantum_AI_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="quantum_AI_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Quantum AI</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/responsible-ai/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/responsible_AI_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="responsible_AI_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Responsible AI</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/anti-abuse/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/anti_abuse_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="anti_abuse_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Anti abuse</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/software-engineering/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/software_engineering_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="software_engineering_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Software engineering</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/software-systems/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/software_systems_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="software_systems_nav1">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Software systems</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                </div>
              

              
              
            </div>
          </div>
        
          <div class="subnav__column">
            <div class="subnav__content">
              
                <div class="subnav__header">
                  
                    <div class="cta-small">Learn More</div>
                  
                  
                </div>
              

              
              
                <div class="subnav__links">
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/pubs/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/publications_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="publications_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Publications</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/resources/our-projects/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/projects_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="projects_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Projects</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                </div>
              

              
              
            </div>
          </div>
        
      </div>
    </div>
  </div>
</nav>
              
            
              
                
<nav class="header flyout desktop"
    data-section="Resources"
    aria-labelledby="Resources">
  <div class="flyout__container grid">
    
    <div class="flyout__intro">
      <div>
        <h2 class="headline-6">Building a collaborative ecosystem</h2>
        
      </div>
      
    </div>

    
    <div class="flyout__content-desktop">
      <div class="flyout__subnav subnav subnav--2-column">
        
          <div class="subnav__column">
            <div class="subnav__content">
              

              
              
                <div class="subnav__links">
                  
                    
                      
                      <a class="subnav__link cta-small  subnav__link--has-icon"
                          href="https://research.google/resources/#datasets-1"
                          
                            target="_self"
                          >
                        
                          <div class="subnav__link-image subnav__link-image--large">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/dataset_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="dataset_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Datasets</div>
                          <div class="small-text">Access high-quality datasets to accelerate your research.</div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small  subnav__link--has-icon"
                          href="https://research.google/resources/#tools-services-2"
                          
                            target="_self"
                          >
                        
                          <div class="subnav__link-image subnav__link-image--large">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/models_products_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="models_products_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Tools &amp; services</div>
                          <div class="small-text">Explore our latest AI models and products.</div>
                        </div>
                      </a>
                      
                    
                  
                </div>
              

              
              
            </div>
          </div>
        
          <div class="subnav__column">
            <div class="subnav__content">
              

              
              
                <div class="subnav__links">
                  
                    
                      
                      <a class="subnav__link cta-small  subnav__link--has-icon"
                          href="https://research.google/resources/#open-source-3"
                          
                            target="_self"
                          >
                        
                          <div class="subnav__link-image subnav__link-image--large">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/software_engineering_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="software_engineering_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Open source</div>
                          <div class="small-text">Discover open-source code and collaborate with the community.</div>
                        </div>
                      </a>
                      
                    
                  
                </div>
              

              
              
            </div>
          </div>
        
      </div>
    </div>
  </div>
</nav>
              
            
              
            
              
                
<nav class="header flyout desktop"
    data-section="Careers"
    aria-labelledby="Careers">
  <div class="flyout__container grid">
    
    <div class="flyout__intro">
      <div>
        <h2 class="headline-6">Shaping the future together</h2>
        
      </div>
      
        <div class="button-group button-group--compact">
          <div class="button-group__buttons">
            
              



  
  
    <a href="/programs-and-events/"
      
      
       class="glue-button glue-button--medium-emphasis cta-small"
      
      
        data-gtm-event="nav_select"
        data-event-nav-type="subheader"
        data-event-nav-name="Careers - See all programs"
      
      
      >
      <div class="button__label">
        
          See all programs
        
      </div>
    </a>
  


            
          </div>
        </div>
      
    </div>

    
    <div class="flyout__content-desktop">
      <div class="flyout__subnav subnav subnav--2-column">
        
          <div class="subnav__column">
            <div class="subnav__content">
              

              
              
                <div class="subnav__links">
                  
                    
                      
                      <a class="subnav__link cta-small  subnav__link--has-icon"
                          href="/programs-and-events/faculty-engagement/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--large">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/faculty_programs_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="faculty_programs_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Faculty programs</div>
                          <div class="small-text">Participating in the academic research community through meaningful engagement with university faculty.</div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small  subnav__link--has-icon"
                          href="/programs-and-events/student-engagement/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--large">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/student_programs_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="student_programs_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Student programs</div>
                          <div class="small-text">Supporting the next generation of researchers through a wide range of programming.</div>
                        </div>
                      </a>
                      
                    
                  
                </div>
              

              
              
            </div>
          </div>
        
          <div class="subnav__column">
            <div class="subnav__content">
              

              
              
                <div class="subnav__links">
                  
                    
                      
                      <a class="subnav__link cta-small  subnav__link--has-icon"
                          href="/programs-and-events/2026-google-carbon-removal-and-superpollutant-elimination-rd-awards/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--large">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/RD-programs_nav_f.svg" class="image image--svg picture__image " loading="lazy"  alt="R&amp;D-programs_nav_f">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">R&amp;D programs</div>
                          <div class="small-text">Collaborating with industry and academic experts to support foundational science and innovation.</div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small  subnav__link--has-icon"
                          href="/careers/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--large">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/locations_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="locations_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Locations</div>
                          <div class="small-text">Find your place in our global offices and research labs.</div>
                        </div>
                      </a>
                      
                    
                  
                </div>
              

              
              
            </div>
          </div>
        
      </div>
    </div>
  </div>
</nav>
              
            
              
            
              
                
<nav class="header flyout desktop"
    data-section="About"
    aria-labelledby="About">
  <div class="flyout__container grid">
    
    <div class="flyout__intro">
      <div>
        <h2 class="headline-6">Translating discovery into real-world impact</h2>
        
      </div>
      
    </div>

    
    <div class="flyout__content-desktop">
      <div class="flyout__subnav subnav subnav--2-column">
        
          <div class="subnav__column">
            <div class="subnav__content">
              

              
              
                <div class="subnav__links">
                  
                    
                      
                      <a class="subnav__link cta-small  subnav__link--has-icon"
                          href="/people/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--large">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/earth_AI_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="earth_AI_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">People</div>
                          <div class="small-text">Our researchers drive advancements in computer science through both fundamental and applied research.</div>
                        </div>
                      </a>
                      
                    
                  
                </div>
              

              
              
            </div>
          </div>
        
          <div class="subnav__column">
            <div class="subnav__content">
              

              
              
                <div class="subnav__links">
                  
                    
                      
                      <a class="subnav__link cta-small  subnav__link--has-icon"
                          href="/teams/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--large">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/teams_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="teams_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Teams</div>
                          <div class="small-text">Collaborative groups tackling the world&#x27;s most challenging AI problems.</div>
                        </div>
                      </a>
                      
                    
                  
                </div>
              

              
              
            </div>
          </div>
        
      </div>
    </div>
  </div>
</nav>
              
            
          </div>
        

        

<nav class="header flyout mobile">
  <div class="flyout__container">
    <div class="flyout__content-mobile">
      
        
          <div class="flyout__accordion">
            
            <button type="button" data-title="Research"
                class="main-menu__label-tablet flyout__accordion__toggle text-call-to-action"
                aria-expanded="false" aria-controls="submenu-1">
              <span class="flyout__accordion__label cta">Research</span>
              <span class="button-group button-group--compact" aria-hidden="true">
                <span class="button-group__buttons">
                  
                  <span class="button flyout__accordion__icon open">
                    <span class="icon-md-outlined">
                      
<svg xmlns="http://www.w3.org/2000/svg"
     height="18px"
     width="18px"
     viewBox="0 -960 960 960"
     fill="currentColor"
     class=""
     aria-hidden="true"
     role="presentation">
  
    <path d="M480-357.85 253.85-584l32.61-32.61L480-423.08l193.54-193.53L706.15-584 480-357.85Z" />
  
</svg>

                    </span>
                  </span>
                  <span class="button flyout__accordion__icon close">
                    <span class="icon-md-outlined">
                      
<svg xmlns="http://www.w3.org/2000/svg"
     height="18px"
     width="18px"
     viewBox="0 -960 960 960"
     fill="currentColor"
     class=""
     aria-hidden="true"
     role="presentation">
  
    <path d="m480-541.85-184 184L253.85-400 480-626.15 706.15-400 664-357.85l-184-184Z" />
  
</svg>

                    </span>
                  </span>
                </span>
              </span>
            </button>
            
            <div id="submenu-1" class="flyout__accordion__content"
                data-section="Research" hidden>
              <div class="flyout__accordion__content-inner">
                <div class="flyout__intro">
                  <div>
                    <h2 class="flyout__title headline-5">Explore our many areas of focus</h2>
                    
                  </div>
                  
                    <div class="button-group button-group--row_start button-group--compact">
                      <div class="button-group__buttons">
                        
                          



  
  
    <a href="/research-areas/"
      
      
       class="glue-button glue-button--medium-emphasis cta-small"
      
      
        data-gtm-event="nav_select"
        data-event-nav-type="subheader"
        data-event-nav-name="Research - Explore all research areas"
      
      
      >
      <div class="button__label">
        
          Explore all research areas
        
      </div>
    </a>
  


                        
                      </div>
                    </div>
                  
                </div>
                <div class="flyout__subnav subnav subnav--3-column">
                  
                    <div class="subnav__column">
                      <div class="subnav__content">
                        
                        
                          
                            <div class="subnav__header">
                              
                                <div class="subnav__title">Applied AI &amp; sciences</div>
                              
                              
                            </div>
                          
                        
                        <div class="subnav__links">
                        
                          
                          
                            
                              
                                <a class="subnav__link"
                                    href="/research-areas/google-earth-ai/"
                                    
                                      
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--small">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/earth_AI_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="earth_AI_nav">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">Earth AI</div>
                                    <div class="subnav__link-description small-text"></div>
                                  </div>
                                </a>
                              
                            
                              
                                <a class="subnav__link"
                                    href="/research-areas/health-ai/"
                                    
                                      
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--small">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/health_AI_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="health_AI_nav">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">Health AI</div>
                                    <div class="subnav__link-description small-text"></div>
                                  </div>
                                </a>
                              
                            
                              
                                <a class="subnav__link"
                                    href="/research-areas/science-ai/"
                                    
                                      
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--small">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/science_AI_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="science_AI_nav">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">Science AI</div>
                                    <div class="subnav__link-description small-text"></div>
                                  </div>
                                </a>
                              
                            
                              
                                <a class="subnav__link"
                                    href="/research-areas/sustainability-crisis-resilience/"
                                    
                                      
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--small">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/sustainability_crisis_resilience_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="sustainability_crisis_resilience_nav">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">Sustainability &amp; crisis resilience</div>
                                    <div class="subnav__link-description small-text"></div>
                                  </div>
                                </a>
                              
                            
                          
                        
                        </div> 

                        
                          
                        
                      </div>
                    </div>
                  
                    <div class="subnav__column">
                      <div class="subnav__content">
                        
                        
                          
                            <div class="subnav__header">
                              
                                <div class="subnav__title">Foundational ML &amp; algorithms</div>
                              
                              
                            </div>
                          
                        
                        <div class="subnav__links">
                        
                          
                          
                            
                              
                                <a class="subnav__link"
                                    href="/research-areas/algorithms-and-theory/"
                                    
                                      
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--small">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/algorithms_theory_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="algorithms_theory_nav">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">Algorithms &amp; theory</div>
                                    <div class="subnav__link-description small-text"></div>
                                  </div>
                                </a>
                              
                            
                              
                                <a class="subnav__link"
                                    href="/research-areas/information-retrieval/"
                                    
                                      
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--small">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/information_retrieval_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="information_retrieval_nav">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">Information retrieval</div>
                                    <div class="subnav__link-description small-text"></div>
                                  </div>
                                </a>
                              
                            
                              
                                <a class="subnav__link"
                                    href="/research-areas/machine-intelligence/"
                                    
                                      
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--small">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/machine_intelligence_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="machine_intelligence_nav">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">Machine intelligence</div>
                                    <div class="subnav__link-description small-text"></div>
                                  </div>
                                </a>
                              
                            
                              
                                <a class="subnav__link"
                                    href="/research-areas/machine-perception/"
                                    
                                      
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--small">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/machine_perception_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="machine_perception_nav">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">Machine perception</div>
                                    <div class="subnav__link-description small-text"></div>
                                  </div>
                                </a>
                              
                            
                              
                                <a class="subnav__link"
                                    href="/research-areas/natural-language-processing/"
                                    
                                      
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--small">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/NLP_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="NLP_nav">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">Natural language processing</div>
                                    <div class="subnav__link-description small-text"></div>
                                  </div>
                                </a>
                              
                            
                          
                        
                        </div> 

                        
                          
                        
                      </div>
                    </div>
                  
                    <div class="subnav__column">
                      <div class="subnav__content">
                        
                        
                          
                            <div class="subnav__header">
                              
                                <div class="subnav__title">People, systems &amp; quantum AI</div>
                              
                              
                            </div>
                          
                        
                        <div class="subnav__links">
                        
                          
                          
                            
                              
                                <a class="subnav__link"
                                    href="/research-areas/human-computer-interaction-and-visualization/"
                                    
                                      
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--small">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/human_computer_interaction_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="human_computer_interaction_nav">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">Human-computer interaction and visualization</div>
                                    <div class="subnav__link-description small-text"></div>
                                  </div>
                                </a>
                              
                            
                              
                                <a class="subnav__link"
                                    href="/research-areas/networking/"
                                    
                                      
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--small">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/networking_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="networking_nav">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">Networking</div>
                                    <div class="subnav__link-description small-text"></div>
                                  </div>
                                </a>
                              
                            
                              
                                <a class="subnav__link"
                                    href="/research-areas/quantum-computing/"
                                    
                                      
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--small">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/quantum_AI_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="quantum_AI_nav">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">Quantum AI</div>
                                    <div class="subnav__link-description small-text"></div>
                                  </div>
                                </a>
                              
                            
                              
                                <a class="subnav__link"
                                    href="/research-areas/responsible-ai/"
                                    
                                      
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--small">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/responsible_AI_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="responsible_AI_nav">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">Responsible AI</div>
                                    <div class="subnav__link-description small-text"></div>
                                  </div>
                                </a>
                              
                            
                              
                                <a class="subnav__link"
                                    href="/research-areas/anti-abuse/"
                                    
                                      
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--small">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/anti_abuse_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="anti_abuse_nav">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">Anti abuse</div>
                                    <div class="subnav__link-description small-text"></div>
                                  </div>
                                </a>
                              
                            
                              
                                <a class="subnav__link"
                                    href="/research-areas/software-engineering/"
                                    
                                      
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--small">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/software_engineering_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="software_engineering_nav">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">Software engineering</div>
                                    <div class="subnav__link-description small-text"></div>
                                  </div>
                                </a>
                              
                            
                              
                                <a class="subnav__link"
                                    href="/research-areas/software-systems/"
                                    
                                      
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--small">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/software_systems_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="software_systems_nav1">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">Software systems</div>
                                    <div class="subnav__link-description small-text"></div>
                                  </div>
                                </a>
                              
                            
                          
                        
                        </div> 

                        
                          
                        
                      </div>
                    </div>
                  
                    <div class="subnav__column">
                      <div class="subnav__content">
                        
                        
                          
                            <div class="subnav__header">
                              
                                <div class="subnav__title">Learn More</div>
                              
                              
                            </div>
                          
                        
                        <div class="subnav__links">
                        
                          
                          
                            
                              
                                <a class="subnav__link"
                                    href="/pubs/"
                                    
                                      
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--small">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/publications_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="publications_nav">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">Publications</div>
                                    <div class="subnav__link-description small-text"></div>
                                  </div>
                                </a>
                              
                            
                              
                                <a class="subnav__link"
                                    href="/resources/our-projects/"
                                    
                                      
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--small">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/projects_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="projects_nav">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">Projects</div>
                                    <div class="subnav__link-description small-text"></div>
                                  </div>
                                </a>
                              
                            
                          
                        
                        </div> 

                        
                          
                        
                      </div>
                    </div>
                  
                </div>
              </div>
            </div>
          </div>
        
      
        
          <div class="flyout__accordion">
            
            <button type="button" data-title="Resources"
                class="main-menu__label-tablet flyout__accordion__toggle text-call-to-action"
                aria-expanded="false" aria-controls="submenu-2">
              <span class="flyout__accordion__label cta">Resources</span>
              <span class="button-group button-group--compact" aria-hidden="true">
                <span class="button-group__buttons">
                  
                  <span class="button flyout__accordion__icon open">
                    <span class="icon-md-outlined">
                      
<svg xmlns="http://www.w3.org/2000/svg"
     height="18px"
     width="18px"
     viewBox="0 -960 960 960"
     fill="currentColor"
     class=""
     aria-hidden="true"
     role="presentation">
  
    <path d="M480-357.85 253.85-584l32.61-32.61L480-423.08l193.54-193.53L706.15-584 480-357.85Z" />
  
</svg>

                    </span>
                  </span>
                  <span class="button flyout__accordion__icon close">
                    <span class="icon-md-outlined">
                      
<svg xmlns="http://www.w3.org/2000/svg"
     height="18px"
     width="18px"
     viewBox="0 -960 960 960"
     fill="currentColor"
     class=""
     aria-hidden="true"
     role="presentation">
  
    <path d="m480-541.85-184 184L253.85-400 480-626.15 706.15-400 664-357.85l-184-184Z" />
  
</svg>

                    </span>
                  </span>
                </span>
              </span>
            </button>
            
            <div id="submenu-2" class="flyout__accordion__content"
                data-section="Resources" hidden>
              <div class="flyout__accordion__content-inner">
                <div class="flyout__intro">
                  <div>
                    <h2 class="flyout__title headline-5">Building a collaborative ecosystem</h2>
                    
                  </div>
                  
                </div>
                <div class="flyout__subnav subnav subnav--2-column">
                  
                    <div class="subnav__column">
                      <div class="subnav__content">
                        
                        
                          
                        
                        <div class="subnav__links">
                        
                          
                          
                            
                              
                                <a class="subnav__link subnav__link--has-icon"
                                    href="https://research.google/resources/#datasets-1"
                                    
                                      target="_self"
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--large">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/dataset_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="dataset_nav">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">Datasets</div>
                                    <div class="subnav__link-description small-text">Access high-quality datasets to accelerate your research.</div>
                                  </div>
                                </a>
                              
                            
                              
                                <a class="subnav__link subnav__link--has-icon"
                                    href="https://research.google/resources/#tools-services-2"
                                    
                                      target="_self"
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--large">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/models_products_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="models_products_nav">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">Tools &amp; services</div>
                                    <div class="subnav__link-description small-text">Explore our latest AI models and products.</div>
                                  </div>
                                </a>
                              
                            
                          
                        
                          
                          
                            
                              
                                <a class="subnav__link subnav__link--has-icon"
                                    href="https://research.google/resources/#open-source-3"
                                    
                                      target="_self"
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--large">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/software_engineering_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="software_engineering_nav">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">Open source</div>
                                    <div class="subnav__link-description small-text">Discover open-source code and collaborate with the community.</div>
                                  </div>
                                </a>
                              
                            
                          
                        
                        </div> 

                        
                          
                        
                          
                        
                      </div>
                    </div>
                  
                </div>
              </div>
            </div>
          </div>
        
      
        
          <a href="/conferences-and-events/"
              class="main-menu__label-tablet text-call-to-action cta"
              data-title="Conferences &amp; events"
              
                
              >
            Conferences &amp; events
          </a>
        
      
        
          <div class="flyout__accordion">
            
            <button type="button" data-title="Careers"
                class="main-menu__label-tablet flyout__accordion__toggle text-call-to-action"
                aria-expanded="false" aria-controls="submenu-4">
              <span class="flyout__accordion__label cta">Careers</span>
              <span class="button-group button-group--compact" aria-hidden="true">
                <span class="button-group__buttons">
                  
                  <span class="button flyout__accordion__icon open">
                    <span class="icon-md-outlined">
                      
<svg xmlns="http://www.w3.org/2000/svg"
     height="18px"
     width="18px"
     viewBox="0 -960 960 960"
     fill="currentColor"
     class=""
     aria-hidden="true"
     role="presentation">
  
    <path d="M480-357.85 253.85-584l32.61-32.61L480-423.08l193.54-193.53L706.15-584 480-357.85Z" />
  
</svg>

                    </span>
                  </span>
                  <span class="button flyout__accordion__icon close">
                    <span class="icon-md-outlined">
                      
<svg xmlns="http://www.w3.org/2000/svg"
     height="18px"
     width="18px"
     viewBox="0 -960 960 960"
     fill="currentColor"
     class=""
     aria-hidden="true"
     role="presentation">
  
    <path d="m480-541.85-184 184L253.85-400 480-626.15 706.15-400 664-357.85l-184-184Z" />
  
</svg>

                    </span>
                  </span>
                </span>
              </span>
            </button>
            
            <div id="submenu-4" class="flyout__accordion__content"
                data-section="Careers" hidden>
              <div class="flyout__accordion__content-inner">
                <div class="flyout__intro">
                  <div>
                    <h2 class="flyout__title headline-5">Shaping the future together</h2>
                    
                  </div>
                  
                    <div class="button-group button-group--row_start button-group--compact">
                      <div class="button-group__buttons">
                        
                          



  
  
    <a href="/programs-and-events/"
      
      
       class="glue-button glue-button--medium-emphasis cta-small"
      
      
        data-gtm-event="nav_select"
        data-event-nav-type="subheader"
        data-event-nav-name="Careers - See all programs"
      
      
      >
      <div class="button__label">
        
          See all programs
        
      </div>
    </a>
  


                        
                      </div>
                    </div>
                  
                </div>
                <div class="flyout__subnav subnav subnav--2-column">
                  
                    <div class="subnav__column">
                      <div class="subnav__content">
                        
                        
                          
                        
                        <div class="subnav__links">
                        
                          
                          
                            
                              
                                <a class="subnav__link subnav__link--has-icon"
                                    href="/programs-and-events/faculty-engagement/"
                                    
                                      
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--large">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/faculty_programs_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="faculty_programs_nav">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">Faculty programs</div>
                                    <div class="subnav__link-description small-text">Participating in the academic research community through meaningful engagement with university faculty.</div>
                                  </div>
                                </a>
                              
                            
                              
                                <a class="subnav__link subnav__link--has-icon"
                                    href="/programs-and-events/student-engagement/"
                                    
                                      
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--large">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/student_programs_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="student_programs_nav">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">Student programs</div>
                                    <div class="subnav__link-description small-text">Supporting the next generation of researchers through a wide range of programming.</div>
                                  </div>
                                </a>
                              
                            
                          
                        
                          
                          
                            
                              
                                <a class="subnav__link subnav__link--has-icon"
                                    href="/programs-and-events/2026-google-carbon-removal-and-superpollutant-elimination-rd-awards/"
                                    
                                      
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--large">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/RD-programs_nav_f.svg" class="image image--svg picture__image " loading="lazy"  alt="R&amp;D-programs_nav_f">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">R&amp;D programs</div>
                                    <div class="subnav__link-description small-text">Collaborating with industry and academic experts to support foundational science and innovation.</div>
                                  </div>
                                </a>
                              
                            
                              
                                <a class="subnav__link subnav__link--has-icon"
                                    href="/careers/"
                                    
                                      
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--large">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/locations_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="locations_nav">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">Locations</div>
                                    <div class="subnav__link-description small-text">Find your place in our global offices and research labs.</div>
                                  </div>
                                </a>
                              
                            
                          
                        
                        </div> 

                        
                          
                        
                          
                        
                      </div>
                    </div>
                  
                </div>
              </div>
            </div>
          </div>
        
      
        
          <a href="/blog/"
              class="main-menu__label-tablet text-call-to-action cta"
              data-title="Blog"
              
                
              >
            Blog
          </a>
        
      
        
          <div class="flyout__accordion">
            
            <button type="button" data-title="About"
                class="main-menu__label-tablet flyout__accordion__toggle text-call-to-action"
                aria-expanded="false" aria-controls="submenu-6">
              <span class="flyout__accordion__label cta">About</span>
              <span class="button-group button-group--compact" aria-hidden="true">
                <span class="button-group__buttons">
                  
                  <span class="button flyout__accordion__icon open">
                    <span class="icon-md-outlined">
                      
<svg xmlns="http://www.w3.org/2000/svg"
     height="18px"
     width="18px"
     viewBox="0 -960 960 960"
     fill="currentColor"
     class=""
     aria-hidden="true"
     role="presentation">
  
    <path d="M480-357.85 253.85-584l32.61-32.61L480-423.08l193.54-193.53L706.15-584 480-357.85Z" />
  
</svg>

                    </span>
                  </span>
                  <span class="button flyout__accordion__icon close">
                    <span class="icon-md-outlined">
                      
<svg xmlns="http://www.w3.org/2000/svg"
     height="18px"
     width="18px"
     viewBox="0 -960 960 960"
     fill="currentColor"
     class=""
     aria-hidden="true"
     role="presentation">
  
    <path d="m480-541.85-184 184L253.85-400 480-626.15 706.15-400 664-357.85l-184-184Z" />
  
</svg>

                    </span>
                  </span>
                </span>
              </span>
            </button>
            
            <div id="submenu-6" class="flyout__accordion__content"
                data-section="About" hidden>
              <div class="flyout__accordion__content-inner">
                <div class="flyout__intro">
                  <div>
                    <h2 class="flyout__title headline-5">Translating discovery into real-world impact</h2>
                    
                  </div>
                  
                </div>
                <div class="flyout__subnav subnav subnav--2-column">
                  
                    <div class="subnav__column">
                      <div class="subnav__content">
                        
                        
                          
                        
                        <div class="subnav__links">
                        
                          
                          
                            
                              
                                <a class="subnav__link subnav__link--has-icon"
                                    href="/people/"
                                    
                                      
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--large">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/earth_AI_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="earth_AI_nav">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">People</div>
                                    <div class="subnav__link-description small-text">Our researchers drive advancements in computer science through both fundamental and applied research.</div>
                                  </div>
                                </a>
                              
                            
                          
                        
                          
                          
                            
                              
                                <a class="subnav__link subnav__link--has-icon"
                                    href="/teams/"
                                    
                                      
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--large">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/teams_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="teams_nav">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">Teams</div>
                                    <div class="subnav__link-description small-text">Collaborative groups tackling the world&#x27;s most challenging AI problems.</div>
                                  </div>
                                </a>
                              
                            
                          
                        
                        </div> 

                        
                          
                        
                          
                        
                      </div>
                    </div>
                  
                </div>
              </div>
            </div>
          </div>
        
      
      <div class="divider"></div>
      <div class="flyout__accordion__right-ctas">
        
      </div>
    </div>
  </div>
</nav>
        <div class="header-bar__background"></div>
        
<div class="header-bar">
  <div class="header-bar__blur" aria-hidden="true">
    <span class="header-bar__blur-layer header-bar__blur-layer--1"></span>
    <span class="header-bar__blur-layer header-bar__blur-layer--2"></span>
    <span class="header-bar__blur-layer header-bar__blur-layer--3"></span>
    <span class="header-bar__blur-layer header-bar__blur-layer--4"></span>
    <span class="header-bar__blur-layer header-bar__blur-layer--5"></span>
  </div>
  <div class="left-menu">
    <div class="hamburger-mobile">
      <div class="button-group button-group--compact">
        <div class="button-group__buttons">
          <button class="button open button--background-blur icon-center icon-center--wide"
                  aria-label="Open the site navigation">
            <span class="icon-md-outlined">
              
<svg xmlns="http://www.w3.org/2000/svg"
     height="18px"
     width="18px"
     viewBox="0 -960 960 960"
     fill="currentColor"
     class=""
     aria-hidden="true"
     role="presentation">
  
    <path d="M164-278.62v-51.99h632v51.99H164ZM164-454v-52h632v52H164Zm0-175.39v-51.99h632v51.99H164Z" />
  
</svg>

            </span>
          </button>
          <button class="button close button--outlined icon-center icon-center--wide"
                  aria-label="Close the site navigation">
            <span class="icon-md-outlined">
              
<svg xmlns="http://www.w3.org/2000/svg"
     height="18px"
     width="18px"
     viewBox="0 -960 960 960"
     fill="currentColor"
     class=""
     aria-hidden="true"
     role="presentation">
  
    <path d="M480-448 266.92-234.92q-6.69 6.69-15.8 6.88-9.12.19-16.2-6.88-7.07-7.08-7.07-16 0-8.93 7.07-16L448-480 234.92-693.08q-6.69-6.69-6.88-15.8-.19-9.12 6.88-16.2 7.08-7.07 16-7.07 8.93 0 16 7.07L480-512l213.08-213.08q6.69-6.69 15.8-6.88 9.12-.19 16.2 6.88 7.07 7.08 7.07 16 0 8.93-7.07 16L512-480l213.08 213.08q6.69 6.69 6.88 15.8.19 9.12-6.88 16.2-7.08 7.07-16 7.07-8.93 0-16-7.07L480-448Z" />
  
</svg>

            </span>
          </button>
        </div>
      </div>
    </div>
    <div class="site-switcher">
      <div class="site-switcher__bar">
        <a class="site-switcher__home"
           href="/"
           data-gtm-tag="header-selection"
           data-event-io="nav_select"
           data-event-nav-type="header"
           data-event-nav-name="Site Home logo">
          <span class="sr-only">Google</span>
          
            
              



  

<svg role="presentation" aria-hidden="true"  class="glue-icon  site-switcher__google-logo">
  <use href="/gr/static/assets/icons/glue-icons.svg#google-solid-logo"></use>
</svg>

              <span class="site-switcher__title">Research</span>
            
          
        </a>
        
          <div class="button-group button-group--micro site-switcher__toggle">
            <div class="button-group__buttons site-switcher__toggle">
              <button class="open button button--background-blur icon-center icon-center--wide"
                      aria-label="Open the website selector panel"
                      data-gtm-event="nav_select"
                      data-event-nav-type="site selector"
                      data-event-nav-name="open"
                      data-event-interaction-type="expand">
                      <span class="icon-md-outlined">
                        
<svg xmlns="http://www.w3.org/2000/svg"
     height="18px"
     width="18px"
     viewBox="0 -960 960 960"
     fill="currentColor"
     class=""
     aria-hidden="true"
     role="presentation">
  
    <path d="M480-357.85 253.85-584l32.61-32.61L480-423.08l193.54-193.53L706.15-584 480-357.85Z" />
  
</svg>

                      </span>
              </button>
              <button class="close button button--outlined icon-center icon-center--wide"
                      aria-label="Close the website selector panel"
                      data-gtm-event="nav_select"
                      data-event-nav-type="site selector"
                      data-event-nav-name="close"
                      data-event-interaction-type="collapse">
                      <span class="icon-md-outlined">
                        
<svg xmlns="http://www.w3.org/2000/svg"
     height="18px"
     width="18px"
     viewBox="0 -960 960 960"
     fill="currentColor"
     class=""
     aria-hidden="true"
     role="presentation">
  
    <path d="m480-541.85-184 184L253.85-400 480-626.15 706.15-400 664-357.85l-184-184Z" />
  
</svg>

                      </span>
              </button>
            </div>
          </div>
        
      </div>
    </div>
    
      <nav class="site-switcher__nav">
  
    <div class="site-switcher__group">
      
      
        <a class="site-switcher__link"
           aria-label="Google AI"
           target="_blank"
           href="https://ai.google/?utm_source=deepmind.google&amp;utm_medium=referral&amp;utm_campaign=gdm&amp;utm_content="
           >
          <div class="site-switcher__link-title cta-small">Google AI</div>
          <div class="site-switcher__link-description small-text">Learn about all our AI</div>
        </a>
      
        <a class="site-switcher__link"
           aria-label="Google DeepMind"
           target="_blank"
           href="https://deepmind.google?utm_source=deepmind.google&amp;utm_medium=referral&amp;utm_campaign=gdm&amp;utm_content=/"
           >
          <div class="site-switcher__link-title cta-small">Google DeepMind</div>
          <div class="site-switcher__link-description small-text">Explore the frontier of AI</div>
        </a>
      
        <a class="site-switcher__link"
           aria-label="Google Labs"
           target="_blank"
           href="https://labs.google/?utm_source=deepmind.google&amp;utm_medium=referral&amp;utm_campaign=gdm&amp;utm_content="
           >
          <div class="site-switcher__link-title cta-small">Google Labs</div>
          <div class="site-switcher__link-description small-text">Try our AI experiments</div>
        </a>
      
    </div>
  
</nav>

    
  </div>
  <div class="main-menu">

<nav class="main-menu__container button-group button-group--compact" aria-label="Main menu">
  
    <div class="main-menu__item" data-title="Research">
      
        <button type="button"
            class="main-menu__label deepai-text-call-to-action--nav button button--hover_outline cta-small"
            data-title="Research"
            aria-haspopup="true"
            aria-expanded="false">
          Research
        </button>
      

      
        <button type="button"
            class="main-menu__submenu-toggle"
            data-title="Research"
            aria-label="Open submenu for Research"
            aria-expanded="false"
            aria-haspopup="true">
          
<svg xmlns="http://www.w3.org/2000/svg"
     height="18px"
     width="18px"
     viewBox="0 -960 960 960"
     fill="currentColor"
     class=""
     aria-hidden="true"
     role="presentation">
  
    <path d="M480-357.85 253.85-584l32.61-32.61L480-423.08l193.54-193.53L706.15-584 480-357.85Z" />
  
</svg>

        </button>
      
    </div>
  
    <div class="main-menu__item" data-title="Resources">
      
        <button type="button"
            class="main-menu__label deepai-text-call-to-action--nav button button--hover_outline cta-small"
            data-title="Resources"
            aria-haspopup="true"
            aria-expanded="false">
          Resources
        </button>
      

      
        <button type="button"
            class="main-menu__submenu-toggle"
            data-title="Resources"
            aria-label="Open submenu for Resources"
            aria-expanded="false"
            aria-haspopup="true">
          
<svg xmlns="http://www.w3.org/2000/svg"
     height="18px"
     width="18px"
     viewBox="0 -960 960 960"
     fill="currentColor"
     class=""
     aria-hidden="true"
     role="presentation">
  
    <path d="M480-357.85 253.85-584l32.61-32.61L480-423.08l193.54-193.53L706.15-584 480-357.85Z" />
  
</svg>

        </button>
      
    </div>
  
    <div class="main-menu__item" data-title="Conferences &amp; events">
      
        <a href="/conferences-and-events/"
            class="main-menu__label deepai-text-call-to-action--nav button button--hover_outline cta-small"
            data-title="Conferences &amp; events"
            default
            
              
            >
          Conferences &amp; events
        </a>
      

      
    </div>
  
    <div class="main-menu__item" data-title="Careers">
      
        <button type="button"
            class="main-menu__label deepai-text-call-to-action--nav button button--hover_outline cta-small"
            data-title="Careers"
            aria-haspopup="true"
            aria-expanded="false">
          Careers
        </button>
      

      
        <button type="button"
            class="main-menu__submenu-toggle"
            data-title="Careers"
            aria-label="Open submenu for Careers"
            aria-expanded="false"
            aria-haspopup="true">
          
<svg xmlns="http://www.w3.org/2000/svg"
     height="18px"
     width="18px"
     viewBox="0 -960 960 960"
     fill="currentColor"
     class=""
     aria-hidden="true"
     role="presentation">
  
    <path d="M480-357.85 253.85-584l32.61-32.61L480-423.08l193.54-193.53L706.15-584 480-357.85Z" />
  
</svg>

        </button>
      
    </div>
  
    <div class="main-menu__item" data-title="Blog">
      
        <a href="/blog/"
            class="main-menu__label deepai-text-call-to-action--nav button button--hover_outline cta-small"
            data-title="Blog"
            default
            
              
            >
          Blog
        </a>
      

      
    </div>
  
    <div class="main-menu__item" data-title="About">
      
        <button type="button"
            class="main-menu__label deepai-text-call-to-action--nav button button--hover_outline cta-small"
            data-title="About"
            aria-haspopup="true"
            aria-expanded="false">
          About
        </button>
      

      
        <button type="button"
            class="main-menu__submenu-toggle"
            data-title="About"
            aria-label="Open submenu for About"
            aria-expanded="false"
            aria-haspopup="true">
          
<svg xmlns="http://www.w3.org/2000/svg"
     height="18px"
     width="18px"
     viewBox="0 -960 960 960"
     fill="currentColor"
     class=""
     aria-hidden="true"
     role="presentation">
  
    <path d="M480-357.85 253.85-584l32.61-32.61L480-423.08l193.54-193.53L706.15-584 480-357.85Z" />
  
</svg>

        </button>
      
    </div>
  
</nav>
</div>
  <div class="right-menu">
    <div class="right-menu__ctas button-group button-group--compact">
      <div class="button-group__buttons">
      
      </div>
    </div>
    
      
    
    
      <div class="header-bar__search glue-header__search js-header-search">
        <div class="glue-header__search__input">
          








<div class="search-input " data-type="header">
  <input type="search" class="caption --empty-search js-search-bar js-gt-search-input"
    aria-label="Search" placeholder="Search" name="search-input">
  <button class="search-input__button --search js-gt-search-btn" aria-label="Submit search">
    



  

<svg role="presentation" aria-hidden="true"  class="glue-icon glue-icon--18px ">
  <use href="/gr/static/assets/icons/glue-icons.svg#search"></use>
</svg>

  </button>
  <button class="search-input__button --clear" aria-label="Clear search">
    



  

<svg role="presentation" aria-hidden="true"  class="glue-icon glue-icon--18px ">
  <use href="/gr/static/assets/icons/glue-icons.svg#close"></use>
</svg>

  </button>
</div>

        </div>
        <button type="button" class="glue-header__search__btn js-header-search-btn cta-small" aria-label="Search">
          



  

<svg role="presentation" aria-hidden="true" aria-hidden="true" class="glue-icon glue-icon--18px search">
  <use href="/gr/static/assets/icons/glue-icons.svg#search"></use>
</svg>

          



  

<svg role="presentation" aria-hidden="true" aria-hidden="true" class="glue-icon glue-icon--18px close">
  <use href="/gr/static/assets/icons/glue-icons.svg#close"></use>
</svg>

          <span class="glue-header__search__label js-header-search-sr-text">Search</span>
        </button>
      </div>
    
  </div>
</div>

      </div>
    </header>
  </site-nav>


      
    
  


    

    <main id="page-content" tabindex="-1">
        
<div class="blog-detail-page --legacy " >
    





















<section class="basic-hero bhoig --theme-light  --large-image" data-gt-id="basic_hero" data-gt-component-name="">
  <div class="glue-page">
    <div class="glue-grid">
      <div class="bhoig__image-wrapper glue-grid__col--span-4 glue-grid__col--span-5-md glue-grid__col--span-4-lg">
      
        
        
          
            <div class="bhoig__image-bg" style="">
              
                <picture>
                  <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/e667f855aee9e830a1c1f9a30b9fdd24-metnethero1.gif" alt="MetNet-3: A state-of-the-art neural weather model available in Google products" class=""/>
                </picture>
              
            </div>
        
      
    </div>

        
        <div class="bhoig__breadcrumb-wrapper glue-grid__col--span-10 glue-grid__col--span-9-md glue-grid__col--span-10-lg">
          




<nav class="glue-breadcrumbs" aria-label="Breadcrumbs">
    
    <ol class="glue-breadcrumbs__list">
        
        
        
        
        <li class="glue-breadcrumbs__item">
            <a class="glue-breadcrumbs__link attribution" href="/">Home</a>
            



  

<svg role="presentation" aria-hidden="true"  class="glue-icon  ">
  <use href="/gr/static/assets/icons/glue-icons.svg#chevron-right"></use>
</svg>

        </li>
        
        
        
        <li class="glue-breadcrumbs__item">
            <a class="glue-breadcrumbs__link attribution" href="/blog/">Blog</a>
            



  

<svg role="presentation" aria-hidden="true"  class="glue-icon  ">
  <use href="/gr/static/assets/icons/glue-icons.svg#chevron-right"></use>
</svg>

        </li>
        
        
    </ol>
    
</nav>
        </div>

        <h1 class="headline-1 bhoig__headline glue-grid__col--span-8 glue-grid__col--span-7-md glue-grid__col--span-8-lg">MetNet-3: A state-of-the-art neural weather model available in Google products</h1>

        

          <div class="basic-hero__description bhoig__description glue-grid__col--span-8 glue-grid__col--span-7-md glue-grid__col--span-8-lg">
            <div class="basic-hero--blog-detail__description"><p>November 1, 2023</p><span class="dot-separator"></span><p>Posted by Samier Merchant, Google Research, and Nal Kalchbrenner, Google DeepMind</p></div>
          </div>

        

        <div class="bhoig__cta glue-grid__col--span-8 glue-grid__col--span-7-md glue-grid__col--span-8-lg">
          
        </div>
    </div>
  </div>
</section>


    <div class="glue-page">
        <div class="glue-grid blog-detail-page__grid">
            <div class="glue-grid__col glue-grid__col--span-4-sm glue-grid__col--span-12-md  glue-grid__col--span-9-lg">
                
                
                <div class="quicklinks-wrapper--mobile">
                    <div class="block-quick_links">


<section class="quicklinks">
    
        <h2 class="eyebrow">Quick links</h2>
        <ul class="quicklinks__list">
            
            
            <li class="quicklinks__item quicklinks__item--share js-quicklinks-share">
                
                <button
                    class="quicklinks__share-button js-quicklinks-share__button"
                    aria-expanded="false"
                    aria-controls="js-quicklinks-share__list-d578cec8">
                    <span class="icon icon--share"></span>
                    <span class="quicklinks__item__text">Share</span>
                </button>
                



<section id="js-quicklinks-share__list-d578cec8" class="glue-social glue-social--monochrome quicklinks__share-list js-quicklinks-share__list glue-elevation-level-1 js-gt-share-wrapper">
  <div class="glue-social__group">
    <ul class="glue-social__list" role="list">

      <li class="glue-social__item">
        <a class="glue-social__link" href="https://twitter.com/intent/tweet?text=https%3A//research.google/blog/metnet-3-a-state-of-the-art-neural-weather-model-available-in-google-products/"
            title="Share on Twitter" target="_blank" rel="noopener" data-gt-method="x">
            <svg role="presentation" aria-hidden="true"
              class="glue-icon glue-icon--social glue-icon--24px">
              <use href="/gr/static/assets/icons/twitter-x.svg#twitter-x"></use>
          </svg>
        </a>
      </li>
      <li class="glue-social__item">
        <a class="glue-social__link" href="https://www.facebook.com/sharer/sharer.php?u=https%3A//research.google/blog/metnet-3-a-state-of-the-art-neural-weather-model-available-in-google-products/"
            title="Share on Facebook" target="_blank" rel="noopener" data-gt-method="facebook">
          <svg role="presentation" aria-hidden="true"
              class="glue-icon glue-icon--social glue-icon--color-facebook glue-icon--24px">
            <use href="/gr/static/assets/icons/facebook.svg#facebook"></use>
          </svg>
        </a>
      </li>
      <li class="glue-social__item">
        <a class="glue-social__link" href="https://www.linkedin.com/shareArticle?url=https%3A//research.google/blog/metnet-3-a-state-of-the-art-neural-weather-model-available-in-google-products/&amp;mini=true" title="Share on LinkedIn" target="_blank" rel="noopener" data-gt-method="linkedin">
          <svg role="presentation" aria-hidden="true"
              class="glue-icon glue-icon--social glue-icon--color-linkedin glue-icon--24px">
            <use href="/gr/static/assets/icons/glue-icons.svg#post-linkedin"></use>
          </svg>
        </a>
      </li>
      <li class="glue-social__item">
        <a class="glue-social__link" href="mailto:name@example.com?subject=Check%20out%20this%20site&body=Check%20out%20https%3A//research.google/blog/metnet-3-a-state-of-the-art-neural-weather-model-available-in-google-products/" title="Send via Email" data-gt-method="email">
          <svg role="presentation" aria-hidden="true"
              class="glue-icon glue-icon--social glue-icon--color-sharemail glue-icon--24px">
            <use href="/gr/static/assets/icons/glue-icons.svg#email"></use>
          </svg>
        </a>
      </li>
      <li class="glue-social__item">
        <div class="glue-social__popover">
          <div class="glue-social__icon-trigger" aria-label="Get shareable link" title="Get shareable link" id="share-static-popover-trigger-d578cec8">
            <svg role="presentation" aria-hidden="true"
                class="glue-icon glue-icon--social glue-icon--color-sharelink glue-icon--24px">
              <use href="/gr/static/assets/icons/glue-icons.svg#link"></use>
            </svg>
          </div>

          <div class="glue-social__dialog" id="share-popover-dialog-d578cec8">
            <svg role="presentation" aria-hidden="true"
                class="glue-icon glue-icon--social glue-icon--color-sharelink glue-icon--24px">
              <use href="/gr/static/assets/icons/glue-icons.svg#link"></use>
            </svg>
            <div class="glue-social__copy" glue-copy-success="Copied to clipboard"
                glue-copy-fail="Press Ctrl+C or ⌘+C to copy">
              <input class="glue-social__copy-input" readonly="" type="text"
                  value="https://research.google/blog/metnet-3-a-state-of-the-art-neural-weather-model-available-in-google-products/" aria-label="URL" name="glue-social__copy-input">
              <button class="glue-social__copy-btn" id="share-copy-btn-d578cec8" data-gt-method="link-copied">Copy link</button>
            </div>
            <div aria-label="Close" class="glue-social__close-btn">
              ×
            </div>
          </div>
        </div>
      </li>
    </ul>
  </div>
</section>
            </li>
            
        </ul>
    
</section>
</div>
                </div>

                <div class="blog-detail-wrapper js-gt-blog-detail-wrapper" data-gt-publish-date="20231101">
                    
                    
    


<div class="rich-text --theme- --mode-" data-gt-id="rich_text"
    data-gt-component-name="">
  




  
<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdgnhML03N9vxEdGH1TkBATtxGpjyO5XYgZwJY5dY0-sPIAvrmCll4J8I9owyJTNOHZdq6MMZskWsYJDZivZA_zvj2atWhUsPoxWnNyifiFAm83GC2EsZ4xgre8bCk32Yzv3vlR4pGn12H7T5Vkbz5BaErZ22JRB-OqveQ7EDHsrCYjKN65Soc1FrZNwvu/s1600/metnethero1.gif" style="display: none;"/>
<p>
Forecasting weather variables such as precipitation, temperature, and wind is key to numerous aspects of society, from daily planning and transportation to energy production. As we continue to see more extreme weather events such as floods, droughts, and heat waves, accurate forecasts can be essential to preparing for and mitigating their effects. The first 24 hours into the future are especially important as they are both highly predictable and actionable, which can help people make informed decisions in a timely manner and stay safe. 
</p> <a name="more"></a>
<p>
Today we present a new weather model called <a href="https://arxiv.org/abs/2306.06079" target="_blank" rel="noopener noreferrer">MetNet-3</a>, developed by Google Research and Google DeepMind. Building on the earlier <a href="https://research.google/blog/a-neural-weather-model-for-eight-hour-precipitation-forecasting/?m=1">MetNet</a> and <a href="https://research.google/blog/metnet-2-deep-learning-for-12-hour-precipitation-forecasting/">MetNet-2</a> models, MetNet-3 provides high resolution predictions up to 24 hours ahead for a larger set of core variables, including precipitation, surface temperature, wind speed and direction, and dew point. MetNet-3 creates a temporally smooth and highly granular forecast, with lead time intervals of 2 minutes and spatial resolutions of 1 to 4 kilometers. MetNet-3 achieves strong performance compared to traditional methods, outperforming the best single- and multi-member physics-based <a href="https://en.wikipedia.org/wiki/Numerical_weather_prediction" target="_blank" rel="noopener noreferrer">numerical weather prediction</a> (NWP) models — such as <a href="https://rapidrefresh.noaa.gov/hrrr/" target="_blank" rel="noopener noreferrer">High-Resolution Rapid Refresh</a> (HRRR) and <a href="https://www.ecmwf.int/en/forecasts/documentation-and-support/medium-range-forecasts#:~:text=ENS%20is%20a%20probabilistic%20forecast,high%20winds%20or%20heavy%20rain)." target="_blank" rel="noopener noreferrer">ensemble forecast suite</a> (ENS) — for multiple regions up to 24 hours ahead. 
</p>
<p>
Finally, we’ve integrated MetNet-3’s capabilities across various Google <a href="https://support.google.com/websearch/answer/13692898" target="_blank" rel="noopener noreferrer">products and technologies</a> where weather is relevant. Currently available in the contiguous United States and parts of Europe with a focus on 12 hour precipitation forecasts, MetNet-3 is helping bring accurate and reliable weather information to people in multiple countries and languages.
</p>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;">
<tbody>
<tr>
<td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQcwPsDQPUe4Uon7vWWSewbqcWsAdfUIJ4yLLFiCvdQKu4ffT6E5qIMeiabtxK5wudSL-jjxa_fW5aOaBvDILq_dQzeT4RMSULORJZrjwkDscDxLnLflUybqHlPf1J8O7KB171g5I9kLVgRbGP0mr0HxbG0pY7J9ojoEZLl4JZHaMQH490XmUR_IUj_YMO/s904/image55.gif" target="_blank" rel="noopener noreferrer"><img alt="Google mobile search homepage listing trending topics like expressway closures, crossword clues, and company layoffs." border="0" data-original-height="904" data-original-width="476" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQcwPsDQPUe4Uon7vWWSewbqcWsAdfUIJ4yLLFiCvdQKu4ffT6E5qIMeiabtxK5wudSL-jjxa_fW5aOaBvDILq_dQzeT4RMSULORJZrjwkDscDxLnLflUybqHlPf1J8O7KB171g5I9kLVgRbGP0mr0HxbG0pY7J9ojoEZLl4JZHaMQH490XmUR_IUj_YMO/s16000/image55.gif"/></a></td>
<td>     </td>
<td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixRY-kzsepNdP_arXnJbHPJFViN_N4CzjOYH_1YxfjIDI5Nben4u8BoJ-tcYrrw4a3Jp7HFBGmakeBMqKAINeVFssClJHNUjvBhYHY6vpy6nOdpEoFDhCulwIE8OM9e7fRRwXqW01AeWUJjqmnNDn32ScCeQ2S64aNvDgigDes5vWA1_RrT7oMxK8sttG7/s904/image1.gif" target="_blank" rel="noopener noreferrer"><img alt="Mobile weather application screen displaying current conditions, precipitation timelines, and short term forecasts for Gifford, Illinois." border="0" data-original-height="904" data-original-width="476" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixRY-kzsepNdP_arXnJbHPJFViN_N4CzjOYH_1YxfjIDI5Nben4u8BoJ-tcYrrw4a3Jp7HFBGmakeBMqKAINeVFssClJHNUjvBhYHY6vpy6nOdpEoFDhCulwIE8OM9e7fRRwXqW01AeWUJjqmnNDn32ScCeQ2S64aNvDgigDes5vWA1_RrT7oMxK8sttG7/s16000/image1.gif"/></a></td>
</tr></tbody></table>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td class="tr-caption" style="text-align: center;">MetNet-3 precipitation output summarized into actionable forecasts in Google Search on mobile.</td></tr></tbody></table>
<div style="line-height: 40%;">
<br/>
</div>
<h2>Densification of sparse observations</h2>
<p>
Many recent machine learning weather models use the atmospheric state generated by traditional methods (e.g., data assimilation from NWPs) as the primary starting point to build forecasts. In contrast, a defining feature of the MetNet models has been to use direct observations of the atmosphere for training and evaluation. The advantage of direct observations is that they often have higher fidelity and resolution. However, direct observations come from a large variety of sensors at different altitudes, including weather stations at the surface level and satellites in orbit, and can be of varying degrees of sparsity. For example, precipitation estimates derived from radar such as <a href="https://mrms.nssl.noaa.gov/" target="_blank" rel="noopener noreferrer">NOAA’s Multi-Radar/Multi-Sensor System</a> (MRMS) are relatively dense images, whereas weather stations located on the ground that provide measurements for variables such as temperature and wind are mere points spread over a region.
</p>
<p>
In addition to the data sources used in previous MetNet models, MetNet-3 includes point measurements from weather stations as both inputs and targets with the goal of making a forecast at all locations. To this end, MetNet-3’s key innovation is a technique called densification, which merges the traditional two-step process of data assimilation and simulation found in physics-based models into a single pass through the neural network. The main components of densification are illustrated below. Although the densification technique applies to a specific stream of data individually, the resulting densified forecast benefits from all the other input streams that go into MetNet-3, including topographical, satellite, radar, and NWP analysis features. No NWP forecasts are included in MetNet-3’s default inputs.
</p>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEie1m1p0i-MWhS7Ih5RGzV-AQuDDPwgao4SpmnSUTdSsy7fcEwk4Soj5IJ8FqtGjhvi4ot2HKZdaQh3Hpu4CviRsx7FujT_4bbvpV8mu15Zt5bO5KbMGaaqIZoAGUp77ltVYH-zt2HTwVxbuGZHJt-0lbXZT-ukJH_KtB3pnHdRrRpZ2r5WgMSNGXnu-H8j/s1929/image22.gif" target="_blank" rel="noopener noreferrer"><img alt="Architectural diagram charting MetNet-3 data workflows across input dropout training, strong generalization, hyperlocal evaluation, and forecasting." border="0" data-original-height="1929" data-original-width="1600" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEie1m1p0i-MWhS7Ih5RGzV-AQuDDPwgao4SpmnSUTdSsy7fcEwk4Soj5IJ8FqtGjhvi4ot2HKZdaQh3Hpu4CviRsx7FujT_4bbvpV8mu15Zt5bO5KbMGaaqIZoAGUp77ltVYH-zt2HTwVxbuGZHJt-0lbXZT-ukJH_KtB3pnHdRrRpZ2r5WgMSNGXnu-H8j/s16000/image22.gif"/></a></td></tr><tr><td class="tr-caption" style="text-align: center;"><b>A</b>) During training, a fraction of the weather stations are masked out from the input while kept in the target. <b>B</b>) To evaluate generalization to untrained locations, a set of weather stations represented by squares is never used for training and is only used for evaluation. <b>C</b>) Data from these held out weather stations with sparse coverage is included during evaluation to determine prediction quality in these areas. <b>D</b>) The final forecasts use the full set of training weather stations as input and produce fully dense forecasts aided by spatial parameter sharing.</td></tr></tbody></table>
<div style="line-height: 40%;">
<br/>
</div>
<h2>High resolution in space and time</h2>
<p>
A central advantage of using direct observations is their high spatial and temporal resolution. For example, weather stations and ground radar stations provide measurements every few minutes at specific points and at 1 km resolutions, respectively; this is in stark contrast with the assimilation state from the state-of-the-art model <a href="https://www.ecmwf.int/en/forecasts/documentation-and-support/medium-range-forecasts#:~:text=ENS%20is%20a%20probabilistic%20forecast,high%20winds%20or%20heavy%20rain)." target="_blank" rel="noopener noreferrer">ENS</a>, which is generated every 6 hours at a resolution of 9 km with hour-by-hour forecasts. To handle such a high resolution, MetNet-3 preserves another of the defining features of this series of models, <em>lead time conditioning</em>. The lead time of the forecast in minutes is directly given as input to the neural network. This allows MetNet-3 to efficiently model the high temporal frequency of the observations for intervals as brief as 2 minutes. Densification combined with lead time conditioning and high resolution direct observations produces a fully dense 24 hour forecast with a temporal resolution of 2 minutes, while learning from just 1,000 points from the <a href="https://madis.ncep.noaa.gov/madis_OMO.shtml" target="_blank" rel="noopener noreferrer">One Minute Observation</a> (OMO) network of weather stations spread across the United States.
</p>
<p>
MetNet-3 predicts a marginal multinomial probability distribution for each output variable and each location that provides rich information beyond just the mean. This allows us to compare the probabilistic outputs of MetNet-3 with the outputs of advanced probabilistic ensemble NWP models, including the ensemble forecast ENS from the <a href="https://www.ecmwf.int/" target="_blank" rel="noopener noreferrer">European Centre for Medium-Range Weather Forecasts</a> and the <a href="https://www.spc.noaa.gov/exper/href/" target="_blank" rel="noopener noreferrer">High Resolution Ensemble Forecast</a> (HREF) from the <a href="https://www.noaa.gov/" target="_blank" rel="noopener noreferrer">National Oceanic and Atmospheric Administration of the US</a>. Due to the probabilistic nature of the outputs of both models, we are able to compute scores such as the <a href="https://confluence.ecmwf.int/display/FUG/Section+12.B+Statistical+Concepts+-+Probabilistic+Data#:~:text=The%20Continuous%20Ranked%20Probability%20Score,the%20forecast%20is%20wholly%20inaccurate." target="_blank" rel="noopener noreferrer">Continuous Ranked Probability Score</a> (CRPS). The following graphics highlight densification results and illustrate that MetNet’s forecasts are not only of much higher resolution, but are also more accurate when evaluated at the overlapping lead times.
</p>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJsf6Y6gV9VjK_rS_Bf_WLWdsJOq3sQbdaW26VSp2vX1Fq5j7VcWl4VDi3BeBFpEcH_YGrkU9ozJyuP5dh8tWWCU4yGzlmGBTfwM-kXGKZvdvI1DF17V4kSJSGGBIacqaCO4N1Oc8P4PymPWdglJbew_cjP9reFSJuHR3_ikZfZFuzN6aC8F17TAtiJPIg/s768/image44.gif" target="_blank" rel="noopener noreferrer"><img alt="Two regional meteorological forecast maps comparing high-resolution MetNet-3 data with lower-resolution blurrier ENS data." border="0" data-original-height="768" data-original-width="600" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJsf6Y6gV9VjK_rS_Bf_WLWdsJOq3sQbdaW26VSp2vX1Fq5j7VcWl4VDi3BeBFpEcH_YGrkU9ozJyuP5dh8tWWCU4yGzlmGBTfwM-kXGKZvdvI1DF17V4kSJSGGBIacqaCO4N1Oc8P4PymPWdglJbew_cjP9reFSJuHR3_ikZfZFuzN6aC8F17TAtiJPIg/s16000/image44.gif"/></a></td></tr><tr><td class="tr-caption" style="text-align: center;"><b>Top</b>: MetNet-3’s forecast of wind speed for each 2 minutes over the future 24 hours with a spatial resolution of 4km. <b>Bottom</b>: ENS’s hourly forecast with a spatial resolution of 18 km. <br/>The two distinct regimes in spatial structure are primarily driven by the presence of the Colorado mountain ranges. Darker corresponds to higher wind speed. More samples available here: <a href="https://youtube.com/watch?v=iB1DzHNqH_o" target="_blank" rel="noopener noreferrer">1</a>, <a href="https://youtube.com/watch?v=LlWB558jKJk" target="_blank" rel="noopener noreferrer">2</a>, <a href="https://youtube.com/watch?v=74bFo3nkbe4" target="_blank" rel="noopener noreferrer">3</a>, <a href="https://youtube.com/watch?v=MKUzYQZn9sQ" target="_blank" rel="noopener noreferrer">4</a>.</td></tr></tbody></table>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhBhlSum7x274E9KQGzLnjM9iXNEhifOJjKzt1Cwa5YyABCbaB68Mkr3gFvIVUhyphenhyphenaIGOqUE78MqGTK992NK8zrdKrqKxtFlYf1qeWYNkTa4PVzD3u_9lmQAjKnbLILHAkPhIOCvyAI6qBtfyf-z_xgUys3gXRJd_GSs3-qnyq0yFbjvmxdXAbVldV-xrIRJ/s1120/image11.png" target="_blank" rel="noopener noreferrer"><img alt="Line graph comparing Continuous Ranked Probability Scores for wind speed forecasts across twenty-four hours among three models." border="0" data-original-height="694" data-original-width="1120" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhBhlSum7x274E9KQGzLnjM9iXNEhifOJjKzt1Cwa5YyABCbaB68Mkr3gFvIVUhyphenhyphenaIGOqUE78MqGTK992NK8zrdKrqKxtFlYf1qeWYNkTa4PVzD3u_9lmQAjKnbLILHAkPhIOCvyAI6qBtfyf-z_xgUys3gXRJd_GSs3-qnyq0yFbjvmxdXAbVldV-xrIRJ/s16000/image11.png"/></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Performance comparison between MetNet-3 and NWP baseline for wind speed based on CRPS (lower is better). In the hyperlocal setting, values of the test weather stations are given as input to the network during evaluation; the results improve further especially in the early lead times.</td></tr></tbody></table>
<p>
In contrast to weather station variables, precipitation estimates are more dense as they come from ground radar. MetNet-3’s modeling of precipitation is similar to that of MetNet-1 and 2, but extends the high resolution precipitation forecasts with a 1km spatial granularity to the same 24 hours of lead time as the other variables, as shown in the animation below. MetNet-3’s performance on precipitation achieves a better CRPS value than ENS’s throughout the 24 hour range.
</p>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEidyInWvqdPpdIndLrxzykAODCeJ_p69uqvYOpasjFcBQU5o8Mtr-DiLfZXZrkJel9TD9SxZEmyIb58r6TZjRw57D8aSjl9P2jxCOsK7XZeXY0J3B8UMIFnl6aqXqhd0wft_NQGBi9KqpSUHAgw2c4JoYMdt27sKp6xcvOyMfjASpaZZzlI9o8lesj3GsrL/s720/image14.gif" target="_blank" rel="noopener noreferrer"><img alt="Stacked weather radar maps comparing ENS, Ground Truth, and MetNet-3 precipitation fields over the United States." border="0" data-original-height="683" data-original-width="720" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEidyInWvqdPpdIndLrxzykAODCeJ_p69uqvYOpasjFcBQU5o8Mtr-DiLfZXZrkJel9TD9SxZEmyIb58r6TZjRw57D8aSjl9P2jxCOsK7XZeXY0J3B8UMIFnl6aqXqhd0wft_NQGBi9KqpSUHAgw2c4JoYMdt27sKp6xcvOyMfjASpaZZzlI9o8lesj3GsrL/s16000/image14.gif"/></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Case study for Thu Jan 17 2019 00:00 UTC showing the probability of instantaneous precipitation rate being above 1 mm/h on CONUS. Darker corresponds to a higher probability value. The maps also show the prediction threshold when optimized towards Critical Success Index <a href="https://en.wikipedia.org/wiki/Precision_and_recall" target="_blank" rel="noopener noreferrer">CSI</a> (dark blue contours). This specific case study shows the formation of a new large precipitation pattern in the central US; it is not just forecasting of existing patterns. <br/><b>Top:</b> ENS’s hourly forecast. <b>Center:</b> Ground truth, source NOAA’s MRMS. <b>Bottom:</b> Probability map as predicted by MetNet-3. <a href="https://www.youtube.com/watch?v=TXqR9lL4368" target="_blank" rel="noopener noreferrer">Native resolution available here.</a></td></tr></tbody></table>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_4M2Sz50c_PDZkyHqZGfc5p5aRGpAS04ztN9N3s3VBn4_AD8GN7Vv6Vw-2phokpqtamutHT_6nGSsXb7271cfijLu3vJT1IV8Mmo1wlq1jfYcUPNs7TL6z0Cls3qGD1jA4Z0uRpj_rNXYLpFSbHEIqNOAA_V8VE_ZhsO7o-D64nDdmRei_hPEY7YT8lcg/s1102/image4.png" target="_blank" rel="noopener noreferrer"><img alt="Line graph plotting Continuous Ranked Probability Scores for precipitation rate forecasts across a twenty-four hour window." border="0" data-original-height="682" data-original-width="1102" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_4M2Sz50c_PDZkyHqZGfc5p5aRGpAS04ztN9N3s3VBn4_AD8GN7Vv6Vw-2phokpqtamutHT_6nGSsXb7271cfijLu3vJT1IV8Mmo1wlq1jfYcUPNs7TL6z0Cls3qGD1jA4Z0uRpj_rNXYLpFSbHEIqNOAA_V8VE_ZhsO7o-D64nDdmRei_hPEY7YT8lcg/s16000/image4.png"/></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Performance comparison between MetNet-3 and NWP baseline for instantaneous precipitation rate on CRPS (lower is better).</td></tr></tbody></table>
<div style="line-height: 40%;">
<br/>
</div>
<h2>Delivering realtime ML forecasts</h2>
<p>
Training and evaluating a weather forecasting model like MetNet-3 on historical data is only a part of the process of delivering ML-powered forecasts to users. There are many considerations when developing a real-time ML system for weather forecasting, such as ingesting real-time input data from multiple distinct sources, running inference, implementing real-time validation of outputs, building insights from the rich output of the model that lead to an intuitive user experience, and serving the results at Google scale — all on a continuous cycle, refreshed every few minutes.
</p>
<p>
We developed such a real-time system that is capable of producing a precipitation forecast every few minutes for the entire contiguous United States and for 27 countries in Europe for a lead time of up to 12 hours.
</p>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg88AA6lzoFtJd9ZOXt6AiiT_gTtFcJwsZNzUJ63kuYtq7XYs0LHUSp3q37zOPolA-rR_WQPciuDZsg-4Y3J0qrLUmNxMi1iBqyR4ICy4MKwRFXHtQhfkWdwPREd4qm9FVlN6rpLEebDC7MfBg7hToXhQvdsFoGObtu-Lqty3ZQSALf1yjna37tJY4fAptE/s1600/image6.gif" target="_blank" rel="noopener noreferrer"><img alt="Block diagram showing input variables including radar, satellite, topology, and NWP feeding into the MetNet-3 model." border="0" data-original-height="367" data-original-width="1600" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg88AA6lzoFtJd9ZOXt6AiiT_gTtFcJwsZNzUJ63kuYtq7XYs0LHUSp3q37zOPolA-rR_WQPciuDZsg-4Y3J0qrLUmNxMi1iBqyR4ICy4MKwRFXHtQhfkWdwPREd4qm9FVlN6rpLEebDC7MfBg7hToXhQvdsFoGObtu-Lqty3ZQSALf1yjna37tJY4fAptE/s16000/image6.gif"/></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Illustration of the process of generating precipitation forecasts using MetNet-3.</td></tr></tbody></table>
<p>
The system's uniqueness stems from its use of near-continuous inference, which allows the model to constantly create full forecasts based on incoming data streams. This mode of inference is different from traditional inference systems, and is necessary due to the distinct characteristics of the incoming data. The model takes in various data sources as input, such as radar, satellite, and numerical weather prediction assimilations. Each of these inputs has a different refresh frequency and spatial and temporal resolution. Some data sources, such as weather observations and radar, have characteristics similar to a continuous stream of data, while others, such as NWP assimilations, are similar to batches of data. The system is able to align all of these data sources spatially and temporally, allowing the model to create an updated understanding of the next 12 hours of precipitation at a very high cadence.
</p>
<p>
With the above process, the model is able to predict arbitrary discrete probability distributions. We developed novel techniques to transform this dense output space into user-friendly information that enables rich experiences throughout Google products and technologies.
</p>
<div style="line-height: 40%;">
<br/>
</div>
<h2>Weather features in Google products</h2>
<p>
People around the world rely on Google every day to provide helpful, timely, and accurate information about the weather. This information is used for a variety of purposes, such as planning outdoor activities, packing for trips, and staying safe during severe weather events.
</p>
<p>
The state-of-the-art accuracy, high temporal and spatial resolution, and probabilistic nature of MetNet-3 makes it possible to create unique hyperlocal weather insights. For the contiguous United States and Europe, MetNet-3 is operational and produces real-time 12 hour precipitation forecasts that are now served across Google <a href="https://support.google.com/websearch/answer/13692898" target="_blank" rel="noopener noreferrer">products and technologies</a> where weather is relevant, such as Search. The rich output from the model is synthesized into actionable information and instantly served to millions of users.
</p>
<p>
For example, a user who searches for weather information for a precise location from their mobile device will receive highly localized precipitation forecast data, including timeline graphs with granular minute breakdowns depending on the product.
</p>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4R591KKD1ZkmhTrjo28JovCeeo2bGjb0Tn5Ohr8KEooVqZqSNlgsrJrROaPWn5XXBzEohkhZMjaX2AV3M1RikyLgO7LfIgTFt54-uumb7xxPU6blnuFC8dN8W2SjK85tBKfZQ9Kn4oR-988YKXVUTbu-N5LWWX6JurqN6RRad7Bve59oEdZC-eMsn4HH9/s600/metnet3.gif" target="_blank" rel="noopener noreferrer"><img alt="Mobile interface layouts comparing an English weather forecasting application with a French Google search result screen." border="0" data-original-height="560" data-original-width="600" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4R591KKD1ZkmhTrjo28JovCeeo2bGjb0Tn5Ohr8KEooVqZqSNlgsrJrROaPWn5XXBzEohkhZMjaX2AV3M1RikyLgO7LfIgTFt54-uumb7xxPU6blnuFC8dN8W2SjK85tBKfZQ9Kn4oR-988YKXVUTbu-N5LWWX6JurqN6RRad7Bve59oEdZC-eMsn4HH9/s16000/metnet3.gif"/></a></td></tr><tr><td class="tr-caption" style="text-align: center;">MetNet-3 precipitation output in weather on the Google app on Android (<b>left</b>) and mobile web Search (<b>right</b>).</td></tr></tbody></table>
<div style="line-height: 40%;">
<br/>
</div>
<h2>Conclusion</h2>
<p>
MetNet-3 is a new deep learning model for weather forecasting that outperforms state-of-the-art physics-based models for 24-hour forecasts of a core set of weather variables. It has the potential to create new possibilities for weather forecasting and to improve the safety and efficiency of many activities, such as transportation, agriculture, and energy production. MetNet-3 is operational and its forecasts are served across several Google products where weather is relevant.
</p>
<div style="line-height: 40%;">
<br/>
</div>
<h2>Acknowledgements</h2>
<p>
<em>Many people were involved in the development of this effort. We would like to especially thank those from Google DeepMind (Di Li, Jeremiah Harmsen, Lasse Espeholt, Marcin Andrychowicz, Zack Ontiveros), Google Research (Aaron Bell, Akib Uddin, Alex Merose, Carla Bromberg, Fred Zyda, Isalo Montacute, Jared Sisk, Jason Hickey, Luke Barrington, Mark Young, Maya Tohidi, Natalie Williams, Pramod Gupta, Shreya Agrawal, Thomas Turnbull, Tom Small, Tyler Russell), and Google Search (Agustin Pesciallo, Bill Myers, Danny Cheresnick, Jonathan Karsh, Lior Cohen, Maca Piombi, Maia Diamant, Max Kamenetsky, Maya Ekron, Mor Schlesinger, Neta Gefen-Doron, Nofar Peled Levi, Ofer Lehr, Or Hillel, Rotem Wertman, Tamar Shevach,Vinay Ruelius Shah, Yechie Labai).</em></p>

  
</div>


                    
                </div>

                
<section class="blog-labels" data-gt-id="blog_labels" data-gt-component-name="Blog Labels">
    <ul class="blog-labels__list">
        <li class="caption" aria-hidden="true">Labels:</li>
        
        <li class="caption">
            <a class="caption" href="/blog/label/machine-intelligence">Machine Intelligence</a>
            
        </li>
        
    </ul>
</section>

                
    


<section aria-label="List of footnotes" data-gt-id="footnotes" data-gt-component-name="Footnotes">
  <ol class="js-footnotes footnotes">
    
  </ol>
</section>


            </div>
            
                <div class="glue-grid__col glue-grid__col--span-4-sm glue-grid__col--span-12-md glue-grid__col--span-3-lg">
                    <div class="quicklinks-wrapper--desktop quicklinks-wrapper--sticky">
                        <div class="block-quick_links">


<section class="quicklinks">
    
        <h2 class="eyebrow">Quick links</h2>
        <ul class="quicklinks__list">
            
            
            <li class="quicklinks__item quicklinks__item--share js-quicklinks-share">
                
                <button
                    class="quicklinks__share-button js-quicklinks-share__button"
                    aria-expanded="false"
                    aria-controls="js-quicklinks-share__list-56f7e525">
                    <span class="icon icon--share"></span>
                    <span class="quicklinks__item__text">Share</span>
                </button>
                



<section id="js-quicklinks-share__list-56f7e525" class="glue-social glue-social--monochrome quicklinks__share-list js-quicklinks-share__list glue-elevation-level-1 js-gt-share-wrapper">
  <div class="glue-social__group">
    <ul class="glue-social__list" role="list">

      <li class="glue-social__item">
        <a class="glue-social__link" href="https://twitter.com/intent/tweet?text=https%3A//research.google/blog/metnet-3-a-state-of-the-art-neural-weather-model-available-in-google-products/"
            title="Share on Twitter" target="_blank" rel="noopener" data-gt-method="x">
            <svg role="presentation" aria-hidden="true"
              class="glue-icon glue-icon--social glue-icon--24px">
              <use href="/gr/static/assets/icons/twitter-x.svg#twitter-x"></use>
          </svg>
        </a>
      </li>
      <li class="glue-social__item">
        <a class="glue-social__link" href="https://www.facebook.com/sharer/sharer.php?u=https%3A//research.google/blog/metnet-3-a-state-of-the-art-neural-weather-model-available-in-google-products/"
            title="Share on Facebook" target="_blank" rel="noopener" data-gt-method="facebook">
          <svg role="presentation" aria-hidden="true"
              class="glue-icon glue-icon--social glue-icon--color-facebook glue-icon--24px">
            <use href="/gr/static/assets/icons/facebook.svg#facebook"></use>
          </svg>
        </a>
      </li>
      <li class="glue-social__item">
        <a class="glue-social__link" href="https://www.linkedin.com/shareArticle?url=https%3A//research.google/blog/metnet-3-a-state-of-the-art-neural-weather-model-available-in-google-products/&amp;mini=true" title="Share on LinkedIn" target="_blank" rel="noopener" data-gt-method="linkedin">
          <svg role="presentation" aria-hidden="true"
              class="glue-icon glue-icon--social glue-icon--color-linkedin glue-icon--24px">
            <use href="/gr/static/assets/icons/glue-icons.svg#post-linkedin"></use>
          </svg>
        </a>
      </li>
      <li class="glue-social__item">
        <a class="glue-social__link" href="mailto:name@example.com?subject=Check%20out%20this%20site&body=Check%20out%20https%3A//research.google/blog/metnet-3-a-state-of-the-art-neural-weather-model-available-in-google-products/" title="Send via Email" data-gt-method="email">
          <svg role="presentation" aria-hidden="true"
              class="glue-icon glue-icon--social glue-icon--color-sharemail glue-icon--24px">
            <use href="/gr/static/assets/icons/glue-icons.svg#email"></use>
          </svg>
        </a>
      </li>
      <li class="glue-social__item">
        <div class="glue-social__popover">
          <div class="glue-social__icon-trigger" aria-label="Get shareable link" title="Get shareable link" id="share-static-popover-trigger-56f7e525">
            <svg role="presentation" aria-hidden="true"
                class="glue-icon glue-icon--social glue-icon--color-sharelink glue-icon--24px">
              <use href="/gr/static/assets/icons/glue-icons.svg#link"></use>
            </svg>
          </div>

          <div class="glue-social__dialog" id="share-popover-dialog-56f7e525">
            <svg role="presentation" aria-hidden="true"
                class="glue-icon glue-icon--social glue-icon--color-sharelink glue-icon--24px">
              <use href="/gr/static/assets/icons/glue-icons.svg#link"></use>
            </svg>
            <div class="glue-social__copy" glue-copy-success="Copied to clipboard"
                glue-copy-fail="Press Ctrl+C or ⌘+C to copy">
              <input class="glue-social__copy-input" readonly="" type="text"
                  value="https://research.google/blog/metnet-3-a-state-of-the-art-neural-weather-model-available-in-google-products/" aria-label="URL" name="glue-social__copy-input">
              <button class="glue-social__copy-btn" id="share-copy-btn-56f7e525" data-gt-method="link-copied">Copy link</button>
            </div>
            <div aria-label="Close" class="glue-social__close-btn">
              ×
            </div>
          </div>
        </div>
      </li>
    </ul>
  </div>
</section>
            </li>
            
        </ul>
    
</section>
</div>
                    </div>
                </div>
            
        </div>
    </div>
    
    

<section class="related-posts offset-two-up" data-gt-id="related_blog_posts" data-gt-component-name="Related Blog Posts">
    <div class="glue-page glue-grid">
        <div
            class="offset-two-up__left-col glue-grid__col glue-grid__col--span-4-sm glue-grid__col--span-12-md glue-grid__col--span-3-lg">
            <h2 class="offset-two-up__headline headline-3">Other posts of interest</h2>
        </div>
        <div class="glue-grid__col glue-grid__col--span-4-sm glue-grid__col--span-12-md glue-grid__col--span-9-lg">
            <ul class="card-stack--basic nested-glue-grid-override">
                
                <li class="glue-grid__col glue-grid__col--span-4-md glue-grid__col--span-4-sm">
                    





    












    <a class="glue-card glue-card--basic not-glue glue-card--blog" href="/blog/glucofm-foundation-model-for-continuous-glucose-monitoring/"  >

        <div class="glue-card__inner">
            
    



<div class="related-posts__image">
  
  
  
  <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/GlucoFM1_Overview.png" alt="Overview diagram of the GlucoFM framework detailing data preprocessing, JEPA-style pre-training architecture, and clinical forecasting applications." />
</div>




            <div class="glue-card__content --no-media">
  
    <p class="glue-card__eyebrow label">August 26, 2026</p>
  

  
    <span class="headline-6 js-gt-item-id">
      GlucoFM: Foundation model for continuous glucose monitoring
    </span>
  

  
</div>


            
    <ul class="glue-card__link-list">
        
            <li class="glue-card__link-list__item">
                <span class="not-glue caption">
                    Health &amp; Bioscience
                    
                    <span class="glue-card__link-list__spacer">&#183;</span>
                    
                </span>
            </li>
        
            <li class="glue-card__link-list__item">
                <span class="not-glue caption">
                    Machine Intelligence
                    
                </span>
            </li>
        
    </ul>



        
            

        
        </div>

    </a>



                </li>
                
                <li class="glue-grid__col glue-grid__col--span-4-md glue-grid__col--span-4-sm">
                    





    












    <a class="glue-card glue-card--basic not-glue glue-card--blog" href="/blog/agenthands-generating-interactive-hand-gestures-for-spatially-grounded-agent-conversations-in-xr/"  >

        <div class="glue-card__inner">
            
    



<div class="related-posts__image">
  
  
  
  <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/AgentHands5_Workflow.png" alt="Workflow diagram of AgentHands system generating annotated text, gesture events, and timestamped speech from a user&#x27;s question and gaze." />
</div>




            <div class="glue-card__content --no-media">
  
    <p class="glue-card__eyebrow label">August 25, 2026</p>
  

  
    <span class="headline-6 js-gt-item-id">
      AgentHands: Generating interactive hand gestures for spatially grounded agent conversations in XR
    </span>
  

  
</div>


            
    <ul class="glue-card__link-list">
        
            <li class="glue-card__link-list__item">
                <span class="not-glue caption">
                    Human-Computer Interaction and Visualization
                    
                    <span class="glue-card__link-list__spacer">&#183;</span>
                    
                </span>
            </li>
        
            <li class="glue-card__link-list__item">
                <span class="not-glue caption">
                    Machine Intelligence
                    
                </span>
            </li>
        
    </ul>



        
            

        
        </div>

    </a>



                </li>
                
                <li class="glue-grid__col glue-grid__col--span-4-md glue-grid__col--span-4-sm">
                    





    












    <a class="glue-card glue-card--basic not-glue glue-card--blog" href="/blog/how-mobility-gives-language-models-a-deeper-understanding-of-place/"  >

        <div class="glue-card__inner">
            
    



<div class="related-posts__image">
  
  
  
  <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/MobilityPOIs_Hero.png" alt="A conceptual map illustrating human mobility patterns to a specific point of interest. Several colorful figures converge from different directions toward a central blue building marked with a red map pin. Text bubbles next to each figure indicate varying" />
</div>




            <div class="glue-card__content --no-media">
  
    <p class="glue-card__eyebrow label">August 21, 2026</p>
  

  
    <span class="headline-6 js-gt-item-id">
      How mobility gives language models a deeper understanding of place
    </span>
  

  
</div>


            
    <ul class="glue-card__link-list">
        
            <li class="glue-card__link-list__item">
                <span class="not-glue caption">
                    Algorithms &amp; Theory
                    
                    <span class="glue-card__link-list__spacer">&#183;</span>
                    
                </span>
            </li>
        
            <li class="glue-card__link-list__item">
                <span class="not-glue caption">
                    Earth AI
                    
                    <span class="glue-card__link-list__spacer">&#183;</span>
                    
                </span>
            </li>
        
            <li class="glue-card__link-list__item">
                <span class="not-glue caption">
                    Machine Intelligence
                    
                </span>
            </li>
        
    </ul>



        
            

        
        </div>

    </a>



                </li>
                
            </ul>
        </div>
    </div>
</section>

    

    
      



  <div id="imageModal" class="image-modal">
    <span class="image-modal-close">&times;</span>
    <span class="image-modal-prev">&#10094;</span>
    <span class="image-modal-next">&#10095;</span>
    <div class="image-modal-content">
    
      
        <div class="modal-slide" data-slide-alt="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixRY-kzsepNdP_arXnJbHPJFViN_N4CzjOYH_1YxfjIDI5Nben4u8BoJ-tcYrrw4a3Jp7HFBGmakeBMqKAINeVFssClJHNUjvBhYHY6vpy6nOdpEoFDhCulwIE8OM9e7fRRwXqW01AeWUJjqmnNDn32ScCeQ2S64aNvDgigDes5vWA1_RrT7oMxK8sttG7/s16000/image1.gif" data-slide-source="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixRY-kzsepNdP_arXnJbHPJFViN_N4CzjOYH_1YxfjIDI5Nben4u8BoJ-tcYrrw4a3Jp7HFBGmakeBMqKAINeVFssClJHNUjvBhYHY6vpy6nOdpEoFDhCulwIE8OM9e7fRRwXqW01AeWUJjqmnNDn32ScCeQ2S64aNvDgigDes5vWA1_RrT7oMxK8sttG7/s16000/image1.gif">
          <img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixRY-kzsepNdP_arXnJbHPJFViN_N4CzjOYH_1YxfjIDI5Nben4u8BoJ-tcYrrw4a3Jp7HFBGmakeBMqKAINeVFssClJHNUjvBhYHY6vpy6nOdpEoFDhCulwIE8OM9e7fRRwXqW01AeWUJjqmnNDn32ScCeQ2S64aNvDgigDes5vWA1_RrT7oMxK8sttG7/s16000/image1.gif" width="760" height="530" alt="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixRY-kzsepNdP_arXnJbHPJFViN_N4CzjOYH_1YxfjIDI5Nben4u8BoJ-tcYrrw4a3Jp7HFBGmakeBMqKAINeVFssClJHNUjvBhYHY6vpy6nOdpEoFDhCulwIE8OM9e7fRRwXqW01AeWUJjqmnNDn32ScCeQ2S64aNvDgigDes5vWA1_RrT7oMxK8sttG7/s16000/image1.gif">
        </div>
      
    
      
        <div class="modal-slide" data-slide-alt="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEie1m1p0i-MWhS7Ih5RGzV-AQuDDPwgao4SpmnSUTdSsy7fcEwk4Soj5IJ8FqtGjhvi4ot2HKZdaQh3Hpu4CviRsx7FujT_4bbvpV8mu15Zt5bO5KbMGaaqIZoAGUp77ltVYH-zt2HTwVxbuGZHJt-0lbXZT-ukJH_KtB3pnHdRrRpZ2r5WgMSNGXnu-H8j/s16000/image22.gif" data-slide-source="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEie1m1p0i-MWhS7Ih5RGzV-AQuDDPwgao4SpmnSUTdSsy7fcEwk4Soj5IJ8FqtGjhvi4ot2HKZdaQh3Hpu4CviRsx7FujT_4bbvpV8mu15Zt5bO5KbMGaaqIZoAGUp77ltVYH-zt2HTwVxbuGZHJt-0lbXZT-ukJH_KtB3pnHdRrRpZ2r5WgMSNGXnu-H8j/s16000/image22.gif">
          <img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEie1m1p0i-MWhS7Ih5RGzV-AQuDDPwgao4SpmnSUTdSsy7fcEwk4Soj5IJ8FqtGjhvi4ot2HKZdaQh3Hpu4CviRsx7FujT_4bbvpV8mu15Zt5bO5KbMGaaqIZoAGUp77ltVYH-zt2HTwVxbuGZHJt-0lbXZT-ukJH_KtB3pnHdRrRpZ2r5WgMSNGXnu-H8j/s16000/image22.gif" width="760" height="530" alt="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEie1m1p0i-MWhS7Ih5RGzV-AQuDDPwgao4SpmnSUTdSsy7fcEwk4Soj5IJ8FqtGjhvi4ot2HKZdaQh3Hpu4CviRsx7FujT_4bbvpV8mu15Zt5bO5KbMGaaqIZoAGUp77ltVYH-zt2HTwVxbuGZHJt-0lbXZT-ukJH_KtB3pnHdRrRpZ2r5WgMSNGXnu-H8j/s16000/image22.gif">
        </div>
      
    
      
        <div class="modal-slide" data-slide-alt="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhBhlSum7x274E9KQGzLnjM9iXNEhifOJjKzt1Cwa5YyABCbaB68Mkr3gFvIVUhyphenhyphenaIGOqUE78MqGTK992NK8zrdKrqKxtFlYf1qeWYNkTa4PVzD3u_9lmQAjKnbLILHAkPhIOCvyAI6qBtfyf-z_xgUys3gXRJd_GSs3-qnyq0yFbjvmxdXAbVldV-xrIRJ/s16000/image11.png" data-slide-source="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhBhlSum7x274E9KQGzLnjM9iXNEhifOJjKzt1Cwa5YyABCbaB68Mkr3gFvIVUhyphenhyphenaIGOqUE78MqGTK992NK8zrdKrqKxtFlYf1qeWYNkTa4PVzD3u_9lmQAjKnbLILHAkPhIOCvyAI6qBtfyf-z_xgUys3gXRJd_GSs3-qnyq0yFbjvmxdXAbVldV-xrIRJ/s16000/image11.png">
          <img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhBhlSum7x274E9KQGzLnjM9iXNEhifOJjKzt1Cwa5YyABCbaB68Mkr3gFvIVUhyphenhyphenaIGOqUE78MqGTK992NK8zrdKrqKxtFlYf1qeWYNkTa4PVzD3u_9lmQAjKnbLILHAkPhIOCvyAI6qBtfyf-z_xgUys3gXRJd_GSs3-qnyq0yFbjvmxdXAbVldV-xrIRJ/s16000/image11.png" width="760" height="530" alt="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhBhlSum7x274E9KQGzLnjM9iXNEhifOJjKzt1Cwa5YyABCbaB68Mkr3gFvIVUhyphenhyphenaIGOqUE78MqGTK992NK8zrdKrqKxtFlYf1qeWYNkTa4PVzD3u_9lmQAjKnbLILHAkPhIOCvyAI6qBtfyf-z_xgUys3gXRJd_GSs3-qnyq0yFbjvmxdXAbVldV-xrIRJ/s16000/image11.png">
        </div>
      
    
      
        <div class="modal-slide" data-slide-alt="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJsf6Y6gV9VjK_rS_Bf_WLWdsJOq3sQbdaW26VSp2vX1Fq5j7VcWl4VDi3BeBFpEcH_YGrkU9ozJyuP5dh8tWWCU4yGzlmGBTfwM-kXGKZvdvI1DF17V4kSJSGGBIacqaCO4N1Oc8P4PymPWdglJbew_cjP9reFSJuHR3_ikZfZFuzN6aC8F17TAtiJPIg/s16000/image44.gif" data-slide-source="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJsf6Y6gV9VjK_rS_Bf_WLWdsJOq3sQbdaW26VSp2vX1Fq5j7VcWl4VDi3BeBFpEcH_YGrkU9ozJyuP5dh8tWWCU4yGzlmGBTfwM-kXGKZvdvI1DF17V4kSJSGGBIacqaCO4N1Oc8P4PymPWdglJbew_cjP9reFSJuHR3_ikZfZFuzN6aC8F17TAtiJPIg/s16000/image44.gif">
          <img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJsf6Y6gV9VjK_rS_Bf_WLWdsJOq3sQbdaW26VSp2vX1Fq5j7VcWl4VDi3BeBFpEcH_YGrkU9ozJyuP5dh8tWWCU4yGzlmGBTfwM-kXGKZvdvI1DF17V4kSJSGGBIacqaCO4N1Oc8P4PymPWdglJbew_cjP9reFSJuHR3_ikZfZFuzN6aC8F17TAtiJPIg/s16000/image44.gif" width="760" height="530" alt="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJsf6Y6gV9VjK_rS_Bf_WLWdsJOq3sQbdaW26VSp2vX1Fq5j7VcWl4VDi3BeBFpEcH_YGrkU9ozJyuP5dh8tWWCU4yGzlmGBTfwM-kXGKZvdvI1DF17V4kSJSGGBIacqaCO4N1Oc8P4PymPWdglJbew_cjP9reFSJuHR3_ikZfZFuzN6aC8F17TAtiJPIg/s16000/image44.gif">
        </div>
      
    
      
        <div class="modal-slide" data-slide-alt="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEidyInWvqdPpdIndLrxzykAODCeJ_p69uqvYOpasjFcBQU5o8Mtr-DiLfZXZrkJel9TD9SxZEmyIb58r6TZjRw57D8aSjl9P2jxCOsK7XZeXY0J3B8UMIFnl6aqXqhd0wft_NQGBi9KqpSUHAgw2c4JoYMdt27sKp6xcvOyMfjASpaZZzlI9o8lesj3GsrL/s16000/image14.gif" data-slide-source="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEidyInWvqdPpdIndLrxzykAODCeJ_p69uqvYOpasjFcBQU5o8Mtr-DiLfZXZrkJel9TD9SxZEmyIb58r6TZjRw57D8aSjl9P2jxCOsK7XZeXY0J3B8UMIFnl6aqXqhd0wft_NQGBi9KqpSUHAgw2c4JoYMdt27sKp6xcvOyMfjASpaZZzlI9o8lesj3GsrL/s16000/image14.gif">
          <img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEidyInWvqdPpdIndLrxzykAODCeJ_p69uqvYOpasjFcBQU5o8Mtr-DiLfZXZrkJel9TD9SxZEmyIb58r6TZjRw57D8aSjl9P2jxCOsK7XZeXY0J3B8UMIFnl6aqXqhd0wft_NQGBi9KqpSUHAgw2c4JoYMdt27sKp6xcvOyMfjASpaZZzlI9o8lesj3GsrL/s16000/image14.gif" width="760" height="530" alt="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEidyInWvqdPpdIndLrxzykAODCeJ_p69uqvYOpasjFcBQU5o8Mtr-DiLfZXZrkJel9TD9SxZEmyIb58r6TZjRw57D8aSjl9P2jxCOsK7XZeXY0J3B8UMIFnl6aqXqhd0wft_NQGBi9KqpSUHAgw2c4JoYMdt27sKp6xcvOyMfjASpaZZzlI9o8lesj3GsrL/s16000/image14.gif">
        </div>
      
    
      
        <div class="modal-slide" data-slide-alt="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQcwPsDQPUe4Uon7vWWSewbqcWsAdfUIJ4yLLFiCvdQKu4ffT6E5qIMeiabtxK5wudSL-jjxa_fW5aOaBvDILq_dQzeT4RMSULORJZrjwkDscDxLnLflUybqHlPf1J8O7KB171g5I9kLVgRbGP0mr0HxbG0pY7J9ojoEZLl4JZHaMQH490XmUR_IUj_YMO/s16000/image55.gif" data-slide-source="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQcwPsDQPUe4Uon7vWWSewbqcWsAdfUIJ4yLLFiCvdQKu4ffT6E5qIMeiabtxK5wudSL-jjxa_fW5aOaBvDILq_dQzeT4RMSULORJZrjwkDscDxLnLflUybqHlPf1J8O7KB171g5I9kLVgRbGP0mr0HxbG0pY7J9ojoEZLl4JZHaMQH490XmUR_IUj_YMO/s16000/image55.gif">
          <img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQcwPsDQPUe4Uon7vWWSewbqcWsAdfUIJ4yLLFiCvdQKu4ffT6E5qIMeiabtxK5wudSL-jjxa_fW5aOaBvDILq_dQzeT4RMSULORJZrjwkDscDxLnLflUybqHlPf1J8O7KB171g5I9kLVgRbGP0mr0HxbG0pY7J9ojoEZLl4JZHaMQH490XmUR_IUj_YMO/s16000/image55.gif" width="760" height="530" alt="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQcwPsDQPUe4Uon7vWWSewbqcWsAdfUIJ4yLLFiCvdQKu4ffT6E5qIMeiabtxK5wudSL-jjxa_fW5aOaBvDILq_dQzeT4RMSULORJZrjwkDscDxLnLflUybqHlPf1J8O7KB171g5I9kLVgRbGP0mr0HxbG0pY7J9ojoEZLl4JZHaMQH490XmUR_IUj_YMO/s16000/image55.gif">
        </div>
      
    
      
        <div class="modal-slide" data-slide-alt="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_4M2Sz50c_PDZkyHqZGfc5p5aRGpAS04ztN9N3s3VBn4_AD8GN7Vv6Vw-2phokpqtamutHT_6nGSsXb7271cfijLu3vJT1IV8Mmo1wlq1jfYcUPNs7TL6z0Cls3qGD1jA4Z0uRpj_rNXYLpFSbHEIqNOAA_V8VE_ZhsO7o-D64nDdmRei_hPEY7YT8lcg/s16000/image4.png" data-slide-source="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_4M2Sz50c_PDZkyHqZGfc5p5aRGpAS04ztN9N3s3VBn4_AD8GN7Vv6Vw-2phokpqtamutHT_6nGSsXb7271cfijLu3vJT1IV8Mmo1wlq1jfYcUPNs7TL6z0Cls3qGD1jA4Z0uRpj_rNXYLpFSbHEIqNOAA_V8VE_ZhsO7o-D64nDdmRei_hPEY7YT8lcg/s16000/image4.png">
          <img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_4M2Sz50c_PDZkyHqZGfc5p5aRGpAS04ztN9N3s3VBn4_AD8GN7Vv6Vw-2phokpqtamutHT_6nGSsXb7271cfijLu3vJT1IV8Mmo1wlq1jfYcUPNs7TL6z0Cls3qGD1jA4Z0uRpj_rNXYLpFSbHEIqNOAA_V8VE_ZhsO7o-D64nDdmRei_hPEY7YT8lcg/s16000/image4.png" width="760" height="530" alt="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_4M2Sz50c_PDZkyHqZGfc5p5aRGpAS04ztN9N3s3VBn4_AD8GN7Vv6Vw-2phokpqtamutHT_6nGSsXb7271cfijLu3vJT1IV8Mmo1wlq1jfYcUPNs7TL6z0Cls3qGD1jA4Z0uRpj_rNXYLpFSbHEIqNOAA_V8VE_ZhsO7o-D64nDdmRei_hPEY7YT8lcg/s16000/image4.png">
        </div>
      
    
      
        <div class="modal-slide" data-slide-alt="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4R591KKD1ZkmhTrjo28JovCeeo2bGjb0Tn5Ohr8KEooVqZqSNlgsrJrROaPWn5XXBzEohkhZMjaX2AV3M1RikyLgO7LfIgTFt54-uumb7xxPU6blnuFC8dN8W2SjK85tBKfZQ9Kn4oR-988YKXVUTbu-N5LWWX6JurqN6RRad7Bve59oEdZC-eMsn4HH9/s16000/metnet3.gif" data-slide-source="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4R591KKD1ZkmhTrjo28JovCeeo2bGjb0Tn5Ohr8KEooVqZqSNlgsrJrROaPWn5XXBzEohkhZMjaX2AV3M1RikyLgO7LfIgTFt54-uumb7xxPU6blnuFC8dN8W2SjK85tBKfZQ9Kn4oR-988YKXVUTbu-N5LWWX6JurqN6RRad7Bve59oEdZC-eMsn4HH9/s16000/metnet3.gif">
          <img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4R591KKD1ZkmhTrjo28JovCeeo2bGjb0Tn5Ohr8KEooVqZqSNlgsrJrROaPWn5XXBzEohkhZMjaX2AV3M1RikyLgO7LfIgTFt54-uumb7xxPU6blnuFC8dN8W2SjK85tBKfZQ9Kn4oR-988YKXVUTbu-N5LWWX6JurqN6RRad7Bve59oEdZC-eMsn4HH9/s16000/metnet3.gif" width="760" height="530" alt="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4R591KKD1ZkmhTrjo28JovCeeo2bGjb0Tn5Ohr8KEooVqZqSNlgsrJrROaPWn5XXBzEohkhZMjaX2AV3M1RikyLgO7LfIgTFt54-uumb7xxPU6blnuFC8dN8W2SjK85tBKfZQ9Kn4oR-988YKXVUTbu-N5LWWX6JurqN6RRad7Bve59oEdZC-eMsn4HH9/s16000/metnet3.gif">
        </div>
      
    
      
        <div class="modal-slide" data-slide-alt="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg88AA6lzoFtJd9ZOXt6AiiT_gTtFcJwsZNzUJ63kuYtq7XYs0LHUSp3q37zOPolA-rR_WQPciuDZsg-4Y3J0qrLUmNxMi1iBqyR4ICy4MKwRFXHtQhfkWdwPREd4qm9FVlN6rpLEebDC7MfBg7hToXhQvdsFoGObtu-Lqty3ZQSALf1yjna37tJY4fAptE/s16000/image6.gif" data-slide-source="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg88AA6lzoFtJd9ZOXt6AiiT_gTtFcJwsZNzUJ63kuYtq7XYs0LHUSp3q37zOPolA-rR_WQPciuDZsg-4Y3J0qrLUmNxMi1iBqyR4ICy4MKwRFXHtQhfkWdwPREd4qm9FVlN6rpLEebDC7MfBg7hToXhQvdsFoGObtu-Lqty3ZQSALf1yjna37tJY4fAptE/s16000/image6.gif">
          <img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg88AA6lzoFtJd9ZOXt6AiiT_gTtFcJwsZNzUJ63kuYtq7XYs0LHUSp3q37zOPolA-rR_WQPciuDZsg-4Y3J0qrLUmNxMi1iBqyR4ICy4MKwRFXHtQhfkWdwPREd4qm9FVlN6rpLEebDC7MfBg7hToXhQvdsFoGObtu-Lqty3ZQSALf1yjna37tJY4fAptE/s16000/image6.gif" width="760" height="530" alt="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg88AA6lzoFtJd9ZOXt6AiiT_gTtFcJwsZNzUJ63kuYtq7XYs0LHUSp3q37zOPolA-rR_WQPciuDZsg-4Y3J0qrLUmNxMi1iBqyR4ICy4MKwRFXHtQhfkWdwPREd4qm9FVlN6rpLEebDC7MfBg7hToXhQvdsFoGObtu-Lqty3ZQSALf1yjna37tJY4fAptE/s16000/image6.gif">
        </div>
      
    
    </div>
  </div>


    
</div>


    </main>

    
    
      
        
          
            


  <div class="gweb-footer__border-top"></div>
  <footer class="gweb-footer" role="contentinfo">
    
      <div class="gweb-footer-wrapper-main">
        
          <div class="gweb-footer-social_links">
            


  <section class="glue-social">
    <div class="glue-social__group glue-social--monochrome">
      <h2 class="glue-social__title glue-social__title--inline caption">
        Follow us
      </h2>
      <nav class="js-gt-follow-us-wrapper" aria-label="Social media links">
        <ul class="glue-social__list" role="list">
            
              
                  <li class="glue-social__item">
                    <a class="glue-social__link"
                        href="https://x.com/GoogleResearch"
                        aria-label="x"
                        title="Follow us on x"
                        target="_blank"
                        rel="noopener"
                        data-gtm-event="social"
                        data-gt-method="x">
                      <svg id="icon-x" role="presentation" aria-hidden="true"
                          class="glue-icon glue-icon--social glue-icon--24px">
                        <use href="/gr/static/assets/icons/x.svg?v=2#x"></use>
                      </svg>
                    </a>
                  </li>
              
                  <li class="glue-social__item">
                    <a class="glue-social__link"
                        href="https://www.linkedin.com/showcase/googleresearch/"
                        aria-label="linkedin"
                        title="Follow us on linkedin"
                        target="_blank"
                        rel="noopener"
                        data-gtm-event="social"
                        data-gt-method="linkedin">
                      <svg id="icon-linkedin" role="presentation" aria-hidden="true"
                          class="glue-icon glue-icon--social glue-icon--24px">
                        <use href="/gr/static/assets/icons/linkedin.svg?v=2#linkedin"></use>
                      </svg>
                    </a>
                  </li>
              
                  <li class="glue-social__item">
                    <a class="glue-social__link"
                        href="https://www.youtube.com/c/GoogleResearch"
                        aria-label="youtube"
                        title="Follow us on youtube"
                        target="_blank"
                        rel="noopener"
                        data-gtm-event="social"
                        data-gt-method="youtube">
                      <svg id="icon-youtube" role="presentation" aria-hidden="true"
                          class="glue-icon glue-icon--social glue-icon--24px">
                        <use href="/gr/static/assets/icons/youtube.svg?v=2#youtube"></use>
                      </svg>
                    </a>
                  </li>
              
                  <li class="glue-social__item">
                    <a class="glue-social__link"
                        href="https://github.com/google-research"
                        aria-label="github"
                        title="Follow us on github"
                        target="_blank"
                        rel="noopener"
                        data-gtm-event="social"
                        data-gt-method="github">
                      <svg id="icon-github" role="presentation" aria-hidden="true"
                          class="glue-icon glue-icon--social glue-icon--24px">
                        <use href="/gr/static/assets/icons/github.svg?v=2#github"></use>
                      </svg>
                    </a>
                  </li>
              
            
        </ul>
      </nav>
    </div>
  </section>


          </div>
        
        <div class="gweb-footer-main_links">
          


  <div class="gweb-footer-main-links__wrapper">
    <div class="gweb-footer-main-links__title-wrapper">
      
        <h2 class="headline">Explore our other initiatives</h2>
      
    </div>
    <div class="gweb-footer-main-links__content-wrapper">
      
        <div class="gweb-footer-main-links__link-group align-auto">
          <div class="gweb-footer-main-links__group-heading-wrapper">
            
              <h3 class="gweb-footer-main-links__group-title headline-6">Google AI</h3>
            
            
              <div class="gweb-footer-main-links__group-description text-body">
                <span>Discover how Google AI is committed to enriching knowledge and solving complex challenges</span>
              </div>
            
          </div>
          <ul class="gweb-footer-main-links__group-links-wrapper" role="list">
            
              
                <li>
                  



  
  
    <a href="https://ai.google/products/"
        target="_blank" rel="noopener noreferrer"
        
        class="not-glue"
        
        data-gtm-event="select_content"
        data-event-content-type="outbound"
        data-event-content-name="Products"
        
        >
      <div class="link__label">
        
          Products
        
      </div>
    </a>
  


                </li>
              
            
              
                <li>
                  



  
  
    <a href="https://ai.google/build/"
        target="_blank" rel="noopener noreferrer"
        
        class="not-glue"
        
        data-gtm-event="select_content"
        data-event-content-type="outbound"
        data-event-content-name="Build"
        
        >
      <div class="link__label">
        
          Build
        
      </div>
    </a>
  


                </li>
              
            
              
                <li>
                  



  
  
    <a href="https://ai.google/research/"
        target="_blank" rel="noopener noreferrer"
        
        class="not-glue"
        
        data-gtm-event="select_content"
        data-event-content-type="outbound"
        data-event-content-name="Research"
        
        >
      <div class="link__label">
        
          Research
        
      </div>
    </a>
  


                </li>
              
            
              
                <li>
                  



  
  
    <a href="https://ai.google/public-policy-perspectives/"
        target="_blank" rel="noopener noreferrer"
        
        class="not-glue"
        
        data-gtm-event="select_content"
        data-event-content-type="outbound"
        data-event-content-name="Responsibility"
        
        >
      <div class="link__label">
        
          Responsibility
        
      </div>
    </a>
  


                </li>
              
            
              
                <li>
                  



  
  
    <a href="https://ai.google/societal-impact/"
        target="_blank" rel="noopener noreferrer"
        
        class="not-glue"
        
        data-gtm-event="select_content"
        data-event-content-type="outbound"
        data-event-content-name="Societal Impact"
        
        >
      <div class="link__label">
        
          Societal Impact
        
      </div>
    </a>
  


                </li>
              
            
              
                <li>
                  



  
  
    <a href="https://ai.google/our-ai-journey/?section=intro"
        target="_blank" rel="noopener noreferrer"
        
        class="not-glue"
        
        data-gtm-event="select_content"
        data-event-content-type="outbound"
        data-event-content-name="About"
        
        >
      <div class="link__label">
        
          About
        
      </div>
    </a>
  


                </li>
              
            
          </ul>
          
        </div>
      
        <div class="gweb-footer-main-links__link-group align-auto">
          <div class="gweb-footer-main-links__group-heading-wrapper">
            
              <h3 class="gweb-footer-main-links__group-title headline-6">Google Cloud</h3>
            
            
              <div class="gweb-footer-main-links__group-description text-body">
                <span>High-performance infrastructure for cloud computing, data analytics &amp; machine learning</span>
              </div>
            
          </div>
          <ul class="gweb-footer-main-links__group-links-wrapper" role="list">
            
              
                <li>
                  



  
  
    <a href="https://cloud.google.com/"
        target="_blank" rel="noopener noreferrer"
        
        class="not-glue"
        
        data-gtm-event="select_content"
        data-event-content-type="outbound"
        data-event-content-name="Overview"
        
        >
      <div class="link__label">
        
          Overview
        
      </div>
    </a>
  


                </li>
              
            
              
                <li>
                  



  
  
    <a href="https://cloud.google.com/solutions"
        target="_blank" rel="noopener noreferrer"
        
        class="not-glue"
        
        data-gtm-event="select_content"
        data-event-content-type="outbound"
        data-event-content-name="Solutions"
        
        >
      <div class="link__label">
        
          Solutions
        
      </div>
    </a>
  


                </li>
              
            
              
                <li>
                  



  
  
    <a href="https://cloud.google.com/products"
        target="_blank" rel="noopener noreferrer"
        
        class="not-glue"
        
        data-gtm-event="select_content"
        data-event-content-type="outbound"
        data-event-content-name="Products"
        
        >
      <div class="link__label">
        
          Products
        
      </div>
    </a>
  


                </li>
              
            
              
                <li>
                  



  
  
    <a href="https://cloud.google.com/pricing"
        target="_blank" rel="noopener noreferrer"
        
        class="not-glue"
        
        data-gtm-event="select_content"
        data-event-content-type="outbound"
        data-event-content-name="Pricing"
        
        >
      <div class="link__label">
        
          Pricing
        
      </div>
    </a>
  


                </li>
              
            
              
                <li>
                  



  
  
    <a href="https://cloud.google.com/resources"
        target="_blank" rel="noopener noreferrer"
        
        class="not-glue"
        
        data-gtm-event="select_content"
        data-event-content-type="outbound"
        data-event-content-name="Resources"
        
        >
      <div class="link__label">
        
          Resources
        
      </div>
    </a>
  


                </li>
              
            
          </ul>
          
        </div>
      
        <div class="gweb-footer-main-links__link-group align-auto">
          <div class="gweb-footer-main-links__group-heading-wrapper">
            
              <h3 class="gweb-footer-main-links__group-title headline-6">Google DeepMind</h3>
            
            
              <div class="gweb-footer-main-links__group-description text-body">
                <span>Our mission is to build AI responsibly to benefit humanity</span>
              </div>
            
          </div>
          <ul class="gweb-footer-main-links__group-links-wrapper" role="list">
            
              
                <li>
                  



  
  
    <a href="https://deepmind.google/models/"
        target="_blank" rel="noopener noreferrer"
        
        class="not-glue"
        
        data-gtm-event="select_content"
        data-event-content-type="outbound"
        data-event-content-name="Models"
        
        >
      <div class="link__label">
        
          Models
        
      </div>
    </a>
  


                </li>
              
            
              
                <li>
                  



  
  
    <a href="https://deepmind.google/research/"
        target="_blank" rel="noopener noreferrer"
        
        class="not-glue"
        
        data-gtm-event="select_content"
        data-event-content-type="outbound"
        data-event-content-name="Research"
        
        >
      <div class="link__label">
        
          Research
        
      </div>
    </a>
  


                </li>
              
            
              
                <li>
                  



  
  
    <a href="https://deepmind.google/science/"
        target="_blank" rel="noopener noreferrer"
        
        class="not-glue"
        
        data-gtm-event="select_content"
        data-event-content-type="outbound"
        data-event-content-name="Science"
        
        >
      <div class="link__label">
        
          Science
        
      </div>
    </a>
  


                </li>
              
            
              
                <li>
                  



  
  
    <a href="https://deepmind.google/about/"
        target="_blank" rel="noopener noreferrer"
        
        class="not-glue"
        
        data-gtm-event="select_content"
        data-event-content-type="outbound"
        data-event-content-name="About"
        
        >
      <div class="link__label">
        
          About
        
      </div>
    </a>
  


                </li>
              
            
          </ul>
          
        </div>
      
        <div class="gweb-footer-main-links__link-group align-auto">
          <div class="gweb-footer-main-links__group-heading-wrapper">
            
              <h3 class="gweb-footer-main-links__group-title headline-6">Google Labs</h3>
            
            
              <div class="gweb-footer-main-links__group-description text-body">
                <span>Explore the future of AI responsibly with Google Labs</span>
              </div>
            
          </div>
          <ul class="gweb-footer-main-links__group-links-wrapper" role="list">
            
              
                <li>
                  



  
  
    <a href="https://labs.google/#about"
        target="_blank" rel="noopener noreferrer"
        
        class="not-glue"
        
        data-gtm-event="select_content"
        data-event-content-type="outbound"
        data-event-content-name="About"
        
        >
      <div class="link__label">
        
          About
        
      </div>
    </a>
  


                </li>
              
            
              
                <li>
                  



  
  
    <a href="https://labs.google/#experiments"
        target="_blank" rel="noopener noreferrer"
        
        class="not-glue"
        
        data-gtm-event="select_content"
        data-event-content-type="outbound"
        data-event-content-name="Experiments"
        
        >
      <div class="link__label">
        
          Experiments
        
      </div>
    </a>
  


                </li>
              
            
              
                <li>
                  



  
  
    <a href="https://labs.google/#stay-connected"
        target="_blank" rel="noopener noreferrer"
        
        class="not-glue"
        
        data-gtm-event="select_content"
        data-event-content-type="outbound"
        data-event-content-name="Stay connected"
        
        >
      <div class="link__label">
        
          Stay connected
        
      </div>
    </a>
  


                </li>
              
            
          </ul>
          
        </div>
      
    </div>
  </div>


        </div>
      </div>
    
    <div class="gweb-footer-wrapper-legal">
      <div class="gweb-footer-google_links">
        


  <div class="gweb-footer-google-links__wrapper">
    <div class="gweb-footer-google-links__title-wrapper">
      <a class="gweb-footer-google-links__brand"
          target="_blank"
          aria-label="Google"
          title="Google"
          href="https://www.google.com/?utm_source=research.google&utm_medium=referral"
          data-gtm-event="nav_select"
          data-event-nav-type="footer"
          data-event-nav-name="https://www.google.com/?utm_source=research.google&utm_medium=referral">
        <svg role="img"
            aria-hidden="true"
            focusable="false"
            width="75"
            height="25">
          <use href="/gr/static/assets/icons/glue-icons.svg#google-solid-logo"></use>
        </svg>
      </a>
    </div>
    <div class="gweb-footer-google-links__content-wrapper">
      
        <div class="gweb-footer-google-links__link">
          <a class="not-glue"
              href="https://about.google/"
              aria-label="About Google"
              data-gtm-event="nav_select"
              data-event-nav-type="footer"
              data-event-nav-name="About Google"
              target="_blank" rel="noopener noreferrer"
              >
            <span>About Google</span>
          </a>
        </div>
      
        <div class="gweb-footer-google-links__link">
          <a class="not-glue"
              href="https://about.google/intl/en/products/"
              aria-label="Google Products"
              data-gtm-event="nav_select"
              data-event-nav-type="footer"
              data-event-nav-name="Google Products"
              target="_blank" rel="noopener noreferrer"
              >
            <span>Google Products</span>
          </a>
        </div>
      
        <div class="gweb-footer-google-links__link">
          <a class="not-glue"
              href="https://policies.google.com/privacy"
              aria-label="Privacy"
              data-gtm-event="nav_select"
              data-event-nav-type="footer"
              data-event-nav-name="Privacy"
              target="_blank" rel="noopener noreferrer"
              >
            <span>Privacy</span>
          </a>
        </div>
      
        <div class="gweb-footer-google-links__link">
          <a class="not-glue"
              href="https://policies.google.com/terms"
              aria-label="Terms"
              data-gtm-event="nav_select"
              data-event-nav-type="footer"
              data-event-nav-name="Terms"
              target="_blank" rel="noopener noreferrer"
              >
            <span>Terms</span>
          </a>
        </div>
      
      
      <div class="gweb-footer-google-links__link">
        <button type="button"
            aria-hidden="true"
            class="not-glue glue-cookie-notification-bar-control">
          Cookies management controls
        </button>
      </div>
    </div>
  </div>


      </div>
    </div>
  </footer>


          
        
      
    

    <div id="dynamicImageModal" class="image-modal">
  <span class="image-modal-close">&times;</span>
  <div class="image-modal-content">
    <div class="dynamic-modal-image">
      <img width="800" height="540">
    </div>
  </div>
</div>


    
    <script>
        var scriptUrl = "https://www.gstatic.com/glue/v27_1/material-components-web.min.js";
        var scriptElement = document.createElement('script');
        scriptElement.async = false;
        scriptElement.src = scriptUrl;
        document.body.appendChild(scriptElement);
    </script>
    <script>
        var scriptUrl = "https://www.youtube.com/player_api";
        var scriptElement = document.createElement('script');
        scriptElement.async = false;
        scriptElement.src = scriptUrl;
        document.body.appendChild(scriptElement);
    </script>
    <script>
        var scriptUrl = "/gr/static/js/googleresearch.js?id=1db86c2c4ce1c6902b92830acba1963e";
        var scriptElement = document.createElement('script');
        scriptElement.async = false;
        scriptElement.src = scriptUrl;
        document.body.appendChild(scriptElement);
    </script>
    <script>
        var scriptUrl = "https://support.google.com/inapp/api.js";
        var scriptElement = document.createElement('script');
        scriptElement.async = false;
        scriptElement.src = scriptUrl;
        document.body.appendChild(scriptElement);
    </script>

    
    
    

    <script>
        var scripts = [
            "https://www.gstatic.com/glue/cookienotificationbar/cookienotificationbar.min.js"
        ];

        scripts.forEach(function(scriptUrl) {
            var scriptElement = document.createElement('script');
            scriptElement.async = false;
            scriptElement.src = scriptUrl;
            scriptElement.setAttribute("data-glue-cookie-notification-bar-category", "2B");
            document.body.appendChild(scriptElement);
        });
    </script>
</body>

</html>

