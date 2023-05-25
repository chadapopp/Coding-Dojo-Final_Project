document.addEventListener('DOMContentLoaded', function () {
    var mainCarousel = new bootstrap.Carousel(document.querySelector('#carouselExampleIndicators'), {
      interval: false
    });

    var thumbnailCarousel = new bootstrap.Carousel(document.querySelector('#carouselThumbnail'), {
      interval: false,
      slidesPerView: 'auto'
    });

    var nextButton = document.querySelector('.carousel-control-next');
    var prevButton = document.querySelector('.carousel-control-prev');

    nextButton.addEventListener('click', function () {
      mainCarousel.next();
      thumbnailCarousel.next();
    });

    prevButton.addEventListener('click', function () {
      mainCarousel.prev();
      thumbnailCarousel.prev();
    });
  });