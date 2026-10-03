"""Generated from Smithy shape ``com.amazonaws.sagemaker#DebugHookConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.collection_configurations
    import capo_sagemaker.types.directory_path
    import capo_sagemaker.types.hook_parameters
    import capo_sagemaker.types.s3_uri


class DebugHookConfig(TypedDict, closed=True):
    local_path: NotRequired["capo_sagemaker.types.directory_path.DirectoryPath"]
    """<p>Path to local storage location for metrics and tensors. Defaults to <code>/opt/ml/output/tensors/</code>.</p>"""
    s3_output_path: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>Path to Amazon S3 storage location for metrics and tensors.</p>"""
    hook_parameters: NotRequired["capo_sagemaker.types.hook_parameters.HookParameters"]
    """<p>Configuration information for the Amazon SageMaker Debugger hook parameters.</p>"""
    collection_configurations: NotRequired[
        "capo_sagemaker.types.collection_configurations.CollectionConfigurations"
    ]
    """<p>Configuration information for Amazon SageMaker Debugger tensor collections. To learn more about how to configure the <code>CollectionConfiguration</code> parameter, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html">Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DebugHookConfig) -> dict:
    out: dict = {}
    if "local_path" in value:
        out["LocalPath"] = value["local_path"]
    if "s3_output_path" in value:
        out["S3OutputPath"] = value["s3_output_path"]
    if "hook_parameters" in value:
        import capo_sagemaker.types.hook_parameters

        out["HookParameters"] = (
            capo_sagemaker.types.hook_parameters.serialize_aws_json_1_1(
                value["hook_parameters"]
            )
        )
    if "collection_configurations" in value:
        import capo_sagemaker.types.collection_configurations

        out["CollectionConfigurations"] = (
            capo_sagemaker.types.collection_configurations.serialize_aws_json_1_1(
                value["collection_configurations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DebugHookConfig:
    out: DebugHookConfig = {}  # type: ignore[typeddict-item]
    if data.get("LocalPath") is not None:
        out["local_path"] = data["LocalPath"]
    if data.get("S3OutputPath") is not None:
        out["s3_output_path"] = data["S3OutputPath"]
    if data.get("HookParameters") is not None:
        import capo_sagemaker.types.hook_parameters

        out["hook_parameters"] = (
            capo_sagemaker.types.hook_parameters.deserialize_aws_json_1_1(
                data["HookParameters"]
            )
        )
    if data.get("CollectionConfigurations") is not None:
        import capo_sagemaker.types.collection_configurations

        out["collection_configurations"] = (
            capo_sagemaker.types.collection_configurations.deserialize_aws_json_1_1(
                data["CollectionConfigurations"]
            )
        )
    return out
