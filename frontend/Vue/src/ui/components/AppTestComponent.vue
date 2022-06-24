<template>
  <div class="content">
    <div class="content-title">
      <h2>What is Lorem Ipsum?</h2>
    </div>
    <div class="content-body">
      <p>
        Lorem Ipsum is simply dummy text of the printing and typesetting
        industry. Lorem Ipsum has been the industry's standard dummy text ever
        since the 1500s, when an unknown printer took a galley of type and
        scrambled it to make a type specimen book. It has survived not only five
        centuries, but also the leap into electronic typesetting, remaining
        essentially unchanged. It was popularised in the 1960s with the release
        of Letraset sheets containing Lorem Ipsum passages, and more recently
        with desktop publishing software like Aldus PageMaker including versions
        of Lorem Ipsum.
      </p>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue } from "vue-class-component";

export default class AppTestComponent extends Vue {}
</script>

<style scoped lang="scss">
.content {
  background-color: rgba(36, 37, 38, 1);
  width: auto;
  height: 730px;
  border-radius: 10px;
  margin: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 10px;
  align-items: center;
  color: white;
}

.content-title {
  height: 10%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.content-body {
  height: 90%;
  margin: 10px;
  padding: 10px;
}
</style>
