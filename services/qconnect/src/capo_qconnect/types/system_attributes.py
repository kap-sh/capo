"""Generated from Smithy shape ``com.amazonaws.qconnect#SystemAttributes``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.message_template_attribute_value
    import capo_qconnect.types.system_endpoint_attributes


class SystemAttributes(TypedDict, closed=True):
    name: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The name of the task.</p>"""
    customer_endpoint: NotRequired[
        "capo_qconnect.types.system_endpoint_attributes.SystemEndpointAttributes"
    ]
    """<p>The CustomerEndpoint attribute.</p>"""
    system_endpoint: NotRequired[
        "capo_qconnect.types.system_endpoint_attributes.SystemEndpointAttributes"
    ]
    """<p>The SystemEndpoint attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SystemAttributes) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "customer_endpoint" in value:
        import capo_qconnect.types.system_endpoint_attributes

        out["customerEndpoint"] = (
            capo_qconnect.types.system_endpoint_attributes.serialize_json(
                value["customer_endpoint"]
            )
        )
    if "system_endpoint" in value:
        import capo_qconnect.types.system_endpoint_attributes

        out["systemEndpoint"] = (
            capo_qconnect.types.system_endpoint_attributes.serialize_json(
                value["system_endpoint"]
            )
        )
    return out


def deserialize_json(data: dict) -> SystemAttributes:
    out: SystemAttributes = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("customerEndpoint") is not None:
        import capo_qconnect.types.system_endpoint_attributes

        out["customer_endpoint"] = (
            capo_qconnect.types.system_endpoint_attributes.deserialize_json(
                data["customerEndpoint"]
            )
        )
    if data.get("systemEndpoint") is not None:
        import capo_qconnect.types.system_endpoint_attributes

        out["system_endpoint"] = (
            capo_qconnect.types.system_endpoint_attributes.deserialize_json(
                data["systemEndpoint"]
            )
        )
    return out


def redact_sensitive(value: SystemAttributes) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "customer_endpoint" in value:
        import capo_qconnect.types.system_endpoint_attributes

        out["customer_endpoint"] = (
            capo_qconnect.types.system_endpoint_attributes.redact_sensitive(
                value["customer_endpoint"]
            )
        )
    if "system_endpoint" in value:
        import capo_qconnect.types.system_endpoint_attributes

        out["system_endpoint"] = (
            capo_qconnect.types.system_endpoint_attributes.redact_sensitive(
                value["system_endpoint"]
            )
        )
    return out
