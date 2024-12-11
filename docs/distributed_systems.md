# Distributed Database Architecture

## Architecture
- Primary database: Handles all write operations.
- Replica databases: Handle read operations to reduce load on the primary database.

## Configuration

### PostgreSQL
1. **Primary Database (`db`)**:
   - Configured for replication using `wal_level` and `max_wal_senders`.
2. **Replica Databases (`db2` and `db3`)**:
   - Configured with `standby_mode` and connected to the primary.

### Django
1. **Multiple Databases**:
   - Configured in `settings.py` using `DATABASES` with `default` (primary) and replicas.
2. **Database Router**:
   - Implements read/write splitting with `PrimaryReplicaRouter`.

## Future Improvements
- Add health checks for replicas.
- Implement automatic failover using tools like Patroni or Pgpool-II.
