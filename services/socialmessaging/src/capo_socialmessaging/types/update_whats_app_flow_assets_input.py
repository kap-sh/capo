"""Generated from Smithy shape ``com.amazonaws.socialmessaging#UpdateWhatsAppFlowAssetsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.linked_whats_app_business_account_id
    import capo_socialmessaging.types.meta_flow_id
    import capo_socialmessaging.types.meta_flow_json_blob


class UpdateWhatsAppFlowAssetsInput(TypedDict, closed=True):
    id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The ID of the WhatsApp Business Account associated with this Flow.</p>"""
    flow_id: "capo_socialmessaging.types.meta_flow_id.MetaFlowId"
    """<p>The unique identifier of the Flow whose assets to update.</p>"""
    flow_json: "capo_socialmessaging.types.meta_flow_json_blob.MetaFlowJsonBlob"
    """<p>The updated Flow JSON definition. Maximum size is 10 MB.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWhatsAppFlowAssetsInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["flowId"] = value["flow_id"]
    import capo_socialmessaging.types.meta_flow_json_blob

    out["flowJson"] = capo_socialmessaging.types.meta_flow_json_blob.serialize_json(
        value["flow_json"]
    )
    return out


def deserialize_json(data: dict) -> UpdateWhatsAppFlowAssetsInput:
    out: UpdateWhatsAppFlowAssetsInput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("flowId") is not None:
        out["flow_id"] = data["flowId"]
    else:
        out["flow_id"] = ""
    if data.get("flowJson") is not None:
        import capo_socialmessaging.types.meta_flow_json_blob

        out["flow_json"] = (
            capo_socialmessaging.types.meta_flow_json_blob.deserialize_json(
                data["flowJson"]
            )
        )
    else:
        out["flow_json"] = b""
    return out
