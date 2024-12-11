class PrimaryReplicaRouter:
    def db_for_read(self, model, **hints):
        return 'replica1'

    def db_for_write(self, model, **hints):
        return 'default'
