"""Generated from Smithy shape ``com.amazonaws.servicediscovery#PrivateDnsPropertiesMutableChange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_servicediscovery.types.soa_change


class PrivateDnsPropertiesMutableChange(TypedDict, closed=True):
    soa: "capo_servicediscovery.types.soa_change.SOAChange"
    """<p>Updated fields for the Start of Authority (SOA) record for the hosted zone for the private DNS namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PrivateDnsPropertiesMutableChange) -> dict:
    out: dict = {}
    import capo_servicediscovery.types.soa_change

    out["SOA"] = capo_servicediscovery.types.soa_change.serialize_aws_json_1_1(
        value["soa"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PrivateDnsPropertiesMutableChange:
    out: PrivateDnsPropertiesMutableChange = {}  # type: ignore[typeddict-item]
    if data.get("SOA") is not None:
        import capo_servicediscovery.types.soa_change

        out["soa"] = capo_servicediscovery.types.soa_change.deserialize_aws_json_1_1(
            data["SOA"]
        )
    else:
        raise DeserializationError("PrivateDnsPropertiesMutableChange.soa required")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PrivateDnsPropertiesMutableChange) -> dict:
    out: dict = {}
    import capo_servicediscovery.types.soa_change

    out["SOA"] = capo_servicediscovery.types.soa_change.serialize_cbor(value["soa"])
    return out


def deserialize_cbor(data: dict) -> PrivateDnsPropertiesMutableChange:
    out: PrivateDnsPropertiesMutableChange = {}  # type: ignore[typeddict-item]
    if data.get("SOA") is not None:
        import capo_servicediscovery.types.soa_change

        out["soa"] = capo_servicediscovery.types.soa_change.deserialize_cbor(
            data["SOA"]
        )
    else:
        raise DeserializationError("PrivateDnsPropertiesMutableChange.soa required")
    return out
