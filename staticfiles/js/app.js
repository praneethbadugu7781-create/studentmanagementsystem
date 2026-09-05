/**
 * STUDENT MANAGEMENT SYSTEM - JAVASCRIPT MICRO-INTERACTIONS
 * Lineysha and Thevan Software Technologies, Vijayawada
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Initialize Bootstrap Tooltips if bootstrap is available
    if (typeof bootstrap !== 'undefined' && bootstrap.Tooltip) {
        const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        tooltipTriggerList.map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
    }

    // 2. Count-Up Animation for Numerical Statistic Cards
    const statCounters = document.querySelectorAll('.stat-count-up');
    statCounters.forEach(counter => {
        const target = parseInt(counter.getAttribute('data-target'), 10);
        if (isNaN(target)) return;

        const duration = 900; // ms
        const startTime = performance.now();

        const updateCount = (currentTime) => {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            // Ease out cubic
            const easeOut = 1 - Math.pow(1 - progress, 3);
            const currentVal = Math.floor(easeOut * target);

            counter.textContent = currentVal.toLocaleString();

            if (progress < 1) {
                requestAnimationFrame(updateCount);
            } else {
                counter.textContent = target.toLocaleString();
            }
        };

        requestAnimationFrame(updateCount);
    });

    // 3. Auto-Dismiss Toast Notifications
    const toasts = document.querySelectorAll('.custom-toast');
    toasts.forEach(toast => {
        // Auto close after 4.5 seconds
        const timer = setTimeout(() => {
            closeToast(toast);
        }, 4500);

        const closeBtn = toast.querySelector('.toast-close-btn');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                clearTimeout(timer);
                closeToast(toast);
            });
        }
    });

    function closeToast(toastElement) {
        toastElement.style.transition = 'all 0.3s ease-in';
        toastElement.style.opacity = '0';
        toastElement.style.transform = 'translateX(100%)';
        setTimeout(() => {
            toastElement.remove();
        }, 300);
    }

    // 4. Universal Delete Student Modal Logic
    const deleteModal = document.getElementById('deleteModal');
    if (deleteModal) {
        deleteModal.addEventListener('show.bs.modal', (event) => {
            const button = event.relatedTarget;
            if (!button) return;

            const studentId = button.getAttribute('data-student-id');
            const studentName = button.getAttribute('data-student-name');
            const deleteForm = deleteModal.querySelector('#deleteStudentForm');
            const studentNameSpan = deleteModal.querySelector('#deleteStudentName');

            if (studentId && deleteForm) {
                deleteForm.action = `/students/${studentId}/delete/`;
            }
            if (studentNameSpan) {
                studentNameSpan.textContent = studentName || 'this student';
            }
        });
    }

    // 5. Mobile Sidebar Toggle & Overlay
    const sidebarToggleBtn = document.getElementById('sidebarToggleBtn');
    const sidebar = document.getElementById('appSidebar');
    const mobileOverlay = document.getElementById('mobileOverlay');

    if (sidebarToggleBtn && sidebar && mobileOverlay) {
        const toggleSidebar = () => {
            sidebar.classList.toggle('show');
            mobileOverlay.classList.toggle('show');
        };

        sidebarToggleBtn.addEventListener('click', toggleSidebar);
        mobileOverlay.addEventListener('click', toggleSidebar);
    }

    // 6. Search Clear Button Functionality
    const searchInput = document.getElementById('studentSearchInput');
    const searchClearBtn = document.getElementById('searchClearBtn');

    if (searchInput && searchClearBtn) {
        searchClearBtn.addEventListener('click', () => {
            searchInput.value = '';
            // If current URL has a query, redirect to base student list
            if (window.location.search.includes('q=')) {
                window.location.href = window.location.pathname;
            } else {
                searchInput.focus();
            }
        });
    }
});
