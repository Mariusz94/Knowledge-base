<template>
  <div class="nav-class">
    <nav>
      <ul>
        <li>
          <router-link to="/"><div>Home</div></router-link>
        </li>
        <li>
          <router-link to="/"><div>Add article</div></router-link>
        </li>
        <li>
          <router-link to="/"><div>Categories</div></router-link>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script lang="ts">
import { Vue } from "vue-class-component";
export default class AppNav extends Vue {}
</script>

<style scoped lang="scss">
nav {
  min-height: 87.3vh;
  color: white;
  font-size: 24px;
  position: relative;
  padding: 0;
  ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    gap: 2px;
    height: 100%;
    margin: 3px 0px 0px 10px;
    li {
      margin-top: 10px;
      width: 100%;
      a {
        text-decoration: none;
        color: white;
        div {
          padding-top: 15px;
          padding-bottom: 15px;
          padding-left: 10px;
          padding-right: 1px;
          width: 100%;
          text-align: left;
        }
        &:hover,
        &:active {
          text-decoration: none;
          color: white;
        }
        &:hover div,
        &:active div {
          background-color: rgba(48, 48, 49, 1);
          border-radius: 10px;
        }
      }
    }
  }
}

.nav-class {
  border-right: 1px solid rgba(48, 48, 49, 1);
  border-bottom: 0px solid rgba(48, 48, 49, 1);
}

@media (max-width: 575px) {
  nav {
    min-height: auto;

    ul {
      margin: 3px 10px 3px 10px;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding-right: 20px;
      padding-left: 20px;
      li a div {
        padding-right: 10px;
        padding-top: 2px;
        padding-bottom: 2px;
        text-align: center;
      }
    }
  }
  .nav-class {
    border-right: 0px solid rgba(48, 48, 49, 1);
    border-bottom: 1px solid rgba(48, 48, 49, 1);
  }
}
</style>
