document.addEventListener("DOMContentLoaded", () => {
    const togglePassword = document.getElementById("togglePassword")
    const password = document.getElementById("senha")
  
    togglePassword.addEventListener("click", () => {
      // Alternar o tipo do input entre 'password' e 'text'
      const type = password.getAttribute("type") === "password" ? "text" : "password"
      password.setAttribute("type", type)
  
      // Alternar o ícone entre 'eye' e 'eye-off'
      const eyeIcon = togglePassword.querySelector(".eye-icon")
  
      if (type === "password") {
        // Mostrar ícone de olho normal
        eyeIcon.innerHTML = `
                  <path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"></path>
                  <circle cx="12" cy="12" r="3"></circle>
              `
      } else {
        // Mostrar ícone de olho cortado
        eyeIcon.innerHTML = `
                  <path d="M9.88 9.88a3 3 0 1 0 4.24 4.24"></path>
                  <path d="M10.73 5.08A10.43 10.43 0 0 1 12 5c7 0 10 7 10 7a13.16 13.16 0 0 1-1.67 2.68"></path>
                  <path d="M6.61 6.61A13.526 13.526 0 0 0 2 12s3 7 10 7a9.74 9.74 0 0 0 5.39-1.61"></path>
                  <line x1="2" x2="22" y1="2" y2="22"></line>
              `
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
  