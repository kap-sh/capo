"""Generated from Smithy shape ``com.amazonaws.codepipeline#StartPipelineExecutionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.client_request_token
    import capo_codepipeline.types.pipeline_name
    import capo_codepipeline.types.pipeline_variable_list
    import capo_codepipeline.types.source_revision_override_list


class StartPipelineExecutionInput(TypedDict, closed=True):
    name: "capo_codepipeline.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline to start.</p>"""
    variables: NotRequired[
        "capo_codepipeline.types.pipeline_variable_list.PipelineVariableList"
    ]
    r"""<p>A list that overrides pipeline variables for a pipeline execution that's being started. Variable names must match <code>[A-Za-z0-9@\-_]+</code>, and the values can be anything except an empty string.</p>"""
    client_request_token: NotRequired[
        "capo_codepipeline.types.client_request_token.ClientRequestToken"
    ]
    """<p>The system-generated unique ID used to identify a unique execution request.</p>"""
    source_revisions: NotRequired[
        "capo_codepipeline.types.source_revision_override_list.SourceRevisionOverrideList"
    ]
    """<p>A list that allows you to specify, or override, the source revision for a pipeline execution that's being started. A source revision is the version with all the changes to your application code, or source artifact, for the pipeline execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartPipelineExecutionInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "variables" in value:
        import capo_codepipeline.types.pipeline_variable_list

        out["variables"] = (
            capo_codepipeline.types.pipeline_variable_list.serialize_aws_json_1_1(
                value["variables"]
            )
        )
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    if "source_revisions" in value:
        import capo_codepipeline.types.source_revision_override_list

        out["sourceRevisions"] = (
            capo_codepipeline.types.source_revision_override_list.serialize_aws_json_1_1(
                value["source_revisions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartPipelineExecutionInput:
    out: StartPipelineExecutionInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("variables") is not None:
        import capo_codepipeline.types.pipeline_variable_list

        out["variables"] = (
            capo_codepipeline.types.pipeline_variable_list.deserialize_aws_json_1_1(
                data["variables"]
            )
        )
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("sourceRevisions") is not None:
        import capo_codepipeline.types.source_revision_override_list

        out["source_revisions"] = (
            capo_codepipeline.types.source_revision_override_list.deserialize_aws_json_1_1(
                data["sourceRevisions"]
            )
        )
    return out
