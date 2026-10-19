"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssetSourceUrlContent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.asset_content_url


class AssetSourceUrlContent(TypedDict, closed=True):
    url: "capo_devops_agent.types.asset_content_url.AssetContentUrl"
    """<p>The source URL to import asset content from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetSourceUrlContent) -> dict:
    out: dict = {}
    out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> AssetSourceUrlContent:
    out: AssetSourceUrlContent = {}  # type: ignore[typeddict-item]
    if data.get("url") is not None:
        out["url"] = data["url"]
    else:
        out["url"] = ""
    return out
