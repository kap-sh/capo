"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaFlowPreviewInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.meta_flow_preview_url
    import capo_socialmessaging.types.meta_flow_timestamp


class MetaFlowPreviewInfo(TypedDict, closed=True):
    preview_url: "capo_socialmessaging.types.meta_flow_preview_url.MetaFlowPreviewUrl"
    """<p>The web URL for previewing the Flow. Can be shared with stakeholders for review.</p>"""
    expires_at: "capo_socialmessaging.types.meta_flow_timestamp.MetaFlowTimestamp"
    """<p>The timestamp when the preview URL expires.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetaFlowPreviewInfo) -> dict:
    out: dict = {}
    out["previewUrl"] = value["preview_url"]
    out["expiresAt"] = value["expires_at"]
    return out


def deserialize_json(data: dict) -> MetaFlowPreviewInfo:
    out: MetaFlowPreviewInfo = {}  # type: ignore[typeddict-item]
    if data.get("previewUrl") is not None:
        out["preview_url"] = data["previewUrl"]
    else:
        out["preview_url"] = ""
    if data.get("expiresAt") is not None:
        out["expires_at"] = data["expiresAt"]
    else:
        out["expires_at"] = ""
    return out
