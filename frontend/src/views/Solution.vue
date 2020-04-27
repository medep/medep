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

MeDEP solves issues related to data acquisition and comes in two flawors: MeDEP local and MeDEP federated. Choose your weapon!<br />
</p>

            </v-col>
        </v-row>
		
		
		
		<v-row class="col-10">

            <v-col class="col-md-5">

                <v-card>
                    <v-card-subtitle><h3>MeDEP local - Join all organizational data sources</h3><br>
                    </v-card-subtitle>

                    <v-img
                            class="white--text align-end"
                            width="400px"
                            src="../assets/medep-local.png"
                    ></v-img>
                    <v-card-text>
					
                        MeDEP local is installed within the organization and is integrated with existing information systems by using specially crafted MeDEP connectors.
						The connectors are tailor-made by us to ensure 100% reliability and security.<br><br>
						Your IT department stays in full control over data access and policies. We grant and revoke user access automatically!<br><br>
						Data owners decide whether data can be accessed by MeDEP users.<br><br>
						  
						Upper management can observe KPIs in real time!
                    </v-card-text>
                </v-card>
            </v-col>
				
   <v-col class="col-md-5">

                <v-card>
				<v-card-subtitle><h3>MeDEP federated - Harness the real power of connected world</h3><br>
                    </v-card-subtitle>
                    <v-img
                            class="white--text align-end"
                            width="400px"
                            src="../assets/medep-federated.png"
                    ></v-img>
                    
                    <v-card-text>
                        MeDEP federated connects multiple MeDEP local instances. Now, different organizations can share research and current business data.
						<br>
						<br>Sharing data can:
<ul>
<li>improve patient treatment and research</li>
<li>optimize purchase plans by monitoring what is in stock and linking that data to financial plans</li>
<li>aid with resource planning in disaster scenarios or epidemic situations</li>
</ul>
Imagine the possibilities!
                    </v-card-text>
                </v-card>
            </v-col>				
				
        </v-row>
	 
	 
	 
    </v-container>
</template>

<script>

    export default {
        name: 'Solution'
    }
</script>
