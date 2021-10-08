async function request(url = '', data = {}) {

    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
    return await response.json();
  }


let href = window.location.href.split("/");
let fields = document.querySelectorAll('.form-group');

href = href[href.length - 2];
let btnSend = fields[fields.length - 1].childNodes;

let LIST_ICON_REG = [
  'fa fa-user fa', 'fa fa-users fa', 'fa fa-users fa',
  'fa fa-envelope fa', 'fa fa-lock fa-lg', 'fa fa-lock fa-lg'
  ];

let LIST_ICON_LOG = ['fa fa-user fa', 'fa fa-lock fa-lg'];


if(href == "registration"){
  btnSend[1].setAttribute('value', 'Регистрация');

  for(let i =0; i < LIST_ICON_REG.length; i++){
    fields[i].childNodes[3].childNodes[1].childNodes[1].childNodes[0].setAttribute("class", LIST_ICON_REG[i]);
  }

  let btnLog = document.querySelector('.login-btn');
  
  btnLog.classList.add('nonactive');
  btnLog.style.borderTop = "1px solid white";
  btnLog.style.borderRight = "1px solid white";

  btnLog.addEventListener('click', () => {
    window.location.href = "/login";
  })

}
else if(href == "login"){
  btnSend[1].setAttribute('value', 'Авторизация');
  for(let i =0; i < LIST_ICON_LOG.length; i++){
    fields[i].childNodes[3].childNodes[1].childNodes[1].childNodes[0].setAttribute("class", LIST_ICON_LOG[i]);
  }

  let btnReg = document.querySelector(".registration-btn");
  
  btnReg.classList.add('nonactive');
  btnReg.style.borderTop = "1px solid white";
  btnReg.style.borderLeft = "1px solid white";
  
  btnReg.addEventListener('click', () => {
    window.location.href = "/registration";
  })
}
