<template>
    <v-app>
        <v-navigation-drawer
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


                <v-list-item link to="/keyword-explorer">
                    <v-list-item-action>
                        <v-icon>mdi-database-search</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>Document library</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>

                <v-list-item link to="/business-plan">
                    <v-list-item-action>
                        <v-icon>mdi-briefcase</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>Business plan</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>


            </v-list>
        </v-navigation-drawer>

        <v-app-bar
                app
                color="indigo"
                dark
        >
            <v-app-bar-nav-icon @click.stop="drawer = !drawer"/>
            <v-toolbar-title>MeDEP - Medical exploration platform</v-toolbar-title>
        </v-app-bar>

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