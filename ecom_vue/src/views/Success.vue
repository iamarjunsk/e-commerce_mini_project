<template>
    <div class="page-success">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Thankyou</h1>
                <p>Your order will be processed within 24 hours</p>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: 'Success',
    mounted(){
        document.title="Success | Feather"
    }
}
</script>