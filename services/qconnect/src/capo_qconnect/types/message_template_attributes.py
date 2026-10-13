"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateAttributes``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.agent_attributes
    import capo_qconnect.types.custom_attributes
    import capo_qconnect.types.customer_profile_attributes
    import capo_qconnect.types.system_attributes


class MessageTemplateAttributes(TypedDict, closed=True):
    system_attributes: NotRequired[
        "capo_qconnect.types.system_attributes.SystemAttributes"
    ]
    """<p>The system attributes that are used with the message template.</p>"""
    agent_attributes: NotRequired[
        "capo_qconnect.types.agent_attributes.AgentAttributes"
    ]
    """<p>The agent attributes that are used with the message template.</p>"""
    customer_profile_attributes: NotRequired[
        "capo_qconnect.types.customer_profile_attributes.CustomerProfileAttributes"
    ]
    """<p>The customer profile attributes that are used with the message template.</p>"""
    custom_attributes: NotRequired[
        "capo_qconnect.types.custom_attributes.CustomAttributes"
    ]
    """<p>The custom attributes that are used with the message template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateAttributes) -> dict:
    out: dict = {}
    if "system_attributes" in value:
        import capo_qconnect.types.system_attributes

        out["systemAttributes"] = capo_qconnect.types.system_attributes.serialize_json(
            value["system_attributes"]
        )
    if "agent_attributes" in value:
        import capo_qconnect.types.agent_attributes

        out["agentAttributes"] = capo_qconnect.types.agent_attributes.serialize_json(
            value["agent_attributes"]
        )
    if "customer_profile_attributes" in value:
        import capo_qconnect.types.customer_profile_attributes

        out["customerProfileAttributes"] = (
            capo_qconnect.types.customer_profile_attributes.serialize_json(
                value["customer_profile_attributes"]
            )
        )
    if "custom_attributes" in value:
        import capo_qconnect.types.custom_attributes

        out["customAttributes"] = capo_qconnect.types.custom_attributes.serialize_json(
            value["custom_attributes"]
        )
    return out


def deserialize_json(data: dict) -> MessageTemplateAttributes:
    out: MessageTemplateAttributes = {}  # type: ignore[typeddict-item]
    if data.get("systemAttributes") is not None:
        import capo_qconnect.types.system_attributes

        out["system_attributes"] = (
            capo_qconnect.types.system_attributes.deserialize_json(
                data["systemAttributes"]
            )
        )
    if data.get("agentAttributes") is not None:
        import capo_qconnect.types.agent_attributes

        out["agent_attributes"] = capo_qconnect.types.agent_attributes.deserialize_json(
            data["agentAttributes"]
        )
    if data.get("customerProfileAttributes") is not None:
        import capo_qconnect.types.customer_profile_attributes

        out["customer_profile_attributes"] = (
            capo_qconnect.types.customer_profile_attributes.deserialize_json(
                data["customerProfileAttributes"]
            )
        )
    if data.get("customAttributes") is not None:
        import capo_qconnect.types.custom_attributes

        out["custom_attributes"] = (
            capo_qconnect.types.custom_attributes.deserialize_json(
                data["customAttributes"]
            )
        )
    return out


def redact_sensitive(value: MessageTemplateAttributes) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "system_attributes" in value:
        import capo_qconnect.types.system_attributes

        out["system_attributes"] = (
            capo_qconnect.types.system_attributes.redact_sensitive(
                value["system_attributes"]
            )
        )
    if "agent_attributes" in value:
        import capo_qconnect.types.agent_attributes

        out["agent_attributes"] = capo_qconnect.types.agent_attributes.redact_sensitive(
            value["agent_attributes"]
        )
    if "customer_profile_attributes" in value:
        import capo_qconnect.types.customer_profile_attributes

        out["customer_profile_attributes"] = (
            capo_qconnect.types.customer_profile_attributes.redact_sensitive(
                value["customer_profile_attributes"]
            )
        )
    if "custom_attributes" in value:
        out["custom_attributes"] = "*** Sensitive Data Redacted ***"
    return out
