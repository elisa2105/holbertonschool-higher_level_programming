#!/usr/bin/node
exports.converter = function nombre (base) {
  // return(number => number.toString(base));
  function conv (num) {
    const result = num.toString(base);
    return result;
  }
  return (conv);
};
