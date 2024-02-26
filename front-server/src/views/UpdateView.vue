<template>
  <div class="userinfo">
    <!-- <h1><strong id="username">&nbsp;<i>{{ userInfo.username }}</i></strong> 님의 개인정보 업데이트</h1> -->
    <div id="logo">
    <img src="@/assets/updatemopick.png" alt="MOPICK">
    </div>
    <!-- 개인정보 입력 폼 -->
    <br><br>
    <form @submit.prevent="updateUserInfo">
    <div id="updatecont">
      <div>
        <label>이&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;름&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;</label>
        <input type="text" v-model="userInfo.first_name" required>
      </div>
      <br>
      <div>
        <label>성&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;</label>
        <input type="text" v-model="userInfo.last_name" required>
      </div>
      <hr>
      <div>
        <label>새 비밀번호 &nbsp;&nbsp; :&nbsp; </label>
        <input type="password" v-model="userInfo.passwd1" required>
      </div>
      <br>
      <div>
        <label>비밀번호 확인&nbsp;:&nbsp;</label>
        <input type="password" v-model="userInfo.passwd2" required>
      </div>
    </div>
    <br>
      <input type="submit" value="저장" class="btn btn-outline-secondary" id="save">
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      userInfo: {
        username: '',
        first_name: '',
        last_name: '',
        passwd1:'',
        passwd2:'',
      }
    };
  },
  mounted() {
    setTimeout(()=>{
      this.getUserInfo();
    }, 200)
  },
  methods: {
    getUserInfo() {
      const token = this.$store.state.token;
      if (token) {
        axios.get('http://127.0.0.1:8000/accounts/user/', {
          headers: {
            Authorization: `Token ${token}`
          }
        })
        .then(response => {
          this.userInfo = response.data;
          console.log(this.userInfo)
        })
        .catch(error => {
          console.error(error);
        });
      }
    },
    updateUserInfo() {
      const token = this.$store.state.token;
      if (token) {
        console.log(token)
        const last_name = this.userInfo.last_name
        const first_name = this.userInfo.first_name
        
        axios({
          method:'patch',
          url:'http://127.0.0.1:8000/accounts/user/',
          headers:{
            Authorization: `Token ${token}`
          },
          data:{
            last_name, first_name
          }
        })
        .then(()=>{
          this.updateUserPassWD()
        })
        .catch((err)=>{
          console.log(err)
        })
      }
      else{
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({name:'LogInView'})
      }
    },
    updateUserPassWD(){
      const token = this.$store.state.token;
      const new_password1 = this.userInfo.passwd1
      const new_password2 = this.userInfo.passwd2
      if (token){
        axios({
          method:'post',
          url:'http://127.0.0.1:8000/accounts/password/change/',
          headers:{
            Authorization: `Token ${token}`
          },
          data:{
            new_password1, new_password2
          }
        })
        .then(()=>{
          alert(`회원정보가 정상적으로 변경되었습니다.
  변경된 정보로 다시 로그인 해주세요.`)
          this.$router.push({name:'LogInView'})
        })
        .catch((err)=>{
          console.log(err)
        })
      }
      else{
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({name:'LogInView'})
      }
    }
  }
};
</script>

<style scoped>
label {
  font-family: omu_allpretty;
  font-size: 25px;
}
@font-face {
  font-family: 'wjdds_reg';
  src: url(@/fonts/wjdds_reg.ttf) format('woff');
  font-weight: normal;
  font-style:normal
}

.userinfo{
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  flex-direction: column;
}

#save {
  float: right;
}

#logo {
  justify-self: start;
}

input {
  width: 280px;
}

#updatecont{
  display: flex;
  align-items: center;
  flex-direction: column;
  height: 100vh;
  border: solid 1px rgb(116, 114, 114);
  width: 500px;
  height:350px;
  align-content: center;
  text-align: center;
  justify-content: center;
  border-radius: 20px;
}


input{
  width: 300px;
  height: 50px;
  font-size: 25px;
  border-radius: 10px;
}

#save{
  border-radius: 10px;
  /* border: none; */
  width: 500px;
  font-family: omu_allpretty;
}
</style>