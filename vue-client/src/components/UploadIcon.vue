<template>
    <span class="mdi mdi-upload upload-icon"></span>
</template>

<script>
export default {
    name: 'UploadIcon'
}
</script>

<style scoped>
    .upload-icon {
        font-size: 8em;
        position: absolute;
        margin: auto;
        left: 0;
        right: 0;
        bottom: 25%;

        animation: moveUpAndDown 2.5s ease infinite;
    }

    @keyframes moveUpAndDown {
        0%, 100% {
            bottom: 25%;
        }
        50% {
            bottom: 50%;
        }
    }

</style>
