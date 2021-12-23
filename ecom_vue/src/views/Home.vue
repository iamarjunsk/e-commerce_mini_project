<template>
  <div class="home">
    <div class="column is-2">
      <input type="text" class="input is-4" placeholder="Enter your place" @change="setPlace" v-model="place">
    </div>
      
    <section class="hero is-medium is-dark mb-6">
        <div class="hero-body has-text-centered">
          <p class="title mb-6">
            Welcome to Feathers
          </p>
          <div class="subtitle">
            A Fashion <b>Store</b>
          </div>
        </div>
    </section>
    <div class="columns is-multiline">
      <div class="column is-2 box ">
        <!-- categories -->
        <a v-for="category in categories" v-bind:key="category.id" v-bind:href="category.get_absolute_url" class="box">{{category.name}}</a>
      </div>

      <!-- based on location -->

      <div class="column is-10" v-if="placeDisp">
        <div class="columns is-multiline">
          <h2 class="is-size-2 has-text-centered">{{place}}</h2>
        </div>
        <div class="pds">

          <ProductBox v-for="product in placeDisp" v-bind:key="product.id" v-bind:product="product" />
        </div>

      </div>

      <div class="column is-10">
        <div class="columns is-multiline">
          <h2 class="is-size-2 has-text-centered">Latest Products</h2>
        </div>
        <div class="pds">

          <ProductBox v-for="product in latestProducts" v-bind:key="product.id" v-bind:product="product" />
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ProductBox from '@/components/ProductBox.vue'

export default {
  name: 'Home',
  data(){
    return{
      latestProducts: [],
      PlaceProduct:[],
      placeDisp:[],
      categories:[],
      place:''
    }
  },
  components: {
    ProductBox
  },
  mounted(){
    this.getLatestProducts(),
    // this.getProductByPlace(),
    this.getCategories()
    this.setPlaceLocaly()
  },
  methods:{
    async getLatestProducts(){

      this.$store.commit('setIsLoading',true)

      await axios.get('/api/v1/latest-products/')
      .then(response => {
        this.latestProducts = response.data

        document.title = 'Home'+'| Feather'
      })
      .catch(er =>{
        console.log(er);
      })
      this.$store.commit('setIsLoading',false)
    },
    async getCategories(){
      await axios.get('/api/v1/listcategories')
      .then(res=>{
        this.categories=res.data
        // console.log(this.categories);
      })
    },
    async setPlace(){
      this.placeDisp=[]
      this.$store.commit('setPlace',this.place)
      this.getProductByPlace()
    },
    setPlaceLocaly(){
      if(localStorage.getItem('place')){
        this.place=localStorage.getItem('place')
        console.log(this.place);
        this.getProductByPlace()
      }
    },
    async getProductByPlace(){
      // /api/v1/list-place
      await axios.get('/api/v1/list-place',{params:{'place':this.place}})
      .then(res=>{
        this.PlaceProduct = res.data
        let pds = []
        this.PlaceProduct.forEach(element => {
          pds.push(element.products)
        });
        this.placeDisp = pds[0]
      })
    console.log(this.placeDisp)
    }
  }
}
</script>
<style scoped>
.pds{
  display: flex;
  /* flex-direction: column; */
}
</style>