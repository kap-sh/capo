"""Generated from Smithy shape ``com.amazonaws.glue#CreateWorkflowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.name_string
    import capo_glue.types.nullable_integer
    import capo_glue.types.tags_map
    import capo_glue.types.workflow_description_string
    import capo_glue.types.workflow_run_properties


class CreateWorkflowRequest(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>The name to be assigned to the workflow. It should be unique within your account.</p>"""
    description: NotRequired[
        "capo_glue.types.workflow_description_string.WorkflowDescriptionString"
    ]
    """<p>A description of the workflow.</p>"""
    default_run_properties: NotRequired[
        "capo_glue.types.workflow_run_properties.WorkflowRunProperties"
    ]
    """<p>A collection of properties to be used as part of each execution of the workflow.</p> <p>Run properties may be logged. Do not pass plaintext secrets as properties. Retrieve secrets from a Glue Connection, Amazon Web Services Secrets Manager or other secret management mechanism if you intend to use them within the workflow run.</p>"""
    tags: NotRequired["capo_glue.types.tags_map.TagsMap"]
    """<p>The tags to be used with this workflow.</p>"""
    max_concurrent_runs: NotRequired["capo_glue.types.nullable_integer.NullableInteger"]
    """<p>You can use this parameter to prevent unwanted multiple updates to data, to control costs, or in some cases, to prevent exceeding the maximum number of concurrent runs of any of the component jobs. If you leave this parameter blank, there is no limit to the number of concurrent workflow runs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWorkflowRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "default_run_properties" in value:
        import capo_glue.types.workflow_run_properties

        out["DefaultRunProperties"] = (
            capo_glue.types.workflow_run_properties.serialize_aws_json_1_1(
                value["default_run_properties"]
            )
        )
    if "tags" in value:
        import capo_glue.types.tags_map

        out["Tags"] = capo_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    if "max_concurrent_runs" in value:
        out["MaxConcurrentRuns"] = value["max_concurrent_runs"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWorkflowRequest:
    out: CreateWorkflowRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DefaultRunProperties") is not None:
        import capo_glue.types.workflow_run_properties

        out["default_run_properties"] = (
            capo_glue.types.workflow_run_properties.deserialize_aws_json_1_1(
                data["DefaultRunProperties"]
            )
        )
    if data.get("Tags") is not None:
        import capo_glue.types.tags_map

        out["tags"] = capo_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    if data.get("MaxConcurrentRuns") is not None:
        out["max_concurrent_runs"] = data["MaxConcurrentRuns"]
    return out
