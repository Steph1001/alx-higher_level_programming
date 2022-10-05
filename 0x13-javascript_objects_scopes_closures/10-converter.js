#!/usr/bin/node

exports.converter = function (base) {
  function convertNum (num) {
    return num.toString(base);
  }
  return convertNum;
};
