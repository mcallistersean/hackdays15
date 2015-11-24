var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    context: __dirname,
    entry: './src/index.js',
    output: {
        path: path.resolve('./build/'),
        filename: "[name].js"
    },
    resolve: {
        extensions: ['', '.js', '.scss']
    },
    module: {
        loaders: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                loader: 'babel-loader',
                query: {
                    cacheDirectory: true,
                    presets: [
                        'react',
                        'es2015'
                    ]
                }
            },
            {
                test: /\.scss$/,
                loaders: ['style', 'css', 'sass']
            }
        ]
    },
    plugins: [
        new BundleTracker({filename: './webpack-stats.json'})
    ],
    sassLoader: {
        includePaths: [path.resolve(__dirname, "node_modules/foundation-sites/scss/")]
    }
};
