"""Generated from Smithy shape ``com.amazonaws.ssm#StartSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.document_arn
    import capo_ssm.types.session_manager_parameters
    import capo_ssm.types.session_reason
    import capo_ssm.types.session_target


class StartSessionRequest(TypedDict, closed=True):
    target: "capo_ssm.types.session_target.SessionTarget"
    """<p>The managed node to connect to for the session.</p>"""
    document_name: NotRequired["capo_ssm.types.document_arn.DocumentARN"]
    """<p>The name of the SSM document you want to use to define the type of session, input parameters, or preferences for the session. For example, <code>SSM-SessionManagerRunShell</code>. You can call the <a>GetDocument</a> API to verify the document exists before attempting to start a session. If no document name is provided, a shell to the managed node is launched by default. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-sessions-start.html">Start a session</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    reason: NotRequired["capo_ssm.types.session_reason.SessionReason"]
    """<p>The reason for connecting to the instance. This value is included in the details for the Amazon CloudWatch Events event created when you start the session.</p>"""
    parameters: NotRequired[
        "capo_ssm.types.session_manager_parameters.SessionManagerParameters"
    ]
    """<p>The values you want to specify for the parameters defined in the Session document. For more information about these parameters, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/getting-started-create-preferences-cli.html">Create a Session Manager preferences document</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartSessionRequest) -> dict:
    out: dict = {}
    out["Target"] = value["target"]
    if "document_name" in value:
        out["DocumentName"] = value["document_name"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    if "parameters" in value:
        import capo_ssm.types.session_manager_parameters

        out["Parameters"] = (
            capo_ssm.types.session_manager_parameters.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartSessionRequest:
    out: StartSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Target") is not None:
        out["target"] = data["Target"]
    else:
        raise DeserializationError("StartSessionRequest.target required")
    if data.get("DocumentName") is not None:
        out["document_name"] = data["DocumentName"]
    if data.get("Reason") is not None:
        out["reason"] = data["Reason"]
    if data.get("Parameters") is not None:
        import capo_ssm.types.session_manager_parameters

        out["parameters"] = (
            capo_ssm.types.session_manager_parameters.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    return out
