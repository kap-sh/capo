"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#PrivateEndpointOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_agent_registry_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry_control.types.private_endpoint
    import capo_agent_registry_control.types.private_endpoint_override_domain


class PrivateEndpointOverride(TypedDict, closed=True):
    domain: "capo_agent_registry_control.types.private_endpoint_override_domain.PrivateEndpointOverrideDomain"
    """<p>The domain name to which this private endpoint override applies.</p>"""
    private_endpoint: (
        "capo_agent_registry_control.types.private_endpoint.PrivateEndpoint"
    )
    """<p>The private endpoint used to reach the specified domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrivateEndpointOverride) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    import capo_agent_registry_control.types.private_endpoint

    out["privateEndpoint"] = (
        capo_agent_registry_control.types.private_endpoint.serialize_json(
            value["private_endpoint"]
        )
    )
    return out


def deserialize_json(data: dict) -> PrivateEndpointOverride:
    out: PrivateEndpointOverride = {}  # type: ignore[typeddict-item]
    if data.get("domain") is not None:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("PrivateEndpointOverride.domain required")
    if data.get("privateEndpoint") is not None:
        import capo_agent_registry_control.types.private_endpoint

        out["private_endpoint"] = (
            capo_agent_registry_control.types.private_endpoint.deserialize_json(
                data["privateEndpoint"]
            )
        )
    else:
        raise DeserializationError("PrivateEndpointOverride.private_endpoint required")
    return out
