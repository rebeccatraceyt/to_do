document.addEventListener("DOMContentLoaded", function () {

    // ARCHIVE TASKS
    const archiveCheckboxes = document.querySelectorAll('.archive-checkbox');

    archiveCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', (e) => {
            const taskId = e.target.dataset.taskId;
            const isArchived = e.target.checked;

            // Update task archive status in the backend
            updateTaskArchiveStatus(taskId, isArchived);
        });
    });

    function updateTaskArchiveStatus(taskId, isArchived) {
        fetch(`/update_task_archive/${taskId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')  // Pass the CSRF token for security
            },
            body: JSON.stringify({ archive: isArchived })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                location.reload();
                console.log('Task archive status updated successfully');
            } else {
                console.error('Failed to update task archive status');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }

    // Function to get CSRF token for AJAX
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // UNARCHIVE TASKS
    const unarchiveButtons = document.querySelectorAll('.unarchive-checkbox');

    unarchiveButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            const taskId = e.target.dataset.taskId;

            // Send AJAX request to unarchive task
            unarchiveTask(taskId);
        });
    });

    function unarchiveTask(taskId) {
        fetch(`/unarchive_task/${taskId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')  // Pass the CSRF token for security
            },
            body: JSON.stringify({ archive: false })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log('Task unarchived successfully');
                // Optionally, remove the task from the archived tasks list or reload the page
                location.reload();  // Refresh the page to update the task list
            } else {
                console.error('Failed to unarchive task');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }

    // Function to get CSRF token for AJAX
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
});
