from src.core.mixins.create_mixin import CreateMixin
from src.core.mixins.list_mixin import ListMixin
from src.core.mixins.retrieve_mixin import RetrieveMixin
from src.core.mixins.update_mixin import UpdateMixin
from src.core.mixins.delete_mixin import DeleteMixin


class BaseManager(CreateMixin, ListMixin, RetrieveMixin, UpdateMixin, DeleteMixin):
    pass
