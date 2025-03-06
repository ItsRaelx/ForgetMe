/**
 * ForgetMe - Main JavaScript
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize any components that need JavaScript
    initTooltips();
    initCurrentYear();
    initImageFallbacks();
    
    // Add smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});

/**
 * Initialize tooltip functionality for elements with data-tooltip attribute
 */
function initTooltips() {
    const tooltipElements = document.querySelectorAll('[title]');
    
    tooltipElements.forEach(element => {
        element.addEventListener('mouseenter', function() {
            // You could implement custom tooltip behavior here
            // For now, we'll rely on the browser's native tooltip
        });
    });
}

/**
 * Set the current year in the footer
 */
function initCurrentYear() {
    const yearElements = document.querySelectorAll('.current-year');
    const currentYear = new Date().getFullYear();
    
    yearElements.forEach(element => {
        element.textContent = currentYear;
    });
}

/**
 * Initialize fallback images for domain icons
 */
function initImageFallbacks() {
    // Add a global error handler for all domain icons
    document.querySelectorAll('.domain-icon img').forEach(img => {
        img.onerror = function() {
            this.src = '/static/img/default-icon.png';
            // If the default icon also fails to load, use a generic icon with CSS
            this.onerror = function() {
                this.style.display = 'none';
                // Add a generic icon using fontawesome
                const icon = document.createElement('i');
                icon.className = 'fas fa-globe';
                icon.style.fontSize = '24px';
                icon.style.color = '#adb5bd';
                this.parentNode.appendChild(icon);
            };
        };
    });
}

/**
 * Toggle mobile navigation menu (for future responsive enhancement)
 */
function toggleMobileMenu() {
    const navMenu = document.querySelector('nav ul');
    if (navMenu) {
        navMenu.classList.toggle('show');
    }
} 