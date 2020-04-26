<template>
    <v-container
            fluid
    >
        <v-row
        >
            <v-col>
                <div style="height:300px;">
                    <info-graph></info-graph>
                </div>


            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <br><br><br><br>
                <v-tabs
                        fixed-tabs
                >
                    <v-tab>
                        Clinical protocols
                    </v-tab>
                    <v-tab>
                        Drugs
                    </v-tab>
                    <v-tab>
                        Legislation changes
                    </v-tab>
                    <v-tab>
                        News
                    </v-tab>


                    <v-tab-item>
                        <v-card
                                flat
                                tile
                        >
                            <v-card-text>blabla</v-card-text>
                        </v-card>
                    </v-tab-item>

                    <v-tab-item>
                        <v-card
                                flat
                                tile
                        >
                            <v-card-text>
                                Drugs used to treat patients with COVID-19:<br/>
                                <ul>
                                    <li>Favipiravir</li>
                                    <li>Chloroquine and hydroxychloroquine</li>
                                    <li>Azytromicin</li>
                                    <li>Remdesivir</li>
                                    <li>Lopinavir/ritonavir (Kaletra)</li>
                                    <li>Umifenovir</li>
                                    <li>Tocilizumab</li>
                                    <li>Losartan</li>
                                </ul>

                            </v-card-text>
                        </v-card>
                    </v-tab-item>


                    <v-tab-item>
                        <v-card
                                flat
                                tile
                        >
                            <v-card-text>


                                <table class="table  table--ul-results">
                                    <tbody>

                                    <tr>
                                        <td class="results-note sequence">
                                            1.
                                        </td>
                                        <td>
                                            <a target="_blank"
                                               href="https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2020-01-0834/sklep-o-izmenjavi-osebnih-podatkov-o-odrejenih-posebnih-ukrepih-osamitve-karantene-in-obveznega-zdravljenja-zaradi-bolezni-covid-19-med-nacionalnim-institutom-za-javno-zdravje-in-policijo?h=covid">Sklep
                                                o izmenjavi osebnih podatkov o odrejenih posebnih ukrepih osamitve,
                                                karantene in obveznega zdravljenja zaradi bolezni COVID-19 med
                                                Nacionalnim inštitutom za javno zdravje in Policijo</a>
                                            <div class="results-note">22. 4. 2020</div>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td class="results-note sequence">
                                            2.
                                        </td>
                                        <td>
                                            <a target="_blank"
                                               href="https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2020-01-0775/odlok-o-odrejanju-in-izvajanju-ukrepov-povezanih-s-preprecevanjem-sirjenja-covid-19-na-mejnih-prehodih-na-zunanji-meji-in-na-kontrolnih-tockah-na-notranjih-mejah-republike-slovenije?h=covid">Odlok
                                                o odrejanju in izvajanju ukrepov, povezanih s preprečevanjem širjenja
                                                COVID-19, na mejnih prehodih na zunanji meji in na kontrolnih točkah na
                                                notranjih mejah Republike Slovenije</a>
                                            <div class="results-note">11. 4. 2020</div>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td class="results-note sequence">
                                            3.
                                        </td>
                                        <td>
                                            <a target="_blank"
                                               href="https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2020-01-0773/odlok-o-dopolnitvi-odloka-o-zacasnih-ukrepih-na-podrocju-zdravstvene-dejavnosti-zaradi-zajezitve-in-obvladovanja-epidemije-covid-19?h=covid">Odlok
                                                o dopolnitvi Odloka o začasnih ukrepih na področju zdravstvene
                                                dejavnosti zaradi zajezitve in obvladovanja epidemije COVID-19</a>
                                            <div class="results-note">10. 4. 2020</div>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td class="results-note sequence">
                                            4.
                                        </td>
                                        <td>
                                            <a target="_blank"
                                               href="https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2020-01-0766/zakon-o-interventnih-ukrepih-za-zajezitev-epidemije-covid-19-in-omilitev-njenih-posledic-za-drzavljane-in-gospodarstvo-ziuzeop?h=covid">Zakon
                                                o interventnih ukrepih za zajezitev epidemije COVID-19 in omilitev
                                                njenih posledic za državljane in gospodarstvo (ZIUZEOP)</a>
                                            <div class="results-note">10. 4. 2020</div>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td class="results-note sequence">
                                            5.
                                        </td>
                                        <td>
                                            <a target="_blank"
                                               href="https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2020-01-0708/odlok-o-zacasnih-ukrepih-na-podrocju-zdravstvene-dejavnosti-zaradi-zajezitve-in-obvladovanja-epidemije-covid-19?h=covid">Odlok
                                                o začasnih ukrepih na področju zdravstvene dejavnosti zaradi zajezitve
                                                in obvladovanja epidemije COVID-19</a>
                                            <div class="results-note">31. 3. 2020</div>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td class="results-note sequence">
                                            6.
                                        </td>
                                        <td>
                                            <a target="_blank"
                                               href="https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2020-01-0700/sklep-o-delu-sodnega-sveta-rs-v-casu-trajanja-odredbe-o-razglasitvi-epidemije-nalezljive-bolezni-sars-cov-2-covid-19?h=covid">Sklep
                                                o delu Sodnega sveta RS v času trajanja Odredbe o razglasitvi epidemije
                                                nalezljive bolezni SARS-CoV-2 (COVID-19)</a>
                                            <div class="results-note">30. 3. 2020</div>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td class="results-note sequence">
                                            7.
                                        </td>
                                        <td>
                                            <a target="_blank"
                                               href="https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2020-01-0681/zakon-o-zacasnih-ukrepih-v-zvezi-s-sodnimi-upravnimi-in-drugimi-javnopravnimi-zadevami-za-obvladovanje-sirjenja-nalezljive-bolezni-sars-cov-2-covid-19-zzusudjz?h=covid">Zakon
                                                o začasnih ukrepih v zvezi s sodnimi, upravnimi in drugimi javnopravnimi
                                                zadevami za obvladovanje širjenja nalezljive bolezni SARS-CoV-2
                                                (COVID-19) (ZZUSUDJZ)</a>
                                            <div class="results-note">28. 3. 2020</div>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td class="results-note sequence">
                                            8.
                                        </td>
                                        <td>
                                            <a target="_blank"
                                               href="https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2020-01-0657/odlok-o-zacasnih-ukrepih-pri-izvajanju-obveznega-zdravstvenega-zavarovanja-zaradi-zajezitve-in-obvladovanja-epidemije-covid-19?h=covid">Odlok
                                                o začasnih ukrepih pri izvajanju obveznega zdravstvenega zavarovanja
                                                zaradi zajezitve in obvladovanja epidemije COVID-19</a>
                                            <div class="results-note">24. 3. 2020</div>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td class="results-note sequence">
                                            9.
                                        </td>
                                        <td>
                                            <a target="_blank"
                                               href="https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2020-01-0650/odredba-o-zacasnem-delovnem-casu-notarjev-v-casu-trajanja-epidemije-virusne-okuzbe-sars-cov-2-covid-19?h=covid">Odredba
                                                o začasnem delovnem času notarjev v času trajanja epidemije virusne
                                                okužbe SARS-CoV-2 (COVID-19)</a>
                                            <div class="results-note">23. 3. 2020</div>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td class="results-note sequence">
                                            10.
                                        </td>
                                        <td>
                                            <a target="_blank"
                                               href="https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2020-01-0645/odlok-o-zacasnih-ukrepih-na-podrocju-zdravstvene-dejavnosti-zaradi-zajezitve-in-obvladovanja-epidemije-covid-19?h=covid">Odlok
                                                o začasnih ukrepih na področju zdravstvene dejavnosti zaradi zajezitve
                                                in obvladovanja epidemije COVID-19</a>
                                            <div class="results-note">20. 3. 2020</div>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td class="results-note sequence">
                                            11.
                                        </td>
                                        <td>
                                            <a target="_blank"
                                               href="https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2020-01-0558/sklep-o-uporabi-ukrepov-ki-jih-doloca-zakon-o-nalezljivih-boleznih-pri-epidemiji-covid-19?h=covid">Sklep
                                                o uporabi ukrepov, ki jih določa Zakon o nalezljivih boleznih, pri
                                                epidemiji COVID-19</a>
                                            <div class="results-note">14. 3. 2020</div>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td class="results-note sequence">
                                            12.
                                        </td>
                                        <td>
                                            <a target="_blank"
                                               href="https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2020-01-0550/odredba-o-zacasnih-ukrepih-za-obvladovanje-sirjenja-nalezljive-bolezni-sars-cov-2-covid-19?h=covid">Odredba
                                                o začasnih ukrepih za obvladovanje širjenja nalezljive bolezni
                                                SARS-CoV-2 (COVID-19)</a>
                                            <div class="results-note">13. 3. 2020</div>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td class="results-note sequence">
                                            13.
                                        </td>
                                        <td>
                                            <a target="_blank"
                                               href="https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2020-01-0532/odredba-o-razglasitvi-epidemije-nalezljive-bolezni-sars-cov-2-covid-19-na-obmocju-republike-slovenije?h=covid">Odredba
                                                o razglasitvi epidemije nalezljive bolezni SARS-CoV-2 (COVID-19) na
                                                območju Republike Slovenije</a>
                                            <div class="results-note">12. 3. 2020</div>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td class="results-note sequence">
                                            14.
                                        </td>
                                        <td>
                                            <a target="_blank"
                                               href="https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2020-01-0525/odredba-o-zacasnih-ukrepih-za-obvladovanje-sirjenja-nalezljive-bolezni-sars-cov-2-covid-19?h=covid">Odredba
                                                o začasnih ukrepih za obvladovanje širjenja nalezljive bolezni
                                                SARS-CoV-2 (COVID-19)</a>
                                            <div class="results-note">11. 3. 2020</div>
                                        </td>
                                    </tr>


                                    </tbody>
                                </table>


                            </v-card-text>
                        </v-card>
                    </v-tab-item>


                    <v-tab-item>
                        <v-card
                                flat
                                tile
                        >
                            <v-card-text>The data about news related to COVID-19 have not been prepared yet.
                            </v-card-text>
                        </v-card>
                    </v-tab-item>


                </v-tabs>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>

    import InfoGraph from "../components/InfoGraphRealData";

    export default {
        name: 'InfoDashboard',
        components: {InfoGraph,}
    }
</script>
