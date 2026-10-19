"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ExportThemesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.theme_list


class ExportThemesResponse(TypedDict, closed=True):
    entities: "capo_amplifyuibuilder.types.theme_list.ThemeList"
    """<p>Represents the configuration of the exported themes.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportThemesResponse) -> dict:
    out: dict = {}
    import capo_amplifyuibuilder.types.theme_list

    out["entities"] = capo_amplifyuibuilder.types.theme_list.serialize_json(
        value["entities"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ExportThemesResponse:
    out: ExportThemesResponse = {}  # type: ignore[typeddict-item]
    if data.get("entities") is not None:
        import capo_amplifyuibuilder.types.theme_list

        out["entities"] = capo_amplifyuibuilder.types.theme_list.deserialize_json(
            data["entities"]
        )
    else:
        out["entities"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
