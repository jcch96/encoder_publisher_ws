# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from local_planner/Sonar.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Sonar(genpy.Message):
  _md5sum = "f867769555dffd428a6a95bc8cdaae9c"
  _type = "local_planner/Sonar"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """float64 back_l
float64 back_r

float64 left_b
float64 left_m
float64 left_f

float64 front_l
float64 front_r

float64 right_f
float64 right_m
float64 right_b"""
  __slots__ = ['back_l','back_r','left_b','left_m','left_f','front_l','front_r','right_f','right_m','right_b']
  _slot_types = ['float64','float64','float64','float64','float64','float64','float64','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       back_l,back_r,left_b,left_m,left_f,front_l,front_r,right_f,right_m,right_b

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Sonar, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.back_l is None:
        self.back_l = 0.
      if self.back_r is None:
        self.back_r = 0.
      if self.left_b is None:
        self.left_b = 0.
      if self.left_m is None:
        self.left_m = 0.
      if self.left_f is None:
        self.left_f = 0.
      if self.front_l is None:
        self.front_l = 0.
      if self.front_r is None:
        self.front_r = 0.
      if self.right_f is None:
        self.right_f = 0.
      if self.right_m is None:
        self.right_m = 0.
      if self.right_b is None:
        self.right_b = 0.
    else:
      self.back_l = 0.
      self.back_r = 0.
      self.left_b = 0.
      self.left_m = 0.
      self.left_f = 0.
      self.front_l = 0.
      self.front_r = 0.
      self.right_f = 0.
      self.right_m = 0.
      self.right_b = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_10d().pack(_x.back_l, _x.back_r, _x.left_b, _x.left_m, _x.left_f, _x.front_l, _x.front_r, _x.right_f, _x.right_m, _x.right_b))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 80
      (_x.back_l, _x.back_r, _x.left_b, _x.left_m, _x.left_f, _x.front_l, _x.front_r, _x.right_f, _x.right_m, _x.right_b,) = _get_struct_10d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_10d().pack(_x.back_l, _x.back_r, _x.left_b, _x.left_m, _x.left_f, _x.front_l, _x.front_r, _x.right_f, _x.right_m, _x.right_b))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 80
      (_x.back_l, _x.back_r, _x.left_b, _x.left_m, _x.left_f, _x.front_l, _x.front_r, _x.right_f, _x.right_m, _x.right_b,) = _get_struct_10d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_10d = None
def _get_struct_10d():
    global _struct_10d
    if _struct_10d is None:
        _struct_10d = struct.Struct("<10d")
    return _struct_10d
