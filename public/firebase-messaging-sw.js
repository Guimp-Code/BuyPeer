importScripts('https://www.gstatic.com/firebasejs/8.10.1/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/8.10.1/firebase-messaging.js');
let config = {
        apiKey: "",
        authDomain: "",
        projectId: "",
        storageBucket: "",
        messagingSenderId: "",
        appId: "",
        measurementId: "",
 };
// NOTA: Este arquivo é regenerado automaticamente quando as credenciais
// Firebase são configuradas no painel admin (Notificações > FCM).
// Não insira credenciais manualmente aqui.
if (config.apiKey && config.projectId) {
    firebase.initializeApp(config);
    const messaging = firebase.messaging();
    messaging.onBackgroundMessage((payload) => {
        const notificationTitle = payload.notification.title;
        const notificationOptions = {
            body: payload.notification.body,
            icon: '/images/required/firebase-logo.png'
        };
        self.registration.showNotification(notificationTitle, notificationOptions);
    });
}
