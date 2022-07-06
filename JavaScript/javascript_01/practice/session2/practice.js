// document.getElementById("id명")
document.getElementById("lion").style.color = "red";
document.getElementById("tiger").style.color = "grean";
document.getElementById("bear").style.color = "blue";

// document.getElementsByTagName("tag명")
const animal = document.getElementsByTagName("li");
console.log(animal)
document.getElementsByTagName("li")[3].style.color = "pink";

// document.getElementsByClassName("class명")
document.getElementsByClassName("animal")[1].style.color = "yellow"

// document.quertSelector("선택자")
document.querySelectorAll(".animal")[2].innerHTML = "dog";
const animals = document.getElementById("animals");
animals.innerHTML += "<li class = 'animal'>cat</li>"

// ClssList
document.querySelectorAll(".box")[0].classList.add("purple")
document.querySelectorAll(".box")[0].classList.remove("purple")
document.querySelectorAll(".box")[0].classList.toggle("yellow")
document.querySelectorAll(".box")[0].classList.toggle("yellow")

// addEventListener 메소드
document.getElementById("btn").addEventListener("click", function(){
    console.log("click!!!");
});

let num = 0;
document.getElementById("plus").addEventListener("click", function(){
    num ++;
    document.getElementById("plus").innerHTML = num;
})

document.getElementById("minus").addEventListener("click", function(){
    num --;
    document.getElementById("minus").innerHTML = num;
})

document.querySelector(".bar").addEventListener("click", function(){
    document.querySelector(".bar").innerHTML = "눌렸어!";
    document.querySelector(".newBar").classList.toggle("show");
})