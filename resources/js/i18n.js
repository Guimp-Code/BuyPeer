import {createI18n} from "vue-i18n";

function loadMessages() {
    const context  = require.context("./languages", true, /[a-z0-9\-_]+\.json$/i);
    const messages = context
        .keys()
        .map((key) => ({key, locale: key.match(/([a-z0-9\-_]+)\.json$/i)[1]}))
        .reduce((messages, {key, locale}) => ({
                ...messages, [locale]: context(key),
            }),
            {}
        );
    return {messages};
}

const {messages} = loadMessages();

const browserLocale = (typeof navigator !== 'undefined' ? navigator.language : 'pt-BR');
const i18n = createI18n({
    legacy: false,
    locale: browserLocale && messages[browserLocale] ? browserLocale : "pt-BR",
    fallbackLocale: "pt-BR",
    messages: messages
});

export default i18n;
