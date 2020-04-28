import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import UseCase from '../views/UseCase'
import Team from '../views/Team'

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
        component: () => import(/* webpackChunkName: "keyword" */ '../views/KeywordExplorer.vue')
    },
    {
        path: '/solution',
        name: 'solution',
        component: () => import(/* webpackChunkName: "solution" */ '../views/Solution.vue')
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
    },
        {
        path: '/team',
        name: 'team',
        component: Team,
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

router.onError(error => {
    if (/loading chunk \d* failed./i.test(error.message)) {
        window.location.reload()
    }
})

export default router
