import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import colors from 'vuetify/lib/util/colors';

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        dark: true,
        themes: {
          dark: {
            primary: '#932026', //red
            secondary: '#393939', //dark-gray
            accent: colors.shades.white,
            error: colors.red.accent3,
          },
        },
      },
});
