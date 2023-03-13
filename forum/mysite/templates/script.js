window.onscroll = function bgHead() {

    var header = document.querySelector('.header');

    if(window.pageYOffset > 10) {
        header.classList.add('header_fill');
    }
    else {
        header.classList.remove('header_filled');
    }

}