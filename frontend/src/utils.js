/**
 * Enter key for events
 * @type {number}
 */
const KEY_CODE_ENTER = 13;

export function randomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

export function secondsByLength(text) {
  return (text.length >> 2 >> 2) * 1000;
}

/**
 * Checks whether the enter key was pressed without using shift.
 * @param event
 * @returns {boolean}
 */
export function isJustEnterKey(event) {
  return event.keyCode === KEY_CODE_ENTER && !event.shiftKey;
}
