<template>
  <b-container fluid>
    <b-row>
      <b-col>
        <header>
          <div>
            <p id="logo">Knowledge base</p>
          </div>
        </header>
      </b-col>
    </b-row>
  </b-container>
</template>

<script lang="ts">
import { Vue } from "vue-class-component";
export default class AppHeader extends Vue {}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.col,
.row,
.container-fluid {
  padding: 0;
  margin: 0;
}

header {
  height: 60px;
  display: flex;
  flex-flow: row wrap;
  justify-content: center;
  align-content: center;
  background-color: rgba(36, 37, 38, 1);
}

#logo {
  font-size: 24px;
  font-family: "Press Start 2P", cursive;
  color: rgb(255, 255, 255);
  overflow: hidden;
  border-right: 0.15em solid white;
  white-space: nowrap;
  margin: 0 auto;
  /* letter-spacing: .15sem; */
  animation: typing 3.5s steps(14, end), blink-caret 0.7s step-end infinite;
}

@keyframes typing {
  from {
    width: 0;
  }

  to {
    width: 100%;
  }
}

@keyframes blink-caret {
  from,
  to {
    border-color: transparent;
  }

  50% {
    border-color: white;
  }
}
</style>
