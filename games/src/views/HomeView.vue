<template>
  <div>

    <carousel-comp></carousel-comp>
    <footer-comp class="text-center text-white bg-dark m-0 p-2"></footer-comp>

  </div>
</template>

<script>

import FooterComp from '../components/FooterComp.vue'
import CarouselComp from '../components/CarouselComp.vue'

export default {
  components: {
    FooterComp,
    CarouselComp,
  }
}
</script>

<style>

</style>