"""Generated from Smithy shape ``com.amazonaws.route53domains#DnssecSigningAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.dnssec_public_key
    import capo_route_53_domains.types.nullable_integer


class DnssecSigningAttributes(TypedDict, closed=True):
    algorithm: NotRequired[
        "capo_route_53_domains.types.nullable_integer.NullableInteger"
    ]
    """<p> Algorithm which was used to generate the digest from the public key. </p>"""
    flags: NotRequired["capo_route_53_domains.types.nullable_integer.NullableInteger"]
    """<p>Defines the type of key. It can be either a KSK (key-signing-key, value 257) or ZSK (zone-signing-key, value 256). Using KSK is always encouraged. Only use ZSK if your DNS provider isn't Route 53 and you don’t have KSK available.</p> <p>If you have KSK and ZSK keys, always use KSK to create a delegations signer (DS) record. If you have ZSK keys only – use ZSK to create a DS record.</p>"""
    public_key: NotRequired[
        "capo_route_53_domains.types.dnssec_public_key.DnssecPublicKey"
    ]
    """<p> The base64-encoded public key part of the key pair that is passed to the registry. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnssecSigningAttributes) -> dict:
    out: dict = {}
    if "algorithm" in value:
        out["Algorithm"] = value["algorithm"]
    if "flags" in value:
        out["Flags"] = value["flags"]
    if "public_key" in value:
        out["PublicKey"] = value["public_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DnssecSigningAttributes:
    out: DnssecSigningAttributes = {}  # type: ignore[typeddict-item]
    if data.get("Algorithm") is not None:
        out["algorithm"] = data["Algorithm"]
    if data.get("Flags") is not None:
        out["flags"] = data["Flags"]
    if data.get("PublicKey") is not None:
        out["public_key"] = data["PublicKey"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DnssecSigningAttributes) -> dict:
    out: dict = {}
    if "algorithm" in value:
        out["Algorithm"] = value["algorithm"]
    if "flags" in value:
        out["Flags"] = value["flags"]
    if "public_key" in value:
        out["PublicKey"] = value["public_key"]
    return out


def deserialize_cbor(data: dict) -> DnssecSigningAttributes:
    out: DnssecSigningAttributes = {}  # type: ignore[typeddict-item]
    if data.get("Algorithm") is not None:
        out["algorithm"] = data["Algorithm"]
    if data.get("Flags") is not None:
        out["flags"] = data["Flags"]
    if data.get("PublicKey") is not None:
        out["public_key"] = data["PublicKey"]
    return out
