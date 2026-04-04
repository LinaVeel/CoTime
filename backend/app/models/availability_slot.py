from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    func,
    CheckConstraint,
    Text,
)

from app.models import Base


class AvailabilitySlot(Base):
    __tablename__ = "availability_slots"

    __table_args__ = (
        CheckConstraint("start_at < end_at", name="check_slot_start_before_end"),
    )

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    start_at = Column(DateTime(timezone=True), nullable=False)
    end_at = Column(DateTime(timezone=True), nullable=False)

    visibility = Column(String, nullable=False, default="public")

    comment = Column(Text, nullable=True)
    city = Column(String, nullable=True)  # где планируется активность
    created_at = Column(DateTime(timezone=True), server_default=func.now())
