"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ShareErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.share_error

ShareErrors: TypeAlias = list["capo_service_catalog.types.share_error.ShareError"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShareErrors) -> list:
    import capo_service_catalog.types.share_error

    out: list = []
    for item in value:
        out.append(capo_service_catalog.types.share_error.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ShareErrors:
    import capo_service_catalog.types.share_error

    out: ShareErrors = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.share_error.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ShareErrors) -> list:
    import capo_service_catalog.types.share_error

    out: list = []
    for item in value:
        out.append(capo_service_catalog.types.share_error.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ShareErrors:
    import capo_service_catalog.types.share_error

    out: ShareErrors = []
    for item in data:
        if item is None:
            continue
        out.append(capo_service_catalog.types.share_error.deserialize_cbor(item))
    return out
