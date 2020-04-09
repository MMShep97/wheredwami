<template>
    <div>
        <b-container>
            <b-row>
                <b-col/>
                <b-col>
                    <div class="floor-container">
                        <div class="red-dot" :style="{right: activePoster.xCoord * 7.5 + 'px'}">
                            
                        </div>
                        <!-- coords scaled by 8 -->
                        <svg class="svg-map" width="580" height="400" xmlns="http://www.w3.org/2000/svg">
                            <!-- Created with Method Draw - http://github.com/duopixel/Method-Draw/ -->
                            <g>
                                <title>background</title>
                                <rect fill="#fff" id="canvas_background" height="402" width="582" y="-1" x="-1" />
                                <g display="none" overflow="visible" y="0" x="0" height="100%" width="100%"
                                    id="canvasGrid">
                                    <rect fill="url(#gridpattern)" stroke-width="0" y="0" x="0" height="100%"
                                        width="100%" />
                                </g>
                            </g>
                            <g>
                                <!-- Created with Method Draw - http://github.com/duopixel/Method-Draw/ -->
                                <g stroke="null" id="svg_15">
                                    <g stroke="null"
                                        transform="matrix(1.1370396021097549,0,0,1.11254870547547,-5946.033486805716,-4013.440771117308) "
                                        id="svg_12">
                                        <title stroke="null"
                                            transform="translate(7.935129165649414,0) translate(5197.52490234375,0) translate(0,3584.5) ">
                                            background</title>
                                        <rect stroke="null" x="5204.460032" y="3583.5" width="582" height="402"
                                            id="svg_10" fill="#fff" />
                                        <g stroke="null" id="svg_9" display="none">
                                            <rect stroke="null" id="svg_13" width="580" height="400" x="5205.460032"
                                                y="3584.5" stroke-width="0" fill="url(#gridpattern)" />
                                        </g>
                                    </g>
                                    <g stroke="null"
                                        transform="matrix(1.129627765235867,0,0,1.0175936947284616,-5916.505486022397,-3621.4305796330295) "
                                        id="svg_14">
                                        <rect stroke="#000" fill="#fff" stroke-width="1.5" x="5243.197323"
                                            y="3869.765114" width="506" height="80" id="svg_8" />
                                        <rect stroke="#000" fill="#fff" stroke-width="1.5" x="5650.197323"
                                            y="3594.765114" width="99" height="275" id="svg_7" />
                                    </g>
                                </g>

                                <g>
                                    <title>pascagoula</title>
                                        <rect id="pascagoula" :class="{'static-active': activePoster.name == 'pascagoula' ? true: false}" height="6.766917" width="31.578947" y="390.726817"
                                            x="415.939838" stroke-width="1.5" stroke="#000" fill="#fff"/>
                                    
                                </g>
                                <g>
                                    <title>metaldust</title>

                                    <rect id="metaldus" :class="{'static-active': activePoster.name == 'metaldus' ? true: false}" height="6.766917" width="31.578947" y="390.726817"
                                        x="374.586455" stroke-width="1.5" stroke="#000" fill="#fff" />
                                </g>
                                <g>
                                    <title>honeywell</title>

                                    <rect id="honeywell" :class="{'static-active': activePoster.name == 'honeywell' ? true: false}" height="6.766917" width="31.578947" y="390.726817"
                                        x="327.969914" stroke-width="1.5" stroke="#000" fill="#fff" />
                                </g>
                                <g>
                                    <title>toxicrelease</title>

                                    <rect id="toxicrelease" :class="{'static-active': activePoster.name == 'toxicrelease' ? true: false}" height="6.766917" width="31.578947" y="390.726817"
                                        x="282.105253" stroke-width="1.5" stroke="#000" fill="#fff" />
                                </g>
                                <g>
                                    <title>formosa</title>

                                    <rect id="pvcexplosion" :class="{'static-active': activePoster.name == 'pvcexplosion' ? true: false}" height="6.766917" width="31.578947" y="390.726817" x="198.646607"
                                        stroke-width="1.5" stroke="#000" fill="#fff" />
                                </g>
                                <g>
                                    <title>fatalgas</title>

                                    <rect id="fatalgas" :class="{'static-active': activePoster.name == 'fatalgas' ? true: false}" height="6.766917" width="31.578947" y="390.726817"
                                        x="153.533826" stroke-width="1.5" stroke="#000" fill="#fff" />
                                </g>
                                <g>
                                    <title>morton</title>

                                    <rect id="morton" :class="{'static-active': activePoster.name == 'morton' ? true: false}" height="6.766917" width="31.578947" y="390.726817" x="80.601495"
                                        stroke-width="1.5" stroke="#000" fill="#fff" />
                                </g>
                                <g>
                                    <title>autowaterer</title>

                                    <rect id="autowaterer" :class="{'static-active': activePoster.name == 'autowaterer' ? true: false}" height="30.827068" width="6.766917" y="250.125313"
                                        x="571.578936" fill-opacity="null" stroke-opacity="null" stroke-width="1.5"
                                        stroke="#000" fill="#fff" />
                                </g>
                                <g>
                                    <title>suntracking</title>

                                    <rect id="suntracking" :class="{'static-active': activePoster.name == 'suntracking' ? true: false}" height="30.827068" width="6.766917" y="211.779449"
                                        x="571.578936" fill-opacity="null" stroke-opacity="null" stroke-width="1.5"
                                        stroke="#000" fill="#fff" />
                                </g>
                                <g>
                                    <title>
                                        snakegame
                                    </title>
                                    <rect id="snakegame" :class="{'static-active': activePoster.name == 'snakegame' ? true: false}" height="30.827068" width="6.766917" y="138.847119"
                                        x="571.578936" fill-opacity="null" stroke-opacity="null" stroke-width="1.5"
                                        stroke="#000" fill="#fff" />
                                </g>
                                <g>
                                    <title>
                                        smartblind
                                    </title>
                                    <rect id="smartblind" :class="{'static-active': activePoster.name == 'smartblind' ? true: false}" height="30.827068" width="6.766917" y="100.501255"
                                        x="571.578936" fill-opacity="null" stroke-opacity="null" stroke-width="1.5"
                                        stroke="#000" fill="#fff" />
                                </g>
                                <g>
                                    <title>
                                        poweroutlet
                                    </title>
                                    <rect id="poweroutlet" :class="{'static-active': activePoster.name == 'poweroutlet' ? true: false}" height="30.827068" width="6.766917" y="100.501255"
                                        x="466.315779" fill-opacity="null" stroke-opacity="null" stroke-width="1.5"
                                        stroke="#000" fill="#fff" />
                                </g>
                                <g>
                                    <title>
                                        rfidlibrary
                                    </title>
                                    <rect id="rfidlibrary" :class="{'static-active': activePoster.name == 'rfidlibrary' ? true: false}" height="30.827068" width="6.766917" y="245.614035"
                                        x="466.315779" fill-opacity="null" stroke-opacity="null" stroke-width="1.5"
                                        stroke="#000" fill="#fff" />
                                </g>
                                <g>
                                    <title>fatalexplosion</title>

                                    <rect id="dupon" :class="{'static-active': activePoster.name == 'dupon' ? true: false}" height="6.766917" width="31.578947" y="390.726817"
                                        x="14.436083" stroke-width="1.5" stroke="#000" fill="#fff" />
                                </g>
                            </g>
                        </svg>
                        <!-- <img :src="floorMap" width="1000px"/> -->
                    </div>
                </b-col>
                <b-col/>
            </b-row>
            <b-row>
                <b-col/>
                <b-col md="6" style="text-align: center">
                    <b-card
      header="Posters on the 4th Floor of the Seaman's Center"
      header-tag="header"
      title="Nearest Poster"
      class="mt-4"
      bg-variant="dark"
      text-variant="light"
    >
      <b-card-text class="mt-0 mb-0">Poster: {{activePoster.name}}</b-card-text>
      <b-card-text class="mt-0 mb-2">x: {{activePoster.xCoord}} | y: {{activePoster.yCoord}}</b-card-text>
      <b-card-text class="text-left mt-2 mb-0"><b><i>Color Legend</i></b></b-card-text>
      <b-card-text class="mt-0 mb-0 text-left">Classification Before Smoothing: <span class="static-active legend"></span></b-card-text>
      <b-card-text class="mt-0 mb-0 text-left">Smoothed Position Estimate: <span class="dynamic-active legend"></span></b-card-text>
      <!-- <b-card-text class="mt-0 mb-0 text-left">If both classify same: <span class="same-active">test</span></b-card-text> -->



      <!-- <b-button href="#" variant="primary">Go somewhere</b-button> -->
    </b-card>
                    </b-col>
                    <b-col/>
            </b-row>
        </b-container>
    </div>
</template>

<script>
    import floorMap from '../assets/images/floormap-4thfloorseamanscenter.svg'
    import axios from 'axios'
    export default {
        data() {
            return {
                floorMap: floorMap,
                activePoster: {
                    xCoord: '',
                    yCoord: '',
                    name: '',
                }
            }
        },

        methods: {
            getActivePoster: function () {
                const path = 'http://172.23.49.107:5000/active-poster'
                axios.get(path)
                    .then((response) => {
                        this.activePoster = response.data
                        console.log(this.activePoster)
                        console.log(this.activePoster.name)
                    })
                    .catch((error) => {
                        console.log(error)
                    })
            }
        },

        created() {
            setInterval(this.getActivePoster, 1000);
        }
    }
</script>

<style scoped>


    .floor-container {
        position: relative;
    }

    .red-dot {
        width: 12px;
        height: 12px;
        background-color: red;
        border-radius: 100%;
        position: absolute;
        bottom: 20px;
        right: 0;
        z-index: 100
    }

    .static-active {
        fill: var(--static);
        color: var(--static);
        background-color: var(--static)
    }

    .legend {
        display: inline-block;
        border-radius: 100%;
        width: 10px;
        height: 10px;
    }

    .dynamic-active {
        color: var(--dynamic);
        fill: var(--dynamic);
        background-color: var(--dynamic);
    }

    .same-active {
        color: var(--same);
        fill: var(--same);
    }
</style>