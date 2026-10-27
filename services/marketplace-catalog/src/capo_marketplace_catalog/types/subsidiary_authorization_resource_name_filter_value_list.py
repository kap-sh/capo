"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SubsidiaryAuthorizationResourceNameFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.subsidiary_authorization_resource_name_string

SubsidiaryAuthorizationResourceNameFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.subsidiary_authorization_resource_name_string.SubsidiaryAuthorizationResourceNameString"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubsidiaryAuthorizationResourceNameFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> SubsidiaryAuthorizationResourceNameFilterValueList:
    return [item for item in data if item is not None]
