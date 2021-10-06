async function request(url = '', data = {}) {

    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },

      body: JSON.stringify(data)
    });
    return await response.json();
  }


let csrf = document.cookie.split("=")
console.log(document.cookie)
console.log(csrf[csrf.length - 1])

request("http://localhost:8000/json-req/", {"data": "hello", "csrfmiddlewaretoken": csrf[csrf.length - 1]}).then((data) => {
    console.log(data)
})


