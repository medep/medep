import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import UseCase from '../views/UseCase'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/keyword-explorer',
        name: 'Keyword explorer',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "keyword" */ '../views/KeywordExplorer.vue')
    },
    {
        path: '/solution',
        name: 'solution',
        component: () => import(/* webpackChunkName: "solution" */ '../views/Solution.vue')
    },
    {
        path: '/business-plan',
        name: 'business plan',
        component: () => import(/* webpackChunkName: "plan" */ '../views/BusinessPlan.vue')
    },
    {
        path: '/use-cases',
        name: 'use cases',
        component: () => import(/* webpackChunkName: "usecase" */ '../views/UseCases.vue')
    },
    {
        path: '/use-cases/:id',
        name: 'use case',
        component: UseCase,
    },
    {
        path: '/info-dashboard',
        name: 'info dashboard',
        component: () => import(/* webpackChunkName: "dashboard" */ '../views/InfoDashboard.vue')
    },
    {
        path: '/dataset-directory',
        name: 'dataset directory',
        component: () => import(/* webpackChunkName: "directory" */ '../views/DatasetDirectory.vue')
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
