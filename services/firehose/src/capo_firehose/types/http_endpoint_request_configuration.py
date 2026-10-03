"""Generated from Smithy shape ``com.amazonaws.firehose#HttpEndpointRequestConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.content_encoding
    import capo_firehose.types.http_endpoint_common_attributes_list


class HttpEndpointRequestConfiguration(TypedDict, closed=True):
    content_encoding: NotRequired[
        "capo_firehose.types.content_encoding.ContentEncoding"
    ]
    """<p>Firehose uses the content encoding to compress the body of a request before sending the request to the destination. For more information, see <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Encoding">Content-Encoding</a> in MDN Web Docs, the official Mozilla documentation.</p>"""
    common_attributes: NotRequired[
        "capo_firehose.types.http_endpoint_common_attributes_list.HttpEndpointCommonAttributesList"
    ]
    """<p>Describes the metadata sent to the HTTP endpoint destination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HttpEndpointRequestConfiguration) -> dict:
    out: dict = {}
    if "content_encoding" in value:
        import capo_firehose.types.content_encoding

        out["ContentEncoding"] = (
            capo_firehose.types.content_encoding.serialize_aws_json_1_1(
                value["content_encoding"]
            )
        )
    if "common_attributes" in value:
        import capo_firehose.types.http_endpoint_common_attributes_list

        out["CommonAttributes"] = (
            capo_firehose.types.http_endpoint_common_attributes_list.serialize_aws_json_1_1(
                value["common_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HttpEndpointRequestConfiguration:
    out: HttpEndpointRequestConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ContentEncoding") is not None:
        import capo_firehose.types.content_encoding

        out["content_encoding"] = (
            capo_firehose.types.content_encoding.deserialize_aws_json_1_1(
                data["ContentEncoding"]
            )
        )
    if data.get("CommonAttributes") is not None:
        import capo_firehose.types.http_endpoint_common_attributes_list

        out["common_attributes"] = (
            capo_firehose.types.http_endpoint_common_attributes_list.deserialize_aws_json_1_1(
                data["CommonAttributes"]
            )
        )
    return out
