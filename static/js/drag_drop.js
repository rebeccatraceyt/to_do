document.addEventListener("DOMContentLoaded", function () {
    const tasks = document.querySelectorAll('.task-box');
    const columns = document.querySelectorAll('.column');

    tasks.forEach(task => {
        task.addEventListener('dragstart', (e) => {
            e.dataTransfer.setData('taskId', e.target.dataset.taskId);
            console.log("Drag started for task:", e.target.dataset.taskId);  // Debugging
        });
    });

    columns.forEach(column => {
        column.addEventListener('dragover', (e) => {
            e.preventDefault();  // Allow dropping
            column.classList.add('dragging-over');
        });

        column.addEventListener('dragleave', () => {
            column.classList.remove('dragging-over');
        });

        column.addEventListener('drop', (e) => {
            e.preventDefault();
            const taskId = e.dataTransfer.getData('taskId');
            const newStatus = column.dataset.status;

            console.log("Dropped task:", taskId);  // Debugging
            console.log("New status:", newStatus);  // Debugging

            // Find the task element
            const task = document.querySelector(`[data-task-id="${taskId}"]`);

            if (task) {
                // Move the task to the new column in the UI
                column.appendChild(task);
                console.log("Task moved to new column.");  // Debugging

                // Update task status in the backend
                updateTaskStatus(taskId, newStatus);
            } else {
                console.error("Task not found:", taskId);  // Debugging
            }

            column.classList.remove('dragging-over');
        });
    });

    function updateTaskStatus(taskId, newStatus) {
        fetch(`/update_task_status/${taskId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')  // Pass the CSRF token for security
            },
            body: JSON.stringify({ status: newStatus })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log('Task status updated successfully');
            } else {
                console.error('Failed to update task status');
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
