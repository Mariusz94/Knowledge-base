<template>
  <div class="search-bar">
    <p>Wyszukaj:</p>
    <div>
      <p></p>
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

    p {
      border-radius: 10px;
    }
  }
}
</style>
