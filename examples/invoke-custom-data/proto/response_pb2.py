# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='response.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0eresponse.proto\"B\n\x0e\x43ustomResponse\x12\x11\n\tisSuccess\x18\x01 \x01(\x08\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\x12\x0f\n\x07message\x18\x03 \x01(\tb\x06proto3')
)




_CUSTOMRESPONSE = _descriptor.Descriptor(
  name='CustomResponse',
  full_name='CustomResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isSuccess', full_name='CustomResponse.isSuccess', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='CustomResponse.code', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='CustomResponse.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=84,
)

DESCRIPTOR.message_types_by_name['CustomResponse'] = _CUSTOMRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CustomResponse = _reflection.GeneratedProtocolMessageType('CustomResponse', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMRESPONSE,
  '__module__' : 'response_pb2'
  # @@protoc_insertion_point(class_scope:CustomResponse)
  })
_sym_db.RegisterMessage(CustomResponse)


# @@protoc_insertion_point(module_scope)
