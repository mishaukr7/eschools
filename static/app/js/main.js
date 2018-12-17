$('.main-banner').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 5000,
    dots: false,
    infinite: true,
    speed: 300,
    adaptiveHeight: true,
    prevArrow: false,
    nextArrow: false

});

$('.slider-new-product').slick({
    slidesToShow: 5,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    prevArrow: '<img class="slick-prev" src="image/arr_l.png">',
    nextArrow: '<img class="slick-next" src="image/arr_r.png">'
});

$('.drop-menu').toggleClass("visible");




// открыть по кнопке
$('.js-button-come').click(function () {

    $('.js-overlay-come').fadeIn();
    $('.js-overlay-come').addClass('disabled');
});

// закрыть на крестик
$('.js-close-come').click(function () {
    $('.js-overlay-come').fadeOut();

});

// закрыть по клику вне окна
$(document).mouseup(function (e) {
    var popup = $('.js-popup-come');
    if (e.target != popup[0] && popup.has(e.target).length === 0) {
        $('.js-overlay-come').fadeOut();
    }
});

// открыть по кнопке
$('.js-button-registration').click(function () {

    $('.js-overlay-registration').fadeIn();
    $('.js-overlay-registration').addClass('disabled');
});

// закрыть на крестик
$('.js-close-registration').click(function () {
    $('.js-overlay-registration').fadeOut();

});

// закрыть по клику вне окна
$(document).mouseup(function (e) {
    var popup = $('.js-popup-registration');
    if (e.target != popup[0] && popup.has(e.target).length === 0) {
        $('.js-overlay-registration').fadeOut();
    }
});



$('.js-button-call').click(function () {

    $('.js-overlay-call').fadeIn();
    $('.js-overlay-call').addClass('disabled');
});

// закрыть на крестик
$('.js-close-call').click(function () {
    $('.js-overlay-call').fadeOut();

});

// закрыть по клику вне окна
$(document).mouseup(function (e) {
    var popup = $('.js-popup-call');
    if (e.target != popup[0] && popup.has(e.target).length === 0) {
        $('.js-overlay-call').fadeOut();
    }
});





$('.js-button-basket').click(function () {

    $('.js-overlay-basket').fadeIn();
    $('.js-overlay-basket').addClass('disabled');
});

// закрыть на крестик
$('.js-close-basket').click(function () {
    $('.js-overlay-basket').fadeOut();

});

// закрыть по клику вне окна
$(document).mouseup(function (e) {
    var popup = $('.js-popup-basket');
    if (e.target != popup[0] && popup.has(e.target).length === 0) {
        $('.js-overlay-basket').fadeOut();
    }
});


$('#login_submit').click(function (e) {
    var form = $('#login_form');
    $.ajax({
        type: "POST",
        url: login_url,
        data: form.serialize(),
        success: function (data) {
            if (data.auth === false) {
                alert(data.message);
            } else if (data.auth === true) {
                window.location.reload();
            }
        }
    });
    e.preventDefault();
});