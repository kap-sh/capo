"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchDisassociateFindingIssueOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.batch_disassociate_finding_issue_errors


class BatchDisassociateFindingIssueOutput(TypedDict, closed=True):
    errors: "capo_securityagent.types.batch_disassociate_finding_issue_errors.BatchDisassociateFindingIssueErrors"
    """<p>The findings whose issue could not be disassociated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDisassociateFindingIssueOutput) -> dict:
    out: dict = {}
    import capo_securityagent.types.batch_disassociate_finding_issue_errors

    out["errors"] = (
        capo_securityagent.types.batch_disassociate_finding_issue_errors.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDisassociateFindingIssueOutput:
    out: BatchDisassociateFindingIssueOutput = {}  # type: ignore[typeddict-item]
    if data.get("errors") is not None:
        import capo_securityagent.types.batch_disassociate_finding_issue_errors

        out["errors"] = (
            capo_securityagent.types.batch_disassociate_finding_issue_errors.deserialize_json(
                data["errors"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDisassociateFindingIssueOutput.errors required"
        )
    return out
