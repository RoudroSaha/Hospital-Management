// Dashboard specific JavaScript
document.addEventListener('DOMContentLoaded', function() {
    console.log('Dashboard loaded successfully');
    
    // Initialize charts
    initStatsChart();
    
    // Refresh appointments functionality
    const refreshBtn = document.getElementById('refreshAppointments');
    if (refreshBtn) {
        refreshBtn.addEventListener('click', function() {
            const originalHtml = this.innerHTML;
            this.innerHTML = '<span class="loading-spinner"></span> Refreshing...';
            this.disabled = true;
            
            // Simulate API call
            setTimeout(() => {
                this.innerHTML = originalHtml;
                this.disabled = false;
                HMS.showNotification('Appointments refreshed successfully!', 'success');
            }, 1500);
        });
    }
    
    // Quick actions
    const quickActions = document.querySelectorAll('.quick-action');
    quickActions.forEach(action => {
        action.addEventListener('click', function(e) {
            e.preventDefault();
            const actionType = this.getAttribute('data-action');
            HMS.showNotification(`Opening ${actionType} management...`, 'info');
            
            // Simulate navigation delay
            setTimeout(() => {
                // Actual navigation would go here
                console.log(`Navigating to ${actionType} section`);
            }, 1000);
        });
    });
    
    // Real-time date update
    function updateCurrentDate() {
        const now = new Date();
        const options = { year: 'numeric', month: 'long', day: 'numeric' };
        const dateString = now.toLocaleDateString('en-US', options);
        const dateElement = document.getElementById('currentDate');
        if (dateElement) {
            dateElement.textContent = dateString;
        }
    }
    
    // Update date every minute
    setInterval(updateCurrentDate, 60000);
    
    // Add hover effects to table rows
    const tableRows = document.querySelectorAll('#appointmentsTable tbody tr');
    tableRows.forEach(row => {
        row.addEventListener('mouseenter', function() {
            this.style.backgroundColor = '#f8f9fa';
        });
        
        row.addEventListener('mouseleave', function() {
            this.style.backgroundColor = '';
        });
    });
});

function initStatsChart() {
    const ctx = document.getElementById('statsChart').getContext('2d');
    
    // Sample data - in real app, this would come from API
    const data = {
        labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        datasets: [
            {
                label: 'Appointments',
                data: [12, 19, 15, 22, 18, 8, 5],
                borderColor: '#2563eb',
                backgroundColor: 'rgba(37, 99, 235, 0.1)',
                tension: 0.4,
                fill: true
            },
            {
                label: 'Patients',
                data: [8, 12, 10, 15, 14, 6, 3],
                borderColor: '#10b981',
                backgroundColor: 'rgba(16, 185, 129, 0.1)',
                tension: 0.4,
                fill: true
            }
        ]
    };
    
    const config = {
        type: 'line',
        data: data,
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    };
    
    new Chart(ctx, config);
}

// Real-time statistics update (simulated)
function updateStatistics() {
    const stats = ['patients', 'doctors', 'appointments', 'medicines'];
    
    stats.forEach(stat => {
        const element = document.querySelector(`[data-stat="${stat}"] .stat-number`);
        if (element) {
            const currentValue = parseInt(element.textContent.replace(/,/g, ''));
            const newValue = currentValue + Math.floor(Math.random() * 3);
            element.textContent = newValue.toLocaleString();
        }
    });
}

// Update statistics every 30 seconds
setInterval(updateStatistics, 30000);