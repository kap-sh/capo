"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListComponentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.component_summaries
    import capo_iottwinmaker.types.next_token


class ListComponentsResponse(TypedDict, closed=True):
    component_summaries: (
        "capo_iottwinmaker.types.component_summaries.ComponentSummaries"
    )
    """<p>A list of objects that contain information about the components.</p>"""
    next_token: NotRequired["capo_iottwinmaker.types.next_token.NextToken"]
    """<p>The string that specifies the next page of component results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListComponentsResponse) -> dict:
    out: dict = {}
    import capo_iottwinmaker.types.component_summaries

    out["componentSummaries"] = (
        capo_iottwinmaker.types.component_summaries.serialize_json(
            value["component_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListComponentsResponse:
    out: ListComponentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("componentSummaries") is not None:
        import capo_iottwinmaker.types.component_summaries

        out["component_summaries"] = (
            capo_iottwinmaker.types.component_summaries.deserialize_json(
                data["componentSummaries"]
            )
        )
    else:
        out["component_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
