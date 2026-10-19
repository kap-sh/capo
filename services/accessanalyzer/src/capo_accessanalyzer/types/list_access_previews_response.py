"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ListAccessPreviewsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.access_previews_list
    import capo_accessanalyzer.types.token


class ListAccessPreviewsResponse(TypedDict, closed=True):
    access_previews: "capo_accessanalyzer.types.access_previews_list.AccessPreviewsList"
    """<p>A list of access previews retrieved for the analyzer.</p>"""
    next_token: NotRequired["capo_accessanalyzer.types.token.Token"]
    """<p>A token used for pagination of results returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccessPreviewsResponse) -> dict:
    out: dict = {}
    import capo_accessanalyzer.types.access_previews_list

    out["accessPreviews"] = (
        capo_accessanalyzer.types.access_previews_list.serialize_json(
            value["access_previews"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAccessPreviewsResponse:
    out: ListAccessPreviewsResponse = {}  # type: ignore[typeddict-item]
    if data.get("accessPreviews") is not None:
        import capo_accessanalyzer.types.access_previews_list

        out["access_previews"] = (
            capo_accessanalyzer.types.access_previews_list.deserialize_json(
                data["accessPreviews"]
            )
        )
    else:
        out["access_previews"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
