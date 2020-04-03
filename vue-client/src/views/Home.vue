<template>
  <div class="home">
    <v-row class="mb-6">
      <v-col cols="12">
        <FileUpload v-on:submit='fileSubmitted'/>
      </v-col>
    </v-row>
  </div>
</template>

<script>
// @ is an alias to /src
import FileUpload from '../components/FileUpload';

export default {
  name: 'Home',
  components: {
    FileUpload
  },
  methods: {
    fileSubmitted: function(e) {
      e.text().then(x => { console.dir(x); });
    }
  }
}
</script>
