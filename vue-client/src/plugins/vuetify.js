import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import colors from 'vuetify/lib/util/colors';

const lightColorPalette = {
    primary: colors.indigo.darken2
};

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        themes: {
            light: lightColorPalette
        }
    }
});
