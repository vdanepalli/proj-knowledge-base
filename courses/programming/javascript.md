# JavaScript

## Coursera: Learn to work with APIs

- API -- Application Programming Interface -- connection between programs
- Server hosts API which is an exposed endpoint
- Client makes a request, connects to Internet
- Server accepts a request, provides response
- 500 Series Codes -- Issue at the Server
- JSON -- key values

```js
fetch("https://dog.ceo/api/breeds/image/random")
.then(response => response.json())
.then(data =>{
    document.getElementById("image-container").innerHTML = `
        <img src='${data.message}'> </img>
    `
})
```

```js
fetch("https://apis.scrimba.com/bored/api/activity")
.then(response => response.json())
.then(data => {
    console.log(data)
    document.getElementById("activity-name").textContent = data.activity
})
```

```js
document.getElementById("get-activity").addEventListener("click", function() {
  fetch("https://apis.scrimba.com/bored/api/activity")
    .then(response => response.json())
    .then(data => {
      document.getElementById("activity").textContent = data.activity
    })
})
```

```js
document.getElementById("get-activity").addEventListener("click", function() {
  fetch("https://apis.scrimba.com/bored/api/activity")
    .then(response => response.json())
    .then(data => {
      document.getElementById("activity").textContent = data.activity
      document.getElementById("title").textContent = "🦾 HappyBot🦿"
      document.body.classList.add("fun")
    })
})
```