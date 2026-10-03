"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#UpdateRecordRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_featurestore_runtime.types.feature_group_name_or_arn
    import capo_sagemaker_featurestore_runtime.types.record
    import capo_sagemaker_featurestore_runtime.types.target_stores
    import capo_sagemaker_featurestore_runtime.types.ttl_duration
    import capo_sagemaker_featurestore_runtime.types.value_as_string


class UpdateRecordRequest(TypedDict, closed=True):
    feature_group_name: "capo_sagemaker_featurestore_runtime.types.feature_group_name_or_arn.FeatureGroupNameOrArn"
    """<p>The identifier for the feature group that contains the record to update. You can specify one of the following:</p> <ul> <li> <p>The feature group name.</p> </li> <li> <p>The feature group Amazon Resource Name (ARN).</p> </li> </ul>"""
    record_identifier_value_as_string: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.value_as_string.ValueAsString"
    ]
    """<p>The value that uniquely identifies the record in the feature group. This must match the value defined by the feature group's record identifier feature.</p>"""
    features: NotRequired["capo_sagemaker_featurestore_runtime.types.record.Record"]
    """<p>The feature values to write to the record.</p>"""
    target_stores: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.target_stores.TargetStores"
    ]
    """<p>The target stores for the record update. By default, Amazon SageMaker Feature Store updates the record in all stores associated with the <code>FeatureGroup</code>.</p>"""
    ttl_duration: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.ttl_duration.TtlDuration"
    ]
    """<p>The time-to-live (TTL) duration for the record. Amazon SageMaker Feature Store deletes the record when <code>EventTime</code> + <code>TtlDuration</code> elapses. If you omit this parameter, the record's existing TTL setting remains unchanged. For information about <code>HardDelete</code>, see the <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_DeleteRecord.html">DeleteRecord</a> operation in the Amazon SageMaker API Reference.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecordRequest) -> dict:
    out: dict = {}
    if "record_identifier_value_as_string" in value:
        out["RecordIdentifierValueAsString"] = value[
            "record_identifier_value_as_string"
        ]
    if "features" in value:
        import capo_sagemaker_featurestore_runtime.types.record

        out["Features"] = (
            capo_sagemaker_featurestore_runtime.types.record.serialize_json(
                value["features"]
            )
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


def deserialize_json(data: dict) -> UpdateRecordRequest:
    out: UpdateRecordRequest = {}  # type: ignore[typeddict-item]
    if data.get("RecordIdentifierValueAsString") is not None:
        out["record_identifier_value_as_string"] = data["RecordIdentifierValueAsString"]
    if data.get("Features") is not None:
        import capo_sagemaker_featurestore_runtime.types.record

        out["features"] = (
            capo_sagemaker_featurestore_runtime.types.record.deserialize_json(
                data["Features"]
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
