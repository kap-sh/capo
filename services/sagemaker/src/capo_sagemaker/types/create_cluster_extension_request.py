"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateClusterExtensionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_arn
    import capo_sagemaker.types.extension_configuration_values
    import capo_sagemaker.types.extension_name
    import capo_sagemaker.types.extension_version
    import capo_sagemaker.types.string
    import capo_sagemaker.types.tag_list


class CreateClusterExtensionRequest(TypedDict, closed=True):
    cluster_arn: NotRequired["capo_sagemaker.types.cluster_arn.ClusterArn"]
    """<p>The Amazon Resource Name (ARN) of the SageMaker HyperPod cluster on which to install the extension. The cluster must use Slurm as the orchestrator and have <code>NodeProvisioningMode</code> set to <code>Continuous</code>.</p>"""
    extension_name: NotRequired["capo_sagemaker.types.extension_name.ExtensionName"]
    """<p>The name of the extension to install, for example <code>sagemaker-observability</code>.</p>"""
    extension_version: NotRequired[
        "capo_sagemaker.types.extension_version.ExtensionVersion"
    ]
    """<p>The version of the extension to install, in <code>MAJOR.MINOR.PATCH</code> format, for example <code>1.0.0</code>. If you don't specify a version, SageMaker HyperPod installs the latest available version of the extension.</p>"""
    configuration_values: NotRequired[
        "capo_sagemaker.types.extension_configuration_values.ExtensionConfigurationValues"
    ]
    """<p>The configuration settings for the extension, as a JSON object serialized as a string, for example <code>{"metricsProvider":{"nodeMetrics":{"level":"ADVANCED"}}}</code>. Each extension version defines which settings it accepts. SageMaker HyperPod validates the settings against that definition, and rejects the request if a setting is unknown or has an invalid value. Settings that you omit use the extension's default values. If you omit <code>ConfigurationValues</code>, all settings use their default values.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>Custom tags for managing the extension as an Amazon Web Services resource. You can add tags to your extension in the same way you add them in other Amazon Web Services services that support tagging. To learn more about tagging Amazon Web Services resources in general, see <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html">Tagging Amazon Web Services Resources User Guide</a>. To use this operation to add tags when you create an extension, you must have the <code>sagemaker:AddTags</code> permission.</p>"""
    client_token: NotRequired["capo_sagemaker.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide so that the operation completes no more than one time. This token is valid for 8 hours. If you retry the request with the same client token and the same parameters within this time, the API returns the Amazon Resource Name (ARN) of the extension that the original request created, without creating a duplicate. If you use the same client token with different parameters, the request fails.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateClusterExtensionRequest) -> dict:
    out: dict = {}
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "extension_name" in value:
        out["ExtensionName"] = value["extension_name"]
    if "extension_version" in value:
        out["ExtensionVersion"] = value["extension_version"]
    if "configuration_values" in value:
        out["ConfigurationValues"] = value["configuration_values"]
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateClusterExtensionRequest:
    out: CreateClusterExtensionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClusterArn") is not None:
        out["cluster_arn"] = data["ClusterArn"]
    if data.get("ExtensionName") is not None:
        out["extension_name"] = data["ExtensionName"]
    if data.get("ExtensionVersion") is not None:
        out["extension_version"] = data["ExtensionVersion"]
    if data.get("ConfigurationValues") is not None:
        out["configuration_values"] = data["ConfigurationValues"]
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
