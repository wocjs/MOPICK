<template>
  <div class="container">
    <div id="logo">
    <img src="@/assets/bigmopick.png" alt="MOPICK">
    <br><br>
    </div>
    <h1>Join us!</h1>
    <form @submit.prevent="signUp">
      <div id="signupcont">
        <br>
      <input type="text" id="username" v-model="username" placeholder="Username"><br>
      <br>
      <input type="password" id="password1" v-model="password1" placeholder="Password"><br>
      <br>
      <input type="password" id="password2" v-model="password2" placeholder="Password confirmation"><br>
      </div>
      <br>
      <input type="submit" value="✔signup" class="btn btn-outline-danger" id="signUp">
      <br>
      <input type="text" value="Back" @click="backToList()" class="btn btn-outline-danger" id="signUp">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return{
      username:null,
      password1:null,
      password2:null,
    }
  },
  methods: {
    signUp(){
      // console.log('signUp')
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username, password1, password2
      }
      this.$store.dispatch('signUp', payload)
    },
    backToList() {
      this.$router.go(-1)
    },
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

#signupcont{
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

#signUp {
  border-radius: 10px;
  border: none;
  width: 400px;
  font-size: 25px;
}

#logo {
  justify-self: start;
}

#username{
  width: 300px;
  height: 50px;
  font-size: 25px;
  border-radius: 5px;
}
#password1{
  width: 300px;
  height: 50px;
  font-size: 25px;
  border-radius: 5px;
}

#password2{
  width: 300px;
  height: 50px;
  font-size: 25px;
  border-radius: 5px;
}

h1{
  color: rgb(168, 168, 164);
}
</style>