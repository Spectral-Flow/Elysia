// DOM Elements
const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');
const chatMessages = document.getElementById('chatMessages');
const maintenanceModal = document.getElementById('maintenanceModal');
const maintenanceForm = document.getElementById('maintenanceForm');
const infoPanel = document.getElementById('infoPanel');

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    setupEventListeners();
    updateMessageTimes();
    setInterval(updateMessageTimes, 60000); // Update times every minute
});

// Event Listeners
function setupEventListeners() {
    // Chat functionality
    sendButton.addEventListener('click', sendMessage);
    messageInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    // Maintenance form
    maintenanceForm.addEventListener('submit', submitMaintenanceRequest);

    // Close modals when clicking outside
    window.addEventListener('click', function(event) {
        if (event.target === maintenanceModal) {
            closeMaintenanceModal();
        }
        if (event.target === infoPanel) {
            closeInfoPanel();
        }
    });
}

// Chat Functions
async function sendMessage() {
    const message = messageInput.value.trim();
    if (!message) return;

    // Add user message to chat
    addMessage(message, 'user');
    messageInput.value = '';

    // Show typing indicator
    const typingIndicator = addTypingIndicator();

    try {
        // Send message to backend
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        });

        const data = await response.json();

        // Remove typing indicator
        typingIndicator.remove();

        if (response.ok) {
            // Add bot response to chat
            addMessage(data.response, 'bot');
        } else {
            addMessage('Sorry, I encountered an error. Please try again.', 'bot');
        }
    } catch (error) {
        console.error('Error:', error);
        typingIndicator.remove();
        addMessage('Sorry, I\'m having trouble connecting. Please check your internet connection and try again.', 'bot');
    }
}

function addMessage(content, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;
    
    const messageContent = document.createElement('div');
    messageContent.className = 'message-content';
    messageContent.textContent = content;
    
    const messageTime = document.createElement('div');
    messageTime.className = 'message-time';
    messageTime.textContent = getCurrentTime();
    
    messageDiv.appendChild(messageContent);
    messageDiv.appendChild(messageTime);
    
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
    
    return messageDiv;
}

function addTypingIndicator() {
    const typingDiv = document.createElement('div');
    typingDiv.className = 'message bot-message typing-indicator';
    
    const messageContent = document.createElement('div');
    messageContent.className = 'message-content';
    messageContent.innerHTML = '<div class="loading"></div> Elysia is typing...';
    
    typingDiv.appendChild(messageContent);
    chatMessages.appendChild(typingDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
    
    return typingDiv;
}

function getCurrentTime() {
    const now = new Date();
    return now.toLocaleTimeString('en-US', { 
        hour: '2-digit', 
        minute: '2-digit' 
    });
}

function updateMessageTimes() {
    const messageTimes = document.querySelectorAll('.message-time');
    const currentTime = getCurrentTime();
    
    messageTimes.forEach((timeElement, index) => {
        if (index === 0) return; // Skip the initial welcome message
        
        const messageTime = timeElement.textContent;
        if (!messageTime || messageTime.includes('typing')) {
            timeElement.textContent = currentTime;
        }
    });
}

// Quick Actions
function askQuickQuestion(question) {
    messageInput.value = question;
    sendMessage();
}

// Maintenance Modal Functions
function openMaintenanceModal() {
    maintenanceModal.style.display = 'block';
    document.body.style.overflow = 'hidden';
}

function closeMaintenanceModal() {
    maintenanceModal.style.display = 'none';
    document.body.style.overflow = 'auto';
    maintenanceForm.reset();
}

async function submitMaintenanceRequest(e) {
    e.preventDefault();
    
    const formData = new FormData(maintenanceForm);
    const requestData = {
        unit: formData.get('unit'),
        issue: formData.get('issue'),
        description: formData.get('description'),
        priority: formData.get('priority')
    };

    try {
        const response = await fetch('/api/maintenance', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(requestData)
        });

        const data = await response.json();

        if (response.ok) {
            closeMaintenanceModal();
            addMessage(`✅ Maintenance request submitted successfully! Your request ID is #${data.request_id}. Our maintenance team will be in touch within 24 hours.`, 'bot');
        } else {
            alert('Error submitting maintenance request. Please try again.');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error submitting maintenance request. Please check your connection and try again.');
    }
}

// Information Panel Functions
function showEvents() {
    fetch('/api/events')
        .then(response => response.json())
        .then(data => {
            let content = '<h2>📅 Upcoming Events</h2>';
            
            if (data.events && data.events.length > 0) {
                content += '<div style="margin-top: 20px;">';
                data.events.forEach(event => {
                    content += `
                        <div style="border: 1px solid #ddd; border-radius: 8px; padding: 15px; margin-bottom: 15px;">
                            <h3>${event.title}</h3>
                            <p><strong>📅 Date:</strong> ${event.date}</p>
                            <p><strong>⏰ Time:</strong> ${event.time}</p>
                            <p><strong>📍 Location:</strong> ${event.location}</p>
                            <p><strong>Description:</strong> ${event.description}</p>
                        </div>
                    `;
                });
                content += '</div>';
            } else {
                content += '<p>No upcoming events at this time.</p>';
            }
            
            showInfoPanel(content);
        })
        .catch(error => {
            console.error('Error:', error);
            showInfoPanel('<h2>📅 Events</h2><p>Unable to load events at this time.</p>');
        });
}

function showBuildingInfo() {
    fetch('/api/building-info')
        .then(response => response.json())
        .then(data => {
            let content = `
                <h2>🏢 Building Information</h2>
                <div style="margin-top: 20px;">
                    <h3>📍 Contact Information</h3>
                    <p><strong>Building:</strong> ${data.name}</p>
                    <p><strong>Address:</strong> ${data.address}</p>
                    <p><strong>Contact:</strong> ${data.contact}</p>
                </div>
                
                <div style="margin-top: 25px;">
                    <h3>🏊‍♀️ Amenities</h3>
                    <ul style="margin-left: 20px; margin-top: 10px;">
            `;
            
            data.amenities.forEach(amenity => {
                content += `<li style="margin-bottom: 5px;">${amenity}</li>`;
            });
            
            content += `
                    </ul>
                </div>
                
                <div style="margin-top: 25px;">
                    <h3>📋 Policies</h3>
                    <p><strong>Quiet Hours:</strong> ${data.policies.quiet_hours}</p>
                    <p><strong>Guest Policy:</strong> ${data.policies.guest_policy}</p>
                    <p><strong>Pet Policy:</strong> ${data.policies.pet_policy}</p>
                    <p><strong>Maintenance Hours:</strong> ${data.policies.maintenance_hours}</p>
                </div>
            `;
            
            showInfoPanel(content);
        })
        .catch(error => {
            console.error('Error:', error);
            showInfoPanel('<h2>🏢 Building Information</h2><p>Unable to load building information at this time.</p>');
        });
}

function showInfoPanel(content) {
    document.getElementById('infoPanelContent').innerHTML = content;
    infoPanel.style.display = 'flex';
    document.body.style.overflow = 'hidden';
}

function closeInfoPanel() {
    infoPanel.style.display = 'none';
    document.body.style.overflow = 'auto';
}

// Utility Functions
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
}

// Initialize chat with welcome message time
window.addEventListener('load', function() {
    const welcomeMessage = document.querySelector('.bot-message .message-time');
    if (welcomeMessage) {
        welcomeMessage.textContent = getCurrentTime();
    }
});