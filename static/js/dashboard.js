// Dashboard specific functionality

document.addEventListener('DOMContentLoaded', function() {
    initDashboard();
});

function initDashboard() {
    // Load dashboard stats
    loadDashboardStats();
    
    // Initialize charts if needed
    initCharts();
    
    // Set up auto-refresh for real-time data
    setInterval(loadDashboardStats, 30000); // Refresh every 30 seconds
}

async function loadDashboardStats() {
    try {
        // Simulate API call to get dashboard data
        const response = await HealthApp.simulateApiCall({
            patients: 1247,
            appointments: 23,
            doctors: 15,
            lowStock: 7,
            recentAppointments: [
                {
                    patient: 'John Smith',
                    doctor: 'Dr. Sarah Johnson',
                    datetime: new Date().toISOString(),
                    status: 'confirmed'
                },
                {
                    patient: 'Maria Garcia',
                    doctor: 'Dr. Michael Chen',
                    datetime: new Date().toISOString(),
                    status: 'pending'
                },
                {
                    patient: 'Robert Wilson',
                    doctor: 'Dr. Emily Brown',
                    datetime: new Date(Date.now() + 86400000).toISOString(),
                    status: 'confirmed'
                }
            ]
        });
        
        updateDashboardUI(response.data);
    } catch (error) {
        console.error('Error loading dashboard stats:', error);
        HealthApp.showNotification('Error loading dashboard data', 'danger');
    }
}

function updateDashboardUI(data) {
    // Update stats cards
    document.querySelector('.dashboard-card:nth-child(1) .number').textContent = data.patients.toLocaleString();
    document.querySelector('.dashboard-card:nth-child(2) .number').textContent = data.appointments;
    document.querySelector('.dashboard-card:nth-child(3) .number').textContent = data.doctors;
    document.querySelector('.dashboard-card:nth-child(4) .number').textContent = data.lowStock;
    
    // Update recent appointments table
    updateAppointmentsTable(data.recentAppointments);
}

function updateAppointmentsTable(appointments) {
    const tbody = document.querySelector('.table tbody');
    if (!tbody) return;
    
    tbody.innerHTML = appointments.map(appointment => `
        <tr>
            <td>${appointment.patient}</td>
            <td>${appointment.doctor}</td>
            <td>${HealthApp.formatDate(appointment.datetime)}</td>
            <td>
                <span class="badge badge-${appointment.status === 'confirmed' ? 'primary' : 'warning'}">
                    ${appointment.status.charAt(0).toUpperCase() + appointment.status.slice(1)}
                </span>
            </td>
        </tr>
    `).join('');
}

function initCharts() {
    // Initialize any charts here
    // This is a placeholder for chart initialization
    console.log('Charts initialized');
}

// Export dashboard functions
window.Dashboard = {
    loadDashboardStats,
    updateDashboardUI
};