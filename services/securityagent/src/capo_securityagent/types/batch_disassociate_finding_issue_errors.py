"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchDisassociateFindingIssueErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.batch_disassociate_finding_issue_error

BatchDisassociateFindingIssueErrors: TypeAlias = list[
    "capo_securityagent.types.batch_disassociate_finding_issue_error.BatchDisassociateFindingIssueError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDisassociateFindingIssueErrors) -> list:
    import capo_securityagent.types.batch_disassociate_finding_issue_error

    out: list = []
    for item in value:
        out.append(
            capo_securityagent.types.batch_disassociate_finding_issue_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchDisassociateFindingIssueErrors:
    import capo_securityagent.types.batch_disassociate_finding_issue_error

    out: BatchDisassociateFindingIssueErrors = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_securityagent.types.batch_disassociate_finding_issue_error.deserialize_json(
                item
            )
        )
    return out
