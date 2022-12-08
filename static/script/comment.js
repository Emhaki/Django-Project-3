// 댓글 생성
function createComment(commentPk, commentUser, commentContent) {
  const commentContainer = document.querySelector("#comment-container");

  const deleteForm = document.createElement("form");
  const button = document.createElement("button");
  const div1 = document.createElement("div");
  const div2 = document.createElement("div");
  const p1 = document.createElement("p");
  const p2 = document.createElement("p");
  const i = document.createElement("i");

  deleteForm.setAttribute("id", `comment-delete-${commentPk}`);
  deleteForm.setAttribute("data-comment-id", `${commentPk}`);

  button.setAttribute("form", `comment-delete-${commentPk}`);
  button.classList.add("delete__comment--btn");
  button.setAttribute("type", "submit");

  div1.classList.add("comment");
  div1.setAttribute("id", `comment-${commentPk}`);

  div2.classList.add("comment__header");
  p1.classList.add("comment__writer");
  p2.classList.add("comment__content");
  i.classList.add("bi");
  i.classList.add("bi-trash-fill");

  // svg
  const svg = document.createElement("svg");
  svg.setAttribute("xmlns", "http://www.w3.org/2000/svg");
  svg.setAttribute("width", "16");
  svg.setAttribute("height", "16");
  svg.setAttribute("fill", "currentColor");
  svg.classList.add("bi")
  svg.classList.add("bi-chat-dots")
  svg.setAttribute("viewBox", "0 0 16 16");

  const path1 = document.createElement("path");
  const path2 = document.createElement("path");

  path1.setAttribute("d", "M5 8a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm4 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm3 1a1 1 0 1 0 0-2 1 1 0 0 0 0 2z");
  path2.setAttribute("d", "m2.165 15.803.02-.004c1.83-.363 2.948-.842 3.468-1.105A9.06 9.06 0 0 0 8 15c4.418 0 8-3.134 8-7s-3.582-7-8-7-8 3.134-8 7c0 1.76.743 3.37 1.97 4.6a10.437 10.437 0 0 1-.524 2.318l-.003.011a10.722 10.722 0 0 1-.244.637c-.079.186.074.394.273.362a21.673 21.673 0 0 0 .693-.125zm.8-3.108a1 1 0 0 0-.287-.801C1.618 10.83 1 9.468 1 8c0-3.192 3.004-6 7-6s7 2.808 7 6c0 3.193-3.004 6-7 6a8.06 8.06 0 0 1-2.088-.272 1 1 0 0 0-.711.074c-.387.196-1.24.57-2.634.893a10.97 10.97 0 0 0 .398-2z");

  // 요소들 추가
  svg.append(path1, path2);

  p1.append(svg, " ", commentUser);

  button.append(i);
  deleteForm.append(button);

  // 댓글 비동기 삭제
  deleteForm.addEventListener("submit", function (event) {
    event.preventDefault();
    axios({
      url: `/articles/comments/${event.target.dataset.commentId}/comment_delete/`,
      headers: { 'X-CSRFToken': csrftoken },
      method: "post",
    })
      .then(response => {
        const targetDiv = document.querySelector(`#comment-${response.data.commentPk}`);
        targetDiv.remove();
      });
  });

  div2.append(p1, deleteForm);
  div1.append(div2, commentContent);

  commentContainer.append(div1);
};

// 댓글 생성 비동기
const commentForm = document.querySelector("#comment-form");
commentForm.addEventListener("submit", function (event) {
  event.preventDefault();
  axios({
    method: "post",
    headers: { 'X-CSRFToken': csrftoken },
    url: `/articles/${event.target.dataset.artId}/comments/`,
    data: new FormData(commentForm)
  })
    .then(response => {
      let auth = "{{ request.user.is_authenticated }}";
      if (auth === "True") {
        const commentContainer = document.querySelector("#comment-container");
        while (commentContainer.hasChildNodes()) {
          commentContainer.removeChild(commentContainer.firstChild);
        };
        for (i = 0; i < Object.keys(response.data.commentSet).length; i++) {
          let comment = response.data.commentSet[`comment_set${i}`];
          createComment(comment.commentPk, comment.commentUser, comment.commentContent);
        };
        commentForm.reset();
      } else if (auth === "False") {
        alert(response.data.errorMsg);
      };
    });
});
