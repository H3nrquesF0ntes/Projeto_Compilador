from enum import Enum


class DataType(str, Enum):
  INTEGER = "integer"
  BOOLEAN = "boolean"
  STRING = "string"
  UNKNOWN = "unknown"
