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
        <v-row>
            <v-col>
                <br><br><br><br>
                <v-tabs
                        fixed-tabs
                >
                    <v-tab>
                        Medical Protocol
                    </v-tab>
                    <v-tab>
                        News
                    </v-tab>
                    <v-tab>
                        Another Selection
                    </v-tab>
                    <v-tab>
                        Another Tab
                    </v-tab>


                    <v-tab-item>
                        <v-card
                                flat
                                tile
                        >
                            <v-card-text>blabla</v-card-text>
                        </v-card>
                    </v-tab-item>

                    <v-tab-item>
                        <v-card
                                flat
                                tile
                        >
                            <v-card-text>lorem ipsum...</v-card-text>
                        </v-card>
                    </v-tab-item>

                    <v-tab-item>
                        <v-card
                                flat
                                tile
                        >
                            <v-card-text>neki tretjega.</v-card-text>
                        </v-card>
                    </v-tab-item>

                    <v-tab-item>
                        <v-card
                                flat
                                tile
                        >
                            <v-card-text>arlarl</v-card-text>
                        </v-card>
                    </v-tab-item>


                </v-tabs>
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
