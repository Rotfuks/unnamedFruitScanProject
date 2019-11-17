<template>
  <div class="home">
    <HelloWorld msg="Welcome to Untitled Fruit Shop!"/>

    <p>
      Please upload a Fruit Picture to scan it.
    </p>
    <p>
      <b-form-file
        v-model="imageFile"
        :state="Boolean(imageFile)"
        placeholder="Choose a file or drop it here..."
        drop-placeholder="Drop file here..."
      ></b-form-file>
    </p>
    <p>
      <b-button variant="success" @click="scanFruit">
        What's this Fruit?
      </b-button>
    </p>
  </div>
</template>


<script lang="ts">
import axios from 'axios';
import { Component, Prop, Vue } from 'vue-property-decorator';
import router from '@/router/index.ts'
import HelloWorld from '@/components/HelloWorld.vue'

@Component ({
  components: {
    HelloWorld
  }
})
export default class extends Vue {
  private imageFile?: File;

  public scanFruit() {
    let bodyFormData:FormData = new FormData();
    bodyFormData.append('file', this.imageFile);
    axios({
      method: "POST",
      url: "http://35.228.108.145:8080/",
      data: this.bodyFormData,
      headers: {'Content-Type': 'multipart/form-data' }
    }).then(result => {
      console.log(result);
    }, error => {
      console.error(error);
    });
  }
}
</script>
