const { defineConfig } = require('@vue/cli-service')
const AutoImport = require('unplugin-auto-import/webpack')
const Components = require('unplugin-vue-components/webpack')
const { ElementPlusResolver } = require('unplugin-vue-components/resolvers')


module.exports = defineConfig({
 transpileDependencies: true,
 configureWebpack: {
  plugins: [
   AutoImport({
    resolvers: [ElementPlusResolver()]
    }),
   Components({
    resolvers: [ElementPlusResolver()]
    })
   ]
  },
  devServer: {
    port: "8080",
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
        pathRewrite: { '^/api': '' }
      }
    },
    client: {
      webSocketURL: 'ws://127.0.0.1:8080/ws', // 正确配置 WebSocket URL
    },
    allowedHosts: 'all', // 使用 allowedHosts 替代 disableHostCheck
  }

})

