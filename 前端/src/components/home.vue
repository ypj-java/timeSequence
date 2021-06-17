<template>
  <el-container>
    <el-header style="height: 150px">
      <header-line></header-line>
    </el-header>
    <el-main>
      <main-page></main-page>
    </el-main>
    <el-footer>
      <footer-line></footer-line>
    </el-footer>
  </el-container>
</template>

<script>
import HeaderLine from "./headerLine";
import MainPage from "./mainPage";
import FooterLine from "./footerLine";
export default {
  name: "home",
  components: {FooterLine, MainPage, HeaderLine}
}
</script>

<style scoped>
.el-header {
  padding: 0;
}
.el-footer {
  padding: 0;
}
</style>
