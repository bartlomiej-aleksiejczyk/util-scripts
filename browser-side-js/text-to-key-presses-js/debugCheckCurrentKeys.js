(function () {
  const events = [
    "click",
    "dblclick",
    "mouseup",
    "mousedown",
    "keydown",
    "keyup",
    "input",
    "change",
    "submit",
    "focus",
    "blur",
    "mouseenter",
    "mouseleave",
    "mouseover",
    "mouseout",
    "mousemove",
    "touchstart",
    "touchend",
    "touchmove",
    "scroll",
  ];

  function logEvent(e) {
    console.log(`Event: ${e.type}`, e);
  }

  events.forEach((event) => {
    document.addEventListener(event, logEvent, true);
  });

  console.log(
    "Event logging initiated for the following events:",
    events.join(", ")
  );
})();
