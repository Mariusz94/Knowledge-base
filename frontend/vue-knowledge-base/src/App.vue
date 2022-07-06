<template>
  <AppHeader />
  <router-view />
  <AppFooter />
</template>

<script lang="ts">
import AppHeader from "@/ui/components/AppHeader.vue";
import AppFooter from "@/ui/components/AppFooter.vue";

export default {
  components: {
    AppHeader,
    AppFooter,
  },
};
</script>

<style lang="scss">
* {
  box-sizing: border-box;
}

#app {
  background-color: rgba(24, 25, 26, 1);
  font-family: sans-serif;
  margin: 0px;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
