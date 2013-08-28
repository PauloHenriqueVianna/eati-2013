class AppRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'inscricoes':
            return 'inscricoes'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'inscricoes':
            return 'inscricoes'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'inscricoes' or obj2._meta.app_label == 'inscricoes':
            return True
        return None

    def allow_syncdb(self, db, model):
        if db == 'inscricoes':
            return model._meta.app_label == 'inscricoes'
        elif model._meta.app_label == 'inscricoes':
            return False
        return None