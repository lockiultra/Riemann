const imageContainer = document.querySelector('.image-container');
const image = imageContainer.querySelector('img');

image.addEventListener('load', () => {
    imageContainer.classList.add('loaded');
});