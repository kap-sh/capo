"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateClusterExtensionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_arn
    import capo_sagemaker.types.extension_arn
    import capo_sagemaker.types.extension_configuration_values
    import capo_sagemaker.types.extension_version
    import capo_sagemaker.types.string


class UpdateClusterExtensionRequest(TypedDict, closed=True):
    cluster_arn: NotRequired["capo_sagemaker.types.cluster_arn.ClusterArn"]
    """<p>The Amazon Resource Name (ARN) of the SageMaker HyperPod cluster on which the extension is installed.</p>"""
    extension_arn: NotRequired["capo_sagemaker.types.extension_arn.ExtensionArn"]
    """<p>The Amazon Resource Name (ARN) of the extension to update.</p>"""
    extension_version: NotRequired[
        "capo_sagemaker.types.extension_version.ExtensionVersion"
    ]
    """<p>The version to update the extension to, in <code>MAJOR.MINOR.PATCH</code> format. The version must be later than the extension's current version. If you omit this parameter, the extension keeps its current version.</p>"""
    configuration_values: NotRequired[
        "capo_sagemaker.types.extension_configuration_values.ExtensionConfigurationValues"
    ]
    """<p>The configuration changes to apply, as a JSON object serialized as a string. Settings that you include are changed, settings that you omit are unchanged, and a setting with the value <code>null</code> returns to its default value. The resulting configuration must be valid for the target extension version. If you omit <code>ConfigurationValues</code>, the configuration is unchanged.</p>"""
    client_token: NotRequired["capo_sagemaker.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide so that the request is idempotent. If you send the same update more than once, SageMaker HyperPod applies it once and doesn't return an error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateClusterExtensionRequest) -> dict:
    out: dict = {}
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "extension_arn" in value:
        out["ExtensionArn"] = value["extension_arn"]
    if "extension_version" in value:
        out["ExtensionVersion"] = value["extension_version"]
    if "configuration_values" in value:
        out["ConfigurationValues"] = value["configuration_values"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateClusterExtensionRequest:
    out: UpdateClusterExtensionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClusterArn") is not None:
        out["cluster_arn"] = data["ClusterArn"]
    if data.get("ExtensionArn") is not None:
        out["extension_arn"] = data["ExtensionArn"]
    if data.get("ExtensionVersion") is not None:
        out["extension_version"] = data["ExtensionVersion"]
    if data.get("ConfigurationValues") is not None:
        out["configuration_values"] = data["ConfigurationValues"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
