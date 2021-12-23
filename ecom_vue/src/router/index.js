import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'
import Home from '../views/Home.vue'
import Product from '../views/Product.vue'
import Category from '../views/Category.vue'
import Search from '../views/Search.vue'
import Cart from '../views/Cart.vue'
import SignUp from '../views/SignUp.vue'
import Login from '../views/Login.vue'
import MyAccount from '../views/MyAccount.vue'
import Checkout from '../views/Checkout.vue'
import Success from '../views/Success.vue'
import AddShop from '../views/AddShop.vue'
import Seller from '../views/Seller.vue'
import AddProduct from '../views/AddProduct.vue'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/search',
    name: 'Search',
    component: Search
  },
  {
    path: '/cart',
    name: 'Cart',
    component: Cart
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'Login',
    component: Login
  },
  {
    path: '/cart/success',
    name: 'Success',
    component: Success,
    
  },
  {
    path: '/seller',
    name: 'Seller',
    component: Seller,
    meta:{
      requireLogin : true
    }
  },
  {
    path: '/seller/add-shop',
    name: 'AddShop',
    component: AddShop,
    meta:{
      requireLogin : true
    }
  },
  {
    path: '/seller/add-product',
    name: 'AddProduct',
    component: AddProduct,
    meta:{
      requireLogin : true
    }
  },
  {
    path: '/cart/checkout',
    name: 'Checkout',
    component: Checkout,
    meta:{
      requireLogin : true
    }
  },
  {
    path: '/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta:{
      requireLogin : true
    }
  },
  {
    path: '/:category_slug/:product_slug',
    name: 'Product',
    component: Product
  },
  {
    path: '/:category_slug',
    name: 'Category',
    component: Category
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})
router.beforeEach((to, from, next) => {
  if(to.matched.some(record=> record.meta.requireLogin) && !store.state.isAuthenticated){
    next({name:'Login',query:{to: to.path}})
  }else{
    next()
  }
})

export default router
