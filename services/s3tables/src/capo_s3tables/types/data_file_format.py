"""Generated from Smithy shape ``com.amazonaws.s3tables#DataFileFormat``."""

from typing import Literal, TypeAlias, cast

DataFileFormat: TypeAlias = Literal["parquet",]


# --- restJson1 ser/de ---
def serialize_json(value: DataFileFormat) -> str:
    return value


def deserialize_json(data: str) -> DataFileFormat:
    return cast(DataFileFormat, data)
