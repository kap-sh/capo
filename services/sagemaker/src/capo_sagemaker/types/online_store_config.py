"""Generated from Smithy shape ``com.amazonaws.sagemaker#OnlineStoreConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.boolean
    import capo_sagemaker.types.online_store_security_config
    import capo_sagemaker.types.storage_type
    import capo_sagemaker.types.ttl_duration


class OnlineStoreConfig(TypedDict, closed=True):
    security_config: NotRequired[
        "capo_sagemaker.types.online_store_security_config.OnlineStoreSecurityConfig"
    ]
    """<p>Use to specify KMS Key ID (<code>KMSKeyId</code>) for at-rest encryption of your <code>OnlineStore</code>.</p>"""
    enable_online_store: NotRequired["capo_sagemaker.types.boolean.Boolean"]
    """<p>Turn <code>OnlineStore</code> off by specifying <code>False</code> for the <code>EnableOnlineStore</code> flag. Turn <code>OnlineStore</code> on by specifying <code>True</code> for the <code>EnableOnlineStore</code> flag. </p> <p>The default value is <code>False</code>.</p>"""
    ttl_duration: NotRequired["capo_sagemaker.types.ttl_duration.TtlDuration"]
    """<p>Time to live duration, where the record is hard deleted after the expiration time is reached; <code>ExpiresAt</code> = <code>EventTime</code> + <code>TtlDuration</code>. For information on HardDelete, see the <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_DeleteRecord.html">DeleteRecord</a> API in the Amazon SageMaker API Reference guide.</p>"""
    storage_type: NotRequired["capo_sagemaker.types.storage_type.StorageType"]
    """<p>Option for different tiers of low latency storage for real-time data retrieval.</p> <ul> <li> <p> <code>Standard</code>: A managed low latency data store for feature groups.</p> </li> <li> <p> <code>Standard_V2</code>: A managed low latency data store for feature groups that supports partial updates to individual features using the <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_UpdateRecord.html">UpdateRecord</a> operation. Choose this storage type at feature group creation time if your use case requires updating specific feature values without rewriting the entire record.</p> </li> <li> <p> <code>InMemory</code>: A managed data store for feature groups that supports very low latency retrieval.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OnlineStoreConfig) -> dict:
    out: dict = {}
    if "security_config" in value:
        import capo_sagemaker.types.online_store_security_config

        out["SecurityConfig"] = (
            capo_sagemaker.types.online_store_security_config.serialize_aws_json_1_1(
                value["security_config"]
            )
        )
    if "enable_online_store" in value:
        out["EnableOnlineStore"] = value["enable_online_store"]
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


def deserialize_aws_json_1_1(data: dict) -> OnlineStoreConfig:
    out: OnlineStoreConfig = {}  # type: ignore[typeddict-item]
    if data.get("SecurityConfig") is not None:
        import capo_sagemaker.types.online_store_security_config

        out["security_config"] = (
            capo_sagemaker.types.online_store_security_config.deserialize_aws_json_1_1(
                data["SecurityConfig"]
            )
        )
    if data.get("EnableOnlineStore") is not None:
        out["enable_online_store"] = data["EnableOnlineStore"]
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
