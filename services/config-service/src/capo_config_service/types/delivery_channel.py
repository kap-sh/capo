"""Generated from Smithy shape ``com.amazonaws.configservice#DeliveryChannel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.channel_name
    import capo_config_service.types.config_snapshot_delivery_properties
    import capo_config_service.types.string


class DeliveryChannel(TypedDict, closed=True):
    name: NotRequired["capo_config_service.types.channel_name.ChannelName"]
    """<p>The name of the delivery channel. By default, Config assigns the name "default" when creating the delivery channel. To change the delivery channel name, you must use the DeleteDeliveryChannel action to delete your current delivery channel, and then you must use the PutDeliveryChannel command to create a delivery channel that has the desired name.</p>"""
    s3_bucket_name: NotRequired["capo_config_service.types.string.String"]
    """<p>The name of the Amazon S3 bucket to which Config delivers configuration snapshots and configuration history files.</p> <p>If you specify a bucket that belongs to another Amazon Web Services account, that bucket must have policies that grant access permissions to Config. For more information, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-policy.html">Permissions for the Amazon S3 Bucket</a> in the <i>Config Developer Guide</i>.</p>"""
    s3_key_prefix: NotRequired["capo_config_service.types.string.String"]
    """<p>The prefix for the specified Amazon S3 bucket.</p>"""
    s3_kms_key_arn: NotRequired["capo_config_service.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Key Management Service (KMS ) KMS key (KMS key) used to encrypt objects delivered by Config. Must belong to the same Region as the destination S3 bucket.</p>"""
    sns_topic_arn: NotRequired["capo_config_service.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Amazon SNS topic to which Config sends notifications about configuration changes.</p> <p>If you choose a topic from another account, the topic must have policies that grant access permissions to Config. For more information, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/sns-topic-policy.html">Permissions for the Amazon SNS Topic</a> in the <i>Config Developer Guide</i>.</p>"""
    config_snapshot_delivery_properties: NotRequired[
        "capo_config_service.types.config_snapshot_delivery_properties.ConfigSnapshotDeliveryProperties"
    ]
    """<p>The options for how often Config delivers configuration snapshots to the Amazon S3 bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliveryChannel) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "s3_bucket_name" in value:
        out["s3BucketName"] = value["s3_bucket_name"]
    if "s3_key_prefix" in value:
        out["s3KeyPrefix"] = value["s3_key_prefix"]
    if "s3_kms_key_arn" in value:
        out["s3KmsKeyArn"] = value["s3_kms_key_arn"]
    if "sns_topic_arn" in value:
        out["snsTopicARN"] = value["sns_topic_arn"]
    if "config_snapshot_delivery_properties" in value:
        import capo_config_service.types.config_snapshot_delivery_properties

        out["configSnapshotDeliveryProperties"] = (
            capo_config_service.types.config_snapshot_delivery_properties.serialize_aws_json_1_1(
                value["config_snapshot_delivery_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeliveryChannel:
    out: DeliveryChannel = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("s3BucketName") is not None:
        out["s3_bucket_name"] = data["s3BucketName"]
    if data.get("s3KeyPrefix") is not None:
        out["s3_key_prefix"] = data["s3KeyPrefix"]
    if data.get("s3KmsKeyArn") is not None:
        out["s3_kms_key_arn"] = data["s3KmsKeyArn"]
    if data.get("snsTopicARN") is not None:
        out["sns_topic_arn"] = data["snsTopicARN"]
    if data.get("configSnapshotDeliveryProperties") is not None:
        import capo_config_service.types.config_snapshot_delivery_properties

        out["config_snapshot_delivery_properties"] = (
            capo_config_service.types.config_snapshot_delivery_properties.deserialize_aws_json_1_1(
                data["configSnapshotDeliveryProperties"]
            )
        )
    return out
