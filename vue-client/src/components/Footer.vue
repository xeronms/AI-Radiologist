<template>
  <v-footer color="secondary" padless>
    <v-card flat tile class="mx-auto secondary white--text text-center">

      <v-card-text class="white--text">
        This application does not provide medical advice It is intended for informational purposes only. It is not a substitute for professional medical advice, diagnosis or treatment.
      </v-card-text>

      <v-divider></v-divider>

      <v-card-text class="white--text">
        {{ new Date().getFullYear() }} — <strong>AI-Radiologist</strong>
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<script>
    export default {
        name: 'NavBar'
    }
</script>

