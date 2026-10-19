"""Generated from Smithy shape ``com.amazonaws.socialmessaging#GetWhatsAppFlowPreviewOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_socialmessaging.types.meta_flow_id
    import capo_socialmessaging.types.meta_flow_preview_info


class GetWhatsAppFlowPreviewOutput(TypedDict, closed=True):
    flow_id: "capo_socialmessaging.types.meta_flow_id.MetaFlowId"
    """<p>The unique identifier of the Flow.</p>"""
    preview: "capo_socialmessaging.types.meta_flow_preview_info.MetaFlowPreviewInfo"
    """<p>The preview URL and its expiration timestamp.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWhatsAppFlowPreviewOutput) -> dict:
    out: dict = {}
    out["flowId"] = value["flow_id"]
    import capo_socialmessaging.types.meta_flow_preview_info

    out["preview"] = capo_socialmessaging.types.meta_flow_preview_info.serialize_json(
        value["preview"]
    )
    return out


def deserialize_json(data: dict) -> GetWhatsAppFlowPreviewOutput:
    out: GetWhatsAppFlowPreviewOutput = {}  # type: ignore[typeddict-item]
    if data.get("flowId") is not None:
        out["flow_id"] = data["flowId"]
    else:
        out["flow_id"] = ""
    if data.get("preview") is not None:
        import capo_socialmessaging.types.meta_flow_preview_info

        out["preview"] = (
            capo_socialmessaging.types.meta_flow_preview_info.deserialize_json(
                data["preview"]
            )
        )
    else:
        raise DeserializationError("GetWhatsAppFlowPreviewOutput.preview required")
    return out
