jQuery(document).ready(function(){
    // for animation
    AOS.init({
        duration: 2000
    });
    
    jQuery("#home-banner-wrapper").slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        dots: true,
        draggable: true,
        autoplay: true,
        autoplaySpeed: 2000,
        arrows: false,
    });
    jQuery(".ksd-researcher-point").slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        dots: true,
        arrows: false,
        autoplay: true,
        autoplaySpeed: 2500,
    });
});