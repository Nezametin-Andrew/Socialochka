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


request(
  "http://localhost:8000/auth/option",
  {"data": "hello"}
    ).then((data) => {
     console.log(data['data'])
}
)


