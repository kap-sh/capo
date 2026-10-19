"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ListFindingsV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.findings_list_v2
    import capo_accessanalyzer.types.token


class ListFindingsV2Response(TypedDict, closed=True):
    findings: "capo_accessanalyzer.types.findings_list_v2.FindingsListV2"
    """<p>A list of findings retrieved from the analyzer that match the filter criteria specified, if any.</p>"""
    next_token: NotRequired["capo_accessanalyzer.types.token.Token"]
    """<p>A token used for pagination of results returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFindingsV2Response) -> dict:
    out: dict = {}
    import capo_accessanalyzer.types.findings_list_v2

    out["findings"] = capo_accessanalyzer.types.findings_list_v2.serialize_json(
        value["findings"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFindingsV2Response:
    out: ListFindingsV2Response = {}  # type: ignore[typeddict-item]
    if data.get("findings") is not None:
        import capo_accessanalyzer.types.findings_list_v2

        out["findings"] = capo_accessanalyzer.types.findings_list_v2.deserialize_json(
            data["findings"]
        )
    else:
        out["findings"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
