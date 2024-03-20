#!/usr/bin/env python3
"""A module with the Base class and all it's methods"""

from uuid import uuid4
from datetime import datetime

class BaseModel:
	"""A Base model for all EDUFLASH models"""

	def __init__(self, *args, **kwargs):
		"""An instantiation of the Base Model
		either created or from a dictionary"""
		if kwargs:
			for key, value in kwargs.items():
				if key == "__class__":
					continue
				if key in ("created_at", "updated_at"):
					value = datetime.fromisoformat(value)
				setattr(self, key, value)
		else:
			self.id = str(uuid4())
			self.created_at = datetime.now()
			self.updated_at = datetime.now()
			# implement storage

	def __str__(self):
		"""Returns a string representation of the instance"""
		# [<class name>] (<self.id>) <self.__dict__>
		string = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
		return string

	def save(self):
		"""A method that updates last updated attribute"""
		self.updated_at = datetime.now()
		# implement new and save storage


	def to_dict(self):
		"""A module that returns a
		dictionary containing key/value of obj instance"""
		attributes = {}
		attributes["__class__"] = self.__class__.__name__
		for key, value in self.__dict__.items():
			if isinstance(value, datetime):
				attributes[key] = value.isoformat()
			else:
				attributes[key] = value
		return attributes

	def delete(self):
		"""Deletes current instance from storage"""
		"""
		implement this
		from models import storage
		storage.delete(self)
"""

"""
Base Model

Update method (self, keyword arg)
To_Dict(self)
Save(self)
Called whenever an object is created or updated
Delete
Delete an object
Str magic method
String representation

User
Setters and getters
Return lists of flashcards created from the resource by the user


Resource Class

Flashcard - to return a list of flashcards
Resource getter
Get all flashcards of a particular resource as a list
Flashcard  getter(depends on user and resource)

Storage system
All(self, cls)
Return all objects of the class present in the storage system as a dict
New(self, obj)
To add obj to d storage system

Save(self)
Save all changes

Delete(self, obi)
Delete an object

Reload
Reload the data from database

Close(self)
Remove current session

Get(self, class, Id)
Return an obj with d specified class and ID

Count()
Returns total number of objs in the database
"""