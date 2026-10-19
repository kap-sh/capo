"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#GetStreamOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_keyspacesstreams.types.date
    import capo_keyspacesstreams.types.keyspace_name
    import capo_keyspacesstreams.types.shard_description_list
    import capo_keyspacesstreams.types.shard_id_token
    import capo_keyspacesstreams.types.stream_arn
    import capo_keyspacesstreams.types.stream_status
    import capo_keyspacesstreams.types.stream_view_type
    import capo_keyspacesstreams.types.table_name


class GetStreamOutput(TypedDict, closed=True):
    stream_arn: "capo_keyspacesstreams.types.stream_arn.StreamArn"
    """<p> The Amazon Resource Name (ARN) that uniquely identifies the stream within Amazon Keyspaces. This ARN can be used in other API operations to reference this specific stream. </p>"""
    stream_label: "str"
    """<p> A timestamp that serves as a unique identifier for this stream, used for debugging and monitoring purposes. The stream label represents the point in time when the stream was created. </p>"""
    stream_status: "capo_keyspacesstreams.types.stream_status.StreamStatus"
    """<p> The current status of the stream. Values can be <code>ENABLING</code>, <code>ENABLED</code>, <code>DISABLING</code>, or <code>DISABLED</code>. Operations on the stream depend on its current status. </p>"""
    stream_view_type: "capo_keyspacesstreams.types.stream_view_type.StreamViewType"
    """<p> The format of the data records in this stream. Currently, this can be one of the following options: </p> <ul> <li> <p> <code>NEW_AND_OLD_IMAGES</code> - both versions of the row, before and after the change. This is the default.</p> </li> <li> <p> <code>NEW_IMAGE</code> - the version of the row after the change.</p> </li> <li> <p> <code>OLD_IMAGE</code> - the version of the row before the change.</p> </li> <li> <p> <code>KEYS_ONLY</code> - the partition and clustering keys of the row that was changed.</p> </li> </ul>"""
    creation_request_date_time: "capo_keyspacesstreams.types.date.Date"
    """<p> The date and time when the request to create this stream was issued. The value is represented in ISO 8601 format. </p>"""
    keyspace_name: "capo_keyspacesstreams.types.keyspace_name.KeyspaceName"
    """<p> The name of the keyspace containing the table associated with this stream. The keyspace name is part of the table's hierarchical identifier in Amazon Keyspaces. </p>"""
    table_name: "capo_keyspacesstreams.types.table_name.TableName"
    """<p> The name of the table associated with this stream. The stream captures changes to rows in this Amazon Keyspaces table. </p>"""
    shards: NotRequired[
        "capo_keyspacesstreams.types.shard_description_list.ShardDescriptionList"
    ]
    """<p> An array of shard objects associated with this stream. Each shard contains a subset of the stream's data records and has its own unique identifier. The collection of shards represents the complete stream data. </p>"""
    next_token: NotRequired["capo_keyspacesstreams.types.shard_id_token.ShardIdToken"]
    """<p> A pagination token that can be used in a subsequent <code>GetStream</code> request. This token is returned if the response contains more shards than can be returned in a single response. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetStreamOutput) -> dict:
    out: dict = {}
    out["streamArn"] = value["stream_arn"]
    out["streamLabel"] = value["stream_label"]
    import capo_keyspacesstreams.types.stream_status

    out["streamStatus"] = (
        capo_keyspacesstreams.types.stream_status.serialize_aws_json_1_0(
            value["stream_status"]
        )
    )
    import capo_keyspacesstreams.types.stream_view_type

    out["streamViewType"] = (
        capo_keyspacesstreams.types.stream_view_type.serialize_aws_json_1_0(
            value["stream_view_type"]
        )
    )
    import capo_keyspacesstreams.types.date

    out["creationRequestDateTime"] = (
        capo_keyspacesstreams.types.date.serialize_aws_json_1_0(
            value["creation_request_date_time"]
        )
    )
    out["keyspaceName"] = value["keyspace_name"]
    out["tableName"] = value["table_name"]
    if "shards" in value:
        import capo_keyspacesstreams.types.shard_description_list

        out["shards"] = (
            capo_keyspacesstreams.types.shard_description_list.serialize_aws_json_1_0(
                value["shards"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetStreamOutput:
    out: GetStreamOutput = {}  # type: ignore[typeddict-item]
    if data.get("streamArn") is not None:
        out["stream_arn"] = data["streamArn"]
    else:
        out["stream_arn"] = ""
    if data.get("streamLabel") is not None:
        out["stream_label"] = data["streamLabel"]
    else:
        out["stream_label"] = ""
    if data.get("streamStatus") is not None:
        import capo_keyspacesstreams.types.stream_status

        out["stream_status"] = (
            capo_keyspacesstreams.types.stream_status.deserialize_aws_json_1_0(
                data["streamStatus"]
            )
        )
    else:
        import typing

        out["stream_status"] = typing.cast(
            "capo_keyspacesstreams.types.stream_status.StreamStatus", ""
        )
    if data.get("streamViewType") is not None:
        import capo_keyspacesstreams.types.stream_view_type

        out["stream_view_type"] = (
            capo_keyspacesstreams.types.stream_view_type.deserialize_aws_json_1_0(
                data["streamViewType"]
            )
        )
    else:
        import typing

        out["stream_view_type"] = typing.cast(
            "capo_keyspacesstreams.types.stream_view_type.StreamViewType", ""
        )
    if data.get("creationRequestDateTime") is not None:
        import capo_keyspacesstreams.types.date

        out["creation_request_date_time"] = (
            capo_keyspacesstreams.types.date.deserialize_aws_json_1_0(
                data["creationRequestDateTime"]
            )
        )
    else:
        import datetime

        out["creation_request_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("keyspaceName") is not None:
        out["keyspace_name"] = data["keyspaceName"]
    else:
        out["keyspace_name"] = ""
    if data.get("tableName") is not None:
        out["table_name"] = data["tableName"]
    else:
        out["table_name"] = ""
    if data.get("shards") is not None:
        import capo_keyspacesstreams.types.shard_description_list

        out["shards"] = (
            capo_keyspacesstreams.types.shard_description_list.deserialize_aws_json_1_0(
                data["shards"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
