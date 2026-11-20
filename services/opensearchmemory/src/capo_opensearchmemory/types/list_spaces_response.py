"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#ListSpacesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.next_token
    import capo_opensearchmemory.types.space_summary_list


class ListSpacesResponse(TypedDict, closed=True):
    spaces: "capo_opensearchmemory.types.space_summary_list.SpaceSummaryList"
    """<p>The spaces.</p>"""
    next_token: NotRequired["capo_opensearchmemory.types.next_token.NextToken"]
    """<p>The token for the next set of results. Absent when there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListSpacesResponse) -> dict:
    out: dict = {}
    import capo_opensearchmemory.types.space_summary_list

    out["spaces"] = (
        capo_opensearchmemory.types.space_summary_list.serialize_aws_json_1_0(
            value["spaces"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListSpacesResponse:
    out: ListSpacesResponse = {}  # type: ignore[typeddict-item]
    if data.get("spaces") is not None:
        import capo_opensearchmemory.types.space_summary_list

        out["spaces"] = (
            capo_opensearchmemory.types.space_summary_list.deserialize_aws_json_1_0(
                data["spaces"]
            )
        )
    else:
        out["spaces"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
