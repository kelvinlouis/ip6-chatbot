export function randomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

export function secondsByLength(text) {
  return (text.length >> 2 >> 2) * 1000;
}
