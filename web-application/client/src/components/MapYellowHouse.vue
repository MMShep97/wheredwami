<template>
    <div>
        <b-container>
            <b-row>
                <b-col />
                <b-col>
                    <div class="floor-container">
                        <div class="red-dot" :style="[{left: activePoster.xCoord * scaleFactor + 'px'}, {bottom: activePoster.yCoord * scaleFactor + 'px'}]">

                        </div>
                        <svg :width="296.00000000000006 * scaleFactor" :height="209 * scaleFactor" viewBox="0 0 296 209"
                            xmlns="http://www.w3.org/2000/svg">
                            <!-- Created with Method Draw - http://github.com/duopixel/Method-Draw/ -->

                            <g>
                                <title>background</title>
                                <rect fill="#fff" id="canvas_background" height="76.64277" width="107.71417" y="-1"
                                    x="-1" />
                                <g display="none" id="canvasGrid">
                                    <rect fill="url(#gridpattern)" stroke-width="0" y="0" x="0" height="100%"
                                        width="100%" id="svg_4" />
                                </g>
                            </g>
                            <g>
                                <title>Layer 1</title>
                                <rect id="kitchen-background" height="137" width="171" y="0.96428" x="123.94737"
                                    stroke-width="1.5" fill="#fff" stroke="#000" />
                                <rect id="hallway-background" height="112" width="177" y="95.96491" x="1"
                                    stroke-width="1.5" stroke="#000" fill="#fff" />
                                <!-- <path id="svg_6" d="m-60.28948,52.77714" opacity="0.5" fill-opacity="1"
                                    stroke-opacity="null" stroke-width="0.4" stroke="#000" fill="yellow" /> -->
                                <path fill="#fff" stroke-width="0.4" stroke-opacity="null" fill-opacity="null"
                                    d="m39.75002,101.45779l1.84236,0l0.5693,-1.70779l0.5693,1.70779l1.84236,0l-1.4905,1.05546l0.56933,1.70779l-1.4905,-1.05549l-1.4905,1.05549l0.56933,-1.70779l-1.4905,-1.05546l0.00002,0z"
                                    id="bens-room" class="star" :class="{'static-active': activePoster.name == 'ben' ? true: false}" stroke="#000" />
                                <path fill="#fff" stroke-width="0.4" stroke-opacity="null" fill-opacity="null"
                                    d="m39.25,174.45779l1.84236,0l0.56931,-1.70779l0.5693,1.70779l1.84236,0l-1.4905,1.05546l0.56934,1.7078l-1.4905,-1.0555l-1.4905,1.0555l0.56933,-1.7078l-1.4905,-1.05546z"
                                    id="daniels-room" class="star" :class="{'static-active': activePoster.name == 'daniel' ? true: false}" stroke="#000" />
                                <path fill="#fff" stroke-width="0.4" stroke-opacity="null" fill-opacity="null"
                                    d="m137.75,174.45779l1.84236,0l0.56931,-1.70779l0.5693,1.70779l1.84236,0l-1.4905,1.05546l0.56934,1.7078l-1.4905,-1.0555l-1.4905,1.0555l0.56933,-1.7078l-1.4905,-1.05546z"
                                    id="sys-room" class="star" :class="{'static-active': activePoster.name == 'sy' ? true: false}" stroke="#000" />
                                <path fill="#fff" stroke-width="0.4" stroke-opacity="null" fill-opacity="null"
                                    d="m137.75,49.45779l1.84236,0l0.56931,-1.70779l0.5693,1.70779l1.84236,0l-1.4905,1.05546l0.56934,1.7078l-1.4905,-1.0555l-1.4905,1.0555l0.56933,-1.7078l-1.4905,-1.05546z"
                                    id="oven" class="star" :class="{'static-active': activePoster.name == 'oven' ? true: false}" stroke="#000" />
                                <path fill="#fff" stroke-width="0.4" stroke-opacity="null" fill-opacity="null"
                                    d="m255.74999,21.45779l1.84236,0l0.56931,-1.70779l0.5693,1.70779l1.84236,0l-1.4905,1.05546l0.56934,1.7078l-1.4905,-1.0555l-1.4905,1.0555l0.56933,-1.7078l-1.4905,-1.05546z"
                                    id="fridge" class="star" :class="{'static-active': activePoster.name == 'fridge' ? true: false}" stroke="#000" />
                                <path fill="#fff" stroke-width="0.4" stroke-opacity="null" fill-opacity="null"
                                    d="m260.74999,132.45779l1.84236,0l0.56931,-1.70779l0.5693,1.70779l1.84236,0l-1.4905,1.05546l0.56934,1.7078l-1.4905,-1.0555l-1.4905,1.0555l0.56933,-1.7078l-1.4905,-1.05546z"
                                    id="table" class="star" :class="{'static-active': activePoster.name == 'table' ? true: false}" stroke="#000" />
                                <text stroke="#000000"
                                    transform="matrix(0.17453773319721222,0,0,0.17453773319721222,14.071552079403773,68.73263155925088) "
                                    xml:space="preserve" text-anchor="start" font-family="Helvetica, Arial, sans-serif"
                                    font-size="24" id="svg_7" :class="{'static-active': activePoster.name == 'ben' ? true: false}" y="194.70518" x="-12.36715" fill-opacity="0.4"
                                    stroke-opacity="null" stroke-width="0" fill="#000000">Ben's Room</text>
                                <text stroke="#000000"
                                    transform="matrix(0.17453773319721222,0,0,0.17453773319721222,14.071552079403773,68.73263155925088) "
                                    xml:space="preserve" text-anchor="start" font-family="Helvetica, Arial, sans-serif"
                                    font-size="24" id="svg_8" :class="{'static-active': activePoster.name == 'daniel' ? true: false}" y="620.54006" x="-24.6247" fill-opacity="0.4"
                                    stroke-opacity="null" stroke-width="0" fill="#000000">Daniel's Room</text>
                                <text stroke="#000000"
                                    transform="matrix(0.17453773319721222,0,0,0.17453773319721222,14.071552079403773,68.73263155925088) "
                                    xml:space="preserve" text-anchor="start" font-family="Helvetica, Arial, sans-serif"
                                    font-size="24" id="svg_14" :class="{'static-active': activePoster.name == 'sy' ? true: false}" y="620.54006" x="566.76828" fill-opacity="0.4"
                                    stroke-opacity="null" stroke-width="0" fill="#000000">Sy's Room</text>
                                <text style="cursor: move;" stroke="#000000"
                                    transform="matrix(0.17453773319721222,0,0,0.17453773319721222,14.071552079403773,68.73263155925088) "
                                    xml:space="preserve" text-anchor="start" font-family="Helvetica, Arial, sans-serif"
                                    font-size="24" id="svg_15" :class="{'static-active': activePoster.name == 'oven' ? true: false}" y="-138.22026" x="690.64752" fill-opacity="0.4"
                                    stroke-opacity="null" stroke-width="0" fill="#000000">Oven</text>
                                <text stroke="#000000"
                                    transform="matrix(0.17453773319721222,0,0,0.17453773319721222,14.071552079403773,68.73263155925088) "
                                    xml:space="preserve" text-anchor="start" font-family="Helvetica, Arial, sans-serif"
                                    font-size="24" id="svg_16" :class="{'static-active': activePoster.name == 'fridge' ? true: false}" y="-296.16629" x="1362.69237" fill-opacity="0.4"
                                    stroke-opacity="null" stroke-width="0" fill="#000000">Fridge</text>
                                <text stroke="#000000"
                                    transform="matrix(0.17453773319721222,0,0,0.17453773319721222,14.071552079403773,68.73263155925088) "
                                    xml:space="preserve" text-anchor="start" font-family="Helvetica, Arial, sans-serif"
                                    font-size="24" id="svg_17" :class="{'static-active': activePoster.name == 'table' ? true: false}" y="337.1663" x="1395.21067" fill-opacity="0.4"
                                    stroke-opacity="null" stroke-width="0" fill="#000000">Table</text>
                                <text style="cursor: move;" stroke="#000000"
                                    transform="matrix(0.17453773319721222,0,0,0.17453773319721222,14.071552079403773,68.73263155925088) "
                                    xml:space="preserve" text-anchor="start" font-family="Helvetica, Arial, sans-serif"
                                    font-size="24" id="svg_18" y="-45.31084" x="1104.09447" fill-opacity="0.2"
                                    stroke-opacity="null" stroke-width="0" fill="#000000">Kitchen</text>
                                <text stroke="#000000"
                                    transform="matrix(0.17453773319721222,0,0,0.17453773319721222,14.071552079403773,68.73263155925088) "
                                    xml:space="preserve" text-anchor="start" font-family="Helvetica, Arial, sans-serif"
                                    font-size="24" id="svg_19" y="450.20611" x="353.0766" fill-opacity="0.2"
                                    stroke-opacity="null" stroke-width="0" fill="#000000">Hallways / Stairs</text>
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
                scaleFactor: 2.5,
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