<template>
    <v-container
            fluid
    >
        <v-row
        >
            <v-col>
                <div style="height:300px;">
                <info-graph></info-graph>
                </div>


            </v-col>
        </v-row>
    </v-container>
</template>

<script>

    import InfoGraph from "../components/InfoGraph";

    export default {
        name: 'InfoDashboard',
        components: {InfoGraph,}
    }
</script>
