<template>
    <div>
        <div id='file-upload' class='content-panel'
            v-cloak @drop.prevent='addFile' @dragover.prevent>

            <h2 class='primary--text'>Drag &amp; drop your file</h2>

            <UploadIcon v-if='!files.length'/>
            <v-img v-else
                :src='imageUrl()'
                alt='Your image'
                transition='scale-transition'
                class='shrink image-preview'
                contain/>
        </div>

        <v-btn :disabled='!canSubmit()' v-on:click='$emit("submit", files[0])'
               x-large color='info' class='submit-button' rounded
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
                alert('No more than 1 file!');
            }

            e.dataTransfer.files.forEach(f => {
                if (f.type.match(/image.*/)) {
                    this.files.push(f);
                } else {
                    alert(`${f.name} is not an image!`);
                }
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
    min-height: 60vh;
}

</style>
