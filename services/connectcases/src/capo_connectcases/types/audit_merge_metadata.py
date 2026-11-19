"""Generated from Smithy shape ``com.amazonaws.connectcases#AuditMergeMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.case_id


class AuditMergeMetadata(TypedDict, closed=True):
    merge_event_id: "str"
    """<p>The unique identifier of the merge. All audit events produced by the same merge, on both cases, have the same value. Use it to group the changes that a merge made.</p>"""
    primary_case_id: "capo_connectcases.types.case_id.CaseId"
    """<p>The unique identifier of the primary case of the merge.</p>"""
    secondary_case_id: "capo_connectcases.types.case_id.CaseId"
    """<p>The unique identifier of the secondary case of the merge.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuditMergeMetadata) -> dict:
    out: dict = {}
    out["mergeEventId"] = value["merge_event_id"]
    out["primaryCaseId"] = value["primary_case_id"]
    out["secondaryCaseId"] = value["secondary_case_id"]
    return out


def deserialize_json(data: dict) -> AuditMergeMetadata:
    out: AuditMergeMetadata = {}  # type: ignore[typeddict-item]
    if data.get("mergeEventId") is not None:
        out["merge_event_id"] = data["mergeEventId"]
    else:
        out["merge_event_id"] = ""
    if data.get("primaryCaseId") is not None:
        out["primary_case_id"] = data["primaryCaseId"]
    else:
        out["primary_case_id"] = ""
    if data.get("secondaryCaseId") is not None:
        out["secondary_case_id"] = data["secondaryCaseId"]
    else:
        out["secondary_case_id"] = ""
    return out
