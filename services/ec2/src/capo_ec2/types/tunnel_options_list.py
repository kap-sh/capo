"""Generated from Smithy shape ``com.amazonaws.ec2#TunnelOptionsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.tunnel_option

TunnelOptionsList: TypeAlias = list["capo_ec2.types.tunnel_option.TunnelOption"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TunnelOptionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.tunnel_option

        capo_ec2.types.tunnel_option.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> TunnelOptionsList:
    import capo_ec2.types.tunnel_option

    out: TunnelOptionsList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.tunnel_option.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> TunnelOptionsList:
    import capo_ec2.types.tunnel_option

    out: TunnelOptionsList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.tunnel_option.deserialize_ec2_query(child))
    return out


def redact_sensitive(value: TunnelOptionsList) -> list[Any]:
    import capo_ec2.types.tunnel_option

    return [capo_ec2.types.tunnel_option.redact_sensitive(item) for item in value]
