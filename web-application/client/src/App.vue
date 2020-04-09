<template>
  <div id="app">
    <Map />
  </div>
</template>

<script>
import Map from './components/MapYellowHouse'
export default {
  components: {
    Map,
  }
}
</script>

<style>
:root {
    --static: blue;
    --dynamic: red;
    --same: yellow;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}


#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
