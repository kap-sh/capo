"""Generated from Smithy shape ``com.amazonaws.socialmessaging#DeprecateWhatsAppFlowInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.linked_whats_app_business_account_id
    import capo_socialmessaging.types.meta_flow_id


class DeprecateWhatsAppFlowInput(TypedDict, closed=True):
    id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The ID of the WhatsApp Business Account associated with this Flow.</p>"""
    flow_id: "capo_socialmessaging.types.meta_flow_id.MetaFlowId"
    """<p>The unique identifier of the Flow to deprecate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeprecateWhatsAppFlowInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["flowId"] = value["flow_id"]
    return out


def deserialize_json(data: dict) -> DeprecateWhatsAppFlowInput:
    out: DeprecateWhatsAppFlowInput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("flowId") is not None:
        out["flow_id"] = data["flowId"]
    else:
        out["flow_id"] = ""
    return out
