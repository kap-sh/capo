"""Generated from Smithy shape ``com.amazonaws.sagemaker#ExtensionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_arn
    import capo_sagemaker.types.extension_arn
    import capo_sagemaker.types.extension_configuration_values
    import capo_sagemaker.types.extension_name
    import capo_sagemaker.types.extension_status
    import capo_sagemaker.types.extension_version
    import capo_sagemaker.types.timestamp


class ExtensionDetails(TypedDict, closed=True):
    cluster_arn: NotRequired["capo_sagemaker.types.cluster_arn.ClusterArn"]
    """<p>The Amazon Resource Name (ARN) of the SageMaker HyperPod cluster on which the extension is installed.</p>"""
    extension_arn: NotRequired["capo_sagemaker.types.extension_arn.ExtensionArn"]
    """<p>The Amazon Resource Name (ARN) of the extension.</p>"""
    extension_name: NotRequired["capo_sagemaker.types.extension_name.ExtensionName"]
    """<p>The name of the extension.</p>"""
    extension_version: NotRequired[
        "capo_sagemaker.types.extension_version.ExtensionVersion"
    ]
    """<p>The version of the extension. While SageMaker HyperPod creates or updates the extension, some nodes might still run a different version. To see how many nodes run this version, see <code>NodeSummary</code>.</p>"""
    status: NotRequired["capo_sagemaker.types.extension_status.ExtensionStatus"]
    """<p>The status of the extension can be one of the following values:</p> <dl> <dt>Creating</dt> <dd> <p>SageMaker HyperPod is installing the extension on the cluster's nodes.</p> </dd> <dt>Active</dt> <dd> <p>The extension runs its current version and configuration on all of the cluster's nodes.</p> </dd> <dt>Updating</dt> <dd> <p>SageMaker HyperPod is applying a configuration change or version update to the cluster's nodes.</p> </dd> <dt>Degraded</dt> <dd> <p>The extension runs its current version and configuration on some of the cluster's nodes but not all of them. Or, at least one node recently reported that the extension is unhealthy.</p> </dd> <dt>CreateFailed</dt> <dd> <p>SageMaker HyperPod couldn't install the extension on any of the cluster's nodes.</p> </dd> <dt>UpdateFailed</dt> <dd> <p>SageMaker HyperPod couldn't apply the update on any of the cluster's nodes.</p> </dd> <dt>Deleting</dt> <dd> <p>SageMaker HyperPod is removing the extension from the cluster's nodes.</p> </dd> <dt>DeleteFailed</dt> <dd> <p>SageMaker HyperPod couldn't remove the extension from any of the cluster's nodes.</p> </dd> </dl>"""
    configuration_values: NotRequired[
        "capo_sagemaker.types.extension_configuration_values.ExtensionConfigurationValues"
    ]
    """<p>The configuration of the extension, as a JSON object serialized as a string. The configuration includes the default value of every setting that you didn't specify.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the extension was created.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the extension was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtensionDetails) -> dict:
    out: dict = {}
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "extension_arn" in value:
        out["ExtensionArn"] = value["extension_arn"]
    if "extension_name" in value:
        out["ExtensionName"] = value["extension_name"]
    if "extension_version" in value:
        out["ExtensionVersion"] = value["extension_version"]
    if "status" in value:
        import capo_sagemaker.types.extension_status

        out["Status"] = capo_sagemaker.types.extension_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "configuration_values" in value:
        out["ConfigurationValues"] = value["configuration_values"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExtensionDetails:
    out: ExtensionDetails = {}  # type: ignore[typeddict-item]
    if data.get("ClusterArn") is not None:
        out["cluster_arn"] = data["ClusterArn"]
    if data.get("ExtensionArn") is not None:
        out["extension_arn"] = data["ExtensionArn"]
    if data.get("ExtensionName") is not None:
        out["extension_name"] = data["ExtensionName"]
    if data.get("ExtensionVersion") is not None:
        out["extension_version"] = data["ExtensionVersion"]
    if data.get("Status") is not None:
        import capo_sagemaker.types.extension_status

        out["status"] = capo_sagemaker.types.extension_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("ConfigurationValues") is not None:
        out["configuration_values"] = data["ConfigurationValues"]
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out
