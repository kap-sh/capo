"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateFeatureGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.description
    import capo_sagemaker.types.feature_definitions
    import capo_sagemaker.types.feature_group_name
    import capo_sagemaker.types.feature_name
    import capo_sagemaker.types.offline_store_config
    import capo_sagemaker.types.online_store_config
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.throughput_config


class CreateFeatureGroupRequest(TypedDict, closed=True):
    feature_group_name: NotRequired[
        "capo_sagemaker.types.feature_group_name.FeatureGroupName"
    ]
    """<p>The name of the <code>FeatureGroup</code>. The name must be unique within an Amazon Web Services Region in an Amazon Web Services account.</p> <p>The name:</p> <ul> <li> <p>Must start with an alphanumeric character.</p> </li> <li> <p>Can only include alphanumeric characters, underscores, and hyphens. Spaces are not allowed.</p> </li> </ul>"""
    record_identifier_feature_name: NotRequired[
        "capo_sagemaker.types.feature_name.FeatureName"
    ]
    """<p>The name of the <code>Feature</code> whose value uniquely identifies a <code>Record</code> defined in the <code>FeatureStore</code>. Only the latest record per identifier value will be stored in the <code>OnlineStore</code>. <code>RecordIdentifierFeatureName</code> must be one of feature definitions' names.</p> <p>You use the <code>RecordIdentifierFeatureName</code> to access data in a <code>FeatureStore</code>.</p> <p>This name:</p> <ul> <li> <p>Must start with an alphanumeric character.</p> </li> <li> <p>Can only contains alphanumeric characters, hyphens, underscores. Spaces are not allowed. </p> </li> </ul>"""
    event_time_feature_name: NotRequired[
        "capo_sagemaker.types.feature_name.FeatureName"
    ]
    """<p>The name of the feature that stores the <code>EventTime</code> of a <code>Record</code> in a <code>FeatureGroup</code>.</p> <p>An <code>EventTime</code> is a point in time when a new event occurs that corresponds to the creation or update of a <code>Record</code> in a <code>FeatureGroup</code>. All <code>Records</code> in the <code>FeatureGroup</code> must have a corresponding <code>EventTime</code>.</p> <p>An <code>EventTime</code> can be a <code>String</code> or <code>Fractional</code>. </p> <ul> <li> <p> <code>Fractional</code>: <code>EventTime</code> feature values must be a Unix timestamp in seconds.</p> </li> <li> <p> <code>String</code>: <code>EventTime</code> feature values must be an ISO-8601 string in the format. The following formats are supported <code>yyyy-MM-dd'T'HH:mm:ssZ</code> and <code>yyyy-MM-dd'T'HH:mm:ss.SSSZ</code> where <code>yyyy</code>, <code>MM</code>, and <code>dd</code> represent the year, month, and day respectively and <code>HH</code>, <code>mm</code>, <code>ss</code>, and if applicable, <code>SSS</code> represent the hour, month, second and milliseconds respsectively. <code>'T'</code> and <code>Z</code> are constants.</p> </li> </ul>"""
    feature_definitions: NotRequired[
        "capo_sagemaker.types.feature_definitions.FeatureDefinitions"
    ]
    """<p>A list of <code>Feature</code> names and types. <code>Name</code> and <code>Type</code> is compulsory per <code>Feature</code>. </p> <p>Valid feature <code>FeatureType</code>s are <code>Integral</code>, <code>Fractional</code> and <code>String</code>.</p> <p> <code>FeatureName</code>s cannot be any of the following: <code>is_deleted</code>, <code>write_time</code>, <code>api_invocation_time</code> </p> <p>You can create up to 2,500 <code>FeatureDefinition</code>s per <code>FeatureGroup</code>.</p>"""
    online_store_config: NotRequired[
        "capo_sagemaker.types.online_store_config.OnlineStoreConfig"
    ]
    """<p>You can turn the <code>OnlineStore</code> on or off by specifying <code>True</code> for the <code>EnableOnlineStore</code> flag in <code>OnlineStoreConfig</code>.</p> <p>You can also include an Amazon Web Services KMS key ID (<code>KMSKeyId</code>) for at-rest encryption of the <code>OnlineStore</code>.</p> <p>The default value is <code>False</code>.</p>"""
    offline_store_config: NotRequired[
        "capo_sagemaker.types.offline_store_config.OfflineStoreConfig"
    ]
    """<p>Use this to configure an <code>OfflineFeatureStore</code>. This parameter allows you to specify:</p> <ul> <li> <p>The Amazon Simple Storage Service (Amazon S3) location of an <code>OfflineStore</code>.</p> </li> <li> <p>A configuration for an Amazon Web Services Glue or Amazon Web Services Hive data catalog. </p> </li> <li> <p>An KMS encryption key to encrypt the Amazon S3 location used for <code>OfflineStore</code>. If KMS encryption key is not specified, by default we encrypt all data at rest using Amazon Web Services KMS key. By defining your <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-key.html">bucket-level key</a> for SSE, you can reduce Amazon Web Services KMS requests costs by up to 99 percent.</p> </li> <li> <p>Format for the offline store table. Supported formats are Glue (Default) and <a href="https://iceberg.apache.org/">Apache Iceberg</a>.</p> </li> </ul> <p>To learn more about this parameter, see <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OfflineStoreConfig.html">OfflineStoreConfig</a>.</p>"""
    throughput_config: NotRequired[
        "capo_sagemaker.types.throughput_config.ThroughputConfig"
    ]
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM execution role used to persist data into the <code>OfflineStore</code> if an <code>OfflineStoreConfig</code> is provided.</p>"""
    description: NotRequired["capo_sagemaker.types.description.Description"]
    """<p>A free-form description of a <code>FeatureGroup</code>.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>Tags used to identify <code>Features</code> in each <code>FeatureGroup</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFeatureGroupRequest) -> dict:
    out: dict = {}
    if "feature_group_name" in value:
        out["FeatureGroupName"] = value["feature_group_name"]
    if "record_identifier_feature_name" in value:
        out["RecordIdentifierFeatureName"] = value["record_identifier_feature_name"]
    if "event_time_feature_name" in value:
        out["EventTimeFeatureName"] = value["event_time_feature_name"]
    if "feature_definitions" in value:
        import capo_sagemaker.types.feature_definitions

        out["FeatureDefinitions"] = (
            capo_sagemaker.types.feature_definitions.serialize_aws_json_1_1(
                value["feature_definitions"]
            )
        )
    if "online_store_config" in value:
        import capo_sagemaker.types.online_store_config

        out["OnlineStoreConfig"] = (
            capo_sagemaker.types.online_store_config.serialize_aws_json_1_1(
                value["online_store_config"]
            )
        )
    if "offline_store_config" in value:
        import capo_sagemaker.types.offline_store_config

        out["OfflineStoreConfig"] = (
            capo_sagemaker.types.offline_store_config.serialize_aws_json_1_1(
                value["offline_store_config"]
            )
        )
    if "throughput_config" in value:
        import capo_sagemaker.types.throughput_config

        out["ThroughputConfig"] = (
            capo_sagemaker.types.throughput_config.serialize_aws_json_1_1(
                value["throughput_config"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFeatureGroupRequest:
    out: CreateFeatureGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("FeatureGroupName") is not None:
        out["feature_group_name"] = data["FeatureGroupName"]
    if data.get("RecordIdentifierFeatureName") is not None:
        out["record_identifier_feature_name"] = data["RecordIdentifierFeatureName"]
    if data.get("EventTimeFeatureName") is not None:
        out["event_time_feature_name"] = data["EventTimeFeatureName"]
    if data.get("FeatureDefinitions") is not None:
        import capo_sagemaker.types.feature_definitions

        out["feature_definitions"] = (
            capo_sagemaker.types.feature_definitions.deserialize_aws_json_1_1(
                data["FeatureDefinitions"]
            )
        )
    if data.get("OnlineStoreConfig") is not None:
        import capo_sagemaker.types.online_store_config

        out["online_store_config"] = (
            capo_sagemaker.types.online_store_config.deserialize_aws_json_1_1(
                data["OnlineStoreConfig"]
            )
        )
    if data.get("OfflineStoreConfig") is not None:
        import capo_sagemaker.types.offline_store_config

        out["offline_store_config"] = (
            capo_sagemaker.types.offline_store_config.deserialize_aws_json_1_1(
                data["OfflineStoreConfig"]
            )
        )
    if data.get("ThroughputConfig") is not None:
        import capo_sagemaker.types.throughput_config

        out["throughput_config"] = (
            capo_sagemaker.types.throughput_config.deserialize_aws_json_1_1(
                data["ThroughputConfig"]
            )
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
