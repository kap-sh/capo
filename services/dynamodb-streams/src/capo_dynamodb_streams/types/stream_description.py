"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#StreamDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb_streams.types.date
    import capo_dynamodb_streams.types.key_schema
    import capo_dynamodb_streams.types.shard_description_list
    import capo_dynamodb_streams.types.shard_id
    import capo_dynamodb_streams.types.stream_arn
    import capo_dynamodb_streams.types.stream_status
    import capo_dynamodb_streams.types.stream_view_type
    import capo_dynamodb_streams.types.string
    import capo_dynamodb_streams.types.table_name


class StreamDescription(TypedDict, closed=True):
    stream_arn: NotRequired["capo_dynamodb_streams.types.stream_arn.StreamArn"]
    """<p>The Amazon Resource Name (ARN) for the stream.</p>"""
    stream_label: NotRequired["capo_dynamodb_streams.types.string.String"]
    """<p>A timestamp, in ISO 8601 format, for this stream.</p> <p>Note that <code>LatestStreamLabel</code> is not a unique identifier for the stream, because it is possible that a stream from another table might have the same timestamp. However, the combination of the following three elements is guaranteed to be unique:</p> <ul> <li> <p>the Amazon Web Services customer ID.</p> </li> <li> <p>the table name</p> </li> <li> <p>the <code>StreamLabel</code> </p> </li> </ul>"""
    stream_status: NotRequired["capo_dynamodb_streams.types.stream_status.StreamStatus"]
    """<p>Indicates the current status of the stream:</p> <ul> <li> <p> <code>ENABLING</code> - Streams is currently being enabled on the DynamoDB table.</p> </li> <li> <p> <code>ENABLED</code> - the stream is enabled.</p> </li> <li> <p> <code>DISABLING</code> - Streams is currently being disabled on the DynamoDB table.</p> </li> <li> <p> <code>DISABLED</code> - the stream is disabled.</p> </li> </ul>"""
    stream_view_type: NotRequired[
        "capo_dynamodb_streams.types.stream_view_type.StreamViewType"
    ]
    """<p>Indicates the format of the records within this stream:</p> <ul> <li> <p> <code>KEYS_ONLY</code> - only the key attributes of items that were modified in the DynamoDB table.</p> </li> <li> <p> <code>NEW_IMAGE</code> - entire items from the table, as they appeared after they were modified.</p> </li> <li> <p> <code>OLD_IMAGE</code> - entire items from the table, as they appeared before they were modified.</p> </li> <li> <p> <code>NEW_AND_OLD_IMAGES</code> - both the new and the old images of the items from the table.</p> </li> </ul>"""
    creation_request_date_time: NotRequired["capo_dynamodb_streams.types.date.Date"]
    """<p>The date and time when the request to create this stream was issued.</p>"""
    table_name: NotRequired["capo_dynamodb_streams.types.table_name.TableName"]
    """<p>The DynamoDB table with which the stream is associated.</p>"""
    key_schema: NotRequired["capo_dynamodb_streams.types.key_schema.KeySchema"]
    """<p>The key attribute(s) of the stream's DynamoDB table.</p>"""
    shards: NotRequired[
        "capo_dynamodb_streams.types.shard_description_list.ShardDescriptionList"
    ]
    """<p>The shards that comprise the stream.</p>"""
    last_evaluated_shard_id: NotRequired["capo_dynamodb_streams.types.shard_id.ShardId"]
    """<p>The shard ID of the item where the operation stopped, inclusive of the previous result set. Use this value to start a new operation, excluding this value in the new request.</p> <p>If <code>LastEvaluatedShardId</code> is empty, then the "last page" of results has been processed and there is currently no more data to be retrieved.</p> <p>If <code>LastEvaluatedShardId</code> is not empty, it does not necessarily mean that there is more data in the result set. The only way to know when you have reached the end of the result set is when <code>LastEvaluatedShardId</code> is empty.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StreamDescription) -> dict:
    out: dict = {}
    if "stream_arn" in value:
        out["StreamArn"] = value["stream_arn"]
    if "stream_label" in value:
        out["StreamLabel"] = value["stream_label"]
    if "stream_status" in value:
        import capo_dynamodb_streams.types.stream_status

        out["StreamStatus"] = (
            capo_dynamodb_streams.types.stream_status.serialize_aws_json_1_0(
                value["stream_status"]
            )
        )
    if "stream_view_type" in value:
        import capo_dynamodb_streams.types.stream_view_type

        out["StreamViewType"] = (
            capo_dynamodb_streams.types.stream_view_type.serialize_aws_json_1_0(
                value["stream_view_type"]
            )
        )
    if "creation_request_date_time" in value:
        import capo_dynamodb_streams.types.date

        out["CreationRequestDateTime"] = (
            capo_dynamodb_streams.types.date.serialize_aws_json_1_0(
                value["creation_request_date_time"]
            )
        )
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "key_schema" in value:
        import capo_dynamodb_streams.types.key_schema

        out["KeySchema"] = (
            capo_dynamodb_streams.types.key_schema.serialize_aws_json_1_0(
                value["key_schema"]
            )
        )
    if "shards" in value:
        import capo_dynamodb_streams.types.shard_description_list

        out["Shards"] = (
            capo_dynamodb_streams.types.shard_description_list.serialize_aws_json_1_0(
                value["shards"]
            )
        )
    if "last_evaluated_shard_id" in value:
        out["LastEvaluatedShardId"] = value["last_evaluated_shard_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StreamDescription:
    out: StreamDescription = {}  # type: ignore[typeddict-item]
    if data.get("StreamArn") is not None:
        out["stream_arn"] = data["StreamArn"]
    if data.get("StreamLabel") is not None:
        out["stream_label"] = data["StreamLabel"]
    if data.get("StreamStatus") is not None:
        import capo_dynamodb_streams.types.stream_status

        out["stream_status"] = (
            capo_dynamodb_streams.types.stream_status.deserialize_aws_json_1_0(
                data["StreamStatus"]
            )
        )
    if data.get("StreamViewType") is not None:
        import capo_dynamodb_streams.types.stream_view_type

        out["stream_view_type"] = (
            capo_dynamodb_streams.types.stream_view_type.deserialize_aws_json_1_0(
                data["StreamViewType"]
            )
        )
    if data.get("CreationRequestDateTime") is not None:
        import capo_dynamodb_streams.types.date

        out["creation_request_date_time"] = (
            capo_dynamodb_streams.types.date.deserialize_aws_json_1_0(
                data["CreationRequestDateTime"]
            )
        )
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    if data.get("KeySchema") is not None:
        import capo_dynamodb_streams.types.key_schema

        out["key_schema"] = (
            capo_dynamodb_streams.types.key_schema.deserialize_aws_json_1_0(
                data["KeySchema"]
            )
        )
    if data.get("Shards") is not None:
        import capo_dynamodb_streams.types.shard_description_list

        out["shards"] = (
            capo_dynamodb_streams.types.shard_description_list.deserialize_aws_json_1_0(
                data["Shards"]
            )
        )
    if data.get("LastEvaluatedShardId") is not None:
        out["last_evaluated_shard_id"] = data["LastEvaluatedShardId"]
    return out
