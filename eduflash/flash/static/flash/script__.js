// window.onload = function() {
//   try {
//     $('.nav_menu').on('click', function () {
//       $('.links').toggleClass('hide');
//       console.log('toggled div');
//     });
//   } catch (error) {
//     console.log(e);
//   }
// };
// function hide()
// {
//   const targ = document.getElementsByClassName("links")[0];
//   if (targ.id === 'hide'){
//     targ.id = "a";
//     console.log('rem');
//   }
//   else if (targ.id === 'a'){
//     targ.id = "hide";
//     console.log('add');
//   }
// }

// $('.nav_menu').on('click', function () {
//   $('.links').toggleClass('hide');
//   console.log('toggled div');
// });

function hide(){
  $('.links').toggleClass('hide');
  console.log('toggled div');
};

// const navMenu = document.querySelector('.nav_menu'); // Select the button
// const navLinks = document.getElementById('a'); // Select the div with links

// const navMenu = document.querySelector('.nav_menu'); // Select the button
// const navLinks = document.getElementById('a'); // Select the div with links

// navMenu.addEventListener('click', function() {
//   navLinks.classList.toggle('hide'); // Toggle the 'hide' class on click
// }); 

// const navMenu = document.querySelector('.nav_menu');
// function hide_links(){
//   const navLinks = document.getElementById('a');
//   navLinks.classList.toggle('hide');
// }

// function hide(){
//   navMenu.addEventListener('click', hide_links())
// }
// hide();
// const navMenuButton = document.querySelector('.nav_menu');

// // Add event listener to the button
// navMenuButton.addEventListener('click', function() {
//     // Select the links div
//     const linksDiv = document.querySelector('.links');
//     // Toggle the 'hide' class on the links div
//     linksDiv.classList.toggle('hide');
// });
