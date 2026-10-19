"""Generated from Smithy shape ``com.amazonaws.glue#PutWorkflowRunPropertiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.id_string
    import capo_glue.types.name_string
    import capo_glue.types.workflow_run_properties


class PutWorkflowRunPropertiesRequest(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>Name of the workflow which was run.</p>"""
    run_id: "capo_glue.types.id_string.IdString"
    """<p>The ID of the workflow run for which the run properties should be updated.</p>"""
    run_properties: "capo_glue.types.workflow_run_properties.WorkflowRunProperties"
    """<p>The properties to put for the specified run.</p> <p>Run properties may be logged. Do not pass plaintext secrets as properties. Retrieve secrets from a Glue Connection, Amazon Web Services Secrets Manager or other secret management mechanism if you intend to use them within the workflow run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutWorkflowRunPropertiesRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["RunId"] = value["run_id"]
    import capo_glue.types.workflow_run_properties

    out["RunProperties"] = (
        capo_glue.types.workflow_run_properties.serialize_aws_json_1_1(
            value["run_properties"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutWorkflowRunPropertiesRequest:
    out: PutWorkflowRunPropertiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("RunId") is not None:
        out["run_id"] = data["RunId"]
    else:
        out["run_id"] = ""
    if data.get("RunProperties") is not None:
        import capo_glue.types.workflow_run_properties

        out["run_properties"] = (
            capo_glue.types.workflow_run_properties.deserialize_aws_json_1_1(
                data["RunProperties"]
            )
        )
    else:
        out["run_properties"] = {}
    return out
