"""Generated from Smithy shape ``aws.iam#RequiredAdditionalActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.action_name_with_optional_service_prefix

RequiredAdditionalActions: TypeAlias = list[
    "capo_partnercentral_marketing.types.action_name_with_optional_service_prefix.ActionNameWithOptionalServicePrefix"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RequiredAdditionalActions) -> list:
    return list(value)


def deserialize_cbor(data: list) -> RequiredAdditionalActions:
    return [item for item in data if item is not None]
