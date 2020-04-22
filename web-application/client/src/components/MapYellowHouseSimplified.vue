<template>
    <div>
        <b-container>
            <b-row>
                <b-col />
                <b-col>
                    <div class="floor-container">
                        <div class="red-dot"
                            :style="[{left: activePoster.xCoord * scaleFactor + 'px'}, {bottom: activePoster.yCoord * scaleFactor + 'px'}]">
                        </div>
                        <svg :width="485.00000000000006 * scaleFactor" :height="198 * scaleFactor" viewBox="0 0 485 198"
                            xmlns="http://www.w3.org/2000/svg">
                            <!-- Created with Method Draw - http://github.com/duopixel/Method-Draw/ -->
                            <g>
                                <title>background</title>
                                <rect fill="#ffffff" id="canvas_background" height="200" width="487" y="-1" x="-1" />
                                <g display="none" overflow="visible" y="0" x="0" height="100%" width="100%"
                                    id="canvasGrid">
                                    <rect fill="url(#gridpattern)" stroke-width="0" y="0" x="0" height="100%"
                                        width="100%" />
                                </g>
                            </g>
                            <g>
                                <title>Layer 1</title>
                                <!-- rectangles -->
                                <rect id="daniel-rect" height="120" width="159" y="14" x="0.74074" stroke-width="1.5"
                                    stroke="#000" fill="#fff" />
                                <rect id="sy-rect" height="160" width="180" y="36.92593" x="304.25926"
                                    stroke-width="1.5" stroke="#000" fill="#fff" />
                                <rect id="rail-rect" height="113" width="207" y="1.01968" x="133.25926"
                                    stroke-width="1.5" stroke="#000" fill="#fff" />
                                <rect id="small-rect-hallway" height="47" width="34" y="86.96296" x="133"
                                    fill-opacity="null" stroke-opacity="null" stroke-width="1.5" stroke="#000"
                                    fill="#fff" />
                                <!-- end of rectangles -->
                                <path stroke="#000" id="daniel-star" class="star" :class="{'static-active': activePoster.name == 'daniel' ? true: false}"
                                    d="m45.25,125.34418l3.25705,0l1.00645,-3.09418l1.00645,3.09418l3.25705,0l-2.635,1.91229l1.00651,3.09418l-2.635,-1.91234l-2.635,1.91234l1.00651,-3.09418l-2.635,-1.91229z"
                                    fill-opacity="null" stroke-opacity="null" stroke-width="0.5" fill="#fff" />
                                <path stroke="#000" id="rail-star" class="star" :class="{'static-active': activePoster.name == 'rail' ? true: false}"
                                    d="m235.25641,76.34419l3.25705,0l1.00645,-3.09419l1.00646,3.09419l3.25704,0c-0.87833,0.63742 -1.75667,1.27485 -2.635,1.91228l1.00651,3.09419l-2.63501,-1.91234l-2.635,1.91234l1.0065,-3.09419l-2.635,-1.91228z"
                                    fill-opacity="null" stroke-opacity="null" stroke-width="0.5" fill="#fff" />
                                <path stroke="#000" id="sy-star" class="star" :class="{'static-active': activePoster.name == 'sy' ? true: false}"
                                    d="m427.24999,76.34419l3.25705,0l1.00645,-3.09419l1.00646,3.09419l3.25704,0l-2.635,1.91228l1.00651,3.09419l-2.63501,-1.91234l-2.635,1.91234l1.0065,-3.09419l-2.635,-1.91228z"
                                    fill-opacity="null" stroke-opacity="null" stroke-width="0.5" fill="#fff" />
                                <text xml:space="preserve" text-anchor="start" :class="{'static-active': activePoster.name == 'rail' ? true: false}"
                                    font-family="Helvetica, Arial, sans-serif" font-size="11" id="svg_12" y="69.90857"
                                    x="230.09259" stroke-opacity="null" stroke-width="0" stroke="#000"
                                    fill="#7a7a7a">Rail</text>
                                <text xml:space="preserve" text-anchor="start" :class="{'static-active': activePoster.name == 'sy' ? true: false}"
                                    font-family="Helvetica, Arial, sans-serif" font-size="11" id="svg_13" y="69.16783"
                                    x="424.53704" stroke-opacity="null" stroke-width="0" stroke="#000"
                                    fill="#898989">Sy</text>
                                <text xml:space="preserve" text-anchor="start" :class="{'static-active': activePoster.name == 'daniel' ? true: false}"
                                    font-family="Helvetica, Arial, sans-serif" font-size="11" id="svg_14" y="117.68635"
                                    x="34.53703" stroke-opacity="null" stroke-width="0" stroke="#000"
                                    fill="#969696">Daniel</text>
                            </g>
                        </svg>
                    </div>
                </b-col>
                <b-col />
            </b-row>
            <b-row>
                <b-col />
                <b-col md="6" style="text-align: center">
                    <b-card header="Location in THE Yellow House" header-tag="header" title="Nearest Poster"
                        class="mt-4" bg-variant="dark" text-variant="light">
                        <b-card-text class="mt-0 mb-0">Poster: {{activePoster.name}}</b-card-text>
                        <b-card-text class="mt-0 mb-2">x: {{activePoster.xCoord}} | y: {{activePoster.yCoord}}
                        </b-card-text>
                        <b-card-text class="text-left mt-2 mb-0"><b><i>Color Legend</i></b></b-card-text>
                        <b-card-text class="mt-0 mb-0 text-left">Classification Before Smoothing: <span
                                class="static-active legend"></span></b-card-text>
                        <b-card-text class="mt-0 mb-0 text-left">Smoothed Position Estimate: <span
                                class="dynamic-active legend"></span></b-card-text>
                        <!-- <b-card-text class="mt-0 mb-0 text-left">If both classify same: <span class="same-active">test</span></b-card-text> -->



                        <!-- <b-button href="#" variant="primary">Go somewhere</b-button> -->
                    </b-card>
                </b-col>
                <b-col />
            </b-row>
        </b-container>
    </div>
</template>

<script>
    // import floorMap from '../assets/images/floormap-yellowhouse.svg'
    import axios from 'axios'
    export default {
        data() {
            return {
                // floorMap: floorMap,
                activePoster: {
                    xCoord: '',
                    yCoord: '',
                    name: '',
                },
                scaleFactor: 2,
            }
        },

        methods: {
            getActivePoster: function () {
                const path = 'http://192.168.1.35:5000/active-poster'
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

    .container {
        width: 100%;
        height: 100%;
    }

    .red-dot {
        width: 12px;
        height: 12px;
        background-color: red;
        border-radius: 100%;
        position: absolute;
        bottom: 0;
        left: 0;
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