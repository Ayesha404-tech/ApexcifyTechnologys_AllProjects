# Email Automation System

This Python script sends the same email message to multiple recipients using Gmail's SMTP server.

## Setup Instructions

1. **Enable 2-Factor Authentication on Gmail:**
   - Go to your Google Account settings.
   - Navigate to Security > 2-Step Verification.
   - Enable 2-Step Verification if not already enabled.

2. **Generate an App Password:**
   - After enabling 2-Step Verification, go to Security > App passwords.
   - Select "Mail" and "Other (custom name)", enter a name like "Email Automation".
   - Generate the app password. This 16-character password is what you'll use in the script (not your regular password).

3. **Update the Script:**
   - Open `send_emails.py`.
   - Replace `"yourgmail@gmail.com"` with your actual Gmail address.
   - Replace `"yourapppassword"` with the generated app password.
   - Replace the recipient emails in the `recipients` list with real email addresses.

4. **Run the Script:**
   - Open a command prompt in the `email_automation` directory.
   - Run: `python send_emails.py`

## Notes
- Gmail may block sign-ins from apps initially. If you receive a security alert, allow access.
- For production use, consider using a dedicated email service like SendGrid for better reliability and to avoid Gmail limits.
- The script sends emails individually; for large lists, consider batching or using BCC to avoid rate limits.
