"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListAppInputSourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.app_input_source_list
    import capo_resiliencehub.types.next_token


class ListAppInputSourcesResponse(TypedDict, closed=True):
    app_input_sources: (
        "capo_resiliencehub.types.app_input_source_list.AppInputSourceList"
    )
    """<p>The list of Resilience Hub application input sources.</p>"""
    next_token: NotRequired["capo_resiliencehub.types.next_token.NextToken"]
    """<p>Token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppInputSourcesResponse) -> dict:
    out: dict = {}
    import capo_resiliencehub.types.app_input_source_list

    out["appInputSources"] = (
        capo_resiliencehub.types.app_input_source_list.serialize_json(
            value["app_input_sources"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppInputSourcesResponse:
    out: ListAppInputSourcesResponse = {}  # type: ignore[typeddict-item]
    if data.get("appInputSources") is not None:
        import capo_resiliencehub.types.app_input_source_list

        out["app_input_sources"] = (
            capo_resiliencehub.types.app_input_source_list.deserialize_json(
                data["appInputSources"]
            )
        )
    else:
        out["app_input_sources"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
