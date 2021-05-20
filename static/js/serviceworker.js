const staticLegitKash = 'legit-kash-v1';
const assets = [
    "{% url 'home' %}",
    "{% url 'vendors' %}",
    "{% url 'disclaimer' %}",
    "{% url 'package' %}",
    "{% url 'testimonies' %}",
    "{% url 'testimony_form' %}",
    "{% url 'about-us' %}",
    "{% url 'advertise' %}",

]
self.addEventListener('install', installEvent => {
    installEvent.waitUntil(
        caches.open(staticLegitKash).then(cache => {
            cache.addAll(assets)
        })
    )
    }
    event.respondWith(
        caches.match(event.request).then(function(response){
            return response || fetch(event.request);
        })
    );
});