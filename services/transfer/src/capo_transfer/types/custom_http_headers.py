"""Generated from Smithy shape ``com.amazonaws.transfer#CustomHttpHeaders``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_transfer.types.custom_http_header

CustomHttpHeaders: TypeAlias = list[
    "capo_transfer.types.custom_http_header.CustomHttpHeader"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomHttpHeaders) -> list:
    import capo_transfer.types.custom_http_header

    out: list = []
    for item in value:
        out.append(capo_transfer.types.custom_http_header.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CustomHttpHeaders:
    import capo_transfer.types.custom_http_header

    out: CustomHttpHeaders = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_transfer.types.custom_http_header.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: CustomHttpHeaders) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
