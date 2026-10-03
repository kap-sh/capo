"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateTrialComponentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.experiment_entity_name
    import capo_sagemaker.types.metadata_properties
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.trial_component_artifacts
    import capo_sagemaker.types.trial_component_parameters
    import capo_sagemaker.types.trial_component_status


class CreateTrialComponentRequest(TypedDict, closed=True):
    trial_component_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the component. The name must be unique in your Amazon Web Services account and is not case-sensitive.</p>"""
    display_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the component as displayed. The name doesn't need to be unique. If <code>DisplayName</code> isn't specified, <code>TrialComponentName</code> is displayed.</p>"""
    status: NotRequired[
        "capo_sagemaker.types.trial_component_status.TrialComponentStatus"
    ]
    """<p>The status of the component. States include:</p> <ul> <li> <p>InProgress</p> </li> <li> <p>Completed</p> </li> <li> <p>Failed</p> </li> </ul>"""
    start_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the component started.</p>"""
    end_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the component ended.</p>"""
    parameters: NotRequired[
        "capo_sagemaker.types.trial_component_parameters.TrialComponentParameters"
    ]
    """<p>The hyperparameters for the component.</p>"""
    input_artifacts: NotRequired[
        "capo_sagemaker.types.trial_component_artifacts.TrialComponentArtifacts"
    ]
    """<p>The input artifacts for the component. Examples of input artifacts are datasets, algorithms, hyperparameters, source code, and instance types.</p>"""
    output_artifacts: NotRequired[
        "capo_sagemaker.types.trial_component_artifacts.TrialComponentArtifacts"
    ]
    """<p>The output artifacts for the component. Examples of output artifacts are metrics, snapshots, logs, and images.</p>"""
    metadata_properties: NotRequired[
        "capo_sagemaker.types.metadata_properties.MetadataProperties"
    ]
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>A list of tags to associate with the component. You can use <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html">Search</a> API to search on the tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTrialComponentRequest) -> dict:
    out: dict = {}
    if "trial_component_name" in value:
        out["TrialComponentName"] = value["trial_component_name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "status" in value:
        import capo_sagemaker.types.trial_component_status

        out["Status"] = (
            capo_sagemaker.types.trial_component_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "start_time" in value:
        import capo_sagemaker.types.timestamp

        out["StartTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_sagemaker.types.timestamp

        out["EndTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "parameters" in value:
        import capo_sagemaker.types.trial_component_parameters

        out["Parameters"] = (
            capo_sagemaker.types.trial_component_parameters.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    if "input_artifacts" in value:
        import capo_sagemaker.types.trial_component_artifacts

        out["InputArtifacts"] = (
            capo_sagemaker.types.trial_component_artifacts.serialize_aws_json_1_1(
                value["input_artifacts"]
            )
        )
    if "output_artifacts" in value:
        import capo_sagemaker.types.trial_component_artifacts

        out["OutputArtifacts"] = (
            capo_sagemaker.types.trial_component_artifacts.serialize_aws_json_1_1(
                value["output_artifacts"]
            )
        )
    if "metadata_properties" in value:
        import capo_sagemaker.types.metadata_properties

        out["MetadataProperties"] = (
            capo_sagemaker.types.metadata_properties.serialize_aws_json_1_1(
                value["metadata_properties"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTrialComponentRequest:
    out: CreateTrialComponentRequest = {}  # type: ignore[typeddict-item]
    if data.get("TrialComponentName") is not None:
        out["trial_component_name"] = data["TrialComponentName"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("Status") is not None:
        import capo_sagemaker.types.trial_component_status

        out["status"] = (
            capo_sagemaker.types.trial_component_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("StartTime") is not None:
        import capo_sagemaker.types.timestamp

        out["start_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_sagemaker.types.timestamp

        out["end_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if data.get("Parameters") is not None:
        import capo_sagemaker.types.trial_component_parameters

        out["parameters"] = (
            capo_sagemaker.types.trial_component_parameters.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    if data.get("InputArtifacts") is not None:
        import capo_sagemaker.types.trial_component_artifacts

        out["input_artifacts"] = (
            capo_sagemaker.types.trial_component_artifacts.deserialize_aws_json_1_1(
                data["InputArtifacts"]
            )
        )
    if data.get("OutputArtifacts") is not None:
        import capo_sagemaker.types.trial_component_artifacts

        out["output_artifacts"] = (
            capo_sagemaker.types.trial_component_artifacts.deserialize_aws_json_1_1(
                data["OutputArtifacts"]
            )
        )
    if data.get("MetadataProperties") is not None:
        import capo_sagemaker.types.metadata_properties

        out["metadata_properties"] = (
            capo_sagemaker.types.metadata_properties.deserialize_aws_json_1_1(
                data["MetadataProperties"]
            )
        )
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
