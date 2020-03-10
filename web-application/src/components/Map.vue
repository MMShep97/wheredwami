<template>
    <div>
        Hello there
        <b-container>
            <b-row>
                <b-col>
                    <div class="floor-container">
                        <img :src="floorMap"/>
                    </div>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
import floorMap from '../assets/images/floormap.png'
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