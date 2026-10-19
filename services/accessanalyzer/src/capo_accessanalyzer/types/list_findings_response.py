"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ListFindingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.findings_list
    import capo_accessanalyzer.types.token


class ListFindingsResponse(TypedDict, closed=True):
    findings: "capo_accessanalyzer.types.findings_list.FindingsList"
    """<p>A list of findings retrieved from the analyzer that match the filter criteria specified, if any.</p>"""
    next_token: NotRequired["capo_accessanalyzer.types.token.Token"]
    """<p>A token used for pagination of results returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFindingsResponse) -> dict:
    out: dict = {}
    import capo_accessanalyzer.types.findings_list

    out["findings"] = capo_accessanalyzer.types.findings_list.serialize_json(
        value["findings"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFindingsResponse:
    out: ListFindingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("findings") is not None:
        import capo_accessanalyzer.types.findings_list

        out["findings"] = capo_accessanalyzer.types.findings_list.deserialize_json(
            data["findings"]
        )
    else:
        out["findings"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
