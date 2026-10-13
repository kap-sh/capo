"""Generated from Smithy shape ``com.amazonaws.storagegateway#ChapCredentials``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_storage_gateway.types.chap_info

ChapCredentials: TypeAlias = list["capo_storage_gateway.types.chap_info.ChapInfo"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChapCredentials) -> list:
    import capo_storage_gateway.types.chap_info

    out: list = []
    for item in value:
        out.append(capo_storage_gateway.types.chap_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ChapCredentials:
    import capo_storage_gateway.types.chap_info

    out: ChapCredentials = []
    for item in data:
        if item is None:
            continue
        out.append(capo_storage_gateway.types.chap_info.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: ChapCredentials) -> list[Any]:
    import capo_storage_gateway.types.chap_info

    return [
        capo_storage_gateway.types.chap_info.redact_sensitive(item) for item in value
    ]
