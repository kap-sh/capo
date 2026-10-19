"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Variant``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.variant_configuration
    import capo_bedrock_agentcore.types.variant_name


class Variant(TypedDict, closed=True):
    name: "capo_bedrock_agentcore.types.variant_name.VariantName"
    """<p>The name of the variant. Must be <code>C</code> for control or <code>T1</code> for treatment.</p>"""
    weight: "int"
    """<p>The percentage of traffic to route to this variant. Weights across all variants must sum to 100.</p>"""
    variant_configuration: (
        "capo_bedrock_agentcore.types.variant_configuration.VariantConfiguration"
    )
    """<p>The configuration for this variant, including the configuration bundle or target reference.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Variant) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["weight"] = value["weight"]
    import capo_bedrock_agentcore.types.variant_configuration

    out["variantConfiguration"] = (
        capo_bedrock_agentcore.types.variant_configuration.serialize_json(
            value["variant_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> Variant:
    out: Variant = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("weight") is not None:
        out["weight"] = data["weight"]
    else:
        out["weight"] = 0
    if data.get("variantConfiguration") is not None:
        import capo_bedrock_agentcore.types.variant_configuration

        out["variant_configuration"] = (
            capo_bedrock_agentcore.types.variant_configuration.deserialize_json(
                data["variantConfiguration"]
            )
        )
    else:
        raise DeserializationError("Variant.variant_configuration required")
    return out
