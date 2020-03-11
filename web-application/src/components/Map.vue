<template>
    <div>
        Hello there
        <b-container>
            <b-row>
                <b-col>
                    <div class="floor-container">
                        <img :src="floorMap" width="1000px"/>
                    </div>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
import floorMap from '../assets/images/floormap.svg'
import '../scripts/js/map'
export default {
    data() {
        return {
            floorMap: floorMap,
        }
    }
}
</script>

<style scoped>
.floor-container {
    margin-left: auto;
    margin-right: auto;
}

</style>