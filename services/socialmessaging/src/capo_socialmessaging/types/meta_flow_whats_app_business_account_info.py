"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaFlowWhatsAppBusinessAccountInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.meta_flow_waba_currency
    import capo_socialmessaging.types.meta_flow_waba_template_namespace
    import capo_socialmessaging.types.meta_flow_waba_timezone_id
    import capo_socialmessaging.types.whats_app_business_account_id
    import capo_socialmessaging.types.whats_app_business_account_name


class MetaFlowWhatsAppBusinessAccountInfo(TypedDict, closed=True):
    id: "capo_socialmessaging.types.whats_app_business_account_id.WhatsAppBusinessAccountId"
    """<p>The WhatsApp Business Account ID from Meta.</p>"""
    name: "capo_socialmessaging.types.whats_app_business_account_name.WhatsAppBusinessAccountName"
    """<p>The name of the WhatsApp Business Account.</p>"""
    currency: NotRequired[
        "capo_socialmessaging.types.meta_flow_waba_currency.MetaFlowWabaCurrency"
    ]
    """<p>The currency code for the WhatsApp Business Account (for example, USD).</p>"""
    timezone_id: NotRequired[
        "capo_socialmessaging.types.meta_flow_waba_timezone_id.MetaFlowWabaTimezoneId"
    ]
    """<p>The timezone ID for the WhatsApp Business Account.</p>"""
    message_template_namespace: NotRequired[
        "capo_socialmessaging.types.meta_flow_waba_template_namespace.MetaFlowWabaTemplateNamespace"
    ]
    """<p>The message template namespace for the WhatsApp Business Account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetaFlowWhatsAppBusinessAccountInfo) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "currency" in value:
        out["currency"] = value["currency"]
    if "timezone_id" in value:
        out["timezoneId"] = value["timezone_id"]
    if "message_template_namespace" in value:
        out["messageTemplateNamespace"] = value["message_template_namespace"]
    return out


def deserialize_json(data: dict) -> MetaFlowWhatsAppBusinessAccountInfo:
    out: MetaFlowWhatsAppBusinessAccountInfo = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("currency") is not None:
        out["currency"] = data["currency"]
    if data.get("timezoneId") is not None:
        out["timezone_id"] = data["timezoneId"]
    if data.get("messageTemplateNamespace") is not None:
        out["message_template_namespace"] = data["messageTemplateNamespace"]
    return out
