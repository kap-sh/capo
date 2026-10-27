"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SubsidiaryAuthorizationResourceIdFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.subsidiary_authorization_resource_id_string

SubsidiaryAuthorizationResourceIdFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.subsidiary_authorization_resource_id_string.SubsidiaryAuthorizationResourceIdString"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubsidiaryAuthorizationResourceIdFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> SubsidiaryAuthorizationResourceIdFilterValueList:
    return [item for item in data if item is not None]
