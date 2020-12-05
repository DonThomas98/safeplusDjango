var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/static/css/flexboxgrid.css',
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(
        fetch(event.request)
        .then(function(result){

            return caches.open(CACHE_NAME)
            .then(function(c){


                c.put(event.request.url,result.clone());
                return result;
            })
        })
        .catch(function(e){

            return caches.match(event.request)
        })
    );
});


//solo para cachear todo reemplazar por esta versión del Fetch


self.addEventListener('fetch', function(event) {
    event.respondWith(

      fetch(event.request)
      .then((result)=>{
        return caches.open(CACHE_NAME)
        .then(function(c) {
          c.put(event.request.url, result.clone())
          return result;
        })
        
      })
      .catch(function(e){
          return caches.match(event.request)
      })
  

     
    );
});




//CODIGO NOTIFICACION PUSHU
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var firebaseConfig = {
  apiKey: "AIzaSyASTMlsCxMMW2a72f9FjWrpZxjPkBy8grg",
  authDomain: "safeplus-5e183.firebaseapp.com",
  projectId: "safeplus-5e183",
  storageBucket: "safeplus-5e183.appspot.com",
  messagingSenderId: "763838870066",
  appId: "1:763838870066:web:6fff29d33a5cf267a7422b"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

let messaging= firebase.messaging();

messaging.setBackgroundMessageHandler(function(payload){

  let tittle='Titulo de la notificacionu';

  let options={

    body:'mensaje del body',
    icon:'static/images/safe.jpg'

  }

  self.registration.showNotification(tittle,options)

});