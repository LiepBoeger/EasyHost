document.addEventListener("DOMContentLoaded", () => {
    // Toggle sidebar on mobile
    const toggleSidebar = document.getElementById("toggle-sidebar")
    const sidebar = document.querySelector(".sidebar")
  
    if (toggleSidebar && sidebar) {
      toggleSidebar.addEventListener("click", () => {
        sidebar.classList.toggle("active")
      })
    }
  
    // Close sidebar when clicking outside on mobile
    document.addEventListener("click", (event) => {
      const isClickInsideSidebar = sidebar.contains(event.target)
      const isClickOnToggle = toggleSidebar.contains(event.target)
  
      if (!isClickInsideSidebar && !isClickOnToggle && window.innerWidth <= 768 && sidebar.classList.contains("active")) {
        sidebar.classList.remove("active")
      }
    })
  
    // Funcionalidade para fechar mensagens flash
    const closeButtons = document.querySelectorAll(".close-flash")
    closeButtons.forEach((button) => {
      button.addEventListener("click", () => {
        const flashMessage = button.parentElement
        flashMessage.style.opacity = "0"
        flashMessage.style.transform = "translateY(-10px)"
        setTimeout(() => {
          flashMessage.remove()
        }, 300)
      })
    })
  
    // Auto-fechar mensagens flash após 5 segundos
    const flashMessages = document.querySelectorAll(".flash-message")
    flashMessages.forEach((message) => {
      setTimeout(() => {
        if (message) {
          message.style.opacity = "0"
          message.style.transform = "translateY(-10px)"
          setTimeout(() => {
            if (message.parentElement) {
              message.remove()
            }
          }, 300)
        }
      }, 5000)
    })
  })
  