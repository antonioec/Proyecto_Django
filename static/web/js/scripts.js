
$(window).on('load', function() {

    $('.precio').each(function() {

        var precio = new String($(this).html())

        if (precio.length == 9) {
            var precio2 = precio.slice(0, 3) + "." + precio.slice(3, 6) + "." + precio.slice(-4, -1)
            $(this).html(precio2)
        }
        else if (precio.length == 8) {
            var precio2 = precio.slice(0, 2) + "." + precio.slice(2, 5) + "." + precio.slice(-4, -1)
            $(this).html(precio2)
        }
        else if (precio.length == 7) {
            var precio2 = precio.slice(0, 1) + "." + precio.slice(1, 4) + "." + precio.slice(-4, -1)
            $(this).html(precio2)
        }
        else if (precio.length > 3) {
            var precio2 = precio.slice(0, -3) + "." + precio.slice(-4, -1)
            $(this).html(precio2)
        }
    })

    $('.supcons').each(function() {

        var supcons = new String($(this).html())

        if (supcons.slice(-2, supcons.length) == ',0') {
            var supcons2 = supcons.slice(0, -2)
            $(this).html(supcons2)
        }

    })

    $('.suputil').each(function() {

        var suputil = new String($(this).html())

        if (suputil.slice(-2, suputil.length) == ',0') {
            var suputil2 = suputil.slice(0, -2)
            $(this).html(suputil2)
        }

    })

    $('.suppar').each(function() {

        var suppar = new String($(this).html())

        if (suppar.slice(-2, suppar.length) == ',0') {
            var suppar2 = suppar.slice(0, -2)
            $(this).html(suppar2)
        }

    })

    $('.row.home_row').fadeIn( 750 ).css('display', 'flex');
    $('.home_hr').fadeIn( 750 ).css('display', 'flex');
})

$('[type=number]').keypress(function(event) {

    if (event.which < 48 || event.which > 57){
        event.preventDefault();
    }

})

$('.container-fade').hover(function() {

        $(this).find('.more-info').fadeIn( 750 );


}, function() {

        $(this).find('.more-info').fadeOut( 750 );


})

function getRotationDegrees(obj) {
    var matrix = obj.css("transform");
    //obj.css("-webkit-transform") ||
    //obj.css("-moz-transform")    ||
    //obj.css("-ms-transform")     ||
    //obj.css("-o-transform")      ||
    if(matrix !== 'none') {
        var values = matrix.split('(')[1].split(')')[0].split(',');
        var a = values[0];
        var b = values[1];
        var angle = Math.round(Math.atan2(b, a) * (180/Math.PI));
    } else { var angle = 0; }
    return (angle < 0) ? angle + 360 : angle;
}

$('.busqueda').click(function() {

    $('#Formulario').slideToggle(750)
    var angle = getRotationDegrees($('.busqueda-img'))
    if (angle == 0) {
        var angle = 180
    }
    else {
        var angle = 0
    }
    $('.busqueda-img').css('transform', 'rotate('+ angle + 'deg)')

})

jQuery(function($) {
    // Grab whatever we need to paginate
    var pageParts = $(".paginate");

    // How many parts do we have?
    var numPages = pageParts.length;
    // How many parts do we want per page?
    var perPage = 12;

    // When the document loads we're on page 1
    // So to start with... hide everything else
    pageParts.slice(perPage).hide();
    // Apply simplePagination to our placeholder
    $(".page-nav").pagination({
        items: numPages,
        itemsOnPage: perPage,
        cssStyle: "light-theme",
        // We implement the actual pagination
        //   in this next function. It runs on
        //   the event that a user changes page
        onPageClick: function(pageNum) {
            // Which page parts do we show?
            var start = perPage * (pageNum - 1);
            var end = start + perPage;

            // First hide all page parts
            // Then show those just for our page
            pageParts.hide()
                     .slice(start, end).fadeIn(750);
            $('html, body').animate({
                scrollTop: $("#viviendas-title").offset().top
            }, 800);
        }
    });
});