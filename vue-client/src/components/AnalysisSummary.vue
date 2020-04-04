<template>
    <v-layout row justify-space-around class='content-panel'>
    <v-flex md8>
      <v-img
        contain class="shrink image-preview"
        :src='imageUrl()'
        alt='Your image'>
      </v-img>
    </v-flex>
    <v-flex md4>
      <h1 class='primary--text'>{{scoreMessage}}%</h1>
      <h2>It most likely is COVID-19</h2>

      <p>File name: {{file.name}}</p>
      <p>File size: {{file.size}}B</p>
    </v-flex>
  </v-layout> 
</template>

<script>
export default {
    name: 'AnalysisSummary',
    props: {
        file: File,
    },
    data: function() {
        return {
            scoreMessage: '?'
        };
    },
    mounted: function() {
        const fileScore = this.processFile(this.file);
        this.scoreMessage = `${Math.round(fileScore * 100)}`;
    },
    methods: {
        imageUrl: function() {
            return URL.createObjectURL(this.file);
        },
        processFile: function(file) {
            console.log(file);
            return Math.random();
        }
    }
}
</script>

