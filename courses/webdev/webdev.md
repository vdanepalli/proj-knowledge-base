# [Web Development](../../courses.md)


- [Web Development](#web-development)
  - [ZTM: Web Developer](#ztm-web-developer)
    - [How the Internet Works](#how-the-internet-works)
      - [Browsing the web](#browsing-the-web)
    - [History of Web](#history-of-web)
    - [HTML5](#html5)
    - [CSS](#css)
    - [Bootstrap, Templates](#bootstrap-templates)
    - [CSS Grid, CSS Layout](#css-grid-css-layout)
    - [Career of a Web Developer](#career-of-a-web-developer)
    - [JavaScript](#javascript)
    - [DOM Manipulation](#dom-manipulation)
    - [Advanced JavaScript](#advanced-javascript)
    - [Command Line, Developer Environment](#command-line-developer-environment)
    - [Git, GitHub, Open Source Projects](#git-github-open-source-projects)
    - [NPM, NPM Scripts](#npm-npm-scripts)
    - [ReactJS Fundamentals](#reactjs-fundamentals)
    - [React Hooks](#react-hooks)
    - [Asynchronous JavaScript](#asynchronous-javascript)
    - [Backend, APIs](#backend-apis)
    - [Final Project: Smart Brain Front End](#final-project-smart-brain-front-end)
    - [NodeJS, ExpressJS](#nodejs-expressjs)
    - [Final Project: Smart Brain Backend Server](#final-project-smart-brain-backend-server)
    - [Database](#database)
    - [Final Project: Smart Brain Backend Database](#final-project-smart-brain-backend-database)
    - [Production Deployment](#production-deployment)
    - [Other](#other)
    - [Conclusion](#conclusion)



## ZTM: Web Developer


### How the Internet Works

#### Browsing the web 

- Browser --(google.com)--> ISP ----> DNS --(IP address)--> Browser 
- Browser ----> Google Servers --(html, css, js)--> Browser
- [Command Line](https://www.lifewire.com/how-to-open-command-prompt-2618089)
- [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701)
- `traceroute -4 google.com` -4 to force to ipv4 instead of ipv6; mac
- `tracert google.com` -- widnows
- BASH - Bourne Again Shell
- speed
  - location of servers
  - how many trips between server and browser
  - size of files 

### History of Web

- Tim Berners Lee -- Invented World Wide Web (WWW) in 1989 -- say a common language; agreed protocols
- WWW, HTML, CSS, JavaScript | HTML, CSS, JavaScript, React 
- JQuery is a library -- makes writing JavaScript easy, clean, simple way; An environment for JS | React
- Backend LAMP Stack
  - Linux
  - Apache Server -- HostGater, ... | Node Server
  - MySQL | PostgreSQL, MongoDB
  - PHP | Node.JS Express.JS

### HTML5

- HyperText Markup Language
- `<!DOCTYPE html> <html> <head> <title></title></head>  <body></body></html>`
- `h1, h2, h3, h4, h5, h6` -- big to small -- headers
- `p` -- paragraphs
- `b` -- `strong`
- `i` -- `em`
- `<ol> <li></li> <li></li></ol>` | `<ul> <li></li> <li></li></ul>`
- `<img src="" alt="" width="" hegiht="">`
- `<br>`
- `<a href=""></a>`

```html
<form method="GET" action="run_script_on_server.php">
		First Name: <input type="text" name="firstname"><br>
		Last Name: <input type="text" name="lasttname"><br>
		Email: <input type="email" name="email"><br>
		Password: <input type="password" name="password" minLength="5"><br>
		Birthday: <input type="date" name="birthday"><br>
		Gender:<br>
		<input type="radio" name="gender" value="Male">Male<br>
		<input type="radio" name="gender" value="Female">Female<br>
		<input type="radio" name="gender" value="Other">Other<br>
		Pets: <br>
		<input type="checkbox" name="cat"> Cat<br>
		<input type="checkbox" name="dog"> Dog<br>
		Cars: <br>
		<select name="cars">
			<option value="volvo" >Volvo</option>
			<option value="audi">Audi</option>
		</select><br>
		<input type="submit" value="Register!">
		<input type="reset">
	</form>
```

- query strings/parameters --- index.html?name1=val1&name2=val2&name3=val3...
  - when you use form GET method -- you can see this in URL
  - when you use form POST method -- these are attached to the body request
- comments `<!-- sometext -->
- `<div></div>` -- block element
- `<span></span>` -- inline element
- semantic elements in Html5
  - `<header></header>`
  - `<nav></nav>`
  - `<footer></footer>`
  - `<section></section>`

### CSS

- Cascading Style Sheets
  - always takes the selector at the end
- comments `/* .... */`
- `Selector {Property : Value;}` 
- `<link rel = "stylesheet" type="text/css" href="___.css">`
- `<tag style="background-color: green; color:red;></tag>` -- inline styles
- `<head> <style> .... </style></head>`
- `rgb(red, greeb, blue)` 0 - 255
- `rgba(red, green, blue, alpha)` 0 - transparent; 1 - opaque

```css
body{
    background-image : url(path.jpg);
    background-size : cover; 
}

h2{
    color: #FF0000;
    text-align: center;
    border: 5px dashed/solid rgba(....);
    cursor: pointer;
}

li{
    line-style: none; /* removes the . from li in ul */
    display: inline-block/block; /* inline-block is horizontal; block is vertical -- default */
}
```

- class -- select a group of elements and css selector is `.class{ .... css ...}`
  - `<p class = "webtext active"></p>` -- webtext is one class, active is another class. same element can have multiple classes
- id -- you can use only once for one element  and css selector is `#id{ .... css ...}`
- `*{ text-align: right;}` -- selects everything
- element
- element1, element2 -- all element 1s and all element2s
- element1 element2 -- all element2s inside element1s
- element1 > element2 -- all element2s where their parent is element1
- element1 + element2 -- select any element2 that is right after element1
- selector:hover
- selector:last-child
- selector:first-child
- property:value !important; -- this won't be overwridden by next coming css



<br/><br/>

- Specificity -- how specific are your selectors 
  - Inline Syles > Ids > Classes, Attributes, Psuedo-Classes > Elements and Psuedo Elements
- Importance !important
- Source Order -- when there are multiple stylesheets linked


<br/><br/>

- text-decoration: underline | line-through
- text-transform: uppercase 
- line-height: 20px;
- font-style: italic;
- font-weight: bold; you can also do a number between 100 and 900
- font-size: 100%; 
- font-family: "Times New Roman", Georgia;  -- falls back to Georgia if TNR is not available


<br/><br/>

- `img {float: left | right}` -- wraps text around image 
- `footer{ clear: both; text-align: center}` -- this needs to always added after above 


<br/><br/>

- Box Model
  - Margin > Border > Padding > Content
```css
.boxmodel{
    border: 5px solid red;
    display: inline-block;
    padding: 5px 20px 5px 20px; /* top right bottom left */
    margin: 0px 20px; /* top and bottom, left and right */
    width: 39px; /* content */
    height: 12px; /* content */
}
```

- px, em, rem
  - px 
  - em -- size in relation to parent element size;  so say `2em` -- twice the size of the containing element
  - rem -- size in relation to the size of the root element;


<br/><br/>

- Critical Render Path
  - Fetch HTML and start reading
  - Fetch CSS and Fonts (render blocking; html file can't render without these)
    - So minifying css might help reduce the number of bytes transferred over wire
  - Reder
- Flexbox
  ```css
  .container{
    display: flex; /* activate flexbox */
    flex-wrap: wrap; /* doesn't put all in one line; */
    justify-content: center;  
  }

  h1{
    border-bottom: 5px solid pink;
    border-rigth: 2px solid red;
    width: 400px;
    font-family:fantasy;
    font-size: 3em;
    text-align: center;
  }
  ```


```css

img {
    width: 339px;
    height: 312px;
    margin: 12px;
    transition: all 1s; /* transition when action is taken upon this is 1s */
}

img: hover{
    transform: scale(1.1); /* specifies the transformation */
    animation: ... 
}
```

- `border-radius: 1px 10px 20px 30px;` -- top left, top right, bottom right, bottom left;

### Bootstrap, Templates

- CSS file and JS file
  - use something that is already created by someone
- CDN : Content Delivery Network
  - some place that is actually hosting the file
- Put you JS at the bottom of the body so that you load these after all content is loaded. Otherwise you will have to wait until all JS is loaded to load the content


<br/><br/>

- Bootstrap Grid (think as 12 spaces for a row)
```html
<div class="container">
  <div class="row">
      <div class="col col-sm-6 col-md-12 col-lg-12"> Col1 </div>
      <div class="col col-sm-3 col-md-6 col-lg-12"> Col2 </div>
      <div class="col col-sm-3 col-md-6 col-lg-12"> Col3 </div>
      <!-- all 3 cols add up to 12 for small -->
      <!-- 12 on its own and 6 and 6 for the next row for medium -->
      <!-- everything on its own -- 12 for each -->
</div>
```

- `meta` allows us to add new information to the page; 
  - responsive meta tag `<meta name="viewport" content="widht=device-width, initial-scale=1, shrink_to_fit=no">`
  - meta charset="utf-8"
- `container d-flex justify-content-center align-items-center h-100` 
  - container, h-100 are bootstrap classes
  - d-flex activates flex features
  - align-items-center -- aligns to center; flex feature
  - justify-content-center -- without this, h1 with shorter text might not align to center of the browser's window; Rather it makes max width  the total width of h1 or button (which ever is longer), aligns left, then centers
- Email Marketing Service
  - Mailchimp
    - Free up to 2000 contacts
  - MailerLite
  - ...
- You can use github repo name as `github_username.github.io` and then use this as your website
- Or create github repo with any name, go to settings, github pages, and select source branch


### CSS Grid, CSS Layout

- CSS flexbox (1 dimension) vs CSS grid (2 dimensions)
- Bootstrap came when we didnot have Flexbox

```css
.container {
  display: grid; /* activate or use css grid; similar to flex; */
  grid-gap: 20px; /* now gap*/
  grid-template-columns: 1fr 1fr 2fr; /* 25px 25px; or 25% 25%; works too */
  /* repeat(3, 1fr) -- is same as 1fr 1fr 1fr */
  /* auto 1fr 2fr; -- sets first to fit the content; followed by 1fr 2fr */
  /* repeat(auto-fill, 339px);*/
  grid-template-columns: repeat(auto-fill, minmax(312px, 1fr)); /* preferred */

  grid-template-rows: 1fr 2fr; 
  
  justify-items: start; /* start, end or stretch with respect to row axis -- horizontal */ 
  /* defualt is stretch; other option is end */

  align-items: start; /* this is around columns -- vertical */
}


.green {
  grid-column-start: 1;
  grid-column-end: 2; /* occupies 1st line till 2nd line; -- say 1 box here*/

  /* writing above two lines is same as below */
  grid-column: 1/2; /* start/end */

  grid-column: 1/-1; /* span entire length */

  grid-column: span 2; /* always spans across 2 */

  grid-row: 1/3; 


  justify-self: start; /* for individual cell use self */ 
  align-self: end;   
}
```

- `height: 50vh` -- 50% of viewport height

```css
body{
  margin auto 0; /* to remove browser added margin */
}

.container{
  display: flex;
  align-items: center;
  justify-content: center;
  height: 50vh;
}


.grid-wrapper{
  display:grid;
  gap: 20px;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
}

box > img { 
  width: 100%;
}

.box {
  background-color: #444;
  padding: 130px;
  margin: 20px;
}

footer{
  text-align: center;
}

.sticky{
  position: fixed;
  top:0;
  width:100%;
}
``` 

### Career of a Web Developer

- WHY? TOOLS? CAREER OPTIONS?

- [Web Developer Roadmap](https://coggle.it/diagram/XgtihGj7x4Fvucp6/t/%F0%9F%9A%80%F0%9F%91%A9%E2%80%8D%F0%9F%92%BB-web-development-%F0%9F%91%A8%E2%80%8D%F0%9F%92%BB%F0%9F%9A%80/24016189368f9b6c68d536238aa1e5d26260a76147667cfa043fec9e613d129f)

- Apply to a job that you are underqualified for so you can learn. 
- Is the job going to tough? Yes, go apply
- Getting the interview
  - github
  - website
  - 1-2 big projects
  - blog

- Debugging
  - Go line by line; Explain yourself the whole process
  - Walk some silly duck through it
  - Google StackOverflow

### JavaScript 

- 1995 NetScape introduced JavaScript
- js types
  - Number
  - String
  - Boolean
  - Undefined
  - Null
  - Symbol (new in ES6)
  - Object
- js comparisons
  - `!==`
  - `===`
  - `>= <= > <`
- js variables
  - var 
    - `var first = prompt(); alert("hey" + first); first = Number(first)`
  - let (new in ES6)
  - const (new in ES6)
- js conditionals 
  - if
  - else
  - else if
  - ternary condition ? expr1_true : expr2_false
- js logical operators
  - &&
  - ||
  - !
- js functions
  - function name(params){ return }


<br/><br/>

- functions
  - alert()
  - prompt()
  - console.log()

```js
function sayHalo(){
  console.log("Haloooo");
}

var sayBi = function(){
  console.log("Biiii");
} // anonymous function

var sayBi = function sayBye(){
  console.log("Biiii");
}
```


<br/><br/>

- List `var list = [1, 2, 3, 4, "apple', undefined, true, function]`
  - `list.shift()` -- remove from first
  - `list.pop()` -- remove from end
  - `list.push()`
  - `list.concat(another list)`
  - `list.sort()`
- Objects -- collection of properties
  - var user = {name: .., age: 39, ....};
  - user.property_name -- access
  - user.new_property = value -- append
  - function inside object is method

- loops
  - `for(var i = 0; i < todos.length; i++){ }`
  - `while() { }`
  - `do{ } while();`
  - `todos.forEach(function(todo, i){ cosole.log(todo, i);})` -- new in ES6


<br/><br/>

- js keywords

### DOM Manipulation

- Document Object Model
  - is simply a `document`
  - `window` is the parent object of `document`
    - document.write("Haloooo")
  - JavaScript Engine
    - V8 Engine -- Chrome
    - Chakra Core -- Edge
    - Nitros -- Safari
    - SpiderMonkey -- Firefox
  - `window`
    - `document`
    - `alert`


<br/><br/>

- DOM Selectors
- `document.getElementsByTagName("h1");`
- `document.getElementsByClassName("second");`
- `document.getElementByIdName("first");`
- `document.querySelector("h1")` -- works with any css selectors
- `document.querySelectorAll("h1")`
- `document.querySelector("li").getAttribute("random")`
- `document.querySelector("li").setAttribute("random", "1000")`


<br/><br/>

- changing styles
  - `document.querySelector("h1").style.background = "yello";` -- style.property -- ok, but not recommended; we need to separate responsibilities between html, css, js
  - `var h1 = document.querySelector("h1");`
  - `h1.className = "coolTitle"` -- best
  - `h1.classList. add/remove/toggle("....")` -- best
- `h1.innerHTML = "<> ... <>" 
- `h1.parentElement;`
- `h1.children;`


<br/><br/>

- `var li = document.createElement("li");`
- `li.appendChild(document.createrTextNode("testing"));`
- `document.querySelector("ul").appendChild(li);`
- `document.getElementById("userinput").value.length > 0`
- `input.value = ""; `

- DRY: Do Not Repeat Yourself

```js
input.addEventListener("keydown", function (event) {
    if (input.value.length > 0 && event.key === "Enter") {
        var li = document.createElement("li");
        li.appendChild(document.createTextNode(input.value));
        ul.appendChild(li);
        input.value = "" ;
    }
})

button.addEventListener("click", addListAfterClick); // call back function. we don't want it to run immediately, that's why we don't add ()
input.addEventListener("keypress", addListAfterKeypress);
```

- `body.style.background = "linear-gradient(to right, " + color1.value + ", " + color2.value + ")";
- `css.textContent`



<br/><br/>

- Imperative: you have to tell exactly what you want one by one : JQuery
- Declarative: : React

### Advanced JavaScript

- scope
  - window scope 
  - function scope
- variables
  - `const player = 'bob'`
    - you can change properties of player obj though
  - `let experienced = false`
  - `let wizadry = 39`
    - scope is {} block level
  - `var omg = true`
    - scope is within function
  - `let symbol1 = Symbol('foo'); `let symbol2 = Symbol('foo');`
    - `symbol1 === symbol1` is false
    - symbols create completely unique object

```js
const obj = {
  player: 'ash', 
  active: false, 
  scope: 39
};

const {player, active} = obj;
let {scope} = obj;


const name = 'ash';
const obj = {
  [name]: "ashuuu", 
  [3+9]: 39
}

const obj = {name , 12:39}

const greetstr = `Hello ${name} you seem to be of ${age} years old!`

const add = (a, b) => a + b; 
function add(a, b){return a + b;}
```

<br/><br/>


- Closures
- a function ran, the function executed. it's never going to be executed again. but it's going to remember that there are references to those variables so the child scope always has access to the parent scope. 
```js
const first = () => {
  const greet = 'ash';
  const second = () => alert(greet);
  return second;
}


const new_func = first(); // is same as const new_func's definition; 
new_func(); // this needs to remember greet as well even if it's not in scope
```

<br/><br/>

- Currying
- process of converting a function that takes multiple arguments into a function that takes them one at a time.

```js
const multiply = (a, b) => a * b;

const curriedMul = (a) => (b) => a * b;;
curriedMul(3); // (b) => a *  b;
curriedMul(3)(9)

const  mul_by_5 = curriedMul(5);
```


<br/><br/>

- Compose
- Act of putting two functions together to form a third function where the output of one function is the input of the other
```js
const compose = (f, g) => (a) => f(g(a));

const sum = (nun) => num + 1;

compose(sum, sum)(5);  // 7
```


- Avoid Side effects -- functional purity
  - avoid side effects and always return something 
- Deterministic -- no matter what, if inputs go through the universe (it's own world), the output is same


<br/><br/>

```js
const arr = [1, 2, 3, 9];
const double = []
const new_add = arr.forEach((num) => {
  double.push(num * 2);
})
console.log(double);
```

- map, filter, reduce
- `const mapArr = array.map((num)=> { return num * 2});`
- `const mapArr = array.map(num=> num * 2);` -- same as above
- `console.log('map', mapArr);`
- `const filterArr = array.filter(num => num>5)
- `const reduceArr = array.reduce((accumulator, num) => { return accumulator + num}, 0)` 


<br/><br/>

- objects are of reference types -- non-primitive
- context vs scope
- instantiation
```js
const obj1 = {
  a: function(){ console.log(this);}
}

class Player {
  constructor(name, type){
    this.name = name;
    this.type = type;
  }

  introduce(){
    console.log(`Hi, ${this.name}, I'm ${this.type}`);
  }
}


class Wizard extends Player{
  constructor(name, type){
    super(name, type) // whenever you extend
  }

  play(){
    console.log(`I am ${this.type}`)
  }
}

const wiz1 = new Wizard('Ash', 'Healer');'
```


<br/><br/>

- pass by value vs pass by reference
- primitive - you can't modify, you need to recreate them; pass by value; copy
- objects - you can modify, pass by reference

```js
var a = 5;
var b = a; // copy, primitive, pass by value
b++; 

var c = [5, 3, 9];
var d = c; // pass by reference
var e = [].concat(c); // new array, copy or push

let obj = {a: 'a', s:'s', h:'h'};
let obj2 = obj; // pass by reference
let clone = Object.assign({}, obj); // shallow copy obj into empty obj {} 
let clone2 = {...obj} // ... is spread operator; shallow copy 


let clone3 = JSON.parse(JSON.stringify(obj)); // deep copy
// can have performance implications
```


<br/><br/>

- type coercion
  - `1 == '1'` -- true; coercion (convert to compatible types)
  - `1 === '1'` -- false; no coercion
- JS has -0 and +0; 
  - `-0 === +0` true
  - `Object.is(-0, +0)` false
  - `NaN === NaN` false
  - `Object.is(NaN, NaN)` true


<br/><br/>

- ES7, 2016, 2 additions
  - `.includes()` on strings and arrays
  - `**` exponential operator 
    - `const sq = (x) => x ** 2`
- ES8, 2017
  - string padding
    - `'ASH'.padStart(10)`
    - `'ASH'.padEnd(10)`
  - trailing commas in functions, parameter lists, calls
    - `const fun = (a, b, c, d, ) => {console.log(a)}`
  - `Object.values` and `Object.entries`
    - Before these, we had `Object.keys`
    - `let obj = {username: .., username1: ...};`
      - `Object.keys(obj).forEach((key, index) => {console.log(key, obj[key])});`
  - Async Await

```js
let obj = {
  username39: 'ASH';
  username12: 'win';
}

Object.keys(obj).forEach((key, index) => {
  console.log(key, obj[key]);
})

Object.values(obj).forEach(value => console.log(value);)

Object.entries(obj).forEach(value => console.log(value)) // key, value pairs

Object.entries(obj).map(value => {
  return value[1] + value[0].replace('username', '');
})
```


<br/><br/>

- ES10 2019
- `flat()` -- can be used on arrays; default: flattens only one layer
  - `flat(2)` -- 2 layers
- `flatMap()`
- `.trimStart()`
- `.trimEnd()`
- `Object.fromEntries()`  -- opposite of `Object.entries()`
- `try{} catch{}`


```js
const arr = [1, [2, 3], [4, 5]];
arr.flat(); // 1, 2, 3, 4, 5

const entries = ['ash', 'win', ,, , , , 'ai']
entries.flat(); // ash, win, ai -- cleans up data

const jParkChaos = jPark.flatMap(creature => creature + '!')

userProfiles = [['ash', 39], ['win', 12]]
const obj = Object.fromEntries(userProfiles) // {ash: 39, win: 12}
userProfiles = Object.entries(obj);

try{
  ash + 'hey'
} catch {
  console.log('You messed up')
}

// before es10

try{
  ash + 'hey'
} catch (error){ // you needed to catch error
  console.log('You messed up')
}
```


<br/><br/>

- loops

```js
const basket = ['apples', 'oranges', 'grapes']
const detailedBasket = {
  apples: 12, 
  oranges: 39, 
  grapes: 51
}

// 1 for i ; i < ; i++

// 2  
basket.forEach(item => {
  console.log(item)
})


// 3 & 4 -- while, do while


// 5 for of : ES6
// Iterating - Iterables (arrays, strings)
for (item of basket){ console.log(item)}

// 6 for in : 
// loops over object properties
// enumerating -- enumerable (if it allows us to see properties)
for (item in detailedBasket){
  console.log(item)
}
```


<br/><br/>

- eS2020 
- BigInt
- Nullish Coalescing Operator ??
- Optional Chaining Operator ?.
- Promise.allSettled
- globalThis

```js
typeof 1n; // bigint  
var a   = Number.MAX_SAFE_INTEGER; // operations after this are unpredictable, not accurate

a + 10; // doesn't produce correct output
a - 1; // doesn't produce correct output

93243293849327432872473286428n - 1n // works because of bigint. 


let ash_pokemon = {
  pikachu:{
    species: 'ASh', 
    height = 39, 
    weight = 12
  }
}

if (ash_pokemon.pikachu && ash_pokemon.pickachu.weight){ 
  let weight1 = ash_pokemon.pikachu.weight}
else{
  let weight 1 = undefined
}

// Optional Chaining
let weight2 = _pokemon?.pikachu?.weight // same  as above

// Nullish Coalescing 

let power = _pokemon?.pikachu?.power || 'no power' // if power was false, it has no power.
// Or operator checks if it is falsy, return no power

let power = _pokemon?.pikachu?.power ?? 'no power' 
// will return no power only when power is null or undefined. 
```


<br/><br/>

- es2021 
  - `.replaceAll()` -- now, replaces all occurrences
  - `.replace()` -- earlier, only replaces first occurrence

```js
const str = 'win you piece of shit'

str.replaceAll('best', 'worst') // returns new string
```

<br/><br/>

- es2022
  - `.at()`
  - top level await


```js
const arr = [1, 2, 3, 4, 5, 0]

arr.at(-1) // last item
arr.at(0) // first item
```

<br/><br/>

- es2023
  - `.findLast()`
  - `.findLastIndex()`
  - `.toReversed()` --- `reverse()`
  - `.toSorted()` --- `sort()`
  - `.toSpliced()` --- `splice()`
  - `.with()`

```js
const lastMonster = ztmMonsters.findLast(item => item.level > 15)
const lastMonseterIndex = ztmMonsters.findLastIndex(item => item.level > 15)

ztmMonsterList.reverse() // inplace

ztmMonstersList.toReversed() // keeps original intact

const spliced = ztmMonsterList.toSpliced(2, 1) // start at 2 and remove 1 item

ztmMonstersList.with(1, "Ghost") // at index 1 put ghost (keeps original intact)
```


<br/><br/>

- es2024
  - `groupBy()`

```js
Object.groupBy(pokemons, (i) => {return i.type})
// collection of objects = pokemons
// call back function. 
```


<br/><br/>

- debugging 

```js
const flattened = [[1, 2], [3, 9], [5, 1]].reduce(
  (accumulator, array) => {
    debugger;
    return accumulator.concat(array)
  }, []);
```


<br/><br/>

- how does JS work?
- program
  - allocate memory
  - parse and execute
- v8 js engine
  - memory heap
    - allocate memory
    - memory leak -- (memory is limited)  
      - unused memory just lying around 
      - global variables are bad because we forget to clean up
  - call stack
    - code is read and executed

- JavaScript is a single threaded language that can be non-blocking
  - single threaded - only one call stack; one thing at a time
    - synchronous
  - multi-threaded -- multiple call stacks
    - deadlocks

```js
console.log('1')
setTimeout(() => { console.log('2')}, 2000)
console.log('3') // 1, 3, 2 -- asynchronous 
```

- JavaScript Run-Time Environment
  - JS Engine
    - Memory Heap
    - Call Stack
  - Web APIs
    - DOM (document)
    - AJAX (XMLHttpRequest)
    - Timeout (setTimeout)
  - Callback Queue
    - onClick
    - onLoad
    - onDone
  - Event Loop
    - checks if call stack is empty, tries to put callback functions from call back queue

  
<br/><br/>
  
- Modules
  - Inline Script 
    - Code reusability (can get big)
    - Pollutes global namespace (window object)
  - Script Tags
    - still have to copy and paste in multiple pages if needed
    - Dependency Resolution (you are responsible for making sure they are ordered correctly)
    - Pollutes global namespace (window object)
  - IIFE (Immediately Invoked Function Expression)
    - solves global namespace problem by using function scopes  
    - order is still important
  - Browserify
    - used CommonJS
    - is a Module Bundler -- runs before you put your website online

```js
var myApp = {} // will be part of window obj

(function(){
  myApp.add = function(a, b){
    return a + b;
  }
})(); 


module.exports = function add(a, b) {
  return a + b;
}

var add = require('./add')  
```

- JavaScript didn't have module features. With ES6, Webpack2, we have export and import 
- Webpack is a module bundler (with this we can use JS ES6 with all browsers)

```js
export const add = (a, b) => a + b; // can have multiple exports
export default function add(){ return a + b} // can only have one export in a single file

import {add} from './add'; // destructuring
import add from './add'; 


// webpack has a config file

module.exports = {
  entry: './app/main.js',
  output: {
    path: './dist',
    filename: 'bundle.js'
  }
}
```

### Command Line, Developer Environment

- iTerm
- Fish

### Git, GitHub, Open Source Projects

- git clone 
- git pull
- git add
- git commit 
- git push
- git branch
- git branch new_branch_name
- git checkout checkout-to-branch-name
- git remote add upstream upstream_url_where-you-are-forking-from
- git pull upstream master

### NPM, NPM Scripts

- node package manager
- npm registry
  - packages or modules 
    - package.json -- meta file
    - js file
- yarn is a similar tool to grab packages from npm registry
- node allows you to run java script outside of browser
- package.json
  - name
  - version
  - main : script.js // starting point
  - repository
  - scripts
    - test
- npm install
  - local `npm install lodash`
  - global `npm install -g live-server browserify ` 
- localhost `127.0.0.1`


<br/><br/>

- SemVer -- Semantic Versioning -- ^4.17.9  
  - 9 is patch release -- bug fixes
  - 17 is minor releases -- say new features
  - 4 is major release
- `npm install` -- looks for a package.json and downloads dependencies 
  - `"dependencies"{ "lodash" : "4.17.44"}`
- there is also dev dependencies -- only needed for development; not required for production release
- `npm run test`
- `"scripts":{"build": "browserify script.js > bundle.js && live-server"}` `npm run build`


### ReactJS Fundamentals

- Before react we had jquery -- do this if this happened
- created at facebook
- manages view, changes the dom in a predictable way
- concepts
  - atoms > molecules > organisms > templates > pages --- components (reusable)
  - one way data flow
    - data flows from top to bottom 
      - only children know about the change and the parent doesn't bother 
  - virtual DOM 
    - it's just a JS object -- describes the current state of website; copy of DOM
    - before react, we were the painters, telling what to change exactly in the DOM
    - react bot automatically makes changes to DOM and paint it in most optimal way.
  - has a big ecosystem


<br/><br/>

- react app
  - `npx create-react-app my-app-name`
    - `npm install -g create-react-app`
    - since npm 5.2 > you have npx out of the box
    - npx is a package runner -- easy to install and manage dependencies   
  - `cd my-app`
  - `npm start`
- alternative build tool -- vite
  - if you care about performance, this works best
  - `npm create vite@latest`
  - `cd vite-project`
  - `npm install`
  - `npm run dev`


<br/><br/>

- package.json
  - `"start": "react-scripts start | build | test | eject"`
  - `"dependencies"` 
- package-lock.json
  - locks the version numbers
  - automatically generated everytime we update package.json
- public/manifest.json
  - say if users need to create a shortcut on desktop to your website or bookmark, this is where we configure it


<br/><br/>

- classes vs hooks
- hooks -- newer ways, specific to react
- `function App(){}` --> `class App extends React.Component { render() { return ()}} 
- React has a webpack that does the bundling for us. (browserify)
- `import React from 'react'` -- view library, react bot
- `import ReactDOM from 'react-dom`
- `ReactDOM.render(<App/>, document.getElementById('root'));`
- Components are capitalized -- `Hello.js`
- `import React, {Component} from 'react'`
- `export default Hello;` -- file only exports one thing, and that is this.


<br/><br/>

- `npm install tachyons` -- package; allows us to have predefined classes similar to bootstrap
- `import tachyons`
- `className` vs `class` -- JSX (use className)
  - separation of concerns -- each component is its own universe
  - react uses JSX to create Virtual DOM
  - class is a reserved keyword in JavaScript; Because its JSX and not html we say className;
  - before it used to break code, but now it gives you warning when you use class in JSX
- we can provide props or properties to react component
  - `<Hello greeting= {'Hello Ash'}/> ` -- {} is the JS expression -- say this is in index.js
  - `<p>{this.props.greeting}</p>` -- you have access to props in Hello.js

```jsx
class Hello extends Component{
  render(){
    return(
      <div className='f1 tc'>
        <h1> Hello Ash</h1>
        <p>{this.props.greeting}</p>
      </div>
    )
  }
}

const Hello = (props) => {
    return(
      <div className='f1 tc'>
        <h1> Hello Ash</h1>
        <p>{props.greeting}</p>
      </div>
    )
}

export default Hello;
```

- if it is a default export like `export default Hello` you can simply use `import Card from './Card'`
- if it is not default like `export const robots` you have to destructure it `import { robots} from './robots';`
- `<Card id = {robots[0].id} name = {robots[0].name} />`
- `const {name, email, id} = props;` -- destructuring.



<br/><br/>

- READ DOCUMENTATION
- READ FULL DOCUMENTATION
- READ EVERYTHING
- READ EVERY SINGLE PIECE


<br/><br/>

- `const cardComponent = robots.map((user, i) => { return <Card key = {i} id = {robots[i].id} name = {robots[i].name} email = {robots[i].email}/>})`
- you need to pass the key prop for below reason
  - there are multiple cards right. 
  - say if any of them changes, how does react know what to update in virtual DOM. 
    - so it updates everything, all card components
  - if we gave a key prop that uniquely identifies a card, it updates just that card. 
- so we talked about one way data flow right
  - let's say there is a parent with two children. 
  - and one of the children wants to talk to their sibling. but, how?
  - well, they can talk to their parent and the parent talk on their behalf. 
- pure functions | dumb functions | deterministic functions. 
- props are always same, inputs, they don't change. 
- STATE -- object describes the application
- React comes with life cycle hooks -- run everytime a component does something
  - mounting
    - constructor()
    - componentWillMount()
    - render()
    - componentDidMount()
  - updating
    - componentWillReceiveProps()
    - shouldComponentUpdate()
    - componentWillUpdate()
    - render()
    - componentDidUpdate()
  - Unmounting
    - componentWillUnmount()
- every component has a props.children
- if you are using JSX and want to specify style use `{{}}` --- `style={{overflow: 'scroll', border: '5px solid black', height: '800px'}}`


<br/><br/>

- some javascript features don't work on some browsers
- reduce network trips 
- improve performance

### React Hooks

- If there is a feature and you need to learn it, refer documentation
- UNDERSTAND MOTIVATION behind introduction of the feature.
  - hard to reuse stateful logic between components
  - complexx components become hard to understand
  - classes confuse both people and machine
- Hooks don't work with classes. Before hooks, we only had functional components that do not have any state. 
- We used classes to represent components with state. 
- But hooks, let us use stateful functional components. 
- `useState`, `useEffect` -- Hooks
- Hook into react features. state or life cycle methods/events

```js
const [robots, setRobots] = useState([]) // array destructuring
const [searchfield, setSearchfield] = useState('')

const onSearchChange = (event) => {
  setSearchfield(event.target.value)
}

useEffect(()=>{
  fetch('https://jsonplaceholder.typicode.com/users')
  .then(response => response.json())
  .then(users => {setRobots(users)})
}, []) // the second parameter tells react to run this effect when any of the list values change. In here, list is empty, so this effect is only run when the component is rendered. 
// say shortcut to ComponentDidMount 

useEffect(()=>{
  fetch('https://jsonplaceholder.typicode.com/users')
  .then(response => response.json())
  .then(users => {setRobots(users)})
}) // If the second parameter is not provided, this effect is run in a loop. 


useEffect(()=>{
  fetch('https://jsonplaceholder.typicode.com/users')
  .then(response => response.json())
  .then(users => {setRobots(users)})
}, [robots]) // it's a loop again because we are updating robots and rendering robots and updating robots and rendering robots ....
```

- Hooks don't work in classes, but they work side by side with class components. 
- Only call Hooks from React function components -- specific to react
- Only call Hooks at the top level. 

### Asynchronous JavaScript

- HyperText Transfer Protocol : HTTP
- Protocol -- say a standard, common, aggreed way or rules. 
- Client Server Protocol
  - Requests
  - Responses
- HTTP Request
  - GET
    - query string parameters (?key=val&key2=vall2&...)
    - body of the request (POST)
      - Form Data
  - POST 
  - PUT - update
  - DELETE
- HTTP Response
  - response status code
    - 1xx Information
    - 2xx Successful
    - 3xx Redirection
    - 4xx Client Error
    - 5xx Server Error
  - files


<br/><br/>

- HTTPS HyperText Transfer Protocol Secure 
  - uses TLS Transfer Layer Security and SSL Secure Socket Layer
- JSON 
  - JavaScript Object Notation
  - syntax for storing and exchanging data (there's also XML - another way)
  - text
- `var obj = JSON.parse(json_obj)` -- load json
- `var http_json = JSON.stringify(data)` -- convert to json text


<br/><br/>

- Earlier, if something changed, the entire page needed to be refreshed or reloaded. 
- Ajax (technology) -- request small chunks of data, and display them as needed solving above refresh problem. 
  - update a page withot reloading entire data, or exchange data in background, while the user is still interacting. 
- was achieveed using a tool (browsers built) XMLHttpRequest
- the old way -- XMLHttpRequest
- the new old way - jQuery $.getJSON('url', function(data){}) 
- the new way -- fetch('url').then(response => {})  

- send a request using fetch(url) -- AJAX Api Call; Returns a JavaScript Promise -- JS will let you know once it is done; you use .then() 
- AJAX is a combination of tools: fetch(), HTTP, JSON, ...


<br/><br/>

- Promise - an object that may produce a single value some time in the future. 
- Either a resolved value, or a reason that it's not resolved (rejected)
- Promise 3 states
  - fulfilled
  - rejected
  - pending
- Callbacks -- if this happens then this happens. 
- Promises serve the same purpose of Callbacks
  - can only succeed or fail once. 

```js
const promise = new Promise((resolve, reject) => {
  if (true){
    resolve('Worked');
  } else{
    reject('Error')
  }
})

promise.then(result => console.log(result));

const promise2 = new Promise((resolve, reject) => {
  setTimeout(resolve, 100, 'Hi ASH') // 100 ms
})

const promise3 = new Promise((resolve, reject) => {
  setTimeout(resolve, 1000, 'Hello ASH')
})

const promise4 = new Promise((resolve, reject) => {
  setTimeout(resolve, 3000, 'ASH!')
})


Promise.all([promise, promise2, promise3, promise4])
.then(values => {
  console.log(values);  
})

promise
.then(result => result + '!')
.then(result2 => result2 + '?')
.catch(() => console.log('error!'))
.then(result3 => {
  throw Error;
  console.log(result3 + '!')
})
```

- promises are great for asynchrounous programming


<br/><br/>

```js
const urls = [
  'https://jsonplaceholder.typicode.com/users',
  'https://jsonplaceholder.typicode.com/posts',
  'https://jsonplaceholder.typicode.com/albums'
]

Promise.all(urls.map(url => {
  return fetch(url).then(resp => resp.json())
})).then(results => {
  console.log(results[0])
  console.log(results[1])
  console.log(results[2])
}).catch(() => console.log('error'))
```


<br/><br/>

- promises are introduced in ES6
- async await is introduced in ES8
- async function returns Promise under the hood -- syntactic sugar 
- promises and async functions allow the main thread continue executing synchronous instructions while the async functions are run in the background and these are added to the call back queue for execution whenever main thread becomes idle (event loop is also in the picture)
- while the await waits for the promise to resolve or reject, event loop is still free to execute other tasks
- await doesn't block the entire event loop, but just the async function in which it is defined

```js
async function playerStart(){
  const firstMove = await movePlayer(100, 'Left'); // pause this until I have something for you
  await movePlayer(400, 'Left');
  await movePlayer(10, 'Right');
  await movePlayer(330, 'Left');
}

async function fetchUsers(){
  const resp = await fetch('endpoint_url')
  const data = await resp.json()
  console.log(data)
}

fetch('endpoint_url')
.then(resp => resp.json())
.then(console.log)

async function fetchUsers2(){
  const resp = await fetch('endpoint_url')
  const data = await resp.json()
  console.log(data)
}

const getData = async function(){
  try{
    const [users, posts, albums] = await Promise.all(urls.map(url => fetch(url).then( resp => resp.json())))
  } catch (error) { // catch always receives error
    console.log('Whopsie', error)
  }
}
console.log('users', users);
```

```js
console.log("Task 1: Start");

async function asyncTask() {
  console.log("Task 2: Async task started");
  
  // Await simulates an asynchronous operation
  await new Promise((resolve) => setTimeout(resolve, 2000));
  
  console.log("Task 4: Async task completed");
}

asyncTask();

console.log("Task 3: End");
```


<br/><br/>

- es9 2018
- object spread operator (...)

```js 
//es6  
const arr = [1, 2, 3, 4, 5]
const function sum(a,b,c,d,e){
  return a+b+c+d+e
}
sum(...arr);
// es9
const animals = { tiger:234, lion:4, monkey:123 }
const {tiger, ...rest} = animals;
```

- finally -- allows us to do something after promise is finished; runs no matter what
```js
Promise().then().catch().finally(() => {console.log(...)})
```

- for await of 

```js
const loopThroughUrls = urls => {
  for (url of urls){
    console.log(url) 
  }
}

const getData2 = async function(){
  const arrayOfPromises = urls.map(url => fetch(url));
  for await (let request of arrayOfPromises){
    const data = await request.json();
    console.log(data);
  }
}
```


<br/><br/>

- es2020
- Promise.allSettled()

```js
Promise.all([promiseOne, promiseTwo]).then(data=>console.log(data)).catch(e=>console.log('something failed', e)); 
// above short circuits, when any of the promises fails and goes to catch

Promise.allSettled([promiseOne, promiseTwo]).then(data=>console.log(data)).catch(e=>console.log('something failed', e)); 
// runs all regardless or resolve, reject
```


<br/><br/>

- es2021
- Promise.any()

```js
const p1 = new Promise((resolve, reject) => {
  setTimeout(() => resolve("A"), Math.floor(Math.random() * 1000));
});
const p2 = new Promise((resolve, reject) => {
  setTimeout(() => resolve("B"), Math.floor(Math.random() * 1000));
});
const p3 = new Promise((resolve, reject) => {
  setTimeout(() => resolve("C"), Math.floor(Math.random() * 1000));
});

// Out of p1, p2 and p3, whichever resolves first is taken by Promise.any().

(async function () {
  const result = await Promise.any([p1, p2, p3]);
  console.log(result); // Prints "A", "B" or "C"
})();

// What if none of the promises resolve? In that case Promise.any() throws an error!
```

- [ECMASCRIPT NEW FEATURES](https://github.com/daumann/ECMAScript-new-features-list)

### Backend, APIs

- LAMP -- linux, apache server (accept req, send resp), MySQL, PHP
- Application Server 
  - Node Server -- Node.js Express.js
    - login req, check db, send custom resp
  - Database -- PostgreSQL, MongoDB
- Load Balancer -- Nginx
  - Application Server
    - Node Server
  - Application Server
    - Node Server
  - Database


<br/><br/>

- apis
  - [Star Wars API](http://swapi.py4e.com/)
  - [Star Wars API clone](https://swapi.dev/)
  - [Numbers API](http://numbersapi.com/#42)
  - [Chuck Norris API](https://api.chucknorris.io/)
  - [Pokemon API](https://pokeapi.co/)
  - [International Space Station API](http://open-notify.org/Open-Notify-API/ISS-Location-Now/)

- Application Programming Interface -- communicate, share data
- Stripe API
- Twilio API -- sending messages 
- [Free Public APIs](https://www.freepublicapis.com/)
- [Public APIs](https://publicapis.dev/)
- [Elevator Game | Something fun](https://play.elevatorsaga.com/)


<br/><br/>

- snapshot model of learning -- mac timemachine
- maintain an app and not just develop; updated libraries
- [clarifai](https://clarifai.com)
- deliberate practice
  - learning process should be tough
  - visualize moves, things
  - start learning -- rapid progress
  - perceived limit -- halt, frustration, limits, flat line -- need to push through
  - specific goals, intense focus, immediate feedback, frequent discomfort
  - passive and active learning 

- [Not all pracatice makes perfect](https://nautil.us/not-all-practice-makes-perfect-235890/)
- [Striving for perfection when perfection is impossible| Kendo - way of the sword](https://www.tofugu.com/japan/kendo/)

### Final Project: Smart Brain Front End

- Draw Wireframes | Screens
- Identify Components

- `npm i --save package` --save adds it to package.json dependencies
- [React setState and It's Async Nature](https://medium.com/geekculture/react-setstate-its-async-nature-bc6bcd78eebd)

### NodeJS, ExpressJS

- nodejs allows js to be run anywhere
- popular for building servers
- `node -v`
- `johnny-five` --- library to build robots
- node has `global` in place of `window`
- `global` `process`


<br/><br/>

- [web requests history](https://blog.logrocket.com/fetch-api-node-js/)
- Web requests
  - Internet Explorer 5 brought `XMLHttpRequest` API in 1998 
  - 2015 - Fetch API 

<br/><br/>

- `node filename.js`

```js
setTimeout(()=>{
  console.log("Merry Christmas!")
}, 3000)

const largeNum = 356;

export default largeNum;

import largeNum from 'script2.js'

// common js way of doing above
module.exports = {
  largeNum: largeNum
}
const script2 = require('./script2.js')
```

- es2020
- `globalThis` -- pretty much `window` object but on Node ; also exists in browser


<br/><br/>



### Final Project: Smart Brain Backend Server


### Database


### Final Project: Smart Brain Backend Database


### Production Deployment


### Other



### Conclusion

