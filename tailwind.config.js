module.exports = {
  purge: [
    './public/**/*.html',
    './src/**/*.vue'
  ],
  theme: {
    extend: {
      padding: {
        full: '100%'
      },
      width: {
        full: '100%'
      },
      height: {
        full: '100%'
      }
    }
  },
  variants: {},
  plugins: [
    require('@tailwindcss/forms')

  ]
}
