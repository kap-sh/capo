"""Generated from Smithy shape ``com.amazonaws.connectcases#GetMergeCasesStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.case_id
    import capo_connectcases.types.case_id_list
    import capo_connectcases.types.merge_status


class GetMergeCasesStatusResponse(TypedDict, closed=True):
    status: "capo_connectcases.types.merge_status.MergeStatus"
    """<p>The merge status of the case.</p>"""
    primary_case_id: NotRequired["capo_connectcases.types.case_id.CaseId"]
    """<p>The unique identifier of the primary case of the merge.</p>"""
    secondary_case_ids: NotRequired["capo_connectcases.types.case_id_list.CaseIdList"]
    """<p>The unique identifiers of the secondary cases of the merge.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMergeCasesStatusResponse) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    if "primary_case_id" in value:
        out["primaryCaseId"] = value["primary_case_id"]
    if "secondary_case_ids" in value:
        import capo_connectcases.types.case_id_list

        out["secondaryCaseIds"] = capo_connectcases.types.case_id_list.serialize_json(
            value["secondary_case_ids"]
        )
    return out


def deserialize_json(data: dict) -> GetMergeCasesStatusResponse:
    out: GetMergeCasesStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("primaryCaseId") is not None:
        out["primary_case_id"] = data["primaryCaseId"]
    if data.get("secondaryCaseIds") is not None:
        import capo_connectcases.types.case_id_list

        out["secondary_case_ids"] = (
            capo_connectcases.types.case_id_list.deserialize_json(
                data["secondaryCaseIds"]
            )
        )
    return out
