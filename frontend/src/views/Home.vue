<template>
    <v-container
            fluid
    >
        <v-row
                align="center"
                justify="center"
        >
            <v-col>
                <h1>We are solving a difficult problem</h1>
				
                <p>
                    Hospitals and healthcare-related organizations use complex information systems. These systems store and process vast amounts of data which must 
					be properly handled. In addition to legal aspects (e.g., GDPR), purely technical problems such as cybersecurity,
                    identity management, persistent and immutable storage, auditing, high-availability, fault-tolerance, backup management and much more need to be addressed. 
				</p>
				
				<p>The listed technicalities are usually not the first thing that comes to mind when talking about data analysis. However, they are very much present 
				in the highly-regulated domains such as healthcare. <br /><br />
				
				Today, data is everywhere. Current technology, including AI, is already capable of doing great things
                by leveraging data, but the fundamental problem remains:
                <v-banner class="ma-7" color="green" dark elevation="3">
				<i>How to efficiently access the data and actually do research with it?</i>
				</v-banner>

				</p>
				
                <h2>Here is how we can help you</h2>

            </v-col>
        </v-row>
        <v-row class="col-12">

            <v-col class="col-md-4">

                <v-card>
                    <v-img
                            class="white--text align-end"
                            height="200px"
                            src="../assets/three-person-looking-at-x-ray-result-1170979.jpg"
                    ></v-img>
                    <v-card-subtitle>Are you a medical doctor that needs to efficiently browse a fast growing body of
                        literature,
                        regarding COVID-19? Are you interested only in particular aspects of the disease?
                    </v-card-subtitle>
                    <v-card-text>
                        By using AI, more than 30.000 biomedical documents have been automatically annotated with
                        key-words,
                        and our
                        <router-link :to="{name:'Keyword explorer'}">keyword explorer</router-link>
                        is ready for rank the documents according to your searches.
                    </v-card-text>
                </v-card>
            </v-col>


            <v-col class="col-md-4">

                <v-card>
                    <v-img
                            class="white--text align-end"
                            height="200px"
                            src="../assets/blue-and-silver-stetoscope-40568.jpg"
                    ></v-img>
                    <v-card-subtitle>Are you a part of hospital management staff? Do you want your analysts to work
                        on
                        outdated data?
                        Probably not.
                    </v-card-subtitle>
                    <v-card-text>
                        Let MeDEP take care of data moving, cleaning, anonymization, access control,
                        audit
                        trails,
                        versioning, etc. and let the analysts use their time to actually analyze the data, and
                        provide
                        you with
                        up-to-date reports and KPIs.
                    </v-card-text>
                </v-card>
            </v-col>


            <v-col class="col-md-4">

                <v-card>
                    <v-img
                            class="white--text align-end"
                            height="200px"
                            src="../assets/person-writing-on-notebook-669615.jpg"
                    >
                    </v-img>
                    <v-card-subtitle>Are you a data scientist who is wasting time on data sourcing and wrangling, rather
                        than building
                        models and doing research?
                    </v-card-subtitle>
                    <v-card-text>
                        Be the voice of reason and advocate MeDEP platform within your organisation to get access to
                        readily
                        available preprocessed, up-to-date and approved data sets. Your colleagues will think you are a
                        rock star
                        because not only will your reports always be on time and accurate, you will also be able to
                        model
                        changes trough time because all data sets are versioned and available to you. When doing
                        research,
                        you can choose to work only with data sets that allow for open publication.
                    </v-card-text>
                </v-card>
            </v-col>


        </v-row>

        <h3>Are you interested in MeDEP? Click
        <router-link :to="{name:'solution'}">here</router-link>
        to learn more.</h3>
        
    </v-container>
</template>

<script>

    export default {
        name: 'Home'
    }
</script>
