var path = require('path');
var webpack = require('webpack');
module.exports = {
    context: __dirname,
    entry: './assets/js/character',
    output: {
        path: path.resolve('./static/src'),
        filename: 'character.js'
    },

 module: {
    loaders: [
      {
        test: /\.jsx?$/,
        loader: 'babel-loader',
        exclude: /node_modules/,
        query: {
          presets: ['es2015', 'react']
        }
      }
    ]
  },


  resolve: {
        modules: ['node_modules', 'bower_components'],
        extensions: ['.js', '.jsx']
    }
};