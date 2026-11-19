"""Generated from Smithy shape ``com.amazonaws.servicediscovery#PrivateDnsPropertiesMutable``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_servicediscovery.types.soa


class PrivateDnsPropertiesMutable(TypedDict, closed=True):
    soa: "capo_servicediscovery.types.soa.SOA"
    """<p>Fields for the Start of Authority (SOA) record for the hosted zone for the private DNS namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PrivateDnsPropertiesMutable) -> dict:
    out: dict = {}
    import capo_servicediscovery.types.soa

    out["SOA"] = capo_servicediscovery.types.soa.serialize_aws_json_1_1(value["soa"])
    return out


def deserialize_aws_json_1_1(data: dict) -> PrivateDnsPropertiesMutable:
    out: PrivateDnsPropertiesMutable = {}  # type: ignore[typeddict-item]
    if data.get("SOA") is not None:
        import capo_servicediscovery.types.soa

        out["soa"] = capo_servicediscovery.types.soa.deserialize_aws_json_1_1(
            data["SOA"]
        )
    else:
        raise DeserializationError("PrivateDnsPropertiesMutable.soa required")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PrivateDnsPropertiesMutable) -> dict:
    out: dict = {}
    import capo_servicediscovery.types.soa

    out["SOA"] = capo_servicediscovery.types.soa.serialize_cbor(value["soa"])
    return out


def deserialize_cbor(data: dict) -> PrivateDnsPropertiesMutable:
    out: PrivateDnsPropertiesMutable = {}  # type: ignore[typeddict-item]
    if data.get("SOA") is not None:
        import capo_servicediscovery.types.soa

        out["soa"] = capo_servicediscovery.types.soa.deserialize_cbor(data["SOA"])
    else:
        raise DeserializationError("PrivateDnsPropertiesMutable.soa required")
    return out
