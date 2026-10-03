"""Generated from Smithy shape ``com.amazonaws.sagemaker#OnlineStoreConfigUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.storage_type
    import capo_sagemaker.types.ttl_duration


class OnlineStoreConfigUpdate(TypedDict, closed=True):
    ttl_duration: NotRequired["capo_sagemaker.types.ttl_duration.TtlDuration"]
    """<p>Time to live duration, where the record is hard deleted after the expiration time is reached; <code>ExpiresAt</code> = <code>EventTime</code> + <code>TtlDuration</code>. For information on HardDelete, see the <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_DeleteRecord.html">DeleteRecord</a> API in the Amazon SageMaker API Reference guide.</p>"""
    storage_type: NotRequired["capo_sagemaker.types.storage_type.StorageType"]
    """<p>The online store storage type to migrate the feature group to. Use this parameter to migrate an existing feature group from <code>Standard</code> to <code>Standard_V2</code> storage format, enabling support for the <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_UpdateRecord.html">UpdateRecord</a> operation. Migration is a one-way operation and cannot be reversed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OnlineStoreConfigUpdate) -> dict:
    out: dict = {}
    if "ttl_duration" in value:
        import capo_sagemaker.types.ttl_duration

        out["TtlDuration"] = capo_sagemaker.types.ttl_duration.serialize_aws_json_1_1(
            value["ttl_duration"]
        )
    if "storage_type" in value:
        import capo_sagemaker.types.storage_type

        out["StorageType"] = capo_sagemaker.types.storage_type.serialize_aws_json_1_1(
            value["storage_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OnlineStoreConfigUpdate:
    out: OnlineStoreConfigUpdate = {}  # type: ignore[typeddict-item]
    if data.get("TtlDuration") is not None:
        import capo_sagemaker.types.ttl_duration

        out["ttl_duration"] = (
            capo_sagemaker.types.ttl_duration.deserialize_aws_json_1_1(
                data["TtlDuration"]
            )
        )
    if data.get("StorageType") is not None:
        import capo_sagemaker.types.storage_type

        out["storage_type"] = (
            capo_sagemaker.types.storage_type.deserialize_aws_json_1_1(
                data["StorageType"]
            )
        )
    return out
