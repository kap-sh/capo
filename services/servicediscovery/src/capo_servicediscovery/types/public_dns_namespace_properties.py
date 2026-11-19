"""Generated from Smithy shape ``com.amazonaws.servicediscovery#PublicDnsNamespaceProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_servicediscovery.types.public_dns_properties_mutable


class PublicDnsNamespaceProperties(TypedDict, closed=True):
    dns_properties: "capo_servicediscovery.types.public_dns_properties_mutable.PublicDnsPropertiesMutable"
    """<p>DNS properties for the public DNS namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PublicDnsNamespaceProperties) -> dict:
    out: dict = {}
    import capo_servicediscovery.types.public_dns_properties_mutable

    out["DnsProperties"] = (
        capo_servicediscovery.types.public_dns_properties_mutable.serialize_aws_json_1_1(
            value["dns_properties"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PublicDnsNamespaceProperties:
    out: PublicDnsNamespaceProperties = {}  # type: ignore[typeddict-item]
    if data.get("DnsProperties") is not None:
        import capo_servicediscovery.types.public_dns_properties_mutable

        out["dns_properties"] = (
            capo_servicediscovery.types.public_dns_properties_mutable.deserialize_aws_json_1_1(
                data["DnsProperties"]
            )
        )
    else:
        raise DeserializationError(
            "PublicDnsNamespaceProperties.dns_properties required"
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PublicDnsNamespaceProperties) -> dict:
    out: dict = {}
    import capo_servicediscovery.types.public_dns_properties_mutable

    out["DnsProperties"] = (
        capo_servicediscovery.types.public_dns_properties_mutable.serialize_cbor(
            value["dns_properties"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> PublicDnsNamespaceProperties:
    out: PublicDnsNamespaceProperties = {}  # type: ignore[typeddict-item]
    if data.get("DnsProperties") is not None:
        import capo_servicediscovery.types.public_dns_properties_mutable

        out["dns_properties"] = (
            capo_servicediscovery.types.public_dns_properties_mutable.deserialize_cbor(
                data["DnsProperties"]
            )
        )
    else:
        raise DeserializationError(
            "PublicDnsNamespaceProperties.dns_properties required"
        )
    return out
