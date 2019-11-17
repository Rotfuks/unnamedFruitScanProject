<template>
  <div class="result">
    <HelloWorld :msg="result"/>

    <p>
      This fruit is the tasty banana!
    </p>
    <p>
      <b-embed
      type="iframe"
      aspect="16by9"
      :src="moreInfo"
      allowfullscreen
      ></b-embed>
    </p>
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

  private recognized:String = "banana";

  public get result() {
    return "It's a " +  this.recognized + "!";
  }

  public get moreInfo() {
    return "https://en.wikipedia.org/wiki/" + this.recognized;
  }
}
</script>
