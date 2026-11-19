"""Generated from Smithy shape ``com.amazonaws.servicediscovery#NamespaceProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.dns_properties
    import capo_servicediscovery.types.http_properties


class NamespaceProperties(TypedDict, closed=True):
    dns_properties: NotRequired[
        "capo_servicediscovery.types.dns_properties.DnsProperties"
    ]
    """<p>A complex type that contains the ID for the Route 53 hosted zone that Cloud Map creates when you create a namespace.</p>"""
    http_properties: NotRequired[
        "capo_servicediscovery.types.http_properties.HttpProperties"
    ]
    """<p>A complex type that contains the name of an HTTP namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NamespaceProperties) -> dict:
    out: dict = {}
    if "dns_properties" in value:
        import capo_servicediscovery.types.dns_properties

        out["DnsProperties"] = (
            capo_servicediscovery.types.dns_properties.serialize_aws_json_1_1(
                value["dns_properties"]
            )
        )
    if "http_properties" in value:
        import capo_servicediscovery.types.http_properties

        out["HttpProperties"] = (
            capo_servicediscovery.types.http_properties.serialize_aws_json_1_1(
                value["http_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NamespaceProperties:
    out: NamespaceProperties = {}  # type: ignore[typeddict-item]
    if data.get("DnsProperties") is not None:
        import capo_servicediscovery.types.dns_properties

        out["dns_properties"] = (
            capo_servicediscovery.types.dns_properties.deserialize_aws_json_1_1(
                data["DnsProperties"]
            )
        )
    if data.get("HttpProperties") is not None:
        import capo_servicediscovery.types.http_properties

        out["http_properties"] = (
            capo_servicediscovery.types.http_properties.deserialize_aws_json_1_1(
                data["HttpProperties"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NamespaceProperties) -> dict:
    out: dict = {}
    if "dns_properties" in value:
        import capo_servicediscovery.types.dns_properties

        out["DnsProperties"] = (
            capo_servicediscovery.types.dns_properties.serialize_cbor(
                value["dns_properties"]
            )
        )
    if "http_properties" in value:
        import capo_servicediscovery.types.http_properties

        out["HttpProperties"] = (
            capo_servicediscovery.types.http_properties.serialize_cbor(
                value["http_properties"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> NamespaceProperties:
    out: NamespaceProperties = {}  # type: ignore[typeddict-item]
    if data.get("DnsProperties") is not None:
        import capo_servicediscovery.types.dns_properties

        out["dns_properties"] = (
            capo_servicediscovery.types.dns_properties.deserialize_cbor(
                data["DnsProperties"]
            )
        )
    if data.get("HttpProperties") is not None:
        import capo_servicediscovery.types.http_properties

        out["http_properties"] = (
            capo_servicediscovery.types.http_properties.deserialize_cbor(
                data["HttpProperties"]
            )
        )
    return out
