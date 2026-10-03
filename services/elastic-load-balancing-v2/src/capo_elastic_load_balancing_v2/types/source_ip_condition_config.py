"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#SourceIpConditionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.list_of_string
    import capo_elastic_load_balancing_v2.types.source_ip_address_type_enum


class SourceIpConditionConfig(TypedDict, closed=True):
    values: NotRequired[
        "capo_elastic_load_balancing_v2.types.list_of_string.ListOfString"
    ]
    """<p>The source IP addresses, in CIDR format. You can use both IPv4 and IPv6 addresses. Wildcards are not supported.</p> <p>If you specify multiple addresses, the condition is satisfied if the source IP address of the request matches one of the CIDR blocks. This condition is not satisfied by the addresses in the X-Forwarded-For header. To search for addresses in the X-Forwarded-For header, use an <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html#http-header-conditions">HTTP header condition</a>.</p> <p>The total number of values must be less than, or equal to five.</p>"""
    ip_address_type: NotRequired[
        "capo_elastic_load_balancing_v2.types.source_ip_address_type_enum.SourceIpAddressTypeEnum"
    ]
    """<p>The IP address type for Network Load Balancers.</p> <p>The valid values are:</p> <ul> <li> <p> <code>ipv4</code> – IPv4 addresses only.</p> </li> <li> <p> <code>ipv6</code> – IPv6 addresses only.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SourceIpConditionConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "values" in value:
        import capo_elastic_load_balancing_v2.types.list_of_string

        capo_elastic_load_balancing_v2.types.list_of_string.serialize_query(
            value["values"], pairs, f"{key_prefix}Values"
        )
    if "ip_address_type" in value:
        import capo_elastic_load_balancing_v2.types.source_ip_address_type_enum

        capo_elastic_load_balancing_v2.types.source_ip_address_type_enum.serialize_query(
            value["ip_address_type"], pairs, f"{key_prefix}IpAddressType"
        )


def deserialize_query(el: Element) -> SourceIpConditionConfig:
    out: SourceIpConditionConfig = {}  # type: ignore[typeddict-item]
    child_values = el.find("Values")
    if child_values is not None:
        import capo_elastic_load_balancing_v2.types.list_of_string

        out["values"] = (
            capo_elastic_load_balancing_v2.types.list_of_string.deserialize_query(
                child_values
            )
        )
    child_ip_address_type = el.find("IpAddressType")
    if child_ip_address_type is not None:
        import capo_elastic_load_balancing_v2.types.source_ip_address_type_enum

        out["ip_address_type"] = (
            capo_elastic_load_balancing_v2.types.source_ip_address_type_enum.deserialize_query(
                child_ip_address_type
            )
        )
    return out
