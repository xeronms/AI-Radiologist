<template>
    <div>
        <div id='file-upload' v-cloak @drop.prevent='addFile' @dragover.prevent>
            <h2>Drag &amp; drop your file</h2>

            <UploadIcon v-if='!files.length'/>
            <v-img v-else
                :src='imageUrl()'
                alt='Your image'
                transition="scale-transition"
                contain/>
        </div>

        <v-btn :disabled='!canSubmit()' v-on:click='$emit("submit", files[0])'
               x-large color='primary' class='submit-button' rounded
            >Submit</v-btn>
    </div>
</template>

<script>
import UploadIcon from './UploadIcon';

export default {
    name: 'FileUpload',
    components: {
        UploadIcon
    },
    data: function() {
        return {
            files: []
        }
    },
    methods: {
        addFile: function(e) {
            if (this.files.length > 0) {
                this.files.length = 0;
            }

            if (e.dataTransfer.files.length > 1) {
                alert('Not more than 1 file!');
            }

            e.dataTransfer.files.forEach(element => {
                this.files.push(element);
            });
        },
        imageUrl: function() {
            return URL.createObjectURL(this.files[0]);
        },
        canSubmit: function() {
            return this.files.length > 0 && !!this.files[0];
        }
    }
}
</script>

<style scoped>

#file-upload {
    border-radius: 2em;
    border: solid 3px navy;
    box-shadow: 2px 2px 2px 1px #aaa;

    position: relative;
    padding: 5px;
    min-height: 60vh;
}

.submit-button {
    margin: 1em auto;
}

</style>
