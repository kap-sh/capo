"""Generated from Smithy shape ``aws.iam#ConditionalActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.action_name_with_optional_service_prefix
    import capo_partnercentral_marketing.types.applies_when

ConditionalActions: TypeAlias = dict[
    "capo_partnercentral_marketing.types.action_name_with_optional_service_prefix.ActionNameWithOptionalServicePrefix",
    "capo_partnercentral_marketing.types.applies_when.AppliesWhen",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: ConditionalActions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_partnercentral_marketing.types.applies_when

        out[key] = capo_partnercentral_marketing.types.applies_when.serialize_cbor(
            value
        )
    return out


def deserialize_cbor(data: dict) -> ConditionalActions:
    out: ConditionalActions = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_partnercentral_marketing.types.applies_when

        out[key] = capo_partnercentral_marketing.types.applies_when.deserialize_cbor(
            value
        )
    return out
