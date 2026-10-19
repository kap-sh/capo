"""Generated from Smithy shape ``com.amazonaws.mediaconnect#PublicRouterNetworkInterfaceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.network_interface_rule_list


class PublicRouterNetworkInterfaceConfiguration(TypedDict, closed=True):
    allow_rules: (
        "capo_mediaconnect.types.network_interface_rule_list.NetworkInterfaceRuleList"
    )
    """<p>The list of allowed CIDR blocks for the public router network interface.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublicRouterNetworkInterfaceConfiguration) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.network_interface_rule_list

    out["allowRules"] = (
        capo_mediaconnect.types.network_interface_rule_list.serialize_json(
            value["allow_rules"]
        )
    )
    return out


def deserialize_json(data: dict) -> PublicRouterNetworkInterfaceConfiguration:
    out: PublicRouterNetworkInterfaceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("allowRules") is not None:
        import capo_mediaconnect.types.network_interface_rule_list

        out["allow_rules"] = (
            capo_mediaconnect.types.network_interface_rule_list.deserialize_json(
                data["allowRules"]
            )
        )
    else:
        out["allow_rules"] = []
    return out
