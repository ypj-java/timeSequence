<template>
  <div>
    <button class="press-button"><i class="el-icon-upload2"></i> {{this.label}}</button>
  </div>

</template>

<script>
export default {
  name: 'PressButton',
  props: ['label']
}
</script>

<style scoped>
.press-button {
  border: none;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  cursor: pointer;
}

/* Content */
.press-button {
  font-size: 1.5em;
  padding: .5em 1em;
  border-radius: 6px;
  /*box-shadow: 0 5px 0 0 #2e8b57;*/
  box-shadow: 0 5px 0 0 #7D7D7D ;
  /*background: #8fbc8f;*/
  /*background-color: #4090B3;*/
  /*background-color:#C1C2C4;*/
  background-color: #33ABA0;
  color: #fff;
  transition: all .1s ease-out;
}

.press-button:hover {
  /*background: #73b173;*/
  background-color:#5AD2C7;
  box-shadow: 0 4px 0 0 #2e8b57;
  transform: translateY(1px);
}

.press-button:hover:active {
  box-shadow: 0 1px 0 0 #2e8b57;
  transform: translateY(4px);
}
</style>
