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

            <p><i>How to efficiently access the data and actually do research with it?</i><p>

            On the other hand, hospitals and CDCs have complex information systems that must comply with legislation such as GDPR.
            Handling personal data comes with high responsibility, thus care must be taken of cybersecurity,
            identity management, persistent and immutable storage, auditing, privacy and much more.

            <h2>What is MeDEP offering?</h2>

            <p>
            <i>Are you a doctor that needs to go efficiently through a fast growing body of literature,
               regarding covid-19? Are you interested only in particular aspects of the disease?
            </i><br/>
            By using AI, more than 30.000 biomedical documents have been automatically annotated with key-words,
            and our <router-link :to="{name:'Keyword explorer'}">keyword explorer</router-link>
            is ready for rank the documents according to your searches.
            </p>

            <p>
            <i>Are you a part of hospital management staff? Do you want your analysts to work on outdated data?
            Probably not.</i><br/>
            Let <b>MeDEP local</b> take care of data moving, cleaning, anonymization, access control, audit trails,
            versioning, etc. and let the analysts use their time to actually analyze the data, and provide you with
            up-to-date reports and KPIs.
            </p>

            <p>
            <i>Are you a data scientist who is wasting time on data sourcing and wrangling, rather than building
            models and doing research?</i><br/>
            Be the voice of reason and advocate MeDEP platform within your organisation to get access to readily
            available preprocessed, up-to-date and approved data sets. Your colleagues will think you are a rock star
            because not only will your reports always be on time and accurate, you will also be able to model
            changes trough time because all data sets are versioned and available to you. When doing research,
            you can choose to work only with data sets that allow for open publication.
            </p>

            <h2>Are you interested in MeDEP?</h2>
            Click <router-link :to="{name:'solution'}">here</router-link> to learn more.


            </v-col>
        </v-row>
    </v-container>
</template>

<script>

    export default {
        name: 'Home'
    }
</script>
