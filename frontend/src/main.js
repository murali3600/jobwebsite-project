import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import home from './components/home'
import adminlogin from './components/adminlogin'
import about from './components/about'
import terms from './components/terms'
Vue.use(VueRouter);
const routes=[
  {path:'/',component:home},
  {path:'/adminlogin',component:adminlogin},
  {path:'/about',component:about},
  {path:'/terms',component:terms}
]
const router= new VueRouter({
  routes
})
Vue.config.productionTip = false

new Vue({
  router:router,
  render: h => h(App),
}).$mount('#app')