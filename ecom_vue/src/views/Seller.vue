<template>
    <div class="seller-page">
        <div class="columns is-multiline">
            <div class="column is-6">
                <router-link to="/seller/add-shop" class="button">Add Shop</router-link>
            </div>
            <div class="column is-6">
                <router-link to="/seller/add-product" class="button">Add Product</router-link>
            </div>
        </div>
        <div class="columns is-multiline">
            <div class="column is-6">
                <div class="title">Orders</div>
                <table class="table">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Qunatity</th>
                            <th>Price</th>
                            <th></th>
                        </tr>
                        <tr v-for="pd in orders" v-bind:key="pd.id">
                            <td>{{pd.product.name}}</td>
                            <td>{{pd.quantity}}</td>
                            <td>{{pd.price}}</td>
                        </tr>
                        
                    </thead>
                    <tbody>
                        <tr ></tr>
                    </tbody>
                </table>
            </div>
            <div class="column is-6">
                <div class="title">Products</div>
                <table class="table">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th></th>
                        </tr>
                        <tr v-for="pd in sellerProducts" v-bind:key="pd.id">
                            <td><a v-bind:href="pd.get_absolute_url">{{pd.name}}</a></td>
                            <td>{{pd.price}}</td>
                            <td><button class="button" @click="deleteProduct(pd.id)">Delete</button></td>
                        </tr>
                        
                    </thead>
                    <tbody>
                        <tr ></tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
export default {
    name:'Seller.vue',
    data(){
        return{
            sellerProducts:[],
            orders:[]
        }
    },
    mounted(){
        this.getProducts(),
        this.getOrders()
    },
    methods:{
        async getProducts(){
                await axios.get('/api/v1/seller-products').then(res=>{
                this.sellerProducts = res.data
                // console.log(this.sellerProducts);
            })
        },
        async deleteProduct(a){
            await axios.get('/api/v1/delete-product/'+a)
            .then(res=>{
                this.sellerProducts = res.data
            })
        },
        async getOrders(){
            await axios.get('/api/v1/seller-orders').then(res=>{
                console.log(res.data);
                this.orders = res.data,
                console.log(this.orders);
            })
        }
    }
}
</script>