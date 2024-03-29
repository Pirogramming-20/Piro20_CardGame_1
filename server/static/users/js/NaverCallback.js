let accsTK = "";
var naver_id_login = new naver_id_login("YOUR_CLIENT_ID", "YOUR_CALLBACK_URL");
// 접근 토큰 값 출력
accsTK = naver_id_login.oauthParams.access_token;
// 네이버 사용자 프로필 조회
naver_id_login.get_naver_userprofile("naverSignInCallback()");
// 네이버 사용자 프로필 조회 이후 프로필 정보를 처리할 callback function
function naverSignInCallback() {
  const name = naver_id_login.getProfileData("name");
  const nickname = naver_id_login.getProfileData("nickname");
  const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;
  fetch("login/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ name: name, nickname: nickname }),
  })
    .then((response) => console.log("fetch 성공"))
    .catch((error) => {
      console.error("Fetch error:", error);
    });
}

// 로그아웃 버튼 클릭시 로그아웃
function naverlogout() {
  fetch(
    `https://nid.naver.com/oauth2.0/token?grant_type=delete&client_id=p3ty5OZcY15ufMgrfHPe&client_secret=EfaVjbEQ5T&access_token=${accsTK}&state=9caf3774-d3e0-4977-ab79-04e4e5e0c2b5&state=be6efbf7-bf94-4b29-b36f-663213729980&service_provider=NAVER`,
    {
      mode: "no-cors",
      method: "GET",
    }
  )
    .then(() => {
      console.log("로그아웃 성공");
    })
    .catch((error) => console.log(error));
}
