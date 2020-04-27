<template>
    <v-container
            fluid
    >

        <v-row>
            <v-col class="col-12">

                <v-select
                        v-model="country"
                        :items="items"
                        label="Select country"
                ></v-select>

            </v-col>
        </v-row>

        <v-row class="mb-3">
            <v-col class="col-12">

                <v-banner
                        elevation="3"
                        color="grey"
                        class="font-weight-light lighten-4"
                >
                    Info Dashboard joins many data sources and efficiently presents the relevant information
                    related to the covid-19 pandemic, for a given country:<br/>
                    <ul>
                        <li>number of currently infected people</li>
                        <li>stock exchange sentiment</li>
                        <li>clinical protocols</li>
                        <li>data related to the drugs used</li>
                        <li>legislation changes in the country, e.g., declaration of quarantine</li>
                        <li>news</li>
                    </ul>

                    The stock exchange sentiment is computed from the main stock exchange index of the chosen country
                    and reflects the trend the current trend of stock prices, as compared to their global trend.<br/>
                </v-banner>
            </v-col>
        </v-row>

        <div v-if="country==='Slovenia'">
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
                            Medical data
                        </v-tab>
                        <v-tab>
                            Legislation changes
                        </v-tab>
                        <v-tab>
                            News
                        </v-tab>


                        <v-tab-item>

                        <v-tabs fixed-tabs>
                        <v-tab>
                            Phases and Protocols
                        </v-tab>
                            <v-tab>
                                Drugs used for treatment
                            </v-tab>

                            <v-tab-item>
                            <v-card
                                    flat
                                    tile
                            >
                                <v-card-text>

                                    <p>In relation to the phase of the epidemy</p>
                                    <p>Phase 0:</p>
                                    <ul>
                                        <li>Intensive testing of potential suspected cases, doing overtesting to try
                                            finding infected individuals. Education of the public about signs and
                                            symptoms of COVID-19.
                                        </li>
                                        <li>Procurement procedures from the government for acquiring personal protective
                                            equipment (PPE) for medical health workers
                                        </li>
                                        <li>Designating hospitals to treat the first COVID 19 patients</li>
                                        <li>Education of health workers on how to treat such patients, how to put on/off
                                            protective gear
                                        </li>
                                        <li>Setting up several testing points to test for COVID-19</li>
                                    </ul>
                                    <p>&nbsp;</p>
                                    <ul>
                                        <li><em>If a patient is ill and shows respiratory symptoms, they should call
                                            their doctor and check with them wheater to get tested. They should avoid
                                            any unnecessary contact and stay at home, and not go to their doctor
                                            personally.</em></li>
                                        <li><em>In a medical emergency calling the emergency medical help number telling
                                            the personel that they also have respiratory symptoms, so they can be
                                            properly protected. Testing the patient.</em></li>
                                    </ul>
                                    <br>
                                    <p>Phase 1:</p>
                                    <ul>
                                        <li>First positive patients, alltogether less then n patients. Intensifying
                                            epidemiologic efforts to quell the transmision of the disease, finding close
                                            contact of the patients, isolating/hospitalising the patients and
                                            quarantining close contacts with all the needed information.
                                        </li>
                                        <li>Intensifying PPE procurement procdures.</li>
                                        <li>Epidemiologists coordinating with the government to prepare protocols for
                                            possible outcomes. Preparing the legislature needed for activating
                                            additional personel, managing the epidemiologic crisis.
                                        </li>
                                        <li>Intensifying the public awareness of the disease transmision and preventive
                                            measures.
                                        </li>
                                        <li>Advising against public gatherings indoors, canceling events of over 500
                                            people indoors. Advising the elderly to stay secluded.
                                        </li>
                                        <li>Setting up additional testing locations as needed.</li>
                                        <li>Setting up a call center for the general public in cooperation with the
                                            medical students
                                        </li>
                                    </ul>
                                    <p>&nbsp;</p>
                                    <ul>
                                        <li><em>Setting up protocols for COVID-19 treatment options.</em></li>
                                        <li><em>Setting up the 24/7 call numbers for other doctors to reach the
                                            infectology department, micribiology laboratory and on call
                                            epidemiologists.</em></li>
                                        <li><em>Setting up designated wards with an appropriate isolation option fort he
                                            COVID+19 positive patients.</em></li>
                                        <li><em>Setting up protocols fort he transportation of those patients in the
                                            hospital, and to the needed diagnostic procedures.</em></li>
                                        <li><em>Getting checked by a doctor in ful PPE, if stable &ndash; they can go
                                            home and wait for the test results. They get additional written information
                                            about the possible disease progression and what they need to look out
                                            for.</em></li>
                                        <li><em>If unstable &ndash; hospitalisation required with proper isolation
                                            protocols (single isolation or cohort isolation). Waiting fort the test
                                            results in the hospital.</em></li>
                                        <li><em>If the patient proves to be positive for COVID-19, according to the
                                            protocols.</em></li>
                                        <li><em>Hospitalizing the first patients in order fort the healthcare workers to
                                            get the needed experience handling these patients, getting to know the
                                            disease progression.</em></li>
                                        <li><em>Minimizing the number of entries to the essential healthcare
                                            infrastructure, doing triage at the entrypoint.</em></li>
                                    </ul>
                                    <br>
                                    <p>Phase 2:</p>
                                    <ul>
                                        <li>After a set number of positive patients and proven community transmision
                                            (without a known contact with a positive patient or travel abroad), the
                                            government institutes the before prepared protocols, declaring a coronavirus
                                            epidemic.
                                        </li>
                                        <li>No longer monitoring the specific contacts of positive patients, since there
                                            already is significant community transmission (except for the high risk
                                            groups &ndash; elderly homes, &hellip;).
                                        </li>
                                        <li>Closing schools, kindergartens, bars, restaurants, advising to work from
                                            home. Temporarilly closing down non-essential buisinesses, only leaving open
                                            the essential infrastructure.
                                        </li>
                                        <li>Legislature provisions prepared beforehand are implemented. Essential
                                            workers are prohibited from leaving the country, no vacations allowed. They
                                            can be called upon to work in different regions according to the healthcare
                                            needs of different regions in the country.
                                        </li>
                                        <li>Stoping public transport.</li>
                                        <li>Obligatory masks/mouth and nose coverings in public spaces, shops,...</li>
                                        <li>Setting up specific timeslots fort he most vulnerable population to be able
                                            to use the non healthcare related essential infrastructure.
                                        </li>
                                    </ul>
                                    <p>&nbsp;</p>
                                    <ul>
                                        <li><em>Stopping all non-essential (life-threatening) procedures and diagnostics
                                            in hospitals.</em></li>
                                        <li><em>Further education of the workforce about the disease in coordination
                                            with international experiences (Webinars, lectures, &hellip;)</em></li>
                                        <li><em>Cooperation of different specialists to treat the patient and the
                                            disease complications, organizing smaller task-oriented teams to further
                                            study treatment options,&hellip;)</em></li>
                                        <li><em>Having a low treshold to test healthcare workers for COVID 19 in case of
                                            potential symptoms.</em></li>
                                        <li><em>Preparing for a possible overflow mof patients, setting up
                                            protocols.</em></li>
                                        <li><em>Setting up telemetric medicine for the risk group patients &ndash; over
                                            60 years of age, immunocompromised, pregnant patients, monitoring them
                                            closely at home.</em></li>
                                    </ul>
                                    <br>
                                    <p>Phase 3:</p>
                                    <ul>
                                        <li>Observing the effects of the implemented restrictions in effect with the
                                            disease transmission paterns.
                                        </li>
                                        <li>Preparing additional restriction if needed.</li>
                                        <li>If reaching a plateau, possibly loosening the restrictions on public life
                                            and movement.
                                        </li>
                                    </ul>
                                    <br>
                                    <p>Phase 4:</p>
                                    <ul>
                                        <li>Gradually loosening the restrictions on public life, reopening businesses.
                                        </li>
                                        <li>Again intensive epidemiologic following of the contacts of the newly found
                                            positive patients.
                                        </li>
                                    </ul>
                                    <p>&nbsp;</p>
                                    <ul>
                                        <li><em>Consider reopening the non-essential procedures and diagnostic
                                            procedures.</em></li>
                                    </ul>
                                    <br>
                                    <p>Phase 5:</p>
                                    <ul>
                                        <li>The resolution of the epidemy, reopening the healthcare to the non-essential
                                            procedures and diagnostics
                                        </li>
                                    </ul>
                                    <br>
                                    <p>Phase 6:</p>
                                    <ul>
                                        <li>In case of a worsening epidemic, implementing the national catastrophy plan,
                                            activating the millitary and reserve workforce, increasing the bed capacity
                                            by setting up field hospitals, calling retired doctors back to work, asking
                                            for international help economically, for supplies or needed workforce.
                                        </li>
                                    </ul>
                                    <p>&nbsp;</p>


                                </v-card-text>
                            </v-card>
                            </v-tab-item>

                                                        <v-tab-item>
                            <v-card
                                    flat
                                    tile
                            >
                                <v-card-text>


                                    <p>Covid-19 therapy (potential therapeutic options for treating COVID-19):</p>
                                    <p>Direct effect on SARS-CoV-2:</p>
                                    <ul class="mb-3">
                                        <li>Favipiravir</li>
                                        <li>Chloroquine and hydroxychloroquine</li>
                                        <li>Azytromicin</li>
                                        <li>Remdesivir</li>
                                        <li>Lopinavir/ritonavir (Kaletra)</li>
                                        <li>Umifenovir</li>
                                    </ul>
                                    <p>Indirect effect on SARS-CoV-2:</p>
                                    <ul class="mb-3">
                                        <li>Tocilizumab</li>
                                        <li>Losartan</li>
                                    </ul>
                                    <p>Appropriate supportive care needed (Oxygen, anticoagulant treatment,
                                        &hellip;)</p>
                                    <p>&nbsp;</p>

                                </v-card-text>
                            </v-card>
                            </v-tab-item>

                        </v-tabs>
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
                                                    o odrejanju in izvajanju ukrepov, povezanih s preprečevanjem
                                                    širjenja
                                                    COVID-19, na mejnih prehodih na zunanji meji in na kontrolnih točkah
                                                    na
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
                                                    o začasnih ukrepih na področju zdravstvene dejavnosti zaradi
                                                    zajezitve
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
                                                    o delu Sodnega sveta RS v času trajanja Odredbe o razglasitvi
                                                    epidemije
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
                                                    o začasnih ukrepih v zvezi s sodnimi, upravnimi in drugimi
                                                    javnopravnimi
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
                                                    o začasnih ukrepih na področju zdravstvene dejavnosti zaradi
                                                    zajezitve
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
        </div>

        <div v-if="country!=='Slovenia'">
            <v-row class="col-12" v-if="!displayError">
                <v-col class="text-center col-12">
                    <v-progress-circular
                            :size="50"
                            color="primary"
                            indeterminate
                    ></v-progress-circular>
                </v-col>
            </v-row>
            <v-row v-if="displayError">
                <v-col>
                    <v-alert type="warning">
                        Data for {{country}} is not yet ready. Please check back later.
                    </v-alert>
                </v-col>
            </v-row>
        </div>

        <v-snackbar
                v-model="snackbar"
                :timeout="5000"
        >
            Notice: the sentiment data displayed here is not official.
            <v-btn
                    color="blue"
                    text
                    @click="snackbar = false"
            >
                Close
            </v-btn>
        </v-snackbar>

    </v-container>

</template>

<script>

    import InfoGraph from "../components/InfoGraphRealData";

    export default {
        name: 'InfoDashboard',
        components: {InfoGraph,},
        watch: {
            country: function (val) {
                if (this.displayError) {
                    this.displayError = false;
                    setTimeout(() => {
                        this.displayError = true;
                    }, 2000)
                }
            }
        },
        data: function () {
            return {
                'snackbar': true,
                'displayError': true,
                'country': 'Slovenia',
                'items': [
                    "Afghanistan",
                    "Albania",
                    "Algeria",
                    "American Samoa",
                    "Andorra",
                    "Angola",
                    "Anguilla",
                    "Antarctica",
                    "Antigua and Barbuda",
                    "Argentina",
                    "Armenia",
                    "Aruba",
                    "Australia",
                    "Austria",
                    "Azerbaijan",
                    "Bahamas (the)",
                    "Bahrain",
                    "Bangladesh",
                    "Barbados",
                    "Belarus",
                    "Belgium",
                    "Belize",
                    "Benin",
                    "Bermuda",
                    "Bhutan",
                    "Bolivia (Plurinational State of)",
                    "Bonaire, Sint Eustatius and Saba",
                    "Bosnia and Herzegovina",
                    "Botswana",
                    "Bouvet Island",
                    "Brazil",
                    "British Indian Ocean Territory (the)",
                    "Brunei Darussalam",
                    "Bulgaria",
                    "Burkina Faso",
                    "Burundi",
                    "Cabo Verde",
                    "Cambodia",
                    "Cameroon",
                    "Canada",
                    "Cayman Islands (the)",
                    "Central African Republic (the)",
                    "Chad",
                    "Chile",
                    "China",
                    "Christmas Island",
                    "Cocos (Keeling) Islands (the)",
                    "Colombia",
                    "Comoros (the)",
                    "Congo (the Democratic Republic of the)",
                    "Congo (the)",
                    "Cook Islands (the)",
                    "Costa Rica",
                    "Croatia",
                    "Cuba",
                    "Curaçao",
                    "Cyprus",
                    "Czechia",
                    "Côte d'Ivoire",
                    "Denmark",
                    "Djibouti",
                    "Dominica",
                    "Dominican Republic (the)",
                    "Ecuador",
                    "Egypt",
                    "El Salvador",
                    "Equatorial Guinea",
                    "Eritrea",
                    "Estonia",
                    "Eswatini",
                    "Ethiopia",
                    "Falkland Islands (the) [Malvinas]",
                    "Faroe Islands (the)",
                    "Fiji",
                    "Finland",
                    "France",
                    "French Guiana",
                    "French Polynesia",
                    "French Southern Territories (the)",
                    "Gabon",
                    "Gambia (the)",
                    "Georgia",
                    "Germany",
                    "Ghana",
                    "Gibraltar",
                    "Greece",
                    "Greenland",
                    "Grenada",
                    "Guadeloupe",
                    "Guam",
                    "Guatemala",
                    "Guernsey",
                    "Guinea",
                    "Guinea-Bissau",
                    "Guyana",
                    "Haiti",
                    "Heard Island and McDonald Islands",
                    "Holy See (the)",
                    "Honduras",
                    "Hong Kong",
                    "Hungary",
                    "Iceland",
                    "India",
                    "Indonesia",
                    "Iran (Islamic Republic of)",
                    "Iraq",
                    "Ireland",
                    "Isle of Man",
                    "Israel",
                    "Italy",
                    "Jamaica",
                    "Japan",
                    "Jersey",
                    "Jordan",
                    "Kazakhstan",
                    "Kenya",
                    "Kiribati",
                    "Korea (the Democratic People's Republic of)",
                    "Korea (the Republic of)",
                    "Kuwait",
                    "Kyrgyzstan",
                    "Lao People's Democratic Republic (the)",
                    "Latvia",
                    "Lebanon",
                    "Lesotho",
                    "Liberia",
                    "Libya",
                    "Liechtenstein",
                    "Lithuania",
                    "Luxembourg",
                    "Macao",
                    "Madagascar",
                    "Malawi",
                    "Malaysia",
                    "Maldives",
                    "Mali",
                    "Malta",
                    "Marshall Islands (the)",
                    "Martinique",
                    "Mauritania",
                    "Mauritius",
                    "Mayotte",
                    "Mexico",
                    "Micronesia (Federated States of)",
                    "Moldova (the Republic of)",
                    "Monaco",
                    "Mongolia",
                    "Montenegro",
                    "Montserrat",
                    "Morocco",
                    "Mozambique",
                    "Myanmar",
                    "Namibia",
                    "Nauru",
                    "Nepal",
                    "Netherlands (the)",
                    "New Caledonia",
                    "New Zealand",
                    "Nicaragua",
                    "Niger (the)",
                    "Nigeria",
                    "Niue",
                    "Norfolk Island",
                    "Northern Mariana Islands (the)",
                    "Norway",
                    "Oman",
                    "Pakistan",
                    "Palau",
                    "Palestine, State of",
                    "Panama",
                    "Papua New Guinea",
                    "Paraguay",
                    "Peru",
                    "Philippines (the)",
                    "Pitcairn",
                    "Poland",
                    "Portugal",
                    "Puerto Rico",
                    "Qatar",
                    "Republic of North Macedonia",
                    "Romania",
                    "Russian Federation (the)",
                    "Rwanda",
                    "Réunion",
                    "Saint Barthélemy",
                    "Saint Helena, Ascension and Tristan da Cunha",
                    "Saint Kitts and Nevis",
                    "Saint Lucia",
                    "Saint Martin (French part)",
                    "Saint Pierre and Miquelon",
                    "Saint Vincent and the Grenadines",
                    "Samoa",
                    "San Marino",
                    "Sao Tome and Principe",
                    "Saudi Arabia",
                    "Senegal",
                    "Serbia",
                    "Seychelles",
                    "Sierra Leone",
                    "Singapore",
                    "Sint Maarten (Dutch part)",
                    "Slovakia",
                    "Slovenia",
                    "Solomon Islands",
                    "Somalia",
                    "South Africa",
                    "South Georgia and the South Sandwich Islands",
                    "South Sudan",
                    "Spain",
                    "Sri Lanka",
                    "Sudan (the)",
                    "Suriname",
                    "Svalbard and Jan Mayen",
                    "Sweden",
                    "Switzerland",
                    "Syrian Arab Republic",
                    "Taiwan (Province of China)",
                    "Tajikistan",
                    "Tanzania, United Republic of",
                    "Thailand",
                    "Timor-Leste",
                    "Togo",
                    "Tokelau",
                    "Tonga",
                    "Trinidad and Tobago",
                    "Tunisia",
                    "Turkey",
                    "Turkmenistan",
                    "Turks and Caicos Islands (the)",
                    "Tuvalu",
                    "Uganda",
                    "Ukraine",
                    "United Arab Emirates (the)",
                    "United Kingdom of Great Britain and Northern Ireland (the)",
                    "United States Minor Outlying Islands (the)",
                    "United States of America (the)",
                    "Uruguay",
                    "Uzbekistan",
                    "Vanuatu",
                    "Venezuela (Bolivarian Republic of)",
                    "Viet Nam",
                    "Virgin Islands (British)",
                    "Virgin Islands (U.S.)",
                    "Wallis and Futuna",
                    "Western Sahara",
                    "Yemen",
                    "Zambia",
                    "Zimbabwe",
                    "Åland Islands"
                ]
            }
        }
    }
</script>
