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
      <h2>{{ scoreDescription }}</h2>

      <v-btn v-on:click='$emit("restart")'
             color='primary' rounded>
        Try with another picture
      </v-btn>
    </v-flex>

<<<<<<< Updated upstream
    <img id='canvas-holder'/>
=======
    <img id="canvas-holder" style='position:absolute; visibility: hidden'/>
>>>>>>> Stashed changes
  </v-layout> 
</template>

<script>
import * as tf from '@tensorflow/tfjs';

export default {
    name: 'AnalysisSummary',
    props: {
        file: File,
    },
    data: function() {
        return {
            scoreMessage: '?',
            scoreDescription: 'It most likely is COVID-19',
            canvas: null,
            ctx: null,
            imageData: null,
        };
    },
    mounted: function() {
        this.canvas = document.createElement('canvas');
        this.ctx = this.canvas.getContext('2d');

        this.assertFileReader();
        this.processFile(this.file);
    },
    methods: {
        computeScore: async function() {
            // Use imageData.
            console.dir(this.imageData);

            // var rgb = [[]];
            // for (var i=0; i < this.imageData.lenght; i+4){
            //     rgb.push([this.imageData[i],
            //                 this.imageData[i+1],
            //                 this.imageData[i+2]]);
            // }

            const MODEL_PATH ='http://localhost:8080/model/model.json'

            console.log('Loading model...');
            let model = await tf.loadLayersModel(MODEL_PATH);

            const imageTensor3d = tf.browser
                                    .fromPixels(this.imageData, 3)
                                    .resizeBilinear([224, 224])
                                    .cast('float32')
                                    .div(tf.scalar(255));
            const imageTensor4d = tf.tensor4d(Array.from(imageTensor3d.dataSync()),[1,224,224,3]);

            console.dir(imageTensor3d);
            console.dir(imageTensor4d);

            const prediction = model.predict(imageTensor4d, {batch_size: 1});
            
            console.log("prediction.print()");
            prediction.print();
            console.log("tostring: \n"+prediction.toString());
            console.log("argMax():");
            prediction.argMax().print();

            // Get and display score.
            const score = prediction.argMax().dataSync()[0];
            console.log(score);
            this.scoreMessage = `${Math.round(score * 100)}`;
        },
        getScoreDescription(score) {
            if (score < 0.4)  return 'It probably isn\'t COVID-19-related.';
            if (score < 0.6)  return 'Hard to say...';
            if (score < 0.9)  return 'It might is COVID-19. Seek medical attention.';
            else return 'COVID-19 is likely. Seek medical attention.';
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
            this.imageData = this.ctx.getImageData(0, 0, img.width, img.height);
            this.computeScore();
        },
        assertFileReader: function() {
            if (!FileReader) throw 'FileReader not supported';
        },
        loadModel: async function() {
             const MODEL_PATH ='http://localhost:8080/model/model.json'

            console.log('Loading model...');
            let model = await tf.loadLayersModel(MODEL_PATH);
            return model
        }
    }
}
</script>


<style scoped>
#canvas-holder {
    position: fixed;
    visibility: hidden;
}
</style>
