"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#RequestedTermList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.requested_term

RequestedTermList: TypeAlias = list[
    "capo_marketplace_agreement.types.requested_term.RequestedTerm"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RequestedTermList) -> list:
    import capo_marketplace_agreement.types.requested_term

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.requested_term.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RequestedTermList:
    import capo_marketplace_agreement.types.requested_term

    out: RequestedTermList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.requested_term.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RequestedTermList) -> list:
    import capo_marketplace_agreement.types.requested_term

    out: list = []
    for item in value:
        out.append(capo_marketplace_agreement.types.requested_term.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> RequestedTermList:
    import capo_marketplace_agreement.types.requested_term

    out: RequestedTermList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.requested_term.deserialize_cbor(item)
        )
    return out
