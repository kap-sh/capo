"""Generated from Smithy shape ``com.amazonaws.servicecatalog#TagOptionDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.tag_option_detail

TagOptionDetails: TypeAlias = list[
    "capo_service_catalog.types.tag_option_detail.TagOptionDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagOptionDetails) -> list:
    import capo_service_catalog.types.tag_option_detail

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.tag_option_detail.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TagOptionDetails:
    import capo_service_catalog.types.tag_option_detail

    out: TagOptionDetails = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.tag_option_detail.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TagOptionDetails) -> list:
    import capo_service_catalog.types.tag_option_detail

    out: list = []
    for item in value:
        out.append(capo_service_catalog.types.tag_option_detail.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> TagOptionDetails:
    import capo_service_catalog.types.tag_option_detail

    out: TagOptionDetails = []
    for item in data:
        if item is None:
            continue
        out.append(capo_service_catalog.types.tag_option_detail.deserialize_cbor(item))
    return out
