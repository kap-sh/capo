"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxySettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.listener_properties


class ProxySettings(TypedDict, closed=True):
    listener_properties: (
        "capo_network_firewall.types.listener_properties.ListenerProperties"
    )
    """<p>Listener properties for HTTP and HTTPS traffic. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProxySettings) -> dict:
    out: dict = {}
    import capo_network_firewall.types.listener_properties

    out["ListenerProperties"] = (
        capo_network_firewall.types.listener_properties.serialize_aws_json_1_0(
            value["listener_properties"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProxySettings:
    out: ProxySettings = {}  # type: ignore[typeddict-item]
    if data.get("ListenerProperties") is not None:
        import capo_network_firewall.types.listener_properties

        out["listener_properties"] = (
            capo_network_firewall.types.listener_properties.deserialize_aws_json_1_0(
                data["ListenerProperties"]
            )
        )
    else:
        out["listener_properties"] = []
    return out
