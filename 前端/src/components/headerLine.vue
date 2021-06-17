<template>
  <div class="head-line-div">
    <span class="head-line-title">基于时间序列的牛发情检测系统1.0</span>
  </div>
</template>

<script>
export default {
  name: "headerLine"
}
</script>

<style scoped>
@font-face {
  font-family: 'webfont';
  font-display: swap;
  src: url('http://at.alicdn.com/t/webfont_cvtp6pgcfou.eot'); /* IE9*/
  src: url('http://at.alicdn.com/t/webfont_cvtp6pgcfou.eot?#iefix') format('embedded-opentype'), /* IE6-IE8 */
  url('http://at.alicdn.com/t/webfont_cvtp6pgcfou.woff2') format('woff2'),
  url('http://at.alicdn.com/t/webfont_cvtp6pgcfou.woff') format('woff'), /* chrome、firefox */
  url('http://at.alicdn.com/t/webfont_cvtp6pgcfou.ttf') format('truetype'), /* chrome、firefox、opera、Safari, Android, iOS 4.2+*/
  url('http://at.alicdn.com/t/webfont_cvtp6pgcfou.svg#杨任东竹石体-Bold') format('svg'); /* iOS 4.1- */
}
.head-line-title {
  font-family: "webfont";
  position: relative;
  font-size: 40px;
  /*top: 15px;*/
}
.head-line-div {
  /*background-color: rgba(64, 158, 255, 0.8);*/
  background-color: rgba(0,150,136,0.8) ;
  /*background-color: #409EFF;*/
  line-height: 150px;
  height: 150px;
  border-radius: 8px;
}

</style>
