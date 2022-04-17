import Vue from 'vue'
import Vuex from 'vuex'
import _ from 'lodash'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {},
    mutations: {
        selectIdx(areaNum) {
            const candidList = _.range(areaNum * 3, areaNum * 3 + 2)
            const idxInArea1 = _.samplesize(candidList, 2)

            return idxInArea1
        },

        placeNumIntoMap() {
            const numShuffle = _.sample(_.range(3, 5))
            const baseMap = [
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [7, 8, 9, 1, 2, 3, 4, 5, 6],
                [4, 5, 6, 7, 8, 9, 1, 2, 3],
                [3, 1, 2, 6, 4, 5, 9, 7, 8],
                [9, 7, 8, 3, 1, 2, 6, 4, 5],
                [6, 4, 5, 9, 7, 8, 3, 1, 2],
                [2, 3, 1, 5, 6, 4, 8, 9, 7],
                [8, 9, 7, 2, 3, 1, 5, 6, 4],
                [5, 6, 4, 8, 9, 7, 2, 3, 1]
            ]
            let count = 1

            while (count !== numShuffle) {
                let areaNumRow = _.sample(0, 2)
                let areaNumColumn = _.sample(0, 2)

                let selectedIdxRow = this.selectIdx(areaNumRow)
                let selectedIdxColumn = this.selectIdx(areaNumColumn)

                for (let row = 0; row < 9; row++) {
                    for (let column = 0; column < 9; column++) {
                        let tempNum = baseMap[row][selectedIdxRow[0]]
                        baseMap[row][selectedIdxRow[0]] = baseMap[row][selectedIdxRow[1]]
                        baseMap[row][selectedIdxRow[1]] = tempNum
                    }
                }

                for (let column = 0; column < 9; column++) {
                    for (let row = 0; row < 9; row++) {
                        let tempNum = baseMap[selectedIdxColumn[0]][column]
                        baseMap[selectedIdxColumn[0]][column] = baseMap[selectedIdxColumn[1]][column]
                        baseMap[selectedIdxColumn[1]][column] = tempNum
                    }
                }
                count = count + 1
            }
            return baseMap
        }
    },
    modules: {}
})