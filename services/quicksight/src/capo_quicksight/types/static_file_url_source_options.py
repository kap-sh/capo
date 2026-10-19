"""Generated from Smithy shape ``com.amazonaws.quicksight#StaticFileUrlSourceOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.string


class StaticFileUrlSourceOptions(TypedDict, closed=True):
    url: "capo_quicksight.types.string.String"
    """<p>The URL to download the static file from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StaticFileUrlSourceOptions) -> dict:
    out: dict = {}
    out["Url"] = value["url"]
    return out


def deserialize_json(data: dict) -> StaticFileUrlSourceOptions:
    out: StaticFileUrlSourceOptions = {}  # type: ignore[typeddict-item]
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    else:
        out["url"] = ""
    return out
