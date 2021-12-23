<template>
    <div class="add-shop">
        <div class="colums is-multiline">
            <div class="column is-12">
                <div class="title">Add shop</div>
            </div>
            <div class="column is-12 box">
                <form @submit.prevent="addShop">
                    <div class="field">
                        <label>Shopname</label>
                        <div class="control">
                            <input type="text" v-model="shopname"  class="input">
                        </div>
                    </div>
                    <div class="field">
                        <label>Address</label>
                        <div class="control">
                            <input type="text" v-model="address"  class="input">
                        </div>
                    </div>
                    <div class="field">
                        <label>district</label>
                        <div class="control">
                            <input type="text" v-model="district"  class="input">
                        </div>
                    </div>
                    <div class="field">
                        <label>Phone</label>
                        <div class="control">
                            <input type="text" v-model="phone"  class="input">
                        </div>
                    </div>
                    
                    <button class="button">Add Shop</button>
                </form>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
export default {
    name: "AddShop",
    data(){
        return{
            shopname: '',
            address: '',
            district:'',
            state: 'Kerala',
            phone: ''
        }
    },
    methods:{
        async addShop(){
            const formdata = {
                    shopname:this.shopname,
                    address:this.address,
                    district:this.district,
                    state:this.state,
                    phone:this.phone
                }
            await axios
                .post('/api/v1/add-shop/',formdata)
        }
    }
}
</script>