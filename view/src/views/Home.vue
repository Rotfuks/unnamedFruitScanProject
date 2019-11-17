<template>
  <div class="home">
    <HelloWorld msg="Welcome to Untitled Fruit Shop!"/>

    <p>
      Please upload a Fruit Picture to scan it.
    </p>
    <p class="my-form">
      <b-form-file
        v-model="imageFile"
        :state="Boolean(imageFile)"
        placeholder="Choose a file or drop it here..."
        drop-placeholder="Drop file here..."
      ></b-form-file>
    </p>
    <p>
      <div ref="spinner" id="mySpinner" class="justify-content-center mb-3">
        <b-spinner label="Loading..."></b-spinner>
      </div>
      <div ref="button" class="my-button">
        <b-button variant="success" @click="scanFruit">
          What's this Fruit?
        </b-button>
      </div>
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

  // @ts-ignore typing
  private imageFile?: File = null;

  public scanFruit() {
    let bodyFormData:FormData = new FormData();
    // @ts-ignore typecheck to make it faster
    bodyFormData.append('file', this.imageFile);
    this.$refs.button.style.display = "none";
    this.$refs.spinner.style.display = "flex";
    axios({
      method: "POST",
      url: "http://35.228.108.145:8080/",
      data: bodyFormData,
      headers: {'Content-Type': 'multipart/form-data' }
    }).then(result => {
      router.push({ path: `/result/?result=${result.data}` });
    }, error => {
      console.error(error);
    });
  }
}
</script>

<style>
.my-form {
  padding: 0 20px;
}
#mySpinner {
  display: none;
}
</style>
