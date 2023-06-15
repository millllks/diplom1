// бургер меню


function burgerMenu(selector) {
	let menu = $(selector);
	let button = menu.find('.burger-menu__button');
	let links = menu.find('.burger-menu__link');
	let overlay = menu.find('.burger-menu__overlay');
	
	button.on('click', (e) => {
		e.preventDefault();
		toggleMenu();
	});
	
	links.on('click',() => toggleMenu());
	overlay.on('click',() => toggleMenu());


	function toggleMenu(){
		menu.toggleClass('burger-menu_active');
		
		if (menu.hasClass('burger-menu_active')) {
			$('body').css('overflow', 'hidden');
		} else {
			$('body').css('overflow', 'visible');
		}
	}
}


burgerMenu ('.burger-menu');


// слайдер отзывов

let swiper = new Swiper(".slide-content", {
    slidesPerView: 3,
    spaceBetween: 20,
    loop: true,
    centerSlide: 'true',
    fade: 'true',
    grabCursor: 'true',
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
      dynamicBullets: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },

    breakpoints:{
        0: {
            slidesPerView: 1,
        },
        550: {
            slidesPerView: 2,
        },
        910: {
            slidesPerView: 3,
        },
    },
  });




  // Модальное окно


  let btns = document.querySelectorAll("*[data-modal-btn]");

  for (let i = 0; i < btns.length; i++) {
    btns[i].addEventListener('click', function () {
      let name = btns[i].getAttribute('data-modal-btn');
      let modal = document.querySelector("[data-modal-window='" + name + "']");
      modal.style.display = "block";
      let close = modal.querySelector(".form__button");
       close.addEventListener('click', function () {
        alert('Форма отправлена успешно')
      });
    });
  }
  
  window.onclick = function (event) {
    if (event.target.hasAttribute('data-modal-window')) {
      let modals = document.querySelectorAll('*[data-modal-window]');
      for (let i = 0; i < modals.length; i++) {
        modals[i].style.display = "none";
      }
    }
  }


  // Валидация формы


const form = document.forms["form"];
const formArr = Array.from(form);
const validFormArr = [];
const button = form.elements["button"];

formArr.forEach((el) => {
  if (el.hasAttribute("data-reg")) {
    el.setAttribute("is-valid", "0");
    validFormArr.push(el);
  }
});

form.addEventListener("input", inputHandler);
button.addEventListener("click", buttonHandler);

function inputHandler({ target }) {
  if (target.hasAttribute("data-reg")) {
    inputCheck(target);
  }
}

function inputCheck(el) {
  const inputValue = el.value;
  const inputReg = el.getAttribute("data-reg");
  const reg = new RegExp(inputReg);
  if (reg.test(inputValue)) {
    el.setAttribute("is-valid", "1");
    el.style.borderBottom = "1px solid rgb(0, 196, 0)";
  } else {
    el.setAttribute("is-valid", "0");
    el.style.borderBottom = "1px solid rgb(255, 0, 0)";
  }
}

function buttonHandler(e) {
  const allValid = [];
  validFormArr.forEach((el) => {
    allValid.push(el.getAttribute("is-valid"));
  });
  const isAllValid = allValid.reduce((acc, current) => {
    return acc && current;
  });

  if (!Boolean(Number(isAllValid))) {
    e.preventDefault();
  }
}
