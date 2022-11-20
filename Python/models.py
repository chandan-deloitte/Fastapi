from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    # id = Column(Integer, primary_key=True, index=True)
    # email = Column(String, unique=True, index=True)
    # hashed_password = Column(String)
    # is_active = Column(Boolean, default=True)

    # items = relationship("Item", back_populates="owner")

    # candidate_name: Column(String, index=True)
    # assignment_code : Column(String, index=True)
    # assignment_deployment_url : Column(String, index=True)
    # assignment_code_quality_rating : Column(Integer,index=True)
    # assignment_code_coverage_percentage : Column(Integer, index=True)
    # quiz_1_score : Column(Integer, index=True)


    username = Column(String, primary_key=True )
    user_mail = Column(String, unique=False)
    keyname= Column(String)
    value=Column(String)
    datatype=Column(String)
    tags= Column(String)




#class Item(Base):
#    __tablename__ = "items"
#
#    id = Column(Integer, primary_key=True, index=True)
#    title = Column(String, index=True)
#    description = Column(String, index=True)
#    owner_id = Column(Integer, ForeignKey("users.id"))
#
#    owner = relationship("User", back_populates="items")