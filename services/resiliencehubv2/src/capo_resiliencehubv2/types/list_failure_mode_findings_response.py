"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListFailureModeFindingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.findings_list
    import capo_resiliencehubv2.types.next_token


class ListFailureModeFindingsResponse(TypedDict, closed=True):
    findings_summary: "capo_resiliencehubv2.types.findings_list.FindingsList"
    """<p>The list of finding summaries.</p>"""
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListFailureModeFindingsResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.findings_list

    out["findingsSummary"] = capo_resiliencehubv2.types.findings_list.serialize_json(
        value["findings_summary"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFailureModeFindingsResponse:
    out: ListFailureModeFindingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("findingsSummary") is not None:
        import capo_resiliencehubv2.types.findings_list

        out["findings_summary"] = (
            capo_resiliencehubv2.types.findings_list.deserialize_json(
                data["findingsSummary"]
            )
        )
    else:
        out["findings_summary"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
