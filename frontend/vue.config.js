module.exports = {
  devServer: {
    proxy: {
      '/foo': {

        target: 'http://localhost:5000',
        changeOrigin: true
      }
    }
  },
  transpileDependencies: [
    'vuetify'
  ],
}