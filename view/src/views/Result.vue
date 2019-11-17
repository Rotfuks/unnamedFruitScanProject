<template>
  <div class="result">
    <div class="row-container">
        <div class="first-row">
          <HelloWorld :msg="result"/>
          <p>
            This fruit is the tasty banana!
          </p>
          <h3>More information about {{ recognized }}</h3>
        </div>
        <iframe :src="moreInfo" class="second-row"></iframe>
      </div>
  </div>
</template>


<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import HelloWorld from '@/components/HelloWorld.vue'

@Component ({
  components: {
    HelloWorld
  }
})
export default class extends Vue {

  private recognized:string|null|undefined = "banana";

  public get result() {
    if (this.recognized == null) {
      return "It's nothing :(";
    }
    if(['a','e','i','o','u','A','E','I','O','U'].includes(this.recognized.charAt(0))) {
      return "It's an " +  this.recognized + "!";
    }
    return "It's a " +  this.recognized + "!";
  }

  public get moreInfo() {
    return "https://en.wikipedia.org/wiki/" + this.recognized;
  }

  public created() {
    // @ts-ignore typing
    this.recognized = this.$route.query.result;
    if(this.recognized==null) {
      this.recognized = "banana"
    }
  }
}
</script>

<style scoped>
.result {height: 100%;}
.row-container {display: flex; width: 100%; height: 100%; flex-direction: column; overflow: hidden;}
h3 {margin: 10px;}
.second-row { flex:2; flex-grow: 1; border: none; margin: 0; padding: 15px 0; }
</style>
