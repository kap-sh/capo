"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ResourceContexts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.resource_context

ResourceContexts: TypeAlias = list[
    "capo_network_firewall.types.resource_context.ResourceContext"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceContexts) -> list:
    import capo_network_firewall.types.resource_context

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.resource_context.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ResourceContexts:
    import capo_network_firewall.types.resource_context

    out: ResourceContexts = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.resource_context.deserialize_aws_json_1_0(item)
        )
    return out
