"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BrowserEnterprisePolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.browser_enterprise_policy_type
    import capo_bedrock_agentcore.types.resource_location


class BrowserEnterprisePolicy(TypedDict, closed=True):
    location: "capo_bedrock_agentcore.types.resource_location.ResourceLocation"
    """<p>The location of the enterprise policy file.</p>"""
    type: NotRequired[
        "capo_bedrock_agentcore.types.browser_enterprise_policy_type.BrowserEnterprisePolicyType"
    ]
    """<p>The enterprise policy type. See BrowserEnterprisePolicyType.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrowserEnterprisePolicy) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.resource_location

    out["location"] = capo_bedrock_agentcore.types.resource_location.serialize_json(
        value["location"]
    )
    if "type" in value:
        import capo_bedrock_agentcore.types.browser_enterprise_policy_type

        out["type"] = (
            capo_bedrock_agentcore.types.browser_enterprise_policy_type.serialize_json(
                value["type"]
            )
        )
    return out


def deserialize_json(data: dict) -> BrowserEnterprisePolicy:
    out: BrowserEnterprisePolicy = {}  # type: ignore[typeddict-item]
    if data.get("location") is not None:
        import capo_bedrock_agentcore.types.resource_location

        out["location"] = (
            capo_bedrock_agentcore.types.resource_location.deserialize_json(
                data["location"]
            )
        )
    else:
        out["location"] = {"$unknown": {"name": ""}}
    if data.get("type") is not None:
        import capo_bedrock_agentcore.types.browser_enterprise_policy_type

        out["type"] = (
            capo_bedrock_agentcore.types.browser_enterprise_policy_type.deserialize_json(
                data["type"]
            )
        )
    return out
