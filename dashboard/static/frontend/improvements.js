document.addEventListener("DOMContentLoaded", function() {
    const wrapper = document.querySelector('.wrapper')
  
    let pressed = false
    let startX = 0
  
    wrapper.addEventListener('mousedown', function (e) {
      pressed = true
      startX = e.clientX
      this.style.cursor = 'grabbing'
    })
  
    wrapper.addEventListener('mouseleave', function (e) {
      pressed = false
    })
  
    window.addEventListener('mouseup', function (e) {
      pressed = false
      wrapper.style.cursor = 'grab'
    })
  
    wrapper.addEventListener('mousemove', function (e) {
      if(!pressed) {
        return
      }
  
      this.scrollLeft += startX - e.clientX
    })
  });