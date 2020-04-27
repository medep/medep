<template>
    <v-container
            fluid
    >
        <v-row
                align="center"
                justify="center"
        >
            <v-col>

                <h1>Dataset directory</h1>

                <v-data-table :items="data" :headers="headers" class="elevation-1" :loading="table_loading"
                              loading-text="Loading... Please wait">
                </v-data-table>

            </v-col>
        </v-row>
    </v-container>
</template>

<script>
    export default {
        name: 'DatasetDirectory',
        data: () => ({
            table_loading: true,
            data: [],
            headers: [
                {
                    text: 'Name',
                    sortable: true,
                    value: 'datasetName',
                },
                {
                    text: 'Authors',
                    sortable: false,
                    value: 'authors'
                },
                {
                    text: 'Owners',
                    sortable: false,
                    value: 'owners',
                }
            ]
        }),
        mounted() {
            this.table_loading = true;
            fetch('https://umcm.medep.org/data/')
                .then(res => res.json())
                .then(res => {
                    this.data = res
                }).finally(() => (this.table_loading = false))
        }
    }
</script>
