<template>
  
</template>

<script>

import _ from 'lodash'

export default {
  methods: {
    selectIdx (areaNum) {
      const candidList = _.range(areaNum * 3, areaNum * 3 + 2)
      const idxInArea1 = _.samplesize(candidList, 2)

      return idxInArea1
    },
    placeNumIntoMap ()
  }
}
</script>

<style>

</style>