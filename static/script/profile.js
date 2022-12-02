// 작가일 경우

const contentTab1 = document.querySelector("#tab01");
const contentTab2 = document.querySelector("#tab02");
const contentTab3 = document.querySelector("#tab03");
const contentTab4 = document.querySelector("#tab04");
const contentTab5 = document.querySelector("#tab05");

const contentBox1 = document.querySelector(".box1");
const contentBox2 = document.querySelector(".box2");
const contentBox3 = document.querySelector(".box3");
const contentBox4 = document.querySelector(".box4");
const contentBox5 = document.querySelector(".box5");

contentTab1.addEventListener("click", () => {
    contentBox1.classList.add("current");
    contentBox2.classList.remove("current");
    contentBox3.classList.remove("current");
    contentBox4.classList.remove("current");
    contentBox5.classList.remove("current");
})

contentTab2.addEventListener("click", () => {
    contentBox1.classList.remove("current");
    contentBox2.classList.add("current");
    contentBox3.classList.remove("current");
    contentBox4.classList.remove("current");
    contentBox5.classList.remove("current");
})

contentTab3.addEventListener("click", () => {
    contentBox1.classList.remove("current");
    contentBox2.classList.remove("current");
    contentBox3.classList.add("current");
    contentBox4.classList.remove("current");
    contentBox5.classList.remove("current");
})

contentTab4.addEventListener("click", () => {
    contentBox1.classList.remove("current");
    contentBox2.classList.remove("current");
    contentBox3.classList.remove("current");
    contentBox4.classList.add("current");
    contentBox5.classList.remove("current");
})

contentTab5.addEventListener("click", () => {
    contentBox1.classList.remove("current");
    contentBox2.classList.remove("current");
    contentBox3.classList.remove("current");
    contentBox4.classList.remove("current");
    contentBox5.classList.add("current");
})