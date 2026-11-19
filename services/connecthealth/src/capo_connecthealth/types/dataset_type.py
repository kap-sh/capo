"""Generated from Smithy shape ``com.amazonaws.connecthealth#DatasetType``."""

from typing import Literal, TypeAlias, cast

"""The Amazon Connect Health feature a Dataset is for. Set by the service from the DatasetConfig member supplied at create: medicalCoding -> MEDICAL_CODING."""
DatasetType: TypeAlias = Literal["MEDICAL_CODING",]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetType) -> str:
    return value


def deserialize_json(data: str) -> DatasetType:
    return cast(DatasetType, data)
