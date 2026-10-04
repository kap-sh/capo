"""Generated from Smithy shape ``com.amazonaws.endusermessaging#JobResourceType``."""

from typing import Literal, TypeAlias, cast

"""Type of resource associated with a job."""
JobResourceType: TypeAlias = Literal[
    "REGISTRATION",
    "BRAND_PROFILE",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobResourceType) -> str:
    return value


def deserialize_json(data: str) -> JobResourceType:
    return cast(JobResourceType, data)
