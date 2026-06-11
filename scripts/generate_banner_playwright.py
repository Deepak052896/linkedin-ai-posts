from playwright.sync_api import sync_playwright
from jinja2 import Template
import os
from datetime import datetime

TOPICS_DATA = {
    "linux": {
        "topic": "LINUX",
        "role": "SYSADMIN",
        "commands": [
            {"name": "Check Failed Services", "command": "systemctl --failed", "description": "List all failed services on the system"},
            {"name": "Check Disk Usage", "command": "df -h", "description": "Display disk space usage in human readable format"},
            {"name": "View Running Processes", "command": "ps aux", "description": "Show all running processes on the system"},
            {"name": "Open Listening Ports", "command": "ss -tulnp", "description": "List all listening ports and connected services"},
            {"name": "Check System Uptime", "command": "uptime", "description": "Show how long the system has been running"}
        ]
    },
    "aws": {
        "topic": "AWS",
        "role": "CLOUD ENGINEER",
        "commands": [
            {"name": "List S3 Buckets", "command": "aws s3 ls", "description": "List all S3 buckets in your account"},
            {"name": "Show EC2 Instances", "command": "aws ec2 describe-instances", "description": "Get details of all EC2 instances"},
            {"name": "List IAM Users", "command": "aws iam list-users", "description": "Display all IAM users"},
            {"name": "CloudFormation Stacks", "command": "aws cloudformation list-stacks", "description": "List all CloudFormation stacks"},
            {"name": "CloudWatch Logs", "command": "aws logs describe-log-groups", "description": "List all CloudWatch log groups"}
        ]
    },
    "windows": {
        "topic": "WINDOWS",
        "role": "WINDOWS ADMIN",
        "commands": [
            {"name": "System Information", "command": "systeminfo", "description": "Display detailed system configuration"},
            {"name": "Process List", "command": "tasklist", "description": "Show all running processes"},
            {"name": "IP Configuration", "command": "ipconfig /all", "description": "Display network configuration"},
            {"name": "Driver List", "command": "driverquery", "description": "Show all installed drivers"},
            {"name": "Event Logs", "command": "wevtutil qe System", "description": "Query Windows event logs"}
        ]
    },
    "networking": {
        "topic": "NETWORKING",
        "role": "NETWORK ENGINEER",
        "commands": [
            {"name": "Show Network Stats", "command": "netstat -an", "description": "Display all network connections"},
            {"name": "Trace Route", "command": "traceroute google.com", "description": "Trace network path to destination"},
            {"name": "DNS Lookup", "command": "nslookup google.com", "description": "Query DNS records"},
            {"name": "Show ARP Table", "command": "arp -a", "description": "Display ARP cache"},
            {"name": "Packet Capture", "command": "tcpdump -i eth0", "description": "Capture network packets"}
        ]
    },
    "security": {
        "topic": "SECURITY",
        "role": "SECURITY ANALYST",
        "commands": [
            {"name": "Check Open Ports", "command": "nmap localhost", "description": "Scan open ports"},
            {"name": "Show Firewall Rules", "command": "iptables -L", "description": "List firewall rules"},
            {"name": "Check Logins", "command": "last", "description": "Show recent logins"},
            {"name": "Find SUID Files", "command": "find / -perm -4000", "description": "Find SUID binaries"},
            {"name": "Check Fail2Ban", "command": "fail2ban-client status", "description": "Check banned IPs"}
        ]
    },
    "devops": {
        "topic": "DEVOPS",
        "role": "DEVOPS ENGINEER",
        "commands": [
            {"name": "Docker PS", "command": "docker ps -a", "description": "List all containers"},
            {"name": "Kubectl Get Pods", "command": "kubectl get pods", "description": "List Kubernetes pods"},
            {"name": "Git Status", "command": "git status", "description": "Check repository status"},
            {"name": "Terraform Plan", "command": "terraform plan", "description": "Preview infrastructure changes"},
            {"name": "Ansible Ping", "command": "ansible all -m ping", "description": "Test connectivity"}
        ]
    }
}

def get_today_category():
    categories = ["linux", "aws", "windows", "networking", "security", "devops"]
    day_index = datetime.now().weekday()
    return categories[day_index % len(categories)]

def generate_banner():
    category = get_today_category()
    print(f"📅 Generating {category.upper()} banner...")
    
    data = TOPICS_DATA[category]
    
    template_path = "templates/banner_template.html"
    if not os.path.exists(template_path):
        print(f"❌ Template not found: {template_path}")
        return None
    
    with open(template_path, 'r') as f:
        html_template = f.read()
    
    template = Template(html_template)
    rendered_html = template.render(
        TOPIC=data["topic"],
        ROLE=data["role"],
        commands=data["commands"]
    )
    
    os.makedirs("temp", exist_ok=True)
    with open("temp/latest.html", "w") as f:
        f.write(rendered_html)
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_viewport_size({"width": 1200, "height": 800})
        page.set_content(rendered_html)
        page.wait_for_timeout(1000)
        
        os.makedirs("banners", exist_ok=True)
        date_str = datetime.now().strftime("%Y-%m-%d")
        output_path = f"banners/{date_str}.png"
        
        page.screenshot(path=output_path, full_page=True)
        browser.close()
    
    print(f"✅ Banner generated: {output_path}")
    return output_path

if __name__ == "__main__":
    generate_banner()
