"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SubsidiaryAuthorizationNameFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.subsidiary_authorization_name_string

SubsidiaryAuthorizationNameFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.subsidiary_authorization_name_string.SubsidiaryAuthorizationNameString"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubsidiaryAuthorizationNameFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> SubsidiaryAuthorizationNameFilterValueList:
    return [item for item in data if item is not None]
