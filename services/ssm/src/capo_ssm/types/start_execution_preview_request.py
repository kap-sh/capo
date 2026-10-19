"""Generated from Smithy shape ``com.amazonaws.ssm#StartExecutionPreviewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.document_name
    import capo_ssm.types.document_version
    import capo_ssm.types.execution_inputs


class StartExecutionPreviewRequest(TypedDict, closed=True):
    document_name: "capo_ssm.types.document_name.DocumentName"
    """<p>The name of the Automation runbook to run. The result of the execution preview indicates what the impact would be of running this runbook.</p>"""
    document_version: NotRequired["capo_ssm.types.document_version.DocumentVersion"]
    """<p>The version of the Automation runbook to run. The default value is <code>$DEFAULT</code>.</p>"""
    execution_inputs: NotRequired["capo_ssm.types.execution_inputs.ExecutionInputs"]
    """<p>Information about the inputs that can be specified for the preview operation. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartExecutionPreviewRequest) -> dict:
    out: dict = {}
    out["DocumentName"] = value["document_name"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    if "execution_inputs" in value:
        import capo_ssm.types.execution_inputs

        out["ExecutionInputs"] = capo_ssm.types.execution_inputs.serialize_aws_json_1_1(
            value["execution_inputs"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartExecutionPreviewRequest:
    out: StartExecutionPreviewRequest = {}  # type: ignore[typeddict-item]
    if data.get("DocumentName") is not None:
        out["document_name"] = data["DocumentName"]
    else:
        out["document_name"] = ""
    if data.get("DocumentVersion") is not None:
        out["document_version"] = data["DocumentVersion"]
    if data.get("ExecutionInputs") is not None:
        import capo_ssm.types.execution_inputs

        out["execution_inputs"] = (
            capo_ssm.types.execution_inputs.deserialize_aws_json_1_1(
                data["ExecutionInputs"]
            )
        )
    return out
