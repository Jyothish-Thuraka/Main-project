document.addEventListener('DOMContentLoaded', function() {
    // Get DOM elements
    const modal = document.getElementById('settingsModal');
    const settingsBtn = document.getElementById('SettingsBtn');
    const closeBtn = document.getElementsByClassName('close')[0];
    const tabBtns = document.querySelectorAll('.tab-btn');
    const websiteForm = document.getElementById('websiteForm');
    const contactForm = document.getElementById('contactForm');

    // Add CSS styles dynamically
    const style = document.createElement('style');
    style.textContent = `
        .modal {
            display: none;
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.7);
            backdrop-filter: blur(5px);
        }

        .modal-content {
            background-color: #1a1a1a;
            color: #fff;
            margin: 5% auto;
            padding: 20px;
            border: 1px solid #888;
            width: 80%;
            max-width: 800px;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
        }

        .close {
            color: #fff;
            float: right;
            font-size: 28px;
            font-weight: bold;
            cursor: pointer;
            transition: color 0.3s;
        }

        .close:hover {
            color: #4CAF50;
        }

        .tab-nav {
            border-bottom: 1px solid #333;
            margin-bottom: 20px;
            display: flex;
            gap: 10px;
        }

        .tab-btn {
            background: none;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            color: #fff;
            opacity: 0.6;
            transition: all 0.3s;
            border-radius: 5px 5px 0 0;
        }

        .tab-btn:hover {
            background-color: #333;
            opacity: 1;
        }

        .tab-btn.active {
            opacity: 1;
            border-bottom: 2px solid #4CAF50;
            background-color: #333;
        }

        .tab-content {
            display: none;
            padding: 20px 0;
        }

        .tab-content.active {
            display: block;
        }

        form {
            margin-bottom: 20px;
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }

        .modal-content input {
            padding: 8px 12px;
            border: 1px solid #333;
            border-radius: 5px;
            background-color: #2a2a2a;
            color: #fff;
            flex: 1;
            min-width: 200px;
        }

        .modal-content input:focus {
            outline: none;
            border-color: #4CAF50;
        }

        .modal-content input::placeholder {
            color: #888;
        }

        .btn-add {
            background-color: #4CAF50;
            color: white;
            padding: 8px 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .btn-add:hover {
            background-color: #45a049;
        }

        .modal-content table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            color: #fff;
        }

        .modal-content th, .modal-content td {
            padding: 12px 8px;
            text-align: left;
            border-bottom: 1px solid #333;
        }

        .modal-content th {
            background-color: #2a2a2a;
            font-weight: bold;
        }

        .modal-content tr:hover {
            background-color: #2a2a2a;
        }

        .btn-edit, .btn-delete {
            padding: 6px 12px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            margin: 0 5px;
            transition: background-color 0.3s;
        }

        .btn-edit {
            background-color: #2196F3;
            color: white;
        }

        .btn-edit:hover {
            background-color: #1976D2;
        }

        .btn-delete {
            background-color: #f44336;
            color: white;
        }

        .btn-delete:hover {
            background-color: #d32f2f;
        }

        .edit-mode input {
            width: 90%;
            margin: 2px;
            background-color: #2a2a2a;
            color: #fff;
            border: 1px solid #4CAF50;
        }

        @media screen and (max-width: 768px) {
            .modal-content {
                width: 95%;
                margin: 10% auto;
            }

            form {
                flex-direction: column;
            }

            input {
                width: 100%;
            }

            table {
                display: block;
                overflow-x: auto;
            }
        }
    `;
    document.head.appendChild(style);

    // Tab switching
    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            tabBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            document.querySelectorAll('.tab-content').forEach(content => {
                content.classList.remove('active');
            });
            document.getElementById(`${btn.dataset.tab}Tab`).classList.add('active');
        });
    });

    // Modal controls
    settingsBtn.onclick = function() {
        modal.style.display = "block";
        loadWebsites();
        loadContacts();
    }

    closeBtn.onclick = function() {
        modal.style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    // Websites CRUD Operations
    async function loadWebsites() {
        try {
            const websites = await eel.get_websites()();
            updateWebsitesTable(websites);
        } catch (error) {
            console.error('Error loading websites:', error);
        }
    }

    function updateWebsitesTable(websites) {
        const tableBody = document.getElementById('websitesTableBody');
        tableBody.innerHTML = '';
        
        websites.forEach(website => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${website.id}</td>
                <td>${website.name}</td>
                <td><a href="${website.url}" target="_blank" style="color: #4CAF50;">${website.url}</a></td>
                <td>
                    <button class="btn-edit" onclick="editWebsite(${website.id}, '${website.name}', '${website.url}')">
                        <i class="bi bi-pencil"></i> Edit
                    </button>
                    <button class="btn-delete" onclick="deleteWebsite(${website.id})">
                        <i class="bi bi-trash"></i> Delete
                    </button>
                </td>
            `;
            tableBody.appendChild(row);
        });
    }

    websiteForm.onsubmit = async function(e) {
        e.preventDefault();
        const name = document.getElementById('websiteName').value;
        const url = document.getElementById('websiteUrl').value;

        try {
            await eel.add_website(name, url)();
            websiteForm.reset();
            loadWebsites();
        } catch (error) {
            console.error('Error adding website:', error);
        }
    }

    window.editWebsite = function(id, name, url) {
        const row = document.querySelector(`tr:has(td:first-child:contains(${id}))`);
        row.classList.add('edit-mode');
        row.innerHTML = `
            <td>${id}</td>
            <td><input type="text" value="${name}" id="edit-name-${id}"></td>
            <td><input type="url" value="${url}" id="edit-url-${id}"></td>
            <td>
                <button class="btn-edit" onclick="saveWebsite(${id})">
                    <i class="bi bi-check-lg"></i> Save
                </button>
                <button class="btn-delete" onclick="loadWebsites()">
                    <i class="bi bi-x-lg"></i> Cancel
                </button>
            </td>
        `;
    }

    window.saveWebsite = async function(id) {
        const name = document.getElementById(`edit-name-${id}`).value;
        const url = document.getElementById(`edit-url-${id}`).value;
        
        try {
            await eel.update_website(id, name, url)();
            loadWebsites();
        } catch (error) {
            console.error('Error updating website:', error);
        }
    }

    window.deleteWebsite = async function(id) {
        if (confirm('Are you sure you want to delete this website?')) {
            try {
                await eel.delete_website(id)();
                loadWebsites();
            } catch (error) {
                console.error('Error deleting website:', error);
            }
        }
    }

    // Contacts CRUD Operations
    async function loadContacts() {
        try {
            const contacts = await eel.get_contacts()();
            updateContactsTable(contacts);
        } catch (error) {
            console.error('Error loading contacts:', error);
        }
    }

    function updateContactsTable(contacts) {
        const tableBody = document.getElementById('contactsTableBody');
        tableBody.innerHTML = '';
        
        contacts.forEach(contact => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${contact.id}</td>
                <td>${contact.name}</td>
                <td>${contact.mobile_no || ''}</td>
                <td>${contact.email || ''}</td>
                <td>
                    <button class="btn-edit" onclick="editContact(${contact.id}, '${contact.name}', '${contact.mobile_no || ''}', '${contact.email || ''}')">
                        <i class="bi bi-pencil"></i> Edit
                    </button>
                    <button class="btn-delete" onclick="deleteContact(${contact.id})">
                        <i class="bi bi-trash"></i> Delete
                    </button>
                </td>
            `;
            tableBody.appendChild(row);
        });
    }

    contactForm.onsubmit = async function(e) {
        e.preventDefault();
        const name = document.getElementById('contactName').value.trim();
        const mobile = document.getElementById('contactMobile').value.trim();
        const email = document.getElementById('contactEmail').value.trim();
    
        // Basic validation
        if (!name) {
            alert('Name is required');
            return;
        }
    
        try {
            const result = await eel.add_contact(name, mobile, email)();
            if (result) {  // Assuming your Python function returns true on success
                contactForm.reset();
                loadContacts();
                alert('Contact added successfully');
            } else {
                alert('Failed to add contact');
            }
        } catch (error) {
            console.error('Error adding contact:', error);
            alert('Error adding contact: ' + error.message);
        }
    }
    

    window.editContact = function(id, name, mobile, email) {
        const row = document.querySelector(`tr:has(td:first-child:contains(${id}))`);
        row.classList.add('edit-mode');
        row.innerHTML = `
            <td>${id}</td>
            <td><input type="text" value="${name}" id="edit-contact-name-${id}"></td>
            <td><input type="tel" value="${mobile}" id="edit-contact-mobile-${id}"></td>
            <td><input type="email" value="${email}" id="edit-contact-email-${id}"></td>
            <td>
                <button class="btn-edit" onclick="saveContact(${id})">
                    <i class="bi bi-check-lg"></i> Save
                </button>
                <button class="btn-delete" onclick="loadContacts()">
                    <i class="bi bi-x-lg"></i> Cancel
                </button>
            </td>
        `;
    }

    window.saveContact = async function(id) {
        const name = document.getElementById(`edit-contact-name-${id}`).value;
        const mobile = document.getElementById(`edit-contact-mobile-${id}`).value;
        const email = document.getElementById(`edit-contact-email-${id}`).value;
        
        try {
            await eel.update_contact(id, name, mobile, email)();
            loadContacts();
        } catch (error) {
            console.error('Error updating contact:', error);
        }
    }

    window.deleteContact = async function(id) {
        if (confirm('Are you sure you want to delete this contact?')) {
            try {
                await eel.delete_contact(id)();
                loadContacts();
            } catch (error) {
                console.error('Error deleting contact:', error);
            }
        }
    }
});



// Add this after your existing contacts code in settings.js

// Email CRUD Operations
document.getElementById('emailForm').onsubmit = async function(e) {
    e.preventDefault();
    const name = document.getElementById('emailName').value;
    const email = document.getElementById('emailAddress').value;

    try {
        await eel.add_mail_to_db(name, email)();
        emailForm.reset();
        loadEmails();
    } catch (error) {
        console.error('Error adding email:', error);
    }
}

async function loadEmails() {
    try {
        const emails = await eel.get_mails_from_db()();
        updateEmailsTable(emails);
    } catch (error) {
        console.error('Error loading emails:', error);
    }
}

function updateEmailsTable(emails) {
    const tableBody = document.getElementById('emailsTableBody');
    tableBody.innerHTML = '';
    
    emails.forEach(email => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${email[0]}</td>
            <td>${email[1]}</td>
            <td>${email[2]}</td>
            <td>
                <button class="btn-edit" onclick="editEmail(${email[0]}, '${email[1]}', '${email[2]}')">
                    <i class="bi bi-pencil"></i> Edit
                </button>
                <button class="btn-delete" onclick="deleteEmail(${email[0]})">
                    <i class="bi bi-trash"></i> Delete
                </button>
            </td>
        `;
        tableBody.appendChild(row);
    });
}

window.editEmail = function(id, name, email) {
    const row = document.querySelector(`tr:has(td:first-child:contains(${id}))`);
    row.classList.add('edit-mode');
    row.innerHTML = `
        <td>${id}</td>
        <td><input type="text" value="${name}" id="edit-email-name-${id}"></td>
        <td><input type="email" value="${email}" id="edit-email-address-${id}"></td>
        <td>
            <button class="btn-edit" onclick="saveEmail(${id})">
                <i class="bi bi-check-lg"></i> Save
            </button>
            <button class="btn-delete" onclick="loadEmails()">
                <i class="bi bi-x-lg"></i> Cancel
            </button>
        </td>
    `;
}

window.saveEmail = async function(id) {
    const name = document.getElementById(`edit-email-name-${id}`).value;
    const email = document.getElementById(`edit-email-address-${id}`).value;
    
    try {
        await eel.update_mail_in_db(id, name, email)();
        loadEmails();
    } catch (error) {
        console.error('Error updating email:', error);
    }
}

window.deleteEmail = async function(id) {
    if (confirm('Are you sure you want to delete this email?')) {
        try {
            await eel.delete_mail_from_db(id)();
            loadEmails();
        } catch (error) {
            console.error('Error deleting email:', error);
        }
    }
}

// Add this to your existing DOMContentLoaded event listener
document.addEventListener('DOMContentLoaded', function() {
    // Your existing code...

    // Add email tab loading
    const emailTab = document.querySelector('[data-tab="emails"]');
    if (emailTab) {
        emailTab.addEventListener('click', () => {
            loadEmails();
        });
    }
});

