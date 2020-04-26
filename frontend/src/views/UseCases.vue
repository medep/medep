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
                            src="../../public/case_studies/case1/header.png"
                    >
                        <v-card-title>Use case 1</v-card-title>
                    </v-img>


                    <v-card-subtitle>COVID-19 vaccine-related literature exploration</v-card-subtitle>
                    <v-card-text>Topic modeling of COVID-19 vaccine-related literature.</v-card-text>
                </v-card>
            </v-col>
            <v-col class="col-4">
                <v-card
                        outlined link to="/use-cases/2">

                    <v-img
                            class="white--text align-end"
                            height="200px"
                            src="../../public/case_studies/case2/header.png"
                    >
                        <v-card-title>Use case 1</v-card-title>
                    </v-img>


                    <v-card-subtitle>Document landscape exploration</v-card-subtitle>
                    <v-card-text>Interactive 2D representations of more than 30k COVID-19 related papers</v-card-text>
                </v-card>
            </v-col>
            <v-col class="col-4">
                <v-card
                        outlined link to="/use-cases/3">

                    <v-img
                            class="white--text align-end"
                            height="200px"
                            src="../../public/case_studies/case3/header.png"
                    >
                        <v-card-title>Use case 3</v-card-title>
                    </v-img>


                    <v-card-subtitle>Modeling of sentiment and clinical outcomes</v-card-subtitle>
                    <v-card-text>Deep learning models were used to explore possible modeling opportunities related to COVID-19 outcome</v-card-text>
                </v-card>
            </v-col>
            <v-col class="col-4">
                <v-card
                        outlined link to="/use-cases/4">

                    <v-img
                            class="white--text align-end"
                            height="200px"
                            src="../../public/case_studies/case4/header.png"
                    >
                        <v-card-title>Use case 4</v-card-title>
                    </v-img>


                    <v-card-subtitle>Assessing potential COVID-19 drug candidates via automated literature exploration</v-card-subtitle>
                    <v-card-text>Discovering novel drug candidates by using the MeDEP's convenient API and text mining functionality.</v-card-text>
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