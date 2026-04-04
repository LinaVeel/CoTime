from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


from app.models.user import User
from app.models.friendship import Friendship
from app.models.availability_slot import AvailabilitySlot
from app.models.availability_slot_viewer import AvailabilitySlotViewer
