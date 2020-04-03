<template>
  <div class="home">
    <v-row class="text-center">
      <v-col cols="12">
        <AnalysisSummary v-if='analysisInProgress' :file='file'/>
        <FileUpload v-else v-on:submit='fileSubmitted'/>
      </v-col>
    </v-row>
  </div>
</template>

<script>
// @ is an alias to /src
import FileUpload from '../components/FileUpload';
import AnalysisSummary from '../components/AnalysisSummary';

export default {
  name: 'Home',
  components: {
    FileUpload,
    AnalysisSummary
  },
  data: function() {
    return {
      analysisInProgress: false,
      file: null
    };
  },
  methods: {
    fileSubmitted: function(f) {
      this.file = f;
      this.analysisInProgress = true;
    }
  }
}
</script>
