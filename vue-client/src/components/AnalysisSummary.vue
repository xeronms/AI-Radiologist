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

    <img id="canvas-holder" style='position:absolute; visibility: hidden'/>
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
            scoreMessage: '?',
            canvas: null,
            ctx: null,
            imageData: null
        };
    },
    mounted: function() {
        this.canvas = document.createElement('canvas');
        this.ctx = this.canvas.getContext('2d');

        this.assertFileReader();
        this.processFile(this.file);
    },
    methods: {
        computeScore: function() {
            // Use imageData.
            console.dir(this.imageData);

            // Get and display score.
            const score = Math.random();
            this.scoreMessage = `${Math.round(score * 100)}`;
        },
        imageUrl: function() {
            return URL.createObjectURL(this.file);
        },
        processFile: function(file) {
            var fr = new FileReader();
            fr.onload = () => this.showImage(fr);
            fr.readAsDataURL(file);
        },
        showImage: function(fileReader) {
            var img = document.getElementById('canvas-holder');
            img.onload = () => this.getImageData(img);
            img.src = fileReader.result;
        },
        getImageData: function(img) {
            this.ctx.drawImage(img, 0, 0);
            this.imageData = this.ctx.getImageData(0, 0, img.width, img.height).data;
            this.computeScore();
        },
        assertFileReader: function() {
            if (!FileReader) throw 'FileReader not supported';
        }
    }
}
</script>

