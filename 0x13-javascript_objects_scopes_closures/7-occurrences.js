#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const result = list.filter(number => number === searchElement);
  return result.length;
};
