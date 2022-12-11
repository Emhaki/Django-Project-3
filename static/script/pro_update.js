const nicknameCheck = document.querySelector("#nicknamecheck");
const alertContentNick = document.querySelector("#toast_nick");
const toastNick = document.querySelector("#toast_update");
const nickCheck = document.querySelector("#nick__check");
const nickP = document.createElement("p")
nicknameCheck.addEventListener('click', () => {
    const nickName = document.querySelector("#nicknames");
    const regExp = /[a-z0-9ㄱ-ㅎ|ㅏ-ㅣ|가-힣]{2,10}$/;
    // 아이디 유효성 검사
    if (!regExp.test(nickName.value)) {
        console.log(nickName.value)
        if (nickName.value == "" || nickName.value == null || nickName.value == undefined) {
            nickP.innerText = "닉네임을 입력해 주세요."
            alertContentNick.prepend(nickP);
            nickCheck.value = 0;
            toastNick.style.setProperty('display', "flex");
        } else {
            nickP.innerText = "닉네임은 2~10자 영어 소문자, 숫자를 사용하세요."
            alertContentNick.prepend(nickP);
            nickCheck.value = 0;
            toastNick.style.setProperty('display', "flex");
        }
    } else {
        // 비동기 처리로 idName 값을 DB에 있는지 확인하는 부분
        console.log("hi");
        axios({
            method: 'get',
            url: `/accounts/profile_update/`,
            params: {
                creater_name: nickName.value
            }
        })
            .then((response) => {
                // 넘겨온 데이터를 바탕으로 판단하여 사용할 수 있는 값인지 아닌지 판단
                if (response.data.check === "False") {
                    nickP.innerText = "사용할 수 있는 닉네임 입니다.";
                    alertContentNick.prepend(nickP);
                    nickCheck.value = 1;
                    toastNick.style.setProperty('display', "flex");
                }
                else {
                    nickP.innerText = "사용할 수 없는 닉네임 입니다."
                    alertContentNick.prepend(nickP);
                    nickCheck.value = 2;
                    toastNick.style.setProperty('display', "flex");
                }
            })
    }
})

window.addEventListener('click', (e) => {
    if ((e.target !== toastNick) && (e.target !== nicknameCheck)) {
        toastNick.style.setProperty('display', "none");
    }
})

const fileUp = document.querySelector("#choosefile");
fileUp.addEventListener("change", () => {
    const imgInfo = document.querySelector("#imginfo");
    imgInfo.value = fileUp.files[0].name;
})