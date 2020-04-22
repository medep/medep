<template>
    <v-container fluid>
        <v-row>
            <v-col>
                <blockquote>Our keyword explorer is a tool for fast and interactive literature prioritization. We
                    computed
                    keyphrases
                    based on whole texts, offering seamless exploration and ranking of biomedical documents related to
                    COVID-19 domain. The database, underlying this tool is accessible as <a
                            href="https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge">CORD19</a>.
                </blockquote>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-card
                        color="primary lighten-2"
                        dark
                >
                    <v-card-title class="headline primary lighten-3">
                        COVID-19 Explorer
                    </v-card-title>
                    <v-card-text>
                        A tool for literature prioritization based on unsupervised keyphrase detection.
                    </v-card-text>
                    <v-card-text>
                        <v-row>
                            <v-col
                                    cols="12"
                                    md="12"
                            >
                                <v-autocomplete
                                        v-model="selected_keyword"
                                        :items="keywords"
                                        :loading="isLoading"
                                        :search-input.sync="search"
                                        color="white"
                                        cache-items
                                        hide-no-data
                                        item-text="value"
                                        item-value="id"
                                        label="Enter keywords"
                                        placeholder="Start typing to Search"
                                        prepend-icon="mdi-database-search"
                                        return-object
                                        @change="search=''"
                                ></v-autocomplete>
                            </v-col>
                            <!--                            <v-col cols="12" md="3">-->
                            <!--                                <v-select-->
                            <!--                                        :items="[{value:1,description:'AND: match all of these'},{value:2,description:'OR: match any of these'}]"-->
                            <!--                                        item-text="description"-->
                            <!--                                        item-value="value"-->
                            <!--                                        label="Choose matching"-->
                            <!--                                        v-model="matching"-->
                            <!--                                ></v-select>-->
                            <!--                            </v-col>-->
                        </v-row>
                    </v-card-text>
                    <!--                    <v-expand-transition>-->
                    <!--                        <div class="ma-2 ml-10">-->
                    <!--                            <v-chip close @click:close="drop(keyword)" class="ma-1" color="red lighten-1"-->
                    <!--                                    v-for="keyword in selected_keywords">-->
                    <!--                                {{keyword.value}}-->
                    <!--                            </v-chip>-->
                    <!--                        </div>-->
                    <!--                    </v-expand-transition>-->
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn
                                :disabled="!selected_keyword"
                                color="grey darken-3"
                                @click="selected_keyword = null"
                        >
                            Clear
                            <v-icon right>mdi-close-circle</v-icon>
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>

        <v-row v-if="selected_keyword !== null">
            <v-col>

                <v-data-table :items="data" :headers="headers" class="elevation-1" :loading="table_loading"
                              loading-text="Loading... Please wait">

                    <template v-slot:item.article_doi="{ item }">
                        <a :href="'https://doi.org/'+item.article_doi" target="_blank">{{item.article_doi}}</a>
                    </template>

                </v-data-table>
            </v-col>

        </v-row>

    </v-container>
</template>

<script>
    export default {
        name: 'KeywordExplorer',
        data: () => ({
            descriptionLimit: 60,
            keywords: [],
            isLoading: false,
            selected_keyword: null,
            selected_keywords: [],
            search: null,
            table_loading: false,
            matching: 1,
            data: [],
            headers: [
                {
                    text: 'Score',
                    sortable: true,
                    value: 'score',
                },
                {
                    text: 'Article title',
                    sortable: true,
                    value: 'article_title'
                },
                {
                    text: 'DOI',
                    sortable: false,
                    value: 'article_doi',
                }
            ]
        }),

        methods: {
            drop(keyword) {
                const index = this.selected_keywords.indexOf(keyword);
                if (index > -1) {
                    this.selected_keywords.splice(index, 1);
                }
            },


            loadTable() {
                this.table_loading = true;
                fetch('http://covid19explorer.ijs.si/gp/api?keyword=' + this.selected_keyword.value)
                    .then(res => res.json())
                    .then(res => {
                        this.data = res
                    }).finally(() => (this.table_loading = false))
            }
        },

        computed: {
            fields() {
                if (!this.selected_keyword) return []

                return Object.keys(this.selected_keyword).map(key => {
                    return {
                        key,
                        value: this.selected_keyword[key] || 'n/a',
                    }
                })
            },
            items() {
                return this.keywords.map(entry => {
                    const Description = entry.value
                    return Object.assign({}, entry, {Description})
                })
            },
        },

        watch: {
            search(val) {
                // Items have already been requested
                if (this.isLoading) return

                this.isLoading = true

                // Lazily load input items
                fetch('http://covid19explorer.ijs.si/gp/autosuggest_keywords',
                    {
                        method: 'POST',
                        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                        body: "term=" + val
                    })
                    .then(res => res.json())
                    .then(res => {
                        this.keywords = res
                    })
                    .catch(err => {
                        console.log(err)
                    })
                    .finally(() => (this.isLoading = false))
            },
            selected_keyword(val) {
                if (val === null) {
                    this.data = []
                }
                const index = this.selected_keywords.indexOf(val);
                if (index < 0) {
                    this.selected_keywords.push(val)
                    // setTimeout(() => {
                    //         this.search = ''
                    //     }, 50
                    // )
                    this.loadTable()
                }
            }
        },
    }
</script>