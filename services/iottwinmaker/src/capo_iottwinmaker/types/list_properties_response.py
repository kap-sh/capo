"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListPropertiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.next_token
    import capo_iottwinmaker.types.property_summaries


class ListPropertiesResponse(TypedDict, closed=True):
    property_summaries: "capo_iottwinmaker.types.property_summaries.PropertySummaries"
    """<p>A list of objects that contain information about the properties.</p>"""
    next_token: NotRequired["capo_iottwinmaker.types.next_token.NextToken"]
    """<p>The string that specifies the next page of property results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPropertiesResponse) -> dict:
    out: dict = {}
    import capo_iottwinmaker.types.property_summaries

    out["propertySummaries"] = (
        capo_iottwinmaker.types.property_summaries.serialize_json(
            value["property_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPropertiesResponse:
    out: ListPropertiesResponse = {}  # type: ignore[typeddict-item]
    if data.get("propertySummaries") is not None:
        import capo_iottwinmaker.types.property_summaries

        out["property_summaries"] = (
            capo_iottwinmaker.types.property_summaries.deserialize_json(
                data["propertySummaries"]
            )
        )
    else:
        out["property_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
