<template>
    <v-container
            fluid style="margin:0; padding:0;"
    >
        <v-row class="col-12"
        >
            <v-col class="col-4">
                <v-card
                        outlined link to="/use-cases/1">

                    <v-img
                            class="white--text align-end"
                            height="200px"
                            src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
                    >
                        <v-card-title>Use case 1</v-card-title>
                    </v-img>


                    <v-card-subtitle>Some subtitle</v-card-subtitle>
                    <v-card-text>This is a text</v-card-text>
                </v-card>
            </v-col>
            <v-col class="col-4">
                <v-card
                        outlined link to="/use-cases/2">

                    <v-img
                            class="white--text align-end"
                            height="200px"
                            src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
                    >
                        <v-card-title>Use case 1</v-card-title>
                    </v-img>


                    <v-card-subtitle>Some subtitle</v-card-subtitle>
                    <v-card-text>This is a text</v-card-text>
                </v-card>
            </v-col>
            <v-col class="col-4">
                <v-card
                        outlined link to="/use-cases/3">

                    <v-img
                            class="white--text align-end"
                            height="200px"
                            src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
                    >
                        <v-card-title>Use case 3</v-card-title>
                    </v-img>


                    <v-card-subtitle>Some subtitle</v-card-subtitle>
                    <v-card-text>This is a text</v-card-text>
                </v-card>
            </v-col>
            <v-col class="col-4">
                <v-card
                        outlined link to="/use-cases/4">

                    <v-img
                            class="white--text align-end"
                            height="200px"
                            src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
                    >
                        <v-card-title>Use case 4</v-card-title>
                    </v-img>


                    <v-card-subtitle>Some subtitle</v-card-subtitle>
                    <v-card-text>This is a text</v-card-text>
                </v-card>
            </v-col>

        </v-row>
    </v-container>
</template>

<script>

    export default {
        name: 'UseCases'
    }
</script>
