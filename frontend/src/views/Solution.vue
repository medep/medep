<template>
    <v-container
            fluid
    >
        <v-row                align="center"                justify="center"        >
            <v-col>
	
	<h1>Connect all stakeholders and win</h1>
	</v-col>
        </v-row>
	
	<v-row class="mb-3">
            <v-col class="col-12">

<p>
In an ideal world, each healthcare organization would have in-house software development engineers or do business with only one ISV. Unfortunately, 
this is not the case. Healthcare IT ecosystems are incredibly complex, developed and maintained by many vendors and often poorly integrated. 
This results in technical difficulties and data integrity issues on a daily basis. It is becoming increasingly difficult to obtain quality data. 

<br/>

MeDEP solves many issues related to data acquisition and comes in two flawors: MeDEP local and MeDEP federated. <br />

</p>

            </v-col>
        </v-row>
		
		
		
		<v-row class="col-10">

            <v-col class="col-md-5">

                <v-card>
                    <v-img
                            class="white--text align-end"
                            height="300px"
                            src="../assets/medep-local.png"
                    ></v-img>
                    <v-card-subtitle>MeDEP local: join all organizational data sources
                    </v-card-subtitle>
                    <v-card-text>
                        MeDEP local is installed within the organization and is integrated with existing information systems by using specially crafted MeDEP connectors.
						The connectors are tailor-made by us to ensure 100% reliability and security.
                    </v-card-text>
                </v-card>
            </v-col>
				
   <v-col class="col-md-5">

                <v-card>
                    <v-img
                            class="white--text align-end"
                            height="300px"
                            src="../assets/medep-local.png"
                    ></v-img>
                    <v-card-subtitle>MeDEP federated: Harness the real power of connected world
                    </v-card-subtitle>
                    <v-card-text>
                        MeDEP federated connects multiple MeDEP local instances. With this, different organizations can share research and current business data.
						All involved organizations 
                    </v-card-text>
                </v-card>
            </v-col>				
				
        </v-row>
				
	 
	   <v-row align="center" justify="center">
            <v-col>
	
	<h2>Technical details</h2>
	
	TODO
	
	</v-col>
	</v-row>
	 
	 
    </v-container>
</template>

<script>

    export default {
        name: 'Solution'
    }
</script>
