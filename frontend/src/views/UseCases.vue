<template>
    <v-container
            fluid style="margin:0; padding:0;"
    >
        <v-row class="col-12"
        >
            <v-col class="col-md-4">
                <v-card
                        outlined link to="/use-cases/1">

                    <v-img
                            class="white--text align-end"
                            height="200px"
                            src="../../public/case_studies/case1/header.png"
                    >
                    </v-img>
                    <v-card-title>COVID-19 vaccine-related literature exploration</v-card-title>
                    <v-card-text>Topic modeling of COVID-19 vaccine-related literature.
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn @click.stop
                               href="https://github.com/medep/medep/blob/master/frontend/public/case_studies/case1/case1.ipynb"
                               target=_blank>
                            <v-icon class="mr-2">mdi-github</v-icon>
                            Github
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
            <v-col class="col-md-4">
                <v-card
                        outlined link to="/use-cases/2">

                    <v-img
                            class="white--text align-end"
                            height="200px"
                            src="../../public/case_studies/case2/header.png"
                    >
                    </v-img>
                    <v-card-title>Document landscape exploration</v-card-title>
                    <v-card-text>Interactive 2D representations of more than 30k COVID-19 related papers
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn @click.stop
                               href="https://github.com/medep/medep/blob/master/frontend/public/case_studies/case2/case2.ipynb"
                               target=_blank>
                            <v-icon class="mr-2">mdi-github</v-icon>
                            Github
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
            <v-col class="col-md-4">
                <v-card
                        outlined link to="/use-cases/3">

                    <v-img
                            class="white--text align-end"
                            height="200px"
                            src="../../public/case_studies/case3/header.png"
                    >
                    </v-img>
                    <v-card-title>Distributed modeling of clinical outcomes</v-card-title>
                    <v-card-text>Deep learning and streaming models were used to explore possible modeling opportunities
                        related to
                        COVID-19 outcome, while preserving privacy of the data.
                    </v-card-text>

                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn @click.stop
                               href="https://github.com/medep/medep/blob/master/frontend/public/case_studies/case3/case3.ipynb"
                               target=_blank>
                            <v-icon class="mr-2">mdi-github</v-icon>
                            Github
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
            <v-col class="col-md-4">
                <v-card
                        outlined link to="/use-cases/4">

                    <v-img
                            class="white--text align-end"
                            height="200px"
                            src="../../public/case_studies/case4/header.png"
                    >
                    </v-img>
                    <v-card-title>Assessing potential COVID-19 drug candidates via automated literature exploration
                    </v-card-title>
                    <v-card-text>Discovering novel drug candidates by using the MeDEP's convenient API and text mining
                        functionality.
                    </v-card-text>

                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn @click.stop
                               href="https://github.com/medep/medep/blob/master/frontend/public/case_studies/case4/case4.ipynb"
                               target=_blank>
                            <v-icon class="mr-2">mdi-github</v-icon>
                            Github
                        </v-btn>
                    </v-card-actions>

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