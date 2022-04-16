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
    placeNumIntoMap () {
      const numShuffle = _.sample(_.range(3, 5))
      const baseMap = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [3, 1, 2, 6, 4, 5, 9, 7, 8],
        [9, 7, 8, 3, 1, 2, 6, 4, 5],
        [6, 4, 5, 9, 7, 8, 3 ,1 ,2],
        [2, 3, 1, 5, 6, 4, 8, 9, 7],
        [8, 9, 7, 2, 3, 1, 5, 6, 4],
        [5, 6, 4, 8, 9, 7, 2, 3, 1]
      ]
      const count = 1

      while (count !== numShuffle) {
        let areaNumRow = _.sample(0, 2)
        let areaNumColumn = _.sample(0, 2)

        let selectedIdxRow = this.selectIdx(areaNumRow)
        let selectedIdxColumn = thiss.selectIdx(areaNumColumn)

        for (row of _.range(0, 8)) {
          for (column of _.range(0, 8)) {
            let tempNum = baseMap[row][selectedIdxRow[0]]
            baseMap[row][selectedIdxRow[0]] = baseMap[row][selectedIdxRow[1]]
            baseMap[row][selectedIdxRow[1]] = tempNum

        for (column of _.range(0, 8)) {
          for (row of _.range(0, 8)) {
            let tempNum = baseMap[selectedIdxColumn[0]][column]
            baseMap[selectedIdxColumn[0]][column] = baseMap[selectedIdxColumn[1]][column]
            baseMap[selectedIdxColumn[1]][column] = tempNum
          }

          count += 1
      return baseMap
        }
      }
    }
  }
}
</script>

<style>

</style>