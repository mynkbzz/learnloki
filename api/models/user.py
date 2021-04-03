from ..db import Base
from sqlalchemy import Boolean, Column, Integer, String
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=True)
    full_name = Column(String)

class user_friend(Base):
    __tablename__ = "userFriend"
    id = Column(Integer, primary_key=True, index=True)
    sourceId = Column(Integer,index=True , unique=True)
    targetId = Column(Integer,unique=True)
    type = Column(Integer, nullable=False, unique=True)
    status = Column(Integer, nullable=True)
    createdAt = Column(datetime)
    updatedAt = Column(datetime)
    notes = Column(String)

class user_message(Base):
    __tablename__ = "userMessage"
    id = Column(Integer, primary_key=True, index=True)
    sourceId = Column(Integer,index=True , unique=True)
    targetId = Column(Integer,unique=True)
    message = Column(String)
    createdAt = Column(datetime)
    updatedAt = Column(datetime)

class user_Follower(Base):
    __tablename__ = "userFollower"
    id = Column(Integer, primary_key=True, index=True)
    sourceId = Column(Integer,index=True , unique=True)
    targetId = Column(Integer,unique=True)
    type = Column(Integer, nullable=False, unique=True)
    createdAt = Column(datetime)
    updatedAt = Column(datetime)

class user_Post(Base):
    __tablename__ = "userPost"
    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer,index=True , unique=True)
    senderId = Column(Integer,unique=True)
    message = Column(String)
    createdAt = Column(datetime)
    updatedAt = Column(datetime)

class group_Follower(Base):
    __tablename__ = "groupFollower"
    id = Column(Integer, primary_key=True, index=True)
    groupId = Column(Integer,index=True , unique=True)
    userId = Column(Integer,unique=True)
    type = Column(Integer)
    createdAt = Column(datetime)
    updatedAt = Column(datetime)

class group_Message(Base):
    __tablename__ = "groupMessage"
    id = Column(Integer, primary_key=True, index=True)
    groupId = Column(Integer,index=True , unique=True)
    userId = Column(Integer,unique=True)
    message = Column(String)
    createdAt = Column(datetime)
    updatedAt = Column(datetime)

class group_Pose(Base):
    __tablename__ = "groupPose"
    id = Column(Integer, primary_key=True, index=True)
    groupId = Column(Integer,index=True , unique=True)
    userId = Column(Integer,unique=True)
    message = Column(String)
    createdAt = Column(datetime)
    updatedAt = Column(datetime)

class group_Member(Base):
    __tablename__ = "groupMember"
     id = Column(Integer, primary_key=True, index=True)
    groupId = Column(Integer,index=True , unique=True)
    userId = Column(Integer,unique=True)
    roleId = Column(Integer, unique=True)
    status = Column(Integer)
    createdAt = Column(datetime)
    updatedAt = Column(datetime)
    notes = Column(String)

class group_Meta(Base):
    __tablename__= "groupMeta"
      id = Column(Integer, primary_key=True, index=True)
    groupId = Column(Integer,index=True , unique=True)
    key = Column(str)
    content = Column(String)

class groups(Base):
    __tablename__ = "group"
     id = Column(Integer, primary_key=True, index=True)
    createdBy = Column(Integer,index=True , unique=True)
    updatedBy = Column(Integer,unique=True)
    title = Column(Integer, nullable=False, unique=True)
    metaTitle = Column(Integer, nullable=True)
    slug = Column(str)
    summary = Column(String)
    status = Column(Integer)
    createdAt = Column(datetime)
    updatedAt = Column(datetime)
    profile = Column(String)
    content = Column(String)