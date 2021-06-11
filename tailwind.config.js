module.exports = {
  purge: [
    './public/**/*.html',
    './src/**/*.vue'
  ],
  theme: {
    screens: {
      sm: {
        min: '641px'
      },
      md: {
        min: '769px'
      },
      lg: {
        min: '1025px'
      },
      xl: {
        min: '1281px'
      },
      '2xl': {
        min: '1537px'
      }
    },
    extend: {
      padding: {
        full: '100%'
      },
      width: {
        128: '32rem'
      },
      minHeight: {
        main: '70vh',
        navbar: '5vh'
      }
    }
  },
  variants: {},
  plugins: [
    require('@tailwindcss/forms')

  ]
}
