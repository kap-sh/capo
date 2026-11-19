"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#Resources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.resource

Resources: TypeAlias = list["capo_marketplace_agreement.types.resource.Resource"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Resources) -> list:
    import capo_marketplace_agreement.types.resource

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.resource.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> Resources:
    import capo_marketplace_agreement.types.resource

    out: Resources = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.resource.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Resources) -> list:
    import capo_marketplace_agreement.types.resource

    out: list = []
    for item in value:
        out.append(capo_marketplace_agreement.types.resource.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Resources:
    import capo_marketplace_agreement.types.resource

    out: Resources = []
    for item in data:
        if item is None:
            continue
        out.append(capo_marketplace_agreement.types.resource.deserialize_cbor(item))
    return out
