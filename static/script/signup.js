const idCheck = document.querySelector("#idcheck");
const alertContent = document.querySelector("#toast_context");
const toast = document.querySelector("#toast_signup");
const loginCheck = document.querySelector("#login__check");
const p = document.createElement("p")
idCheck.addEventListener('click', () => {
    const idName = document.querySelector("#idname");
    const regExp = /^[a-z0-9]{4,20}$/;
    // 아이디 유효성 검사
    if (!regExp.test(idName.value)) {
        if (idName.value === "") {
            p.innerText = "아이디를 입력해 주세요."
            alertContent.prepend(p);
            loginCheck.value = 0;
            toast.style.setProperty('display', "flex");
            const allChild = toast.childNodes;
        } else {
            p.innerText = "아이디는 4~20자 영어 소문자, 숫자를 사용하세요."
            alertContent.prepend(p);
            loginCheck.value = 0;
            toast.style.setProperty('display', "flex");
            const allChild = toast.childNodes; x
        }
    } else {
        // 비동기 처리로 idName 값을 DB에 있는지 확인하는 부분
        axios({
            method: 'get',
            url: `/accounts/signup/`,
            params: {
                username: idName.value
            }
        })
            .then((response) => {
                // 넘겨온 데이터를 바탕으로 판단하여 사용할 수 있는 값인지 아닌지 판단
                if (response.data.check === "False") {
                    p.innerText = "사용할 수 있는 아이디 입니다.";
                    alertContent.prepend(p);
                    loginCheck.value = 1;
                    toast.style.setProperty('display', "flex");
                }
                else {
                    p.innerText = "사용할 수 없는 아이디 입니다."
                    alertContent.prepend(p);
                    loginCheck.value = 2;
                    toast.style.setProperty('display', "flex");
                }
            })
    }
})

const CloseBtn = document.querySelector("#closebtn");
CloseBtn.addEventListener("click", () => {
    toast.style.setProperty('display', "none");
})

window.addEventListener('click', (e) => {
    if ((e.target !== toast) && (e.target !== idCheck)) {
        toast.style.setProperty('display', "none");
    }
})