"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrialComponent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.experiment_entity_name
    import capo_sagemaker.types.lineage_group_arn
    import capo_sagemaker.types.metadata_properties
    import capo_sagemaker.types.parents
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.trial_component_arn
    import capo_sagemaker.types.trial_component_artifacts
    import capo_sagemaker.types.trial_component_metric_summaries
    import capo_sagemaker.types.trial_component_parameters
    import capo_sagemaker.types.trial_component_source
    import capo_sagemaker.types.trial_component_source_detail
    import capo_sagemaker.types.trial_component_status
    import capo_sagemaker.types.user_context


class TrialComponent(TypedDict, closed=True):
    trial_component_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the trial component.</p>"""
    display_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the component as displayed. If <code>DisplayName</code> isn't specified, <code>TrialComponentName</code> is displayed.</p>"""
    trial_component_arn: NotRequired[
        "capo_sagemaker.types.trial_component_arn.TrialComponentArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the trial component.</p>"""
    source: NotRequired[
        "capo_sagemaker.types.trial_component_source.TrialComponentSource"
    ]
    """<p>The Amazon Resource Name (ARN) and job type of the source of the component.</p>"""
    status: NotRequired[
        "capo_sagemaker.types.trial_component_status.TrialComponentStatus"
    ]
    start_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the component started.</p>"""
    end_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the component ended.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the component was created.</p>"""
    created_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    """<p>Who created the trial component.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the component was last modified.</p>"""
    last_modified_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    parameters: NotRequired[
        "capo_sagemaker.types.trial_component_parameters.TrialComponentParameters"
    ]
    """<p>The hyperparameters of the component.</p>"""
    input_artifacts: NotRequired[
        "capo_sagemaker.types.trial_component_artifacts.TrialComponentArtifacts"
    ]
    """<p>The input artifacts of the component.</p>"""
    output_artifacts: NotRequired[
        "capo_sagemaker.types.trial_component_artifacts.TrialComponentArtifacts"
    ]
    """<p>The output artifacts of the component.</p>"""
    metrics: NotRequired[
        "capo_sagemaker.types.trial_component_metric_summaries.TrialComponentMetricSummaries"
    ]
    """<p>The metrics for the component.</p>"""
    metadata_properties: NotRequired[
        "capo_sagemaker.types.metadata_properties.MetadataProperties"
    ]
    source_detail: NotRequired[
        "capo_sagemaker.types.trial_component_source_detail.TrialComponentSourceDetail"
    ]
    """<p>Details of the source of the component.</p>"""
    lineage_group_arn: NotRequired[
        "capo_sagemaker.types.lineage_group_arn.LineageGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the lineage group resource.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>The list of tags that are associated with the component. You can use <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html">Search</a> API to search on the tags.</p>"""
    parents: NotRequired["capo_sagemaker.types.parents.Parents"]
    """<p>An array of the parents of the component. A parent is a trial the component is associated with and the experiment the trial is part of. A component might not have any parents.</p>"""
    run_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the experiment run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrialComponent) -> dict:
    out: dict = {}
    if "trial_component_name" in value:
        out["TrialComponentName"] = value["trial_component_name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "trial_component_arn" in value:
        out["TrialComponentArn"] = value["trial_component_arn"]
    if "source" in value:
        import capo_sagemaker.types.trial_component_source

        out["Source"] = (
            capo_sagemaker.types.trial_component_source.serialize_aws_json_1_1(
                value["source"]
            )
        )
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
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "created_by" in value:
        import capo_sagemaker.types.user_context

        out["CreatedBy"] = capo_sagemaker.types.user_context.serialize_aws_json_1_1(
            value["created_by"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "last_modified_by" in value:
        import capo_sagemaker.types.user_context

        out["LastModifiedBy"] = (
            capo_sagemaker.types.user_context.serialize_aws_json_1_1(
                value["last_modified_by"]
            )
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
    if "metrics" in value:
        import capo_sagemaker.types.trial_component_metric_summaries

        out["Metrics"] = (
            capo_sagemaker.types.trial_component_metric_summaries.serialize_aws_json_1_1(
                value["metrics"]
            )
        )
    if "metadata_properties" in value:
        import capo_sagemaker.types.metadata_properties

        out["MetadataProperties"] = (
            capo_sagemaker.types.metadata_properties.serialize_aws_json_1_1(
                value["metadata_properties"]
            )
        )
    if "source_detail" in value:
        import capo_sagemaker.types.trial_component_source_detail

        out["SourceDetail"] = (
            capo_sagemaker.types.trial_component_source_detail.serialize_aws_json_1_1(
                value["source_detail"]
            )
        )
    if "lineage_group_arn" in value:
        out["LineageGroupArn"] = value["lineage_group_arn"]
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "parents" in value:
        import capo_sagemaker.types.parents

        out["Parents"] = capo_sagemaker.types.parents.serialize_aws_json_1_1(
            value["parents"]
        )
    if "run_name" in value:
        out["RunName"] = value["run_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TrialComponent:
    out: TrialComponent = {}  # type: ignore[typeddict-item]
    if data.get("TrialComponentName") is not None:
        out["trial_component_name"] = data["TrialComponentName"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("TrialComponentArn") is not None:
        out["trial_component_arn"] = data["TrialComponentArn"]
    if data.get("Source") is not None:
        import capo_sagemaker.types.trial_component_source

        out["source"] = (
            capo_sagemaker.types.trial_component_source.deserialize_aws_json_1_1(
                data["Source"]
            )
        )
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
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("CreatedBy") is not None:
        import capo_sagemaker.types.user_context

        out["created_by"] = capo_sagemaker.types.user_context.deserialize_aws_json_1_1(
            data["CreatedBy"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("LastModifiedBy") is not None:
        import capo_sagemaker.types.user_context

        out["last_modified_by"] = (
            capo_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["LastModifiedBy"]
            )
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
    if data.get("Metrics") is not None:
        import capo_sagemaker.types.trial_component_metric_summaries

        out["metrics"] = (
            capo_sagemaker.types.trial_component_metric_summaries.deserialize_aws_json_1_1(
                data["Metrics"]
            )
        )
    if data.get("MetadataProperties") is not None:
        import capo_sagemaker.types.metadata_properties

        out["metadata_properties"] = (
            capo_sagemaker.types.metadata_properties.deserialize_aws_json_1_1(
                data["MetadataProperties"]
            )
        )
    if data.get("SourceDetail") is not None:
        import capo_sagemaker.types.trial_component_source_detail

        out["source_detail"] = (
            capo_sagemaker.types.trial_component_source_detail.deserialize_aws_json_1_1(
                data["SourceDetail"]
            )
        )
    if data.get("LineageGroupArn") is not None:
        out["lineage_group_arn"] = data["LineageGroupArn"]
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("Parents") is not None:
        import capo_sagemaker.types.parents

        out["parents"] = capo_sagemaker.types.parents.deserialize_aws_json_1_1(
            data["Parents"]
        )
    if data.get("RunName") is not None:
        out["run_name"] = data["RunName"]
    return out
