"""Generated from Smithy shape ``com.amazonaws.networkfirewall#TCPFlagField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.flags


class TCPFlagField(TypedDict, closed=True):
    flags: "capo_network_firewall.types.flags.Flags"
    """<p>Used in conjunction with the <code>Masks</code> setting to define the flags that must be set and flags that must not be set in order for the packet to match. This setting can only specify values that are also specified in the <code>Masks</code> setting.</p> <p>For the flags that are specified in the masks setting, the following must be true for the packet to match: </p> <ul> <li> <p>The ones that are set in this flags setting must be set in the packet. </p> </li> <li> <p>The ones that are not set in this flags setting must also not be set in the packet. </p> </li> </ul>"""
    masks: NotRequired["capo_network_firewall.types.flags.Flags"]
    """<p>The set of flags to consider in the inspection. To inspect all flags in the valid values list, leave this with no setting.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TCPFlagField) -> dict:
    out: dict = {}
    import capo_network_firewall.types.flags

    out["Flags"] = capo_network_firewall.types.flags.serialize_aws_json_1_0(
        value["flags"]
    )
    if "masks" in value:
        import capo_network_firewall.types.flags

        out["Masks"] = capo_network_firewall.types.flags.serialize_aws_json_1_0(
            value["masks"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TCPFlagField:
    out: TCPFlagField = {}  # type: ignore[typeddict-item]
    if data.get("Flags") is not None:
        import capo_network_firewall.types.flags

        out["flags"] = capo_network_firewall.types.flags.deserialize_aws_json_1_0(
            data["Flags"]
        )
    else:
        out["flags"] = []
    if data.get("Masks") is not None:
        import capo_network_firewall.types.flags

        out["masks"] = capo_network_firewall.types.flags.deserialize_aws_json_1_0(
            data["Masks"]
        )
    return out
