<template>
    <v-app>

        <v-app-bar
                app
                clipped-left
                color="primary"
                dark
        >
            <v-app-bar-nav-icon @click.stop="drawer = !drawer"/>
            <v-toolbar-title><v-avatar tile class="mr-6"><img src="./assets/logo-1.png"></v-avatar> MeDEP - Medical Data Exploitation Platform</v-toolbar-title>
        </v-app-bar>

        <v-navigation-drawer
                clipped
                v-model="drawer"
                app
        >
            <v-list dense>
                <v-list-item link to="/">
                    <v-list-item-action>
                        <v-icon>mdi-home</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>Introduction</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item link to="/solution">
                    <v-list-item-action>
                        <v-icon>mdi-lightbulb</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>Solution</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>

                <v-list-item link to="/keyword-explorer">
                    <v-list-item-action>
                        <v-icon> mdi-state-machine</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>COVID-19 literature</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>

                <v-list-item link to="/dataset-directory">
                    <v-list-item-action>
                        <v-icon>mdi-database-search</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>Dataset directory</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>

                <v-list-item link to="/info-dashboard">
                    <v-list-item-action>
                        <v-icon>mdi-finance</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>Info dashboard</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>

                <v-list-item link to="/use-cases">
                    <v-list-item-action>
                        <v-icon>mdi-virus</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>Use cases</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>

                <v-list-item link to="/team">
                    <v-list-item-action>
                        <v-icon>mdi-account-multiple</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>The team</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>

 


            </v-list>
        </v-navigation-drawer>

        <v-content>
            <router-view></router-view>
        </v-content>
    </v-app>
</template>

<script>

    export default {
        name: 'App',

        data: () => ({
            drawer: null,
        }),
    };
</script>