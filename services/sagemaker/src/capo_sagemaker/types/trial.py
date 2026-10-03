"""Generated from Smithy shape ``com.amazonaws.sagemaker#Trial``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.experiment_entity_name
    import capo_sagemaker.types.metadata_properties
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.trial_arn
    import capo_sagemaker.types.trial_component_simple_summaries
    import capo_sagemaker.types.trial_source
    import capo_sagemaker.types.user_context


class Trial(TypedDict, closed=True):
    trial_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the trial.</p>"""
    trial_arn: NotRequired["capo_sagemaker.types.trial_arn.TrialArn"]
    """<p>The Amazon Resource Name (ARN) of the trial.</p>"""
    display_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the trial as displayed. If <code>DisplayName</code> isn't specified, <code>TrialName</code> is displayed.</p>"""
    experiment_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the experiment the trial is part of.</p>"""
    source: NotRequired["capo_sagemaker.types.trial_source.TrialSource"]
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the trial was created.</p>"""
    created_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    """<p>Who created the trial.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Who last modified the trial.</p>"""
    last_modified_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    metadata_properties: NotRequired[
        "capo_sagemaker.types.metadata_properties.MetadataProperties"
    ]
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>The list of tags that are associated with the trial. You can use <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html">Search</a> API to search on the tags.</p>"""
    trial_component_summaries: NotRequired[
        "capo_sagemaker.types.trial_component_simple_summaries.TrialComponentSimpleSummaries"
    ]
    """<p>A list of the components associated with the trial. For each component, a summary of the component's properties is included.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Trial) -> dict:
    out: dict = {}
    if "trial_name" in value:
        out["TrialName"] = value["trial_name"]
    if "trial_arn" in value:
        out["TrialArn"] = value["trial_arn"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "experiment_name" in value:
        out["ExperimentName"] = value["experiment_name"]
    if "source" in value:
        import capo_sagemaker.types.trial_source

        out["Source"] = capo_sagemaker.types.trial_source.serialize_aws_json_1_1(
            value["source"]
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
    if "trial_component_summaries" in value:
        import capo_sagemaker.types.trial_component_simple_summaries

        out["TrialComponentSummaries"] = (
            capo_sagemaker.types.trial_component_simple_summaries.serialize_aws_json_1_1(
                value["trial_component_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Trial:
    out: Trial = {}  # type: ignore[typeddict-item]
    if data.get("TrialName") is not None:
        out["trial_name"] = data["TrialName"]
    if data.get("TrialArn") is not None:
        out["trial_arn"] = data["TrialArn"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("ExperimentName") is not None:
        out["experiment_name"] = data["ExperimentName"]
    if data.get("Source") is not None:
        import capo_sagemaker.types.trial_source

        out["source"] = capo_sagemaker.types.trial_source.deserialize_aws_json_1_1(
            data["Source"]
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
    if data.get("TrialComponentSummaries") is not None:
        import capo_sagemaker.types.trial_component_simple_summaries

        out["trial_component_summaries"] = (
            capo_sagemaker.types.trial_component_simple_summaries.deserialize_aws_json_1_1(
                data["TrialComponentSummaries"]
            )
        )
    return out
