"""Generated from Smithy shape ``com.amazonaws.servicediscovery#PublicDnsPropertiesMutable``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_servicediscovery.types.soa


class PublicDnsPropertiesMutable(TypedDict, closed=True):
    soa: "capo_servicediscovery.types.soa.SOA"
    """<p>Start of Authority (SOA) record for the hosted zone for the public DNS namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PublicDnsPropertiesMutable) -> dict:
    out: dict = {}
    import capo_servicediscovery.types.soa

    out["SOA"] = capo_servicediscovery.types.soa.serialize_aws_json_1_1(value["soa"])
    return out


def deserialize_aws_json_1_1(data: dict) -> PublicDnsPropertiesMutable:
    out: PublicDnsPropertiesMutable = {}  # type: ignore[typeddict-item]
    if data.get("SOA") is not None:
        import capo_servicediscovery.types.soa

        out["soa"] = capo_servicediscovery.types.soa.deserialize_aws_json_1_1(
            data["SOA"]
        )
    else:
        raise DeserializationError("PublicDnsPropertiesMutable.soa required")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PublicDnsPropertiesMutable) -> dict:
    out: dict = {}
    import capo_servicediscovery.types.soa

    out["SOA"] = capo_servicediscovery.types.soa.serialize_cbor(value["soa"])
    return out


def deserialize_cbor(data: dict) -> PublicDnsPropertiesMutable:
    out: PublicDnsPropertiesMutable = {}  # type: ignore[typeddict-item]
    if data.get("SOA") is not None:
        import capo_servicediscovery.types.soa

        out["soa"] = capo_servicediscovery.types.soa.deserialize_cbor(data["SOA"])
    else:
        raise DeserializationError("PublicDnsPropertiesMutable.soa required")
    return out
