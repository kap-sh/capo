"""Generated from Smithy shape ``com.amazonaws.kinesis#SubscribeToShardEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_kinesis.types.child_shard_list
    import capo_kinesis.types.millis_behind_latest
    import capo_kinesis.types.record_list
    import capo_kinesis.types.sequence_number


class SubscribeToShardEvent(TypedDict, closed=True):
    records: "capo_kinesis.types.record_list.RecordList"
    """<p></p>"""
    continuation_sequence_number: "capo_kinesis.types.sequence_number.SequenceNumber"
    """<p>Use this as <code>SequenceNumber</code> in the next call to <a>SubscribeToShard</a>, with <code>StartingPosition</code> set to <code>AT_SEQUENCE_NUMBER</code> or <code>AFTER_SEQUENCE_NUMBER</code>. Use <code>ContinuationSequenceNumber</code> for checkpointing because it captures your shard progress even when no data is written to the shard.</p>"""
    millis_behind_latest: "capo_kinesis.types.millis_behind_latest.MillisBehindLatest"
    """<p>The number of milliseconds the read records are from the tip of the stream, indicating how far behind current time the consumer is. A value of zero indicates that record processing is caught up, and there are no new records to process at this moment.</p>"""
    child_shards: NotRequired["capo_kinesis.types.child_shard_list.ChildShardList"]
    """<p>The list of the child shards of the current shard, returned only at the end of the current shard.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubscribeToShardEvent) -> dict:
    out: dict = {}
    import capo_kinesis.types.record_list

    out["Records"] = capo_kinesis.types.record_list.serialize_aws_json_1_1(
        value["records"]
    )
    out["ContinuationSequenceNumber"] = value["continuation_sequence_number"]
    out["MillisBehindLatest"] = value["millis_behind_latest"]
    if "child_shards" in value:
        import capo_kinesis.types.child_shard_list

        out["ChildShards"] = capo_kinesis.types.child_shard_list.serialize_aws_json_1_1(
            value["child_shards"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SubscribeToShardEvent:
    out: SubscribeToShardEvent = {}  # type: ignore[typeddict-item]
    if data.get("Records") is not None:
        import capo_kinesis.types.record_list

        out["records"] = capo_kinesis.types.record_list.deserialize_aws_json_1_1(
            data["Records"]
        )
    else:
        out["records"] = []
    if data.get("ContinuationSequenceNumber") is not None:
        out["continuation_sequence_number"] = data["ContinuationSequenceNumber"]
    else:
        out["continuation_sequence_number"] = ""
    if data.get("MillisBehindLatest") is not None:
        out["millis_behind_latest"] = data["MillisBehindLatest"]
    else:
        out["millis_behind_latest"] = 0
    if data.get("ChildShards") is not None:
        import capo_kinesis.types.child_shard_list

        out["child_shards"] = (
            capo_kinesis.types.child_shard_list.deserialize_aws_json_1_1(
                data["ChildShards"]
            )
        )
    return out


def serialize_event_aws_json_1_1(value: SubscribeToShardEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "SubscribeToShardEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_aws_json_1_1(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_aws_json_1_1(message: Message) -> SubscribeToShardEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: SubscribeToShardEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_aws_json_1_1(json.loads(payload))
    return out
