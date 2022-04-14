import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView'
import OthelloView from '../views/OthelloView'
import SudokuView from '../views/SudokuView'


Vue.use(VueRouter)

const routes = [{

        path: '/sudoku',
        name: 'SudokuView',
        component: SudokuView,
    },

    {
        path: '/othello',
        name: 'OthelloView',
        component: OthelloView,
    },

    {
        path: '/home',
        name: 'HomeView',
        component: HomeView,
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router