"""Generated from Smithy shape ``com.amazonaws.firehose#HttpEndpointCommonAttributesList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_firehose.types.http_endpoint_common_attribute

HttpEndpointCommonAttributesList: TypeAlias = list[
    "capo_firehose.types.http_endpoint_common_attribute.HttpEndpointCommonAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HttpEndpointCommonAttributesList) -> list:
    import capo_firehose.types.http_endpoint_common_attribute

    out: list = []
    for item in value:
        out.append(
            capo_firehose.types.http_endpoint_common_attribute.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> HttpEndpointCommonAttributesList:
    import capo_firehose.types.http_endpoint_common_attribute

    out: HttpEndpointCommonAttributesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_firehose.types.http_endpoint_common_attribute.deserialize_aws_json_1_1(
                item
            )
        )
    return out


def redact_sensitive(value: HttpEndpointCommonAttributesList) -> list[Any]:
    import capo_firehose.types.http_endpoint_common_attribute

    return [
        capo_firehose.types.http_endpoint_common_attribute.redact_sensitive(item)
        for item in value
    ]
