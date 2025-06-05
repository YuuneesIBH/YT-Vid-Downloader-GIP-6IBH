const menu = document.querySelector('#mobile-menu')
const menuLinks = document.querySelector('.navbar__menu')

//!Dit zorgt ervoor dat ik de mobiele menu kan zien!
const mobilemenu = () => {
    menu.classList.toggle('is-active')
    menuLinks.classList.toggle('active')
}

menu.addEventListener('click', mobilemenu)



//? Vanaf hier begint de volgende script

/* afbeeldingen animaties (niet goed genoeg voor de website) */




