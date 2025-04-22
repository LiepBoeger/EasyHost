document.addEventListener("DOMContentLoaded", () => {
    const togglePassword = document.getElementById("togglePassword")
    const password = document.getElementById("senha")
    const toggleConfirmPassword = document.getElementById("toggleConfirmPassword")
    const confirmPassword = document.getElementById("confirma_senha")
  
    function togglePasswordVisibility(passwordField, toggleButton) {
      const type = passwordField.getAttribute("type") === "password" ? "text" : "password"
      passwordField.setAttribute("type", type)
  
      const eyeIcon = toggleButton.querySelector("svg")
  
      if (type === "password") {
        eyeIcon.innerHTML = `
                  <path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"></path>
                  <circle cx="12" cy="12" r="3"></circle>
              `
      } else {
        eyeIcon.innerHTML = `
                  <path d="M9.88 9.88a3 3 0 1 0 4.24 4.24"></path>
                  <path d="M10.73 5.08A10.43 10.43 0 0 1 12 5c7 0 10 7 10 7a13.16 13.16 0 0 1-1.67 2.68"></path>
                  <path d="M6.61 6.61A13.526 13.526 0 0 0 2 12s3 7 10 7a9.74 9.74 0 0 0 5.39-1.61"></path>
                  <line x1="2" x2="22" y1="2" y2="22"></line>
              `
      }
    }
  
    togglePassword.addEventListener("click", () => {
      togglePasswordVisibility(password, togglePassword)
    })
  
    toggleConfirmPassword.addEventListener("click", () => {
      togglePasswordVisibility(confirmPassword, toggleConfirmPassword)
    })
  
    const form = document.querySelector("form")
  
    form.addEventListener("submit", (e) => {
      if (password.value !== confirmPassword.value) {
        e.preventDefault()
        alert("As senhas não coincidem. Por favor, verifique.")
      }
    })

    confirmPassword.addEventListener("input", () => {
      if (password.value && confirmPassword.value) {
        if (password.value !== confirmPassword.value) {
          confirmPassword.style.borderColor = "#e53e3e"
        } else {
          confirmPassword.style.borderColor = "#10b981"
        }
      }
    })
  
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
  