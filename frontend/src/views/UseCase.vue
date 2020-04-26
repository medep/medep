<template>
    <v-container
            fluid class="fill-height" style="margin:0; padding:0;"
    >
        <iframe class="fill-height" width="100%" :src="route" frameborder="0"></iframe>
    </v-container>
</template>

<script>

    export default {
        name: 'UseCase',
        computed: {
            route: function () {
                switch (this.$route.params.id) {
                    case '1':
                        return '/case_studies/case1/case1.slides.html'
                    case '2':
                        return '/case_studies/case2/case2.html'
                    case '3':
                        return '/case_studies/case3/case3_2.html'
                    case '4':
                        return '/case_studies/case4/case4.html'
                }
            }
        }
    }
</script>
