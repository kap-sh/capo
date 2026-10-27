"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SubsidiaryAuthorizationSubsidiaryAccountIdFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.subsidiary_authorization_subsidiary_account_id_string

SubsidiaryAuthorizationSubsidiaryAccountIdFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.subsidiary_authorization_subsidiary_account_id_string.SubsidiaryAuthorizationSubsidiaryAccountIdString"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: SubsidiaryAuthorizationSubsidiaryAccountIdFilterValueList,
) -> list:
    return list(value)


def deserialize_json(
    data: list,
) -> SubsidiaryAuthorizationSubsidiaryAccountIdFilterValueList:
    return [item for item in data if item is not None]
