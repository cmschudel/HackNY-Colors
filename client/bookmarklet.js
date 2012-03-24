function foo() { 

  var SEARCH_URL = "http://127.0.0.1:5000/search";

  // Add jQuery - this introduces unncessary overhead, but it's convenient.
  var s = document.createElement('script');
  s.src = 'http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js';
  document.body.appendChild(s);

  // Get colors from the page.
  function getColors() {
    // TODO
    return 'blue,red';
  }

  function sendColors() {
    $.getJSON(SEARCH_URL + "?callback=?", { colors : getColors() }, function(data) {
      console.log('in callback');
      console.log(data);
    });
  }

  // This calls the callback after jQuery has loaded.
  function onJQReady(cb) {
    if (window.$) {
      cb();
    } else {
      setTimeout(function() {
        onJQReady(cb);
      }, 10);
    }
  }

  onJQReady(sendColors);

 }
