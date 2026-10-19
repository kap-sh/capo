"""Generated from Smithy shape ``com.amazonaws.dynamodb#StreamSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.stream_enabled
    import capo_dynamodb.types.stream_view_type


class StreamSpecification(TypedDict, closed=True):
    stream_enabled: "capo_dynamodb.types.stream_enabled.StreamEnabled"
    """<p>Indicates whether DynamoDB Streams is enabled (true) or disabled (false) on the table.</p>"""
    stream_view_type: NotRequired["capo_dynamodb.types.stream_view_type.StreamViewType"]
    """<p> When an item in the table is modified, <code>StreamViewType</code> determines what information is written to the stream for this table. Valid values for <code>StreamViewType</code> are:</p> <ul> <li> <p> <code>KEYS_ONLY</code> - Only the key attributes of the modified item are written to the stream.</p> </li> <li> <p> <code>NEW_IMAGE</code> - The entire item, as it appears after it was modified, is written to the stream.</p> </li> <li> <p> <code>OLD_IMAGE</code> - The entire item, as it appeared before it was modified, is written to the stream.</p> </li> <li> <p> <code>NEW_AND_OLD_IMAGES</code> - Both the new and the old item images of the item are written to the stream.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StreamSpecification) -> dict:
    out: dict = {}
    out["StreamEnabled"] = value["stream_enabled"]
    if "stream_view_type" in value:
        import capo_dynamodb.types.stream_view_type

        out["StreamViewType"] = (
            capo_dynamodb.types.stream_view_type.serialize_aws_json_1_0(
                value["stream_view_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StreamSpecification:
    out: StreamSpecification = {}  # type: ignore[typeddict-item]
    if data.get("StreamEnabled") is not None:
        out["stream_enabled"] = data["StreamEnabled"]
    else:
        out["stream_enabled"] = False
    if data.get("StreamViewType") is not None:
        import capo_dynamodb.types.stream_view_type

        out["stream_view_type"] = (
            capo_dynamodb.types.stream_view_type.deserialize_aws_json_1_0(
                data["StreamViewType"]
            )
        )
    return out
