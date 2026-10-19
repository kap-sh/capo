"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#NamespaceKeyEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.namespace_key_validation
    import capo_bedrock_agentcore_control.types.namespace_variable_key


class NamespaceKeyEntry(TypedDict, closed=True):
    key: "capo_bedrock_agentcore_control.types.namespace_variable_key.NamespaceVariableKey"
    """<p>The namespace variable key name.</p>"""
    validation: NotRequired[
        "capo_bedrock_agentcore_control.types.namespace_key_validation.NamespaceKeyValidation"
    ]
    """<p>The validation rules that constrain values for this namespace variable at runtime (<code>CreateEvent</code> API).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NamespaceKeyEntry) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    if "validation" in value:
        import capo_bedrock_agentcore_control.types.namespace_key_validation

        out["validation"] = (
            capo_bedrock_agentcore_control.types.namespace_key_validation.serialize_json(
                value["validation"]
            )
        )
    return out


def deserialize_json(data: dict) -> NamespaceKeyEntry:
    out: NamespaceKeyEntry = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("validation") is not None:
        import capo_bedrock_agentcore_control.types.namespace_key_validation

        out["validation"] = (
            capo_bedrock_agentcore_control.types.namespace_key_validation.deserialize_json(
                data["validation"]
            )
        )
    return out
