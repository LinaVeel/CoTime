from sqlalchemy import Column, Integer, ForeignKey

from app.models import Base


class AvailabilitySlotViewer(Base):
    __tablename__ = "availability_slot_viewers"

    id = Column(Integer, primary_key=True, index=True)

    # К какому слоту относится это разрешение
    slot_id = Column(Integer, ForeignKey("availability_slots.id"), nullable=False)

    # Какому пользователю разрешено видеть этот слот
    viewer_user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
