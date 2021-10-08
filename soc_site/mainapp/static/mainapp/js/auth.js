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


// request(
//   "http://localhost:8000/auth/option",
//   {"data": "hello"}
//     ).then((data) => {
//      console.log(data['data'])
// }
// )



let fields = document.querySelectorAll('.form-group');
let formContainer = document.querySelector('.form-container');
let loginCont = document.querySelector(".login-btn");
let registCont = document.querySelector(".registration-btn");



function cleanContSwitch(){
  formContainer.textContent = "";
}


function renderLoginForm(){
  cleanContSwitch();
  loginCont.style.borderTop = "0px";
  loginCont.style.borderRight = "0px"
  registCont.style.borderLeft = "1px solid white"
  registCont.style.borderTop = "1px solid white"
  registCont.classList.add('nonactive');
  formContainer.appendChild(fields[0]);
  formContainer.appendChild(fields[fields.length - 3]);
  fields[fields.length -1].childNodes[1].textContent = "Login";
  formContainer.appendChild(fields[fields.length - 1]);
}

function renderRegistrationForm(){
  cleanContSwitch();
  registCont.style.borderTop = "0px";
  registCont.style.borderLeft = "0px";
  registCont.classList.remove("nonactive");
  loginCont.style.borderTop = "1px solid white";
  loginCont.style.borderRight = "1px solid white";
  loginCont.classList.add('nonactive');
  
  for (let i = 0; i < fields.length; i++) formContainer.appendChild(fields[i]);


}


renderLoginForm();


loginCont.addEventListener('click', () =>{

  renderLoginForm();
})


registCont.addEventListener('click', () => {

  renderRegistrationForm();
})