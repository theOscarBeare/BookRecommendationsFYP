const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const HTMLWebpackPlugin = require('html-webpack-plugin');

module.exports = {

    mode: 'development',

  context: __dirname,

  entry: {
    app: './frontend/static/ReactFrontend/main.js',
  },


  output: {
    path: './frontend/static/ReactFrontend/src/components/bundles/',
    filename: 'bundle.js',
  },

  plugins: [

        //tells webpack where to store data about your bundles.
      new BundleTracker({
          path: __dirname,
          filename: './webpack-stats.json'
      }),



      new HTMLWebpackPlugin ({
        title: 'Book Recommendations',
      }),


      //makes jQuery available in every module
      new webpack.ProvidePlugin({
          $: 'jquery',
          jQuery: 'jquery',
          'window.jQuery': 'jquery'
        })
    ],

  module: {

    rules: [

      {
        test: /\.css$/,
        exclude: /node_modules/,
        use: {
          loader: 'css-loader'
        }
      },

      {
        test: /\.jsx$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      },

      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      }
    ]
  },
};
