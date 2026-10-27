"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SubsidiaryAuthorizationSortBy``."""

from typing import Literal, TypeAlias, cast

SubsidiaryAuthorizationSortBy: TypeAlias = Literal[
    "EntityId",
    "Status",
    "ResourceId",
    "SubsidiaryAccountId",
    "CreatedDate",
    "LastModifiedDate",
]


# --- restJson1 ser/de ---
def serialize_json(value: SubsidiaryAuthorizationSortBy) -> str:
    return value


def deserialize_json(data: str) -> SubsidiaryAuthorizationSortBy:
    return cast(SubsidiaryAuthorizationSortBy, data)
