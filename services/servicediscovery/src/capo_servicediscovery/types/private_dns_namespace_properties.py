"""Generated from Smithy shape ``com.amazonaws.servicediscovery#PrivateDnsNamespaceProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_servicediscovery.types.private_dns_properties_mutable


class PrivateDnsNamespaceProperties(TypedDict, closed=True):
    dns_properties: "capo_servicediscovery.types.private_dns_properties_mutable.PrivateDnsPropertiesMutable"
    """<p>DNS properties for the private DNS namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PrivateDnsNamespaceProperties) -> dict:
    out: dict = {}
    import capo_servicediscovery.types.private_dns_properties_mutable

    out["DnsProperties"] = (
        capo_servicediscovery.types.private_dns_properties_mutable.serialize_aws_json_1_1(
            value["dns_properties"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PrivateDnsNamespaceProperties:
    out: PrivateDnsNamespaceProperties = {}  # type: ignore[typeddict-item]
    if data.get("DnsProperties") is not None:
        import capo_servicediscovery.types.private_dns_properties_mutable

        out["dns_properties"] = (
            capo_servicediscovery.types.private_dns_properties_mutable.deserialize_aws_json_1_1(
                data["DnsProperties"]
            )
        )
    else:
        raise DeserializationError(
            "PrivateDnsNamespaceProperties.dns_properties required"
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PrivateDnsNamespaceProperties) -> dict:
    out: dict = {}
    import capo_servicediscovery.types.private_dns_properties_mutable

    out["DnsProperties"] = (
        capo_servicediscovery.types.private_dns_properties_mutable.serialize_cbor(
            value["dns_properties"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> PrivateDnsNamespaceProperties:
    out: PrivateDnsNamespaceProperties = {}  # type: ignore[typeddict-item]
    if data.get("DnsProperties") is not None:
        import capo_servicediscovery.types.private_dns_properties_mutable

        out["dns_properties"] = (
            capo_servicediscovery.types.private_dns_properties_mutable.deserialize_cbor(
                data["DnsProperties"]
            )
        )
    else:
        raise DeserializationError(
            "PrivateDnsNamespaceProperties.dns_properties required"
        )
    return out
