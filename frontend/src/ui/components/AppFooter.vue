<template>
  <b-container fluid>
    <b-row>
      <b-col>
        <footer>
          <p>{{ year }} © Made with passion by Mariusz Łyszczarz</p>
        </footer>
      </b-col>
    </b-row>
  </b-container>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";

@Options({
  props: {
    year: String,
  },
})
export default class AppFooter extends Vue {
  today = new Date();
  year = this.today.getFullYear();
}
</script>

<style scoped lang="scss">
.col,
.row,
.container-fluid {
  padding: 0;
  margin: 0;
}

footer {
  height: 60px;
  background-color: rgba(36, 37, 38, 1);
  color: white;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  p {
    font-size: 14px;
    opacity: 0.3;
    margin: auto;
  }
}
</style>
