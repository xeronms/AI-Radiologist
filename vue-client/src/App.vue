<template>
  <v-app>
    <NavBar/>

    <v-content>
      <v-container>
        <v-row class="text-center">
          <v-col cols="12">
            <router-view/>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import NavBar from './components/NavBar';

export default {
  name: 'App',
  components: {
    NavBar
  },

  data: () => ({
    //
  }),
};
</script>
