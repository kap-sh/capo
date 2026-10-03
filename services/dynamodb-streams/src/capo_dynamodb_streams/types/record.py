"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#Record``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb_streams.types.identity
    import capo_dynamodb_streams.types.operation_type
    import capo_dynamodb_streams.types.stream_record
    import capo_dynamodb_streams.types.string


class Record(TypedDict, closed=True):
    event_id: NotRequired["capo_dynamodb_streams.types.string.String"]
    """<p>A globally unique identifier for the event that was recorded in this stream record.</p>"""
    event_name: NotRequired["capo_dynamodb_streams.types.operation_type.OperationType"]
    """<p>The type of data modification that was performed on the DynamoDB table:</p> <ul> <li> <p> <code>INSERT</code> - a new item was added to the table.</p> </li> <li> <p> <code>MODIFY</code> - one or more of an existing item's attributes were modified.</p> </li> <li> <p> <code>REMOVE</code> - the item was deleted from the table</p> </li> </ul>"""
    event_version: NotRequired["capo_dynamodb_streams.types.string.String"]
    """<p>The version number of the stream record format. This number is updated whenever the structure of <code>Record</code> is modified.</p> <p>Client applications must not assume that <code>eventVersion</code> will remain at a particular value, as this number is subject to change at any time. In general, <code>eventVersion</code> will only increase as the low-level DynamoDB Streams API evolves.</p>"""
    event_source: NotRequired["capo_dynamodb_streams.types.string.String"]
    """<p>The Amazon Web Services service from which the stream record originated. For DynamoDB Streams, this is <code>aws:dynamodb</code>.</p>"""
    aws_region: NotRequired["capo_dynamodb_streams.types.string.String"]
    """<p>The region in which the <code>GetRecords</code> request was received.</p>"""
    dynamodb: NotRequired["capo_dynamodb_streams.types.stream_record.StreamRecord"]
    """<p>The main body of the stream record, containing all of the DynamoDB-specific fields.</p>"""
    user_identity: NotRequired["capo_dynamodb_streams.types.identity.Identity"]
    """<p>Items that are deleted by the Time to Live process after expiration have the following fields: </p> <ul> <li> <p>Records[].userIdentity.type</p> <p>"Service"</p> </li> <li> <p>Records[].userIdentity.principalId</p> <p>"dynamodb.amazonaws.com"</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Record) -> dict:
    out: dict = {}
    if "event_id" in value:
        out["eventID"] = value["event_id"]
    if "event_name" in value:
        import capo_dynamodb_streams.types.operation_type

        out["eventName"] = (
            capo_dynamodb_streams.types.operation_type.serialize_aws_json_1_0(
                value["event_name"]
            )
        )
    if "event_version" in value:
        out["eventVersion"] = value["event_version"]
    if "event_source" in value:
        out["eventSource"] = value["event_source"]
    if "aws_region" in value:
        out["awsRegion"] = value["aws_region"]
    if "dynamodb" in value:
        import capo_dynamodb_streams.types.stream_record

        out["dynamodb"] = (
            capo_dynamodb_streams.types.stream_record.serialize_aws_json_1_0(
                value["dynamodb"]
            )
        )
    if "user_identity" in value:
        import capo_dynamodb_streams.types.identity

        out["userIdentity"] = (
            capo_dynamodb_streams.types.identity.serialize_aws_json_1_0(
                value["user_identity"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Record:
    out: Record = {}  # type: ignore[typeddict-item]
    if data.get("eventID") is not None:
        out["event_id"] = data["eventID"]
    if data.get("eventName") is not None:
        import capo_dynamodb_streams.types.operation_type

        out["event_name"] = (
            capo_dynamodb_streams.types.operation_type.deserialize_aws_json_1_0(
                data["eventName"]
            )
        )
    if data.get("eventVersion") is not None:
        out["event_version"] = data["eventVersion"]
    if data.get("eventSource") is not None:
        out["event_source"] = data["eventSource"]
    if data.get("awsRegion") is not None:
        out["aws_region"] = data["awsRegion"]
    if data.get("dynamodb") is not None:
        import capo_dynamodb_streams.types.stream_record

        out["dynamodb"] = (
            capo_dynamodb_streams.types.stream_record.deserialize_aws_json_1_0(
                data["dynamodb"]
            )
        )
    if data.get("userIdentity") is not None:
        import capo_dynamodb_streams.types.identity

        out["user_identity"] = (
            capo_dynamodb_streams.types.identity.deserialize_aws_json_1_0(
                data["userIdentity"]
            )
        )
    return out
