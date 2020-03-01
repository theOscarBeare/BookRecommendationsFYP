module.exports = {
  entry:'frontend/static/frontend/index.js',
  module: {
    rules: [
      {test: /\.css$/, use: 'css-loader'},
      {test: /\.jsx$/, use: 'babel-loader'},
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      }
    ]
  }
};