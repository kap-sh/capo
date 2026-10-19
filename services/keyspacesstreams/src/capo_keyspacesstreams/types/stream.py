"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#Stream``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_keyspacesstreams.types.keyspace_name
    import capo_keyspacesstreams.types.stream_arn
    import capo_keyspacesstreams.types.table_name


class Stream(TypedDict, closed=True):
    stream_arn: "capo_keyspacesstreams.types.stream_arn.StreamArn"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies this stream.</p>"""
    keyspace_name: "capo_keyspacesstreams.types.keyspace_name.KeyspaceName"
    """<p>The name of the keyspace containing the table associated with this stream.</p>"""
    table_name: "capo_keyspacesstreams.types.table_name.TableName"
    """<p>The name of the table associated with this stream.</p>"""
    stream_label: "str"
    """<p>A unique identifier for this stream that can be used in stream operations.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Stream) -> dict:
    out: dict = {}
    out["streamArn"] = value["stream_arn"]
    out["keyspaceName"] = value["keyspace_name"]
    out["tableName"] = value["table_name"]
    out["streamLabel"] = value["stream_label"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Stream:
    out: Stream = {}  # type: ignore[typeddict-item]
    if data.get("streamArn") is not None:
        out["stream_arn"] = data["streamArn"]
    else:
        out["stream_arn"] = ""
    if data.get("keyspaceName") is not None:
        out["keyspace_name"] = data["keyspaceName"]
    else:
        out["keyspace_name"] = ""
    if data.get("tableName") is not None:
        out["table_name"] = data["tableName"]
    else:
        out["table_name"] = ""
    if data.get("streamLabel") is not None:
        out["stream_label"] = data["streamLabel"]
    else:
        out["stream_label"] = ""
    return out
