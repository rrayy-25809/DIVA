export default {
    server: {
      proxy: {
        '/api': 'http://localhost:5000', // Flask 서버 주소
      },
    },
  }
  