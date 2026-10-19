"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ListComponentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.component_summary_list


class ListComponentsResponse(TypedDict, closed=True):
    entities: "capo_amplifyuibuilder.types.component_summary_list.ComponentSummaryList"
    """<p>The list of components for the Amplify app.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListComponentsResponse) -> dict:
    out: dict = {}
    import capo_amplifyuibuilder.types.component_summary_list

    out["entities"] = capo_amplifyuibuilder.types.component_summary_list.serialize_json(
        value["entities"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListComponentsResponse:
    out: ListComponentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("entities") is not None:
        import capo_amplifyuibuilder.types.component_summary_list

        out["entities"] = (
            capo_amplifyuibuilder.types.component_summary_list.deserialize_json(
                data["entities"]
            )
        )
    else:
        out["entities"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
