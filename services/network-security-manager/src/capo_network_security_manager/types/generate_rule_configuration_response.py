"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#GenerateRuleConfigurationResponse``."""

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError


class GenerateRuleConfigurationResponse(TypedDict, closed=True):
    configuration: "str"
    """<p>The generated configuration, as a JSON string. You can use this value in the <code>configuration</code> field of a rule.</p>"""
    description: NotRequired["str"]
    """<p>Reserved for a future human-readable description of the generated configuration. This field is currently not populated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateRuleConfigurationResponse) -> dict:
    out: dict = {}
    out["configuration"] = value["configuration"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> GenerateRuleConfigurationResponse:
    out: GenerateRuleConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("configuration") is not None:
        out["configuration"] = data["configuration"]
    else:
        raise DeserializationError(
            "GenerateRuleConfigurationResponse.configuration required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
