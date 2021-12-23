<template>
    <div class="add-product">
        <div class="colums is-multiline">
            <div class="column is-12">
                <div class="title">Add Product</div>
            </div>
            <div class="column is-12 box">
                <form @submit.prevent="addProduct" class="column is-6">
                    <div class="field">
                        <label>Product name</label>
                        <div class="control">
                            <input type="text" v-model="product.productname"  class="input">
                        </div>
                    </div>
                    <div class="field">
                        <label>Discription</label>
                        <div class="control">
                            <textarea type="text" v-model="product.discription"  class="input"></textarea>
                        </div>
                    </div>
                    <div class="field">
                        <label>Category</label>
                        <div class="control">
                            <select class="input" v-model="product.category" id="">
                                <option  v-for="category in categories" v-bind:key="category.id" v-bind:value="category.slug">{{category.name}}</option>  
                                <!-- remove this and add categories -->
                            </select>
                        </div>
                    </div>
                    <div class="field">
                        <label>Gender</label>
                        <div class="control">
                            <select class="input" v-model="product.gender" id="">
                                <option value="Male">Male</option>  
                                <option value="Female">Female</option>  
                                <option value="Unisex">Unisex</option>  
                                <!-- remove this and add categories -->
                            </select>
                        </div>
                    </div>
                    <div class="field">
                        <label>Price</label>
                        <div class="control">
                            <input type="text" v-model="product.price"  class="input">
                        </div>
                    </div>
                    <div class="field">
                        <label>Image</label>
                        <div class="control">
                            <input type="file" @change="fileSelected"  class="input">
                        </div>
                    </div>
                    
                    <button class="button">Add Product</button>
                </form>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
export default {
    name: 'AddProduct',
    data(){
        return{
            product:{
                productname:'',
                discription:'',
                category:'',
                price:'',
                gender:'',
                image:null,
            },
            categories:[]
        }
    },
    mounted(){
        this.addCategories()
    },
    methods:{
        fileSelected(event){
            this.product.image = event.target.files[0]
        },
        async addProduct(){
            if(this.product.productname && this.product.discription && this.product.category && this.product.image && this.product.price && this.product.gender){
                // console.log(this.product);
                // await axios('/api/v1/add_product/',this.product,{headers:{'Content-Type':'multipart/form-data'}}).then(res=>{
                //     console.log(res.data);
                // })
                let formData = new FormData();
                formData.append('productname',this.product.productname)
                formData.append('discription',this.product.discription)
                formData.append('category',this.product.category)
                formData.append('image',this.product.image)
                formData.append('price',this.product.price)
                formData.append('gender',this.product.gender)
                // formData.append('image',this.product.image)
                // formData=this.product
                // console.log(formData);
                // print(formData)
                await axios({
                    method:"post",
                    url:'/api/v1/add_product/',
                    data:formData
                })
                .then(res=>{
                    console.log(res.data);
                    // let imageData = new FormData();
                    // imageData.append('image',this.product.image)
                //     axios({
                //     method:"post",
                //     url:'/api/v1/add_product/',
                //     data:formData
                // })
                })
            }
        },

        async addCategories(){  // used to fetch category
            await axios.get('/api/v1/listcategories')
            .then(res=>{
                this.categories=res.data
                console.log(this.categories);
            })
        }
    }
}
</script>