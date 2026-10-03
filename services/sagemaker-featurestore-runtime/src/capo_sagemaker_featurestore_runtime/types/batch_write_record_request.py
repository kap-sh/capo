"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#BatchWriteRecordRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_featurestore_runtime.types.batch_write_record_entries
    import capo_sagemaker_featurestore_runtime.types.ttl_duration


class BatchWriteRecordRequest(TypedDict, closed=True):
    entries: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.batch_write_record_entries.BatchWriteRecordEntries"
    ]
    """<p>A list of records to write. Each entry specifies the <code>FeatureGroup</code>, the record data, and optionally target stores and a TTL duration.</p>"""
    ttl_duration: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.ttl_duration.TtlDuration"
    ]
    """<p>Time to live duration applied to all entries in the batch that do not specify their own <code>TtlDuration</code>; <code>ExpiresAt</code> = <code>EventTime</code> + <code>TtlDuration</code>. For information on HardDelete, see the <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_DeleteRecord.html">DeleteRecord</a> API in the Amazon SageMaker API Reference guide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchWriteRecordRequest) -> dict:
    out: dict = {}
    if "entries" in value:
        import capo_sagemaker_featurestore_runtime.types.batch_write_record_entries

        out["Entries"] = (
            capo_sagemaker_featurestore_runtime.types.batch_write_record_entries.serialize_json(
                value["entries"]
            )
        )
    if "ttl_duration" in value:
        import capo_sagemaker_featurestore_runtime.types.ttl_duration

        out["TtlDuration"] = (
            capo_sagemaker_featurestore_runtime.types.ttl_duration.serialize_json(
                value["ttl_duration"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchWriteRecordRequest:
    out: BatchWriteRecordRequest = {}  # type: ignore[typeddict-item]
    if data.get("Entries") is not None:
        import capo_sagemaker_featurestore_runtime.types.batch_write_record_entries

        out["entries"] = (
            capo_sagemaker_featurestore_runtime.types.batch_write_record_entries.deserialize_json(
                data["Entries"]
            )
        )
    if data.get("TtlDuration") is not None:
        import capo_sagemaker_featurestore_runtime.types.ttl_duration

        out["ttl_duration"] = (
            capo_sagemaker_featurestore_runtime.types.ttl_duration.deserialize_json(
                data["TtlDuration"]
            )
        )
    return out
