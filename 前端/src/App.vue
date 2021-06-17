<template>
  <div id="app">
    <home></home>
  </div>
</template>

<script>
import home from "./components/home";
export default {
  name: 'app',
  components: {
    home
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-size: 120px 90px;
  background: url("~@/assets/background4.jpg");
  background-size: cover;
  /*opacity: 0.5;*/
  color: #2c3e50;
}
</style>
