"use strict"; // Start of use strict



function accrodion () {
    if ($('.accrodion-grp').length) {
        var accrodionGrp = $('.accrodion-grp');
        accrodionGrp.each(function () {
            var accrodionName = $(this).data('grp-name');
            var Self = $(this);
            Self.addClass(accrodionName);
            Self.find('.accrodion .accrodion-content').hide();
            Self.find('.accrodion.active').find('.accrodion-content').show();
            var accordionWrap = Self.find('.accrodion');
            accordionWrap.each(function() {
                $(this).find('.accrodion-title').on('click', function () {
                    if ($(this).parent().hasClass('active') === false ) {                   
                        $('.accrodion-grp.'+accrodionName).find('.accrodion').removeClass('active');
                        $('.accrodion-grp.'+accrodionName).find('.accrodion').find('.accrodion-content').slideUp();
                        $(this).parent().addClass('active');                    
                        $(this).parent().find('.accrodion-content').slideDown();    
                    };
                });
            });
        });
        
    };
}

function thmMailchimp() {
    if ($('.mailchimp-form').length) {
        var mailchimpFrm = $('.mailchimp-form');
        mailchimpFrm.each(function() {
            var mailChimpWrapper = $(this);

            mailChimpWrapper.validate({ // initialize the plugin
                rules: {
                    email: {
                        required: true,
                        email: true
                    }
                },
                submitHandler: function(form) {
                    // sending value with ajax request
                    $.post($(form).attr('action'), $(form).serialize(), function(response) {
                        $(form).parent().find('.result').append(response);
                        $(form).find('input[type="text"]').val('');
                        $(form).find('input[type="email"]').val('');
                        $(form).find('textarea').val('');
                    });
                    return false;
                }
            });
        });
    };
}

function priceFilter() {
    if ($('.range-slider-price').length) {

        var priceRange = document.getElementById('range-slider-price');

        noUiSlider.create(priceRange, {
            start: [30, 150],
            limit: 200,
            behaviour: 'drag',
            connect: true,
            range: {
                'min': 10,
                'max': 200
            }
        });

        var limitFieldMin = document.getElementById('min-value-rangeslider');
        var limitFieldMax = document.getElementById('max-value-rangeslider');

        priceRange.noUiSlider.on('update', function(values, handle) {
            (handle ? $(limitFieldMax) : $(limitFieldMin)).text(values[handle]);
        });
    };
}

function thmOwlCarousel() {
    if ($('.testimonial-carousel-one').length) {
        $('.testimonial-carousel-one').owlCarousel({
            loop: true,
            margin: 0,
            nav: false,
            navText: [
                '<i class="fa fa-angle-left"></i>',
                '<i class="fa fa-angle-right"></i>'
            ],
            dots: true,
            autoWidth: false,
            autoplay: true,
            autoplayTimeout: 3000,
            autoplayHoverPause: true,
            responsive: {
                0: {
                    items: 1
                },
                480: {
                    items: 1
                },
                600: {
                    items: 1
                },
                1000: {
                    items: 1
                }
            }
        });
    };
    if ($('.service-home-one-carousel').length) {
        $('.service-home-one-carousel').owlCarousel({
            loop: true,
            margin: 30,
            nav: true,
            navText: [
                '<i class="fa fa-angle-left"></i>',
                '<i class="fa fa-angle-right"></i>'
            ],
            dots: false,
            autoWidth: false,
            autoplay: true,
            autoplayTimeout: 3000,
            autoplayHoverPause: true,
            responsive: {
                0: {
                    items: 1
                },
                480: {
                    items: 1
                },
                667: {
                    items: 2
                },
                768: {
                    items: 2
                },
                1024: {
                    items: 3
                },
                1200: {
                    items: 4
                }
            }
        });
    };
    if ($('.testimonial-carousel').length) {
        $('.testimonial-carousel').owlCarousel({
            loop: true,
            margin: 0,
            nav: true,
            navText: [
                '<i class="fa fa-angle-left"></i>',
                '<i class="fa fa-angle-right"></i>'
            ],
            dots: false,
            autoWidth: false,
            autoplay: true,
            autoplayTimeout: 3000,
            autoplayHoverPause: true,
            responsive: {
                0: {
                    items: 1
                },
                480: {
                    items: 1
                },
                768: {
                    items: 1
                },
                1000: {
                    items: 1
                }
            }
        });
    };
    if ($('.what-we-do-carousel').length) {
        $('.what-we-do-carousel').owlCarousel({
            loop: true,
            margin: 30,
            nav: true,
            navText: [
                '<i class="fa fa-angle-left"></i>',
                '<i class="fa fa-angle-right"></i>'
            ],
            dots: false,
            autoWidth: false,
            autoplay: true,
            autoplayTimeout: 3000,
            autoplayHoverPause: true,
            responsive: {
                0: {
                    items: 1
                },
                480: {
                    items: 1
                },
                600: {
                    items: 3
                },
                1000: {
                    items: 4
                },
                1200: {
                    items: 4
                },
                1400: {
                    items: 4
                }
            }
        });
    };
    if ($('.client-carousel-home-three').length) {
        $('.client-carousel-home-three').owlCarousel({
            loop: true,
            margin: 70,
            nav: false,
            navText: [
                '<i class="fa fa-angle-left"></i>',
                '<i class="fa fa-angle-right"></i>'
            ],
            dots: false,
            autoWidth: false,
            autoplay: true,
            autoplayTimeout: 3000,
            autoplayHoverPause: true,
            responsive: {
                0: {
                    items: 1
                },
                480: {
                    items: 2
                },
                600: {
                    items: 3
                },
                1000: {
                    items: 6
                }
            }
        });
    };
    if ($('.project-carousel-home-two').length) {
        $('.project-carousel-home-two').owlCarousel({
            loop: true,
            margin: 30,
            nav: false,
            navText: [
                '<i class="fa fa-angle-left"></i>',
                '<i class="fa fa-angle-right"></i>'
            ],
            dots: false,
            autoWidth: false,
            autoplay: true,
            autoplayTimeout: 3000,
            autoplayHoverPause: true,
            responsive: {
                0: {
                    items: 1
                },
                480: {
                    items: 1
                },
                600: {
                    items: 3
                },
                768: {
                    items: 1
                },
                1000: {
                    items: 3
                },
                1200: {
                    items: 3
                }
            }
        });
        var leftNav = $('.project-carousel-btn .left-nav');
        var rightNav = $('.project-carousel-btn .right-nav');
        leftNav.on('click', function() {
           $('.project-carousel-home-two').trigger('next.owl.carousel'); 
           return false;
        });
        rightNav.on('click', function() {
           $('.project-carousel-home-two').trigger('prev.owl.carousel'); 
           return false;
        });
    };
    if ($('.brand-carousel').length) {
        $('.brand-carousel').owlCarousel({
            loop: true,
            margin: 50,
            nav: false,
            navText: [
                '<i class="fa fa-angle-left"></i>',
                '<i class="fa fa-angle-right"></i>'
            ],
            dots: false,
            autoWidth: false,
            autoplay: true,
            autoplayTimeout: 3000,
            autoplayHoverPause: true,
            responsive: {
                0: {
                    items: 1
                },
                480: {
                    items: 2
                },
                600: {
                    items: 3
                },
                1000: {
                    items: 5
                },
                1200: {
                    items: 5
                }
            }
        });
    };
    
}

function cartTouchSpin() {
    if ($('.quantity-spinner').length) {
        $("input.quantity-spinner").TouchSpin({
            verticalbuttons: true
        });
    }
}


function galleryMasonaryLayout() {
    if ($('.masonary-layout').length) {
        $('.masonary-layout').isotope({
            layoutMode: 'masonry'
        });
    }

    if ($('.post-filter').length) {
        $('.post-filter li').children('span').on('click', function() {
            var Self = $(this);
            var selector = Self.parent().attr('data-filter');
            var postFilterLi = $('.post-filter li');
            postFilterLi.children('span').parent().removeClass('active');
            Self.parent().addClass('active');


            $('.filter-layout').isotope({
                filter: selector,
                animationOptions: {
                    duration: 500,
                    easing: 'linear',
                    queue: false
                }
            });
            return false;
        });
    }

    if ($('.post-filter.has-dynamic-filter-counter').length) {
        // var allItem = $('.single-filter-item').length;

        var activeFilterItem = $('.post-filter.has-dynamic-filter-counter').find('li');

        activeFilterItem.each(function() {
            var filterElement = $(this).data('filter');
            var count = $('.gallery-content').find(filterElement).length;

            $(this).children('span').append('<span class="count"><b>' + count + '</b></span>');
        });
    };
}


function thmbxSlider() {
    if ($('.feature-carousel-box').length) {
        $('.feature-carousel-box').bxSlider({
            mode: 'vertical',
            auto: true,
            autoControls: false,
            controls: false,
            pause: 3000,
            slideMargin: 0
        });
    }
}



function thmMasterSliderStaff() {
    if ($('.testimonial-about-carousel').length) {
        var slider = new MasterSlider();
        slider.setup('masterslider', {
            loop: true,
            width: 80,
            height: 80,
            speed: 20,
            view: 'fadeBasic',
            preload: 'all',
            space: 20,
            wheel: true
        });
        slider.control('arrows');
        slider.control('slideinfo', { insertTo: '#staff-info' });
    };
}
thmMasterSliderStaff();

function stickyHeader() {
    if ($('.stricky').length) {
        var strickyScrollPos = 100;
        var sticky = $('.stricky');
        if ($(window).scrollTop() > strickyScrollPos) {
            sticky.removeClass('slideIn animated').addClass('stricky-fixed slideInDown animated');
            $('.scroll-to-top').fadeIn(500);
        } else if ($(this).scrollTop() <= strickyScrollPos) {
            sticky.removeClass('stricky-fixed slideInDown animated').addClass('slideIn animated');
            $('.scroll-to-top').fadeOut(500);
        }
    };
}


function thmLightBox() {
    if ($('.img-popup').length) {
        var groups = {};
        var imgPOpup = $('.img-popup');
        imgPOpup.each(function() {
            var id = parseInt($(this).attr('data-group'), 10);

            if (!groups[id]) {
                groups[id] = [];
            }

            groups[id].push(this);
        });


        $.each(groups, function() {

            $(this).magnificPopup({
                type: 'image',
                closeOnContentClick: true,
                closeBtnInside: false,
                gallery: { enabled: true }
            });

        });

    };
}

function thmCounter() {
    if ($('.counter').length) {
        $('.counter').counterUp({
            delay: 10,
            time: 3000
        });
    };
}

function thmScrollAnim() {
    if ($('.wow').length) {
        var wow = new WOW({
            mobile: false
        });
        wow.init();
    };
}

function contactFormValidation() {
    if ($('.contact-form').length) {
        $('.contact-form').validate({ // initialize the plugin
            rules: {
                name: {
                    required: true
                },
                email: {
                    required: true,
                    email: true
                },
                message: {
                    required: true
                },
                subject: {
                    required: true
                }
            },
            submitHandler: function(form) {
                // sending value with ajax request
                $.post($(form).attr('action'), $(form).serialize(), function(response) {
                    $(form).find('.form-result').append(response);
                    $(form).find('input[type="text"]').val('');
                    $(form).find('input[type="email"]').val('');
                    $(form).find('textarea').val('');
                    console.log(response);
                });
                return false;
            }
        });
    }
}

function thmVideoPopup() {
    if ($('.video-popup').length) {
        $('.video-popup').magnificPopup({
            disableOn: 700,
            type: 'iframe',
            mainClass: 'mfp-fade',
            removalDelay: 160,
            preloader: true,

            fixedContentPos: false
        });
    };
}

function scrollToTarget() {
    if ($('.scroll-to-target').length) {
        $(".scroll-to-target").on('click', function() {
            var target = $(this).attr('data-target');
            // animate
            $('html, body').animate({
                scrollTop: $(target).offset().top
            }, 1000);
            return false;

        });
    }
}

function mobileNavToggle () {
    if ($('#main-nav-bar .navbar-nav .sub-menu').length) {
        var submenuWrap = $('#main-nav-bar .navbar-nav .sub-menu');
        submenuWrap.parent('li').children('a').append(function () {
            // return '<button class="sub-nav-toggler"> <span class="sr-only">Toggle navigation</span> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button>';
            return '<button class="sub-nav-toggler"><i class="fa fa-angle-down"></i></button>';
        });
        var subNavToggler = $('#main-nav-bar .navbar-nav .sub-nav-toggler');
        subNavToggler.on('click', function () {
            var Self = $(this);
            Self.parent().parent().children('.sub-menu').slideToggle();
            return false;
        });

    };
}

function sideNavToggler () {
    if ($('.side-navigation').length) {
        $('.side-nav-opener').on('click', function () {
            $('.side-navigation').addClass('open');
            return false;
        });
        $('.side-navigation-close-btn').on('click', function () {
            $('.side-navigation').removeClass('open');
            return false;
        });
    };
}

function countDownTimer () {
    if ($('.countdown-box').length) {
        var countDownBox = $('.countdown-box');
        countDownBox.each(function () {
            var Self = $(this);
            var countDate = Self.data('countdown-time'); // getting date

            Self.countdown(countDate, function(event) {                    
                $(this).html('<li> <div class="box"> <h4>'+ event.strftime('%D') +'</h4> <span>Days</span> </div> </li> <li> <div class="box"> <h4>'+ event.strftime('%H') +'</h4> <span>Hours</span> </div> </li> <li> <div class="box"> <h4>'+ event.strftime('%M') +'</h4> <span>Minutes</span> </div> </li> <li> <div class="box"> <h4>'+ event.strftime('%S') +'</h4> <span>Seconds</span> </div> </li> ');
            });
        });

        

    };
}

function bootstrapAnimatedLayer() {

    /* Demo Scripts for Bootstrap Carousel and Animate.css article
     * on SitePoint by Maria Antonietta Perna
     */

    //Function to animate slider captions 
    function doAnimations(elems) {
        //Cache the animationend event in a variable
        var animEndEv = 'webkitAnimationEnd animationend';

        elems.each(function() {
            var $this = $(this),
                $animationType = $this.data('animation');
            $this.addClass($animationType).one(animEndEv, function() {
                $this.removeClass($animationType);
            });
        });
    }

    //Variables on page load 
    var $myCarousel = $('#minimal-bootstrap-carousel'),
        $firstAnimatingElems = $myCarousel.find('.item:first').find("[data-animation ^= 'animated']");

    //Initialize carousel 
    $myCarousel.carousel({
        interval: 7000
    });

    //Animate captions in first slide on page load 
    doAnimations($firstAnimatingElems);

    //Pause carousel  
    $myCarousel.carousel('pause');


    //Other slides to be animated on carousel slide event 
    $myCarousel.on('slide.bs.carousel', function(e) {
        var $animatingElems = $(e.relatedTarget).find("[data-animation ^= 'animated']");
        doAnimations($animatingElems);
    });
}

function searchPopup () {
    if ($('.popup-with-zoom-anim').length) {
        $('.popup-with-zoom-anim').magnificPopup({
            type: 'inline',

            fixedContentPos: false,
            fixedBgPos: true,

            overflowY: 'auto',

            closeBtnInside: true,
            preloader: false,

            midClick: true,
            removalDelay: 300,
            mainClass: 'my-mfp-zoom-in'
        });
    };
}

// instance of fuction while Document ready event   
jQuery(document).on('ready', function() {
    (function($) {
        thmMailchimp();
        priceFilter();
        thmOwlCarousel();
        cartTouchSpin();
        thmLightBox();
        thmCounter();
        thmScrollAnim();
        contactFormValidation();
        scrollToTarget();
        thmVideoPopup();
        accrodion();
        mobileNavToggle();
        sideNavToggler();
        countDownTimer();
        bootstrapAnimatedLayer();
        searchPopup();
    })(jQuery);
});

// instance of fuction while Window Load event
jQuery(window).on('load', function() {
    (function($) {
        thmbxSlider();
        galleryMasonaryLayout();
    })(jQuery);
});

// instance of fuction while Window Scroll event
jQuery(window).on('scroll', function() {
    (function($) {
        stickyHeader();
    })(jQuery);
});
