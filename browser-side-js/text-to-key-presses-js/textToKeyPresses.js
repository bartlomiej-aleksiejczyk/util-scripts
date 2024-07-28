function simulateTypingOnCanvas(canvasSelector, text) {
  const canvas = document.querySelector(canvasSelector);
  if (!canvas) {
    console.error("Canvas not found!");
    return;
  }

  const keyMap = {
    a: 65,
    b: 66,
    c: 67,
    d: 68,
    e: 69,
    f: 70,
    g: 71,
    h: 72,
    i: 73,
    j: 74,
    k: 75,
    l: 76,
    m: 77,
    n: 78,
    o: 79,
    p: 80,
    q: 81,
    r: 82,
    s: 83,
    t: 84,
    u: 85,
    v: 86,
    w: 87,
    x: 88,
    y: 89,
    z: 90,
    0: 48,
    1: 49,
    2: 50,
    3: 51,
    4: 52,
    5: 53,
    6: 54,
    7: 55,
    8: 56,
    9: 57,
    "`": 192,
    "-": 173,
    "=": 61,
    "[": 219,
    "]": 221,
    "\\": 220,
    ";": 59,
    "'": 222,
    ",": 188,
    ".": 190,
    "/": 191,
    " ": 32,
  };

  const specialNonShiftChars = [
    "`",
    "-",
    "=",
    "[",
    "]",
    "\\",
    ";",
    "'",
    ",",
    ".",
    "/",
  ];

  const shiftChars = {
    "~": "`",
    "!": "1",
    "@": "2",
    "#": "3",
    $: "4",
    "%": "5",
    "^": "6",
    "&": "7",
    "*": "8",
    "(": "9",
    ")": "0",
    _: "-",
    "+": "=",
    "{": "[",
    "}": "]",
    "|": "\\",
    ":": ";",
    '"': "'",
    "<": ",",
    ">": ".",
    "?": "/",
  };

  function simulateKeyEvent(eventType, keyChar, isShiftNeeded, delay) {
    const keyCode =
      keyMap[keyChar.toLowerCase()] || keyMap[shiftChars[keyChar]];
    if (!keyCode) {
      console.error(`No map for '${keyChar}' (${keyChar.charCodeAt(0)})`);
      return;
    }
    const event = new KeyboardEvent(eventType, {
      key: keyChar,
      keyCode: keyCode,
      code: `Key${keyChar.toUpperCase()}`,
      shiftKey: isShiftNeeded,
      bubbles: true,
      cancelable: true,
      composed: true,
      view: window,
    });
    setTimeout(() => canvas.dispatchEvent(event), delay);
  }

  function simulateShiftKey(eventType, delay) {
    const event = new KeyboardEvent(eventType, {
      key: "Shift",
      keyCode: 16,
      code: "ShiftLeft",
      shiftKey: true,
      bubbles: true,
      cancelable: true,
      composed: true,
      view: window,
    });
    setTimeout(() => canvas.dispatchEvent(event), delay);
  }

  let delay = 0;
  for (let char of text) {
    console.log(char);
    const isShiftNeeded =
      (char === char.toUpperCase() &&
        isNaN(char) &&
        !specialNonShiftChars.find((element) => element === char)) ||
      shiftChars.hasOwnProperty(char);
    console.log(
      char,
      char === char.toUpperCase(),
      isNaN(char),
      shiftChars.hasOwnProperty(char)
    );
    if (isShiftNeeded) simulateShiftKey("keydown", delay);
    simulateKeyEvent(
      "keydown",
      char,
      isShiftNeeded,
      delay + (isShiftNeeded ? 5 : 0)
    );

    simulateKeyEvent(
      "keyup",
      char,
      isShiftNeeded,
      delay + 5 + (isShiftNeeded ? 5 : 0)
    );
    delay += 100;
  }
}

simulateTypingOnCanvas("#spice_surface_0", "Hello, World! @2023");
