// hello_world.js
(function () {
  function onReady(fn) {
    // Multiple handlers are supported: just add more onReady(...) calls.
    if (window.jQuery) {
      jQuery(fn); // shorthand for $(document).ready(fn)
      return;
    }

    // Fallback without jQuery
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", fn, { once: true });
    } else {
      fn();
    }
  }

  onReady(function () {
    window.alert("hello-world");
  });
})();
