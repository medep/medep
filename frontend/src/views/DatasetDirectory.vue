<template>
    <v-container
            fluid
    >
        <v-row
                align="center"
                justify="center"
                v-if="detail_data === null"
        >
            <v-col>

                <h1>Dataset directory</h1>
                <v-subheader>Click on a table row to open the dataset.</v-subheader>

                <v-data-table :items="data" :headers="headers" class="elevation-1" :loading="table_loading"
                              loading-text="Loading... Please wait" @click:row="handleClick">

                    <template v-slot:item.authors="{ item }">
                        <v-chip v-for="author in item.authors" class="ma-1">{{author}}</v-chip>
                    </template>

                    <template v-slot:item.owners="{ item }">
                        <v-chip v-for="author in item.owners" class="ma-1">{{author}}</v-chip>
                    </template>

                </v-data-table>

            </v-col>
        </v-row>

        <v-row
                align="center"
                justify="center"
                v-if="detail_data !== null"
                class="col-12"
        >
            <v-col class="col-12">

                <h1>{{detail_data.datasetName}}</h1>

                <v-data-table disable-pagination :hide-default-footer="true" :items="detail_data_computed"
                              :headers="detail_headers" class="elevation-1" :loading="table_loading"
                              loading-text="Loading... Please wait" dense>
                </v-data-table>

            </v-col>

        </v-row>

        <v-row
                align="center"
                justify="center"
                v-if="detail_data !== null"
                class="col-12"
        >
            <v-col class="col-12">

                <v-btn @click="detail_data=null">Back</v-btn>

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
            detail_data: null,
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
        methods: {
            handleClick: function (value) {
                this.detail_data = value;
            }
        },
        computed: {
            detail_headers: function () {
                let h = []
                for (let j = 0; j < this.detail_data.data.attributes.length; j++) {
                    h.push({
                        text: this.detail_data.data.attributes[j].attributeName,
                        value: this.detail_data.data.attributes[j].attributeName
                    })
                }
                return h;
            },
            detail_data_computed: function () {
                let data = []
                for (let i = 0; i < this.detail_data.data.data.length; i++) {
                    let obj = {}
                    for (let j = 0; j < this.detail_data.data.attributes.length; j++) {
                        obj[this.detail_data.data.attributes[j].attributeName] = this.detail_data.data.data[i][j]
                    }
                    data.push(obj)
                }
                return data;
            }
        },
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
