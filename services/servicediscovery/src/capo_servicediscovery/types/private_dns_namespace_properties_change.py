"""Generated from Smithy shape ``com.amazonaws.servicediscovery#PrivateDnsNamespacePropertiesChange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_servicediscovery.types.private_dns_properties_mutable_change


class PrivateDnsNamespacePropertiesChange(TypedDict, closed=True):
    dns_properties: "capo_servicediscovery.types.private_dns_properties_mutable_change.PrivateDnsPropertiesMutableChange"
    """<p>Updated DNS properties for the private DNS namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PrivateDnsNamespacePropertiesChange) -> dict:
    out: dict = {}
    import capo_servicediscovery.types.private_dns_properties_mutable_change

    out["DnsProperties"] = (
        capo_servicediscovery.types.private_dns_properties_mutable_change.serialize_aws_json_1_1(
            value["dns_properties"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PrivateDnsNamespacePropertiesChange:
    out: PrivateDnsNamespacePropertiesChange = {}  # type: ignore[typeddict-item]
    if data.get("DnsProperties") is not None:
        import capo_servicediscovery.types.private_dns_properties_mutable_change

        out["dns_properties"] = (
            capo_servicediscovery.types.private_dns_properties_mutable_change.deserialize_aws_json_1_1(
                data["DnsProperties"]
            )
        )
    else:
        raise DeserializationError(
            "PrivateDnsNamespacePropertiesChange.dns_properties required"
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PrivateDnsNamespacePropertiesChange) -> dict:
    out: dict = {}
    import capo_servicediscovery.types.private_dns_properties_mutable_change

    out["DnsProperties"] = (
        capo_servicediscovery.types.private_dns_properties_mutable_change.serialize_cbor(
            value["dns_properties"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> PrivateDnsNamespacePropertiesChange:
    out: PrivateDnsNamespacePropertiesChange = {}  # type: ignore[typeddict-item]
    if data.get("DnsProperties") is not None:
        import capo_servicediscovery.types.private_dns_properties_mutable_change

        out["dns_properties"] = (
            capo_servicediscovery.types.private_dns_properties_mutable_change.deserialize_cbor(
                data["DnsProperties"]
            )
        )
    else:
        raise DeserializationError(
            "PrivateDnsNamespacePropertiesChange.dns_properties required"
        )
    return out
