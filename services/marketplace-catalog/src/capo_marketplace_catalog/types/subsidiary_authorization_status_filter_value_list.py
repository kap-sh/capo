"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SubsidiaryAuthorizationStatusFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.subsidiary_authorization_status_string

SubsidiaryAuthorizationStatusFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.subsidiary_authorization_status_string.SubsidiaryAuthorizationStatusString"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubsidiaryAuthorizationStatusFilterValueList) -> list:
    import capo_marketplace_catalog.types.subsidiary_authorization_status_string

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_catalog.types.subsidiary_authorization_status_string.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SubsidiaryAuthorizationStatusFilterValueList:
    import capo_marketplace_catalog.types.subsidiary_authorization_status_string

    out: SubsidiaryAuthorizationStatusFilterValueList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_catalog.types.subsidiary_authorization_status_string.deserialize_json(
                item
            )
        )
    return out
