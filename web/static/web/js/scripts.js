
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
    console.log(angle)
    $('.busqueda-img').css('transform', 'rotate('+ angle + 'deg)')

})


jQuery(function($) {
    // Grab whatever we need to paginate
    var pageParts = $(".paginate");

    // How many parts do we have?
    var numPages = pageParts.length;
    // How many parts do we want per page?
    var perPage = 4;

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
                scrollTop: $(".row").offset().top
            }, 1000);
        }
    });
});