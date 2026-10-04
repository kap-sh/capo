"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateClusterSchedulerConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_arn
    import capo_sagemaker.types.entity_description
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.scheduler_config
    import capo_sagemaker.types.tag_list


class CreateClusterSchedulerConfigRequest(TypedDict, closed=True):
    name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name for the cluster policy. The name must be unique within the SageMaker AI HyperPod cluster specified by <code>ClusterArn</code>. You can use the same name in other clusters within a Region or across Regions.</p>"""
    cluster_arn: NotRequired["capo_sagemaker.types.cluster_arn.ClusterArn"]
    """<p>ARN of the cluster.</p>"""
    scheduler_config: NotRequired[
        "capo_sagemaker.types.scheduler_config.SchedulerConfig"
    ]
    """<p>Configuration about the monitoring schedule.</p>"""
    description: NotRequired[
        "capo_sagemaker.types.entity_description.EntityDescription"
    ]
    """<p>Description of the cluster policy.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>Tags of the cluster policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateClusterSchedulerConfigRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "scheduler_config" in value:
        import capo_sagemaker.types.scheduler_config

        out["SchedulerConfig"] = (
            capo_sagemaker.types.scheduler_config.serialize_aws_json_1_1(
                value["scheduler_config"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateClusterSchedulerConfigRequest:
    out: CreateClusterSchedulerConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ClusterArn") is not None:
        out["cluster_arn"] = data["ClusterArn"]
    if data.get("SchedulerConfig") is not None:
        import capo_sagemaker.types.scheduler_config

        out["scheduler_config"] = (
            capo_sagemaker.types.scheduler_config.deserialize_aws_json_1_1(
                data["SchedulerConfig"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
