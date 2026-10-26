"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PrivateEndpointOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.private_endpoint
    import capo_bedrock_agentcore_control.types.private_endpoint_override_domain


class PrivateEndpointOverride(TypedDict, closed=True):
    domain: "capo_bedrock_agentcore_control.types.private_endpoint_override_domain.PrivateEndpointOverrideDomain"
    """<p>The domain to override with a private endpoint.</p>"""
    private_endpoint: (
        "capo_bedrock_agentcore_control.types.private_endpoint.PrivateEndpoint"
    )
    """<p>The private endpoint configuration for the specified domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrivateEndpointOverride) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    import capo_bedrock_agentcore_control.types.private_endpoint

    out["privateEndpoint"] = (
        capo_bedrock_agentcore_control.types.private_endpoint.serialize_json(
            value["private_endpoint"]
        )
    )
    return out


def deserialize_json(data: dict) -> PrivateEndpointOverride:
    out: PrivateEndpointOverride = {}  # type: ignore[typeddict-item]
    if data.get("domain") is not None:
        out["domain"] = data["domain"]
    else:
        out["domain"] = ""
    if data.get("privateEndpoint") is not None:
        import capo_bedrock_agentcore_control.types.private_endpoint

        out["private_endpoint"] = (
            capo_bedrock_agentcore_control.types.private_endpoint.deserialize_json(
                data["privateEndpoint"]
            )
        )
    else:
        out["private_endpoint"] = {"$unknown": {"name": ""}}
    return out
