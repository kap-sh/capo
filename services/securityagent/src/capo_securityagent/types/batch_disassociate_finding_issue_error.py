"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchDisassociateFindingIssueError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.error_code


class BatchDisassociateFindingIssueError(TypedDict, closed=True):
    finding_id: "str"
    """<p>The identifier of the finding that failed to disassociate.</p>"""
    code: "capo_securityagent.types.error_code.ErrorCode"
    """<p>The machine-readable failure category.</p>"""
    message: "str"
    """<p>A customer-facing explanation of the failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDisassociateFindingIssueError) -> dict:
    out: dict = {}
    out["findingId"] = value["finding_id"]
    import capo_securityagent.types.error_code

    out["code"] = capo_securityagent.types.error_code.serialize_json(value["code"])
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchDisassociateFindingIssueError:
    out: BatchDisassociateFindingIssueError = {}  # type: ignore[typeddict-item]
    if data.get("findingId") is not None:
        out["finding_id"] = data["findingId"]
    else:
        out["finding_id"] = ""
    if data.get("code") is not None:
        import capo_securityagent.types.error_code

        out["code"] = capo_securityagent.types.error_code.deserialize_json(data["code"])
    else:
        import typing

        out["code"] = typing.cast("capo_securityagent.types.error_code.ErrorCode", "")
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
