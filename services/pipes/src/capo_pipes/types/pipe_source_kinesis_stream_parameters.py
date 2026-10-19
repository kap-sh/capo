"""Generated from Smithy shape ``com.amazonaws.pipes#PipeSourceKinesisStreamParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.dead_letter_config
    import capo_pipes.types.kinesis_stream_start_position
    import capo_pipes.types.limit_max10
    import capo_pipes.types.limit_max10000
    import capo_pipes.types.maximum_batching_window_in_seconds
    import capo_pipes.types.maximum_record_age_in_seconds
    import capo_pipes.types.maximum_retry_attempts_esm
    import capo_pipes.types.on_partial_batch_item_failure_streams
    import capo_pipes.types.timestamp


class PipeSourceKinesisStreamParameters(TypedDict, closed=True):
    batch_size: NotRequired["capo_pipes.types.limit_max10000.LimitMax10000"]
    """<p>The maximum number of records to include in each batch.</p>"""
    dead_letter_config: NotRequired[
        "capo_pipes.types.dead_letter_config.DeadLetterConfig"
    ]
    """<p>Define the target queue to send dead-letter queue events to.</p>"""
    on_partial_batch_item_failure: NotRequired[
        "capo_pipes.types.on_partial_batch_item_failure_streams.OnPartialBatchItemFailureStreams"
    ]
    """<p>Define how to handle item process failures. <code>AUTOMATIC_BISECT</code> halves each batch and retry each half until all the records are processed or there is one failed message left in the batch.</p>"""
    maximum_batching_window_in_seconds: NotRequired[
        "capo_pipes.types.maximum_batching_window_in_seconds.MaximumBatchingWindowInSeconds"
    ]
    """<p>The maximum length of a time to wait for events.</p>"""
    maximum_record_age_in_seconds: NotRequired[
        "capo_pipes.types.maximum_record_age_in_seconds.MaximumRecordAgeInSeconds"
    ]
    """<p>Discard records older than the specified age. The default value is -1, which sets the maximum age to infinite. When the value is set to infinite, EventBridge never discards old records. </p>"""
    maximum_retry_attempts: NotRequired[
        "capo_pipes.types.maximum_retry_attempts_esm.MaximumRetryAttemptsESM"
    ]
    """<p>Discard records after the specified number of retries. The default value is -1, which sets the maximum number of retries to infinite. When MaximumRetryAttempts is infinite, EventBridge retries failed records until the record expires in the event source.</p>"""
    parallelization_factor: NotRequired["capo_pipes.types.limit_max10.LimitMax10"]
    """<p>The number of batches to process concurrently from each shard. The default value is 1.</p>"""
    starting_position: (
        "capo_pipes.types.kinesis_stream_start_position.KinesisStreamStartPosition"
    )
    """<p>The position in a stream from which to start reading.</p>"""
    starting_position_timestamp: NotRequired["capo_pipes.types.timestamp.Timestamp"]
    """<p>With <code>StartingPosition</code> set to <code>AT_TIMESTAMP</code>, the time from which to start reading, in Unix time seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipeSourceKinesisStreamParameters) -> dict:
    out: dict = {}
    if "batch_size" in value:
        out["BatchSize"] = value["batch_size"]
    if "dead_letter_config" in value:
        import capo_pipes.types.dead_letter_config

        out["DeadLetterConfig"] = capo_pipes.types.dead_letter_config.serialize_json(
            value["dead_letter_config"]
        )
    if "on_partial_batch_item_failure" in value:
        out["OnPartialBatchItemFailure"] = value["on_partial_batch_item_failure"]
    if "maximum_batching_window_in_seconds" in value:
        out["MaximumBatchingWindowInSeconds"] = value[
            "maximum_batching_window_in_seconds"
        ]
    if "maximum_record_age_in_seconds" in value:
        out["MaximumRecordAgeInSeconds"] = value["maximum_record_age_in_seconds"]
    if "maximum_retry_attempts" in value:
        out["MaximumRetryAttempts"] = value["maximum_retry_attempts"]
    if "parallelization_factor" in value:
        out["ParallelizationFactor"] = value["parallelization_factor"]
    out["StartingPosition"] = value["starting_position"]
    if "starting_position_timestamp" in value:
        import capo_pipes.types.timestamp

        out["StartingPositionTimestamp"] = capo_pipes.types.timestamp.serialize_json(
            value["starting_position_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> PipeSourceKinesisStreamParameters:
    out: PipeSourceKinesisStreamParameters = {}  # type: ignore[typeddict-item]
    if data.get("BatchSize") is not None:
        out["batch_size"] = data["BatchSize"]
    if data.get("DeadLetterConfig") is not None:
        import capo_pipes.types.dead_letter_config

        out["dead_letter_config"] = (
            capo_pipes.types.dead_letter_config.deserialize_json(
                data["DeadLetterConfig"]
            )
        )
    if data.get("OnPartialBatchItemFailure") is not None:
        out["on_partial_batch_item_failure"] = data["OnPartialBatchItemFailure"]
    if data.get("MaximumBatchingWindowInSeconds") is not None:
        out["maximum_batching_window_in_seconds"] = data[
            "MaximumBatchingWindowInSeconds"
        ]
    if data.get("MaximumRecordAgeInSeconds") is not None:
        out["maximum_record_age_in_seconds"] = data["MaximumRecordAgeInSeconds"]
    if data.get("MaximumRetryAttempts") is not None:
        out["maximum_retry_attempts"] = data["MaximumRetryAttempts"]
    if data.get("ParallelizationFactor") is not None:
        out["parallelization_factor"] = data["ParallelizationFactor"]
    if data.get("StartingPosition") is not None:
        out["starting_position"] = data["StartingPosition"]
    else:
        out["starting_position"] = ""
    if data.get("StartingPositionTimestamp") is not None:
        import capo_pipes.types.timestamp

        out["starting_position_timestamp"] = (
            capo_pipes.types.timestamp.deserialize_json(
                data["StartingPositionTimestamp"]
            )
        )
    return out
