version: '3'

services:
  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    environment:
      - GF_SMTP_ENABLED=true
      - GF_SMTP_HOST=smtp.example.com:587         # Replace with your SMTP server and port
      - GF_SMTP_USER=your-email@example.com       # Replace with your SMTP username/email
      - GF_SMTP_PASSWORD=your-password            # Replace with your SMTP password
      - GF_SMTP_SKIP_VERIFY=true                  # Skip verification (optional)
      - GF_SMTP_FROM_ADDRESS=your-email@example.com
      - GF_SMTP_FROM_NAME=Grafana                 # Customize the from name
    ports:
      - "3000:3000"
    volumes:
      - grafana-storage:/var/lib/grafana

volumes:
  grafana-storage:
