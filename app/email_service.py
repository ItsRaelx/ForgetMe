import re
import aiosmtplib
import email
from email.header import decode_header
from email.parser import BytesParser
from email.policy import default
from typing import List, Dict, Set, Optional
import logging
import random

class EmailService:
    """Service for interacting with email servers and extracting domain information."""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.domains = set()
        self.email_connection = None
    
    async def connect_and_scan(
        self, 
        email: str, 
        password: str, 
        smtp_server: str, 
        smtp_port: int
    ) -> List[str]:
        """
        Connect to the user's email server and scan emails to extract domains.
        
        Args:
            email: User's email address
            password: User's email password
            smtp_server: SMTP server address
            smtp_port: SMTP server port
            
        Returns:
            List of domains found in emails
        """
        self.logger.info(f"Connecting to {smtp_server}:{smtp_port} for {email}")
        
        try:
            # In a real implementation, we would:
            # 1. Establish SMTP connection
            # 2. Authenticate with credentials
            # 3. Get list of emails
            # 4. Parse emails to extract domains
            # 5. Return unique domains
            
            # For demo purposes, we'll simulate the connection
            # and return a list of fake domains
            self.logger.info(f"Successfully connected to {smtp_server}")
            
            # Simulate email scanning delay
            # In a real app, this would analyze emails
            self.email = email
            
            # Return list of unique domains
            domains = self.get_domains_for_demo(email)
            return domains
            
        except Exception as e:
            self.logger.error(f"Failed to connect: {str(e)}")
            raise Exception(f"Failed to connect to email server: {str(e)}")
    
    def extract_domains_from_emails(self, emails: List[dict]) -> List[str]:
        """
        Extract domains from a list of email messages.
        
        Args:
            emails: List of email message objects
            
        Returns:
            List of unique domains found in the emails
        """
        domains = set()
        
        for email_msg in emails:
            # Extract sender domain
            from_address = email_msg.get('from', '')
            if '@' in from_address:
                domain = from_address.split('@')[-1].strip('>')
                domains.add(domain)
            
            # Could also extract domains from links in the email body
        
        return list(domains)
    
    def get_domains_for_demo(self, email: str) -> List[str]:
        """
        Generate a list of fake domains for demo purposes.
        
        Args:
            email: User email (used for randomization)
            
        Returns:
            List of fake domains
        """
        # List of common domains that might send emails
        common_domains = [
            "facebook.com",
            "twitter.com",
            "linkedin.com",
            "amazon.com",
            "google.com",
            "microsoft.com",
            "apple.com",
            "netflix.com",
            "spotify.com",
            "instagram.com",
            "pinterest.com",
            "dropbox.com",
            "slack.com",
            "zoom.us",
            "uber.com",
            "airbnb.com",
            "booking.com",
            "expedia.com",
            "paypal.com",
            "ebay.com"
        ]
        
        # Select random sample of 5-15 domains
        num_domains = random.randint(5, 15)
        selected_domains = random.sample(common_domains, min(num_domains, len(common_domains)))
        
        return selected_domains 