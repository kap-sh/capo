"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SubsidiaryAuthorizationStatusString``."""

from typing import Literal, TypeAlias, cast

SubsidiaryAuthorizationStatusString: TypeAlias = Literal[
    "Draft",
    "Active",
    "Restricted",
]


# --- restJson1 ser/de ---
def serialize_json(value: SubsidiaryAuthorizationStatusString) -> str:
    return value


def deserialize_json(data: str) -> SubsidiaryAuthorizationStatusString:
    return cast(SubsidiaryAuthorizationStatusString, data)
