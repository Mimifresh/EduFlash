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


document.getElementById('mobile-menu-toggle').addEventListener('click', function() {
  const menu = document.getElementById('mobile-menu');
  menu.classList.toggle('active');
});

// Auto-hide messages after 5 seconds
setTimeout(() => {
  const messages = document.querySelectorAll('.message');
  messages.forEach(message => {
      message.style.transition = 'opacity 0.5s';
      message.style.opacity = '0';
      setTimeout(() => message.remove(), 500);
  });
}, 5000);

// Smooth scroll for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
          target.scrollIntoView({
              behavior: 'smooth',
              block: 'start'
          });
      }
  });
});

// Add scroll effect to navbar
let lastScrollTop = 0;
window.addEventListener('scroll', function() {
  const navbar = document.querySelector('.navbar');
  const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
  
  if (scrollTop > lastScrollTop && scrollTop > 100) {
      navbar.style.transform = 'translateY(-100%)';
  } else {
      navbar.style.transform = 'translateY(0)';
  }
  lastScrollTop = scrollTop;
});

// Add loading animation to buttons on click
document.querySelectorAll('.btn').forEach(btn => {
  btn.addEventListener('click', function(e) {
      if (!this.classList.contains('loading')) {
          this.classList.add('loading');
          setTimeout(() => {
              this.classList.remove('loading');
          }, 1500);
      }
  });
});


//home

const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);

    // Observe all fade-in elements
    document.querySelectorAll('.fade-in').forEach(el => {
        observer.observe(el);
    });

    // Button loading states
    document.querySelectorAll('.btn').forEach(btn => {
        btn.addEventListener('click', function(e) {
            if (!this.classList.contains('loading')) {
                this.classList.add('loading');
                setTimeout(() => {
                    this.classList.remove('loading');
                }, 2000);
            }
        });
    });

    // Parallax effect for hero section
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const hero = document.querySelector('.hero');
        if (hero) {
            hero.style.transform = `translateY(${scrolled * 0.5}px)`;
        }
    });

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add floating animation to feature cards
    document.querySelectorAll('.feature-card').forEach((card, index) => {
        card.style.animationDelay = `${index * 0.2}s`;
    });

    // Add staggered animation to steps
    document.querySelectorAll('.step').forEach((step, index) => {
        step.style.animationDelay = `${index * 0.3}s`;
    });

    // Dynamic gradient animation
    let gradientPosition = 0;
    setInterval(() => {
        gradientPosition += 1;
        document.documentElement.style.setProperty(
            '--gradient-hero', 
            `linear-gradient(${135 + gradientPosition}deg, #667eea 0%, #764ba2 50%, #f093fb 100%)`
        );
    }, 100);