"""Generated from Smithy shape ``com.amazonaws.pipes#PipeSourceManagedStreamingKafkaParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_pipes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pipes.types.kafka_topic_name
    import capo_pipes.types.limit_max10000
    import capo_pipes.types.maximum_batching_window_in_seconds
    import capo_pipes.types.msk_access_credentials
    import capo_pipes.types.msk_start_position
    import capo_pipes.types.uri


class PipeSourceManagedStreamingKafkaParameters(TypedDict, closed=True):
    topic_name: "capo_pipes.types.kafka_topic_name.KafkaTopicName"
    """<p>The name of the topic that the pipe will read from.</p>"""
    starting_position: NotRequired[
        "capo_pipes.types.msk_start_position.MSKStartPosition"
    ]
    """<p>The position in a stream from which to start reading.</p>"""
    batch_size: NotRequired["capo_pipes.types.limit_max10000.LimitMax10000"]
    """<p>The maximum number of records to include in each batch.</p>"""
    maximum_batching_window_in_seconds: NotRequired[
        "capo_pipes.types.maximum_batching_window_in_seconds.MaximumBatchingWindowInSeconds"
    ]
    """<p>The maximum length of a time to wait for events.</p>"""
    consumer_group_id: NotRequired["capo_pipes.types.uri.URI"]
    """<p>The name of the destination queue to consume.</p>"""
    credentials: NotRequired[
        "capo_pipes.types.msk_access_credentials.MSKAccessCredentials"
    ]
    """<p>The credentials needed to access the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipeSourceManagedStreamingKafkaParameters) -> dict:
    out: dict = {}
    out["TopicName"] = value["topic_name"]
    if "starting_position" in value:
        out["StartingPosition"] = value["starting_position"]
    if "batch_size" in value:
        out["BatchSize"] = value["batch_size"]
    if "maximum_batching_window_in_seconds" in value:
        out["MaximumBatchingWindowInSeconds"] = value[
            "maximum_batching_window_in_seconds"
        ]
    if "consumer_group_id" in value:
        out["ConsumerGroupID"] = value["consumer_group_id"]
    if "credentials" in value:
        import capo_pipes.types.msk_access_credentials

        out["Credentials"] = capo_pipes.types.msk_access_credentials.serialize_json(
            value["credentials"]
        )
    return out


def deserialize_json(data: dict) -> PipeSourceManagedStreamingKafkaParameters:
    out: PipeSourceManagedStreamingKafkaParameters = {}  # type: ignore[typeddict-item]
    if data.get("TopicName") is not None:
        out["topic_name"] = data["TopicName"]
    else:
        raise DeserializationError(
            "PipeSourceManagedStreamingKafkaParameters.topic_name required"
        )
    if data.get("StartingPosition") is not None:
        out["starting_position"] = data["StartingPosition"]
    if data.get("BatchSize") is not None:
        out["batch_size"] = data["BatchSize"]
    if data.get("MaximumBatchingWindowInSeconds") is not None:
        out["maximum_batching_window_in_seconds"] = data[
            "MaximumBatchingWindowInSeconds"
        ]
    if data.get("ConsumerGroupID") is not None:
        out["consumer_group_id"] = data["ConsumerGroupID"]
    if data.get("Credentials") is not None:
        import capo_pipes.types.msk_access_credentials

        out["credentials"] = capo_pipes.types.msk_access_credentials.deserialize_json(
            data["Credentials"]
        )
    return out


def redact_sensitive(
    value: PipeSourceManagedStreamingKafkaParameters,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "topic_name" in value:
        out["topic_name"] = "*** Sensitive Data Redacted ***"
    if "consumer_group_id" in value:
        out["consumer_group_id"] = "*** Sensitive Data Redacted ***"
    return out
