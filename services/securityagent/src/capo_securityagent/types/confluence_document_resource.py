"""Generated from Smithy shape ``com.amazonaws.securityagent#ConfluenceDocumentResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.provider_resource_name


class ConfluenceDocumentResource(TypedDict, closed=True):
    name: "capo_securityagent.types.provider_resource_name.ProviderResourceName"
    space_key: "str"
    """<p>The Confluence space key containing the document.</p>"""
    page_id: "str"
    """<p>The Confluence page identifier.</p>"""
    title: NotRequired["str"]
    """<p>The display title of the Confluence page.</p>"""
    space_title: NotRequired["str"]
    """<p>The display title of the Confluence space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfluenceDocumentResource) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["spaceKey"] = value["space_key"]
    out["pageId"] = value["page_id"]
    if "title" in value:
        out["title"] = value["title"]
    if "space_title" in value:
        out["spaceTitle"] = value["space_title"]
    return out


def deserialize_json(data: dict) -> ConfluenceDocumentResource:
    out: ConfluenceDocumentResource = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("spaceKey") is not None:
        out["space_key"] = data["spaceKey"]
    else:
        out["space_key"] = ""
    if data.get("pageId") is not None:
        out["page_id"] = data["pageId"]
    else:
        out["page_id"] = ""
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("spaceTitle") is not None:
        out["space_title"] = data["spaceTitle"]
    return out
