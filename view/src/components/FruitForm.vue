<template>
  <div>
     <h1>test</h1>
     <input :value="file" placeholder="add a image" type="file" @change="onFileChange">
     <div>{{answer}}</div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class FruitForm extends Vue {
   import axios from 'axios';

   file: File;

   answer: string;

   constructor() {
      super();
      this.file = undefined;
      this.answer = '';
   }

   private onFileChange() {
     let response;
     await response = axios.get('https://api.coindesk.com/v1/bpi/currentprice.json');
     this.answer = response;
   }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
