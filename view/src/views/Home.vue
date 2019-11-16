<template>
  <div class="home">
    <HelloWorld msg="Welcome to the UnnamedFruitScanProject"/>
    <FruitForm file=""/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue';
import FruitForm from '@/components/FruitForm.vue';

export default {
  name: 'home',
  components: {
    HelloWorld,
    FruitForm,
  },
};
</script>
