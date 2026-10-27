"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SubsidiaryAuthorizationEntityIdFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.subsidiary_authorization_entity_id_string

SubsidiaryAuthorizationEntityIdFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.subsidiary_authorization_entity_id_string.SubsidiaryAuthorizationEntityIdString"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubsidiaryAuthorizationEntityIdFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> SubsidiaryAuthorizationEntityIdFilterValueList:
    return [item for item in data if item is not None]
