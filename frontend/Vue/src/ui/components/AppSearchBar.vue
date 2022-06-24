<template>
  <div class="search-bar">
    <p>Wyszukaj:</p>
    <div>
      <input type="text" placeholder="Tu wpisz frazę do wyszukania" />
      <button><span class="material-symbols-outlined"> search </span></button>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue } from "vue-class-component";

export default class AppSearchBar extends Vue {}
</script>

<style scoped lang="scss">
.search-bar {
  background-color: rgba(36, 37, 38, 1);
  width: auto;
  height: 80px;
  border-radius: 10px;
  margin: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  p {
    color: white;
    align-self: flex-start;
    margin: 0 0 0 10px;
  }

  div {
    background-color: rgba(58, 59, 60, 1);
    margin: 10px;
    width: 96%;
    height: 40px;
    border-radius: 30px;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
  }
}
input {
  height: 40px;
  border: 0px solid rgb(252, 7, 7);
  border-radius: 30px 0px 0px 30px;
  background-color: rgba(58, 59, 60, 1);
  color: white;
  outline: 0;
  padding-left: 1%;
  padding-right: 1%;
  // width: 89%;
  width: 93%;
  box-sizing: border-box;
  font-size: 16px;
}
button {
  height: 40px;
  border: 0px solid rgb(252, 7, 7);
  border-radius: 0px 30px 30px 0px;
  background-color: rgba(58, 59, 60, 1);
  width: 7%;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
.material-symbols-outlined {
  color: white;
}
</style>
