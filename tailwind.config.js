/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./*.html",
    "./blog/*.html",
    "./blog_posts.py",
    "./generate_blog.py",
    "./assets/js/**/*.js",
    "./generate_pages.py"
  ],
  theme: {
    extend: {
      colors: {
        brand: '#1E40AF',
        brandDeep: '#1E3A8A',
        brandSoft: '#EFF4FF',
        navy: '#111827',
        navyLight: '#1F2937',
        accent: '#10B981',
        accentDeep: '#047857',
        accentSoft: '#ECFDF5',
        mist: '#F8FAFC',
      },
      fontFamily: {
        sans: ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
        display: ['Manrope', 'Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
};
