<template>
    <v-container
            fluid
    >
        <v-row
                align="center"
                justify="center"
        >
            <v-col>
                <h1>Enter the medical data exploitation platform.</h1>

                Today, data is everywhere. Current technology, including AI, is already capable of doing great things
                by leveraging data, but the fundamental problem remains:

                <v-banner class="ma-7" color="green" dark elevation="3"><i>How to efficiently access the data and actually do research with it?</i></v-banner>
                <p>

                    On the other hand, hospitals and CDCs have complex information systems that must comply with
                    legislation such as GDPR.
                    Handling personal data comes with high responsibility, thus care must be taken of cybersecurity,
                    identity management, persistent and immutable storage, auditing, privacy and much more.


                <h2>What is MeDEP offering?</h2>

            </v-col>
        </v-row>
        <v-row class="col-12">

            <v-col class="col-4">

                <v-card>
                    <v-img
                            class="white--text align-end"
                            height="200px"
                            src="../assets/three-person-looking-at-x-ray-result-1170979.jpg"
                    ></v-img>
                    <v-card-subtitle>Are you a doctor that needs to go efficiently through a fast growing body of
                        literature,
                        regarding covid-19? Are you interested only in particular aspects of the disease?
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


            <v-col class="col-4">

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
                        Let <b>MeDEP local</b> take care of data moving, cleaning, anonymization, access control,
                        audit
                        trails,
                        versioning, etc. and let the analysts use their time to actually analyze the data, and
                        provide
                        you with
                        up-to-date reports and KPIs.
                    </v-card-text>
                </v-card>
            </v-col>


            <v-col class="col-4">

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

        <h2>Are you interested in MeDEP?</h2>
        Click
        <router-link :to="{name:'solution'}">here</router-link>
        to learn more.


        Cybersecurity, identity management, persistent and immutable storage, auditing,
        privacy and much more has to be taken into account.

        All these requirements are met by using specifically designed software solutions,
        which are often maintained by independent software vendors.
        That kind of data access is usually not enough to do research.

        Enter the medical data exploitation platform.

        2)
        [fensi šmensi overall complexity & hospital IS related gibberish] - martin
        dasd sadasd sadasd sadasd sadasd sadasd sadasd sadasd sadasd sadasd sadasd sadasd sadasd sadasd sadasd sadasd
        sadasd sadasd sadasd sadasd sadasd sadasd sadasd sadasd sadasd sadasd sadasd sadasd sadasd sadasd sadasd sadasd
        sadasd sadasd sadasd sadasd sadasd sa
        apache airflow --> periodicne analize

        The platform enables faster and more efficient research by providing access to various relevant medical and
        business-focused data sources. Clean and anonymised data are readily available for use by researchers and
        business analysts.


        3)
        Currently, the platform is in prototype phase.
        It allows access to publicly available literature related to novel corona virus. Our search engine goes beyond
        simple keyword search and uses cutting edge AI approaches to automatically annotate whole scientific documents.
        We regularly update the database which currently contains more than 30.000 documents.

        Our platform also offers a unique view of novel corona virus incidence, coupled with side-by-side information
        about the stock exchange sentiment, medical protocols, legislation changes.

        To showcase the power of our platform, we have prepared four case studies. They encompass visualization and
        topic detection in existing literature, a cross-hospital predictive novel corona virus modeling scenario, and
        drug candidate detection.


    </v-container>
</template>

<script>

    export default {
        name: 'Home'
    }
</script>
