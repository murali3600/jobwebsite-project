<template>
  <div>
    <div class="row">
      <img src="./assets/logo-design.jpg" style="padding: 20px 10px 10px 25px; width:150px;height:150px;">
      <h2 style="color:#ebf5f9;padding:20px 0px 0px 25px">Murali Job Portal<br><br>Here You can find your perfect job</h2>
    </div>
    <hr>
    <div class="kar">
      <ul>
        <li> <router-link to="/"> Home </router-link>  </li>
        <li> <router-link to="/about"> About</router-link></li>
        <li><router-link to="/adminlogin">Sign-in/up(For Job Hirer)</router-link> </li>
        <li> <router-link to="/terms">Terms and condition</router-link></li>
      </ul>
    </div>
    <hr>
    <router-view></router-view>
  
  </div>  
</template>

<script>

export default {
components :{
  
}
}
</script>

<style>
.row {
  display: flex;
}
body{
background:#112c38;
height: 100vh;  
}
.kar{
margin:0;
padding:25px 30px 10px 50px;
}
ul
{
margin:0;
padding:0;
display:flex;
}
ul li {
list-style:none;
margin:0 20px;
transition:0.1s;
}
ul li a{
display:block;
position:relative;
text-decoration:none;
padding:5px;
font-size:18px;
font-family:sans-serif;
color:#fff;
text-transform:uppercase;
}
a:hover {
  background-color: #ff497c;
}
</style>