<template>
  <div class="home">
    <HelloWorld msg="Welcome to Untitled Fruit Shop!"/>

    <p>
      Please upload a Fruit Picture to scan it.
    </p>
    <p>
      <b-form-file
        v-model="image"
        :state="Boolean(image)"
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
import { Component, Prop, Vue } from 'vue-property-decorator';
import router from '@/router/index.ts'
import HelloWorld from '@/components/HelloWorld.vue'

@Component ({
  components: {
    HelloWorld
  }
})
export default class extends Vue {
  private image: blob = null;

  public scanFruit() {
    router.push('Result')
  }
}
</script>
