<template>
  <div id="footer">
    <p id="footerFont"><a href="https://github.com/ypj-java" target="_blank"><img src="img/github.png" style="height: 20px" alt=""></a><br>&#169; 2021 - Yang PeiJin</p>
  </div>
</template>

<script>
export default {
  name: 'footerLine'
}
</script>

<style scoped>
#footer{
  /*background-color: rgb(64, 158, 255);*/
  background-color: rgba(0,150,136,0.8) ;
  height: 90px;
  border-radius: 8px;
}
#footerFont{
  line-height: 30px;
  color:#204f7f;
  text-align: center;
  margin:0;
  top: 12px;
  position: relative;
}
</style>
