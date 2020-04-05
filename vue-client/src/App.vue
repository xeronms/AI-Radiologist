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

    <Footer/>
  </v-app>
</template>

<script>
import NavBar from './components/NavBar';
import Footer from './components/Footer';

export default {
  name: 'App',
  components: {
    NavBar,
    Footer
  },

  data: () => ({
    //
  }),
};
</script>
