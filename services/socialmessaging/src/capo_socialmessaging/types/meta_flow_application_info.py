"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaFlowApplicationInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.meta_flow_application_id
    import capo_socialmessaging.types.meta_flow_application_link
    import capo_socialmessaging.types.meta_flow_application_name


class MetaFlowApplicationInfo(TypedDict, closed=True):
    link: NotRequired[
        "capo_socialmessaging.types.meta_flow_application_link.MetaFlowApplicationLink"
    ]
    """<p>The URL link for the Meta application.</p>"""
    name: (
        "capo_socialmessaging.types.meta_flow_application_name.MetaFlowApplicationName"
    )
    """<p>The name of the Meta application.</p>"""
    id: "capo_socialmessaging.types.meta_flow_application_id.MetaFlowApplicationId"
    """<p>The unique identifier of the Meta application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetaFlowApplicationInfo) -> dict:
    out: dict = {}
    if "link" in value:
        out["link"] = value["link"]
    out["name"] = value["name"]
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> MetaFlowApplicationInfo:
    out: MetaFlowApplicationInfo = {}  # type: ignore[typeddict-item]
    if data.get("link") is not None:
        out["link"] = data["link"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out
