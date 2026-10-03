"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateAIWorkloadConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_dataset_config
    import capo_sagemaker.types.ai_entity_name
    import capo_sagemaker.types.ai_workload_configs
    import capo_sagemaker.types.tag_list


class CreateAIWorkloadConfigRequest(TypedDict, closed=True):
    ai_workload_config_name: NotRequired[
        "capo_sagemaker.types.ai_entity_name.AIEntityName"
    ]
    """<p>The name of the AI workload configuration. The name must be unique within your Amazon Web Services account in the current Amazon Web Services Region.</p>"""
    dataset_config: NotRequired[
        "capo_sagemaker.types.ai_dataset_config.AIDatasetConfig"
    ]
    """<p>The dataset configuration for the workload. Specify input data channels with their data sources for benchmark workloads.</p>"""
    ai_workload_configs: NotRequired[
        "capo_sagemaker.types.ai_workload_configs.AIWorkloadConfigs"
    ]
    """<p>The benchmark tool configuration and workload specification. Provide the specification as an inline YAML or JSON string.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>The metadata that you apply to Amazon Web Services resources to help you categorize and organize them. Each tag consists of a key and a value, both of which you define. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services Resources</a> in the Amazon Web Services General Reference.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAIWorkloadConfigRequest) -> dict:
    out: dict = {}
    if "ai_workload_config_name" in value:
        out["AIWorkloadConfigName"] = value["ai_workload_config_name"]
    if "dataset_config" in value:
        import capo_sagemaker.types.ai_dataset_config

        out["DatasetConfig"] = (
            capo_sagemaker.types.ai_dataset_config.serialize_aws_json_1_1(
                value["dataset_config"]
            )
        )
    if "ai_workload_configs" in value:
        import capo_sagemaker.types.ai_workload_configs

        out["AIWorkloadConfigs"] = (
            capo_sagemaker.types.ai_workload_configs.serialize_aws_json_1_1(
                value["ai_workload_configs"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAIWorkloadConfigRequest:
    out: CreateAIWorkloadConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("AIWorkloadConfigName") is not None:
        out["ai_workload_config_name"] = data["AIWorkloadConfigName"]
    if data.get("DatasetConfig") is not None:
        import capo_sagemaker.types.ai_dataset_config

        out["dataset_config"] = (
            capo_sagemaker.types.ai_dataset_config.deserialize_aws_json_1_1(
                data["DatasetConfig"]
            )
        )
    if data.get("AIWorkloadConfigs") is not None:
        import capo_sagemaker.types.ai_workload_configs

        out["ai_workload_configs"] = (
            capo_sagemaker.types.ai_workload_configs.deserialize_aws_json_1_1(
                data["AIWorkloadConfigs"]
            )
        )
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
