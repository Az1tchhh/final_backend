# Load Balancer Configuration

## Load Balancer: Nginx

### Configuration
1. The Nginx configuration file is located at `nginx.conf` in the root of the repository.
2. The configuration uses an `upstream` block to define multiple backend application servers.
3. Static and media files are served directly by Nginx for better performance.

### Docker Compose Setup
1. Nginx is defined as a service in `docker-compose.yml`.
2. Multiple `web` services are defined (e.g., `web1`, `web2`) to allow horizontal scaling.

### Deployment
1. Start the services:
   ```bash
   docker-compose up --scale web=2