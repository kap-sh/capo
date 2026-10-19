"""Generated from Smithy shape ``com.amazonaws.quicksight#ConfluenceParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.site_base_url


class ConfluenceParameters(TypedDict, closed=True):
    confluence_url: "capo_quicksight.types.site_base_url.SiteBaseUrl"
    """<p>The URL of the Confluence site to connect to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfluenceParameters) -> dict:
    out: dict = {}
    out["ConfluenceUrl"] = value["confluence_url"]
    return out


def deserialize_json(data: dict) -> ConfluenceParameters:
    out: ConfluenceParameters = {}  # type: ignore[typeddict-item]
    if data.get("ConfluenceUrl") is not None:
        out["confluence_url"] = data["ConfluenceUrl"]
    else:
        out["confluence_url"] = ""
    return out
