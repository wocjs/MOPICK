<template>
  <div class="container">
    <div id="logo">
    <img src="@/assets/bigmopick.png" alt="MOPICK">
    </div>
    <p></p>
    <div>
    <form @submit.prevent="login">
      <div id="logincont">
        <br>
        <input type="text" id="username" v-model="username" placeholder="Username"><br>
        <br>
        <input type="password" id="password" v-model="password" placeholder="Password"><br>
        <br>
        <input type="submit" class="btn" value="logIn" id="login-btn"><br>
      </div>
      <br>

      <button @click="toSignUp" id="signUp" class="btn btn-outline-danger">아직 회원이 아니시라면?</button>
    </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return{
      username: null,
      password: null,
    }
  },
  created(){
    this.logout()
  },
  methods: {
    login(){
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }
      this.$store.dispatch('login', payload)
    },
    toSignUp() {
      this.$router.push({ name: 'SignUpView' })
    },
    logout(){
      this.$store.dispatch('logout')
    }
  }
}
</script>
<style scoped>
nav{
  display: none;
}

.container{
  align-items: center;
  display: flex;
  justify-content: center;
  flex-direction: column;
  height: 100vh;
  font-family: omu_allpretty;
}
#login-btn{
  color:#fff;
  border: solid 1px white;
  
  width: 300px;
  height: 50px;
  font-size: 25px;
}
#logincont{
  display: flex;
  align-items: center;
  flex-direction: column;
  height: 100vh;
  border: solid 1px rgb(116, 114, 114);
  width: 400px;
  height:300px;
  align-content: center;
  text-align: center;
  justify-content: center;
  border-radius: 20px;
}
#username{
  width: 300px;
  height: 50px;
  font-size: 25px;
  border-radius: 5px;
}
#password{
  width: 300px;
  height: 50px;
  font-size: 25px;
  border-radius: 5px;
}

#signUp {
  border-radius: 10px;
  border: none;
  width: 400px;
  font-family: omu_allpretty;
  font-size: 22px;
}

#logo {
  justify-self: start;
}
</style>