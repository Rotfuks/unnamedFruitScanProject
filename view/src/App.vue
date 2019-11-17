<template>
  <div id="app">
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
}

.global-content {
  max-width: 600px;
  margin: auto;
}
</style>
