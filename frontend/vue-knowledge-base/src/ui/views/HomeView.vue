<template>
  <b-container fluid>
    <b-row>
      <b-col xs="12" sm="4" md="3" lg="2">
        <AppNav />
      </b-col>
      <b-col xs="12" sm="8" md="9" lg="10" style="padding: 0">
        <main>
          <AppSearchBar />
          <AppTestComponent />
        </main>
      </b-col>
    </b-row>
  </b-container>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import AppNav from "../components/AppNav.vue";
import AppSearchBar from "../components/AppSearchBar.vue";
import AppTestComponent from "../components/AppTestComponent.vue";

@Options({
  components: {
    AppNav,
    AppSearchBar,
    AppTestComponent,
  },
})
export default class HomeView extends Vue {}
</script>
<style scoped lang="scss">
main {
  align-items: center;
  justify-content: center;
  margin: 5px;
}
</style>
