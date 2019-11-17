<template>
  <div id="app" class="box">
    <div class="global-navbar">
      <navbar/>
    </div>
    <div class="global-content">
      <router-view/>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import Navbar from '@/components/Navbar.vue'

@Component ({
  components: {
    Navbar
  }
})
export default class extends Vue {
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.global-navbar {
  padding-bottom: 30px;
  flex: 0 1 auto;
}

.global-content {
  flex: 1 1 auto;
  margin: 15px;
  height: 100vh;
}


.box {
  display: flex;
  flex-flow: column;
  height: 100%;
}

</style>
