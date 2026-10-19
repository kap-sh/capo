"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ListAccessPreviewFindingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.access_preview_findings_list
    import capo_accessanalyzer.types.token


class ListAccessPreviewFindingsResponse(TypedDict, closed=True):
    findings: "capo_accessanalyzer.types.access_preview_findings_list.AccessPreviewFindingsList"
    """<p>A list of access preview findings that match the specified filter criteria.</p>"""
    next_token: NotRequired["capo_accessanalyzer.types.token.Token"]
    """<p>A token used for pagination of results returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccessPreviewFindingsResponse) -> dict:
    out: dict = {}
    import capo_accessanalyzer.types.access_preview_findings_list

    out["findings"] = (
        capo_accessanalyzer.types.access_preview_findings_list.serialize_json(
            value["findings"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAccessPreviewFindingsResponse:
    out: ListAccessPreviewFindingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("findings") is not None:
        import capo_accessanalyzer.types.access_preview_findings_list

        out["findings"] = (
            capo_accessanalyzer.types.access_preview_findings_list.deserialize_json(
                data["findings"]
            )
        )
    else:
        out["findings"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
