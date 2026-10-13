"""Generated from Smithy shape ``com.amazonaws.qconnect#AgentAttributes``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.message_template_attribute_value


class AgentAttributes(TypedDict, closed=True):
    first_name: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The agent’s first name as entered in their Amazon Connect user account.</p>"""
    last_name: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The agent’s last name as entered in their Amazon Connect user account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentAttributes) -> dict:
    out: dict = {}
    if "first_name" in value:
        out["firstName"] = value["first_name"]
    if "last_name" in value:
        out["lastName"] = value["last_name"]
    return out


def deserialize_json(data: dict) -> AgentAttributes:
    out: AgentAttributes = {}  # type: ignore[typeddict-item]
    if data.get("firstName") is not None:
        out["first_name"] = data["firstName"]
    if data.get("lastName") is not None:
        out["last_name"] = data["lastName"]
    return out


def redact_sensitive(value: AgentAttributes) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "first_name" in value:
        out["first_name"] = "*** Sensitive Data Redacted ***"
    if "last_name" in value:
        out["last_name"] = "*** Sensitive Data Redacted ***"
    return out
