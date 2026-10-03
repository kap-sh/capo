"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#PutRecordRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_featurestore_runtime.types.feature_group_name_or_arn
    import capo_sagemaker_featurestore_runtime.types.record
    import capo_sagemaker_featurestore_runtime.types.target_stores
    import capo_sagemaker_featurestore_runtime.types.ttl_duration


class PutRecordRequest(TypedDict, closed=True):
    feature_group_name: "capo_sagemaker_featurestore_runtime.types.feature_group_name_or_arn.FeatureGroupNameOrArn"
    """<p>The name or Amazon Resource Name (ARN) of the feature group that you want to insert the record into.</p>"""
    record: NotRequired["capo_sagemaker_featurestore_runtime.types.record.Record"]
    """<p>List of FeatureValues to be inserted. This will be a full over-write. If you only want to update few of the feature values, do the following:</p> <ul> <li> <p>Use <code>GetRecord</code> to retrieve the latest record.</p> </li> <li> <p>Update the record returned from <code>GetRecord</code>. </p> </li> <li> <p>Use <code>PutRecord</code> to update feature values.</p> </li> </ul>"""
    target_stores: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.target_stores.TargetStores"
    ]
    """<p>A list of stores to which you're adding the record. By default, Feature Store adds the record to all of the stores that you're using for the <code>FeatureGroup</code>.</p>"""
    ttl_duration: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.ttl_duration.TtlDuration"
    ]
    """<p>Time to live duration, where the record is hard deleted after the expiration time is reached; <code>ExpiresAt</code> = <code>EventTime</code> + <code>TtlDuration</code>. For information on HardDelete, see the <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_DeleteRecord.html">DeleteRecord</a> API in the Amazon SageMaker API Reference guide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutRecordRequest) -> dict:
    out: dict = {}
    if "record" in value:
        import capo_sagemaker_featurestore_runtime.types.record

        out["Record"] = capo_sagemaker_featurestore_runtime.types.record.serialize_json(
            value["record"]
        )
    if "target_stores" in value:
        import capo_sagemaker_featurestore_runtime.types.target_stores

        out["TargetStores"] = (
            capo_sagemaker_featurestore_runtime.types.target_stores.serialize_json(
                value["target_stores"]
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


def deserialize_json(data: dict) -> PutRecordRequest:
    out: PutRecordRequest = {}  # type: ignore[typeddict-item]
    if data.get("Record") is not None:
        import capo_sagemaker_featurestore_runtime.types.record

        out["record"] = (
            capo_sagemaker_featurestore_runtime.types.record.deserialize_json(
                data["Record"]
            )
        )
    if data.get("TargetStores") is not None:
        import capo_sagemaker_featurestore_runtime.types.target_stores

        out["target_stores"] = (
            capo_sagemaker_featurestore_runtime.types.target_stores.deserialize_json(
                data["TargetStores"]
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
