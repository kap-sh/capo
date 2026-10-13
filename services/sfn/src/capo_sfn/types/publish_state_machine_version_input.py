"""Generated from Smithy shape ``com.amazonaws.sfn#PublishStateMachineVersionInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sfn.types.arn
    import capo_sfn.types.revision_id
    import capo_sfn.types.version_description


class PublishStateMachineVersionInput(TypedDict, closed=True):
    state_machine_arn: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the state machine.</p>"""
    revision_id: NotRequired["capo_sfn.types.revision_id.RevisionId"]
    """<p>Only publish the state machine version if the current state machine's revision ID matches the specified ID.</p> <p>Use this option to avoid publishing a version if the state machine changed since you last updated it. If the specified revision ID doesn't match the state machine's current revision ID, the API returns <code>ConflictException</code>.</p> <note> <p>To specify an initial revision ID for a state machine with no revision ID assigned, specify the string <code>INITIAL</code> for the <code>revisionId</code> parameter. For example, you can specify a <code>revisionID</code> of <code>INITIAL</code> when you create a state machine using the <a>CreateStateMachine</a> API action.</p> </note>"""
    description: NotRequired["capo_sfn.types.version_description.VersionDescription"]
    """<p>An optional description of the state machine version.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PublishStateMachineVersionInput) -> dict:
    out: dict = {}
    out["stateMachineArn"] = value["state_machine_arn"]
    if "revision_id" in value:
        out["revisionId"] = value["revision_id"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PublishStateMachineVersionInput:
    out: PublishStateMachineVersionInput = {}  # type: ignore[typeddict-item]
    if data.get("stateMachineArn") is not None:
        out["state_machine_arn"] = data["stateMachineArn"]
    else:
        raise DeserializationError(
            "PublishStateMachineVersionInput.state_machine_arn required"
        )
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out


def redact_sensitive(value: PublishStateMachineVersionInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
