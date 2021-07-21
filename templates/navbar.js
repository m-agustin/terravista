const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelector('.nav-links li');

    burger.addEventListener('click', () => {
        //Toggle burger
        nav.classList.toggle('nav-activate');
        
        //Animate links on burger
        navLinks.forEach(link, index => {
            if (link.style.animation) {
                link.style.animation = '';
            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.3}s`;       
            }
        });

        //Anime the burger lines
        burger.classList.toggle('toggle');
    });
}

navSlide();