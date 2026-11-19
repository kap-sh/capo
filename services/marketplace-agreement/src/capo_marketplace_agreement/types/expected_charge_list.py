"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ExpectedChargeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.expected_charge

ExpectedChargeList: TypeAlias = list[
    "capo_marketplace_agreement.types.expected_charge.ExpectedCharge"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExpectedChargeList) -> list:
    import capo_marketplace_agreement.types.expected_charge

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.expected_charge.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ExpectedChargeList:
    import capo_marketplace_agreement.types.expected_charge

    out: ExpectedChargeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.expected_charge.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExpectedChargeList) -> list:
    import capo_marketplace_agreement.types.expected_charge

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.expected_charge.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ExpectedChargeList:
    import capo_marketplace_agreement.types.expected_charge

    out: ExpectedChargeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.expected_charge.deserialize_cbor(item)
        )
    return out
