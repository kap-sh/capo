"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchExportFindingResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.linked_issue


class BatchExportFindingResult(TypedDict, closed=True):
    finding_id: "str"
    """<p>The identifier of the finding this result corresponds to.</p>"""
    linked_issue: "capo_securityagent.types.linked_issue.LinkedIssue"
    """<p>The issue that was created for the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchExportFindingResult) -> dict:
    out: dict = {}
    out["findingId"] = value["finding_id"]
    import capo_securityagent.types.linked_issue

    out["linkedIssue"] = capo_securityagent.types.linked_issue.serialize_json(
        value["linked_issue"]
    )
    return out


def deserialize_json(data: dict) -> BatchExportFindingResult:
    out: BatchExportFindingResult = {}  # type: ignore[typeddict-item]
    if data.get("findingId") is not None:
        out["finding_id"] = data["findingId"]
    else:
        out["finding_id"] = ""
    if data.get("linkedIssue") is not None:
        import capo_securityagent.types.linked_issue

        out["linked_issue"] = capo_securityagent.types.linked_issue.deserialize_json(
            data["linkedIssue"]
        )
    else:
        raise DeserializationError("BatchExportFindingResult.linked_issue required")
    return out
