var naver_id_login = new naver_id_login(
  "p3ty5OZcY15ufMgrfHPe",
  "http://127.0.0.1:8000/login/naver_login/callback/"
);
var state = naver_id_login.getUniqState();
naver_id_login.setButton("white", 2, 40);
naver_id_login.setDomain(".service.com");
naver_id_login.setState(state);
naver_id_login.init_naver_id_login();
