"""Generated from Smithy shape ``com.amazonaws.ec2#VpnConnectionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpn_connection

VpnConnectionList: TypeAlias = list["capo_ec2.types.vpn_connection.VpnConnection"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpnConnectionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.vpn_connection

        capo_ec2.types.vpn_connection.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> VpnConnectionList:
    import capo_ec2.types.vpn_connection

    out: VpnConnectionList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.vpn_connection.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> VpnConnectionList:
    import capo_ec2.types.vpn_connection

    out: VpnConnectionList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.vpn_connection.deserialize_ec2_query(child))
    return out


def redact_sensitive(value: VpnConnectionList) -> list[Any]:
    import capo_ec2.types.vpn_connection

    return [capo_ec2.types.vpn_connection.redact_sensitive(item) for item in value]
