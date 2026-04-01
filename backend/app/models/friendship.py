from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    func,
    CheckConstraint,
    UniqueConstraint,
)

from app.models import Base


class Friendship(Base):
    __tablename__ = "friendships"

    __table_args__ = (
        CheckConstraint(
            "requester_id != addressee_id", name="check_not_self_friendship"
        ),
        UniqueConstraint(
            "requester_id", "addressee_id", name="uq_friendship_request_pair"
        ),
    )

    id = Column(Integer, primary_key=True, index=True)
    requester_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    addressee_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(String, nullable=False, default="pending")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
