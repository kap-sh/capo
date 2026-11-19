"""Generated from Smithy shape ``com.amazonaws.appstream#ErrorDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.error_details

ErrorDetailsList: TypeAlias = list["capo_appstream.types.error_details.ErrorDetails"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ErrorDetailsList) -> list:
    import capo_appstream.types.error_details

    out: list = []
    for item in value:
        out.append(capo_appstream.types.error_details.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ErrorDetailsList:
    import capo_appstream.types.error_details

    out: ErrorDetailsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appstream.types.error_details.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ErrorDetailsList) -> list:
    import capo_appstream.types.error_details

    out: list = []
    for item in value:
        out.append(capo_appstream.types.error_details.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ErrorDetailsList:
    import capo_appstream.types.error_details

    out: ErrorDetailsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appstream.types.error_details.deserialize_cbor(item))
    return out
