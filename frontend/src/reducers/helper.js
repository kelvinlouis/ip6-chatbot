// Curried function for cleaner code to update the state
export const patch = state => parts => Object.assign({}, state, parts);
