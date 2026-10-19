"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ContainerAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.container_attribute_key
    import capo_network_firewall.types.container_attribute_value


class ContainerAttribute(TypedDict, closed=True):
    key: "capo_network_firewall.types.container_attribute_key.ContainerAttributeKey"
    """<p>The attribute key to filter on.</p>"""
    value: (
        "capo_network_firewall.types.container_attribute_value.ContainerAttributeValue"
    )
    """<p>The attribute value to match.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContainerAttribute) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ContainerAttribute:
    out: ContainerAttribute = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
