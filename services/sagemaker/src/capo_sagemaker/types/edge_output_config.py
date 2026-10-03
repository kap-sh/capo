"""Generated from Smithy shape ``com.amazonaws.sagemaker#EdgeOutputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.edge_preset_deployment_type
    import capo_sagemaker.types.kms_key_id
    import capo_sagemaker.types.s3_uri
    import capo_sagemaker.types.string


class EdgeOutputConfig(TypedDict, closed=True):
    s3_output_location: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>The Amazon Simple Storage (S3) bucker URI.</p>"""
    kms_key_id: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt data on the storage volume after compilation job. If you don't provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role's account.</p>"""
    preset_deployment_type: NotRequired[
        "capo_sagemaker.types.edge_preset_deployment_type.EdgePresetDeploymentType"
    ]
    """<p>The deployment type SageMaker Edge Manager will create. Currently only supports Amazon Web Services IoT Greengrass Version 2 components.</p>"""
    preset_deployment_config: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The configuration used to create deployment artifacts. Specify configuration options with a JSON string. The available configuration options for each type are:</p> <ul> <li> <p> <code>ComponentName</code> (optional) - Name of the GreenGrass V2 component. If not specified, the default name generated consists of "SagemakerEdgeManager" and the name of your SageMaker Edge Manager packaging job.</p> </li> <li> <p> <code>ComponentDescription</code> (optional) - Description of the component.</p> </li> <li> <p> <code>ComponentVersion</code> (optional) - The version of the component.</p> <note> <p>Amazon Web Services IoT Greengrass uses semantic versions for components. Semantic versions follow a<i> major.minor.patch</i> number system. For example, version 1.0.0 represents the first major release for a component. For more information, see the <a href="https://semver.org/">semantic version specification</a>.</p> </note> </li> <li> <p> <code>PlatformOS</code> (optional) - The name of the operating system for the platform. Supported platforms include Windows and Linux.</p> </li> <li> <p> <code>PlatformArchitecture</code> (optional) - The processor architecture for the platform. </p> <p>Supported architectures Windows include: Windows32_x86, Windows64_x64.</p> <p>Supported architectures for Linux include: Linux x86_64, Linux ARMV8.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EdgeOutputConfig) -> dict:
    out: dict = {}
    if "s3_output_location" in value:
        out["S3OutputLocation"] = value["s3_output_location"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "preset_deployment_type" in value:
        import capo_sagemaker.types.edge_preset_deployment_type

        out["PresetDeploymentType"] = (
            capo_sagemaker.types.edge_preset_deployment_type.serialize_aws_json_1_1(
                value["preset_deployment_type"]
            )
        )
    if "preset_deployment_config" in value:
        out["PresetDeploymentConfig"] = value["preset_deployment_config"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EdgeOutputConfig:
    out: EdgeOutputConfig = {}  # type: ignore[typeddict-item]
    if data.get("S3OutputLocation") is not None:
        out["s3_output_location"] = data["S3OutputLocation"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("PresetDeploymentType") is not None:
        import capo_sagemaker.types.edge_preset_deployment_type

        out["preset_deployment_type"] = (
            capo_sagemaker.types.edge_preset_deployment_type.deserialize_aws_json_1_1(
                data["PresetDeploymentType"]
            )
        )
    if data.get("PresetDeploymentConfig") is not None:
        out["preset_deployment_config"] = data["PresetDeploymentConfig"]
    return out
