"""Generated from Smithy shape ``com.amazonaws.route53domains#DnssecKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.dnssec_public_key
    import capo_route_53_domains.types.nullable_integer
    import capo_route_53_domains.types.string


class DnssecKey(TypedDict, closed=True):
    algorithm: NotRequired[
        "capo_route_53_domains.types.nullable_integer.NullableInteger"
    ]
    """<p>The number of the public key’s cryptographic algorithm according to an <a href="https://www.iana.org/assignments/dns-sec-alg-numbers/dns-sec-alg-numbers.xml">IANA</a> assignment. </p> <p>If Route 53 is your DNS service, set this to 13.</p> <p>For more information about enabling DNSSEC signing, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec-enable-signing.html">Enabling DNSSEC signing and establishing a chain of trust</a>.</p>"""
    flags: NotRequired["capo_route_53_domains.types.nullable_integer.NullableInteger"]
    """<p>Defines the type of key. It can be either a KSK (key-signing-key, value 257) or ZSK (zone-signing-key, value 256). Using KSK is always encouraged. Only use ZSK if your DNS provider isn't Route 53 and you don’t have KSK available.</p> <p>If you have KSK and ZSK keys, always use KSK to create a delegations signer (DS) record. If you have ZSK keys only – use ZSK to create a DS record.</p>"""
    public_key: NotRequired[
        "capo_route_53_domains.types.dnssec_public_key.DnssecPublicKey"
    ]
    """<p>The base64-encoded public key part of the key pair that is passed to the registry .</p>"""
    digest_type: NotRequired[
        "capo_route_53_domains.types.nullable_integer.NullableInteger"
    ]
    """<p> The number of the DS digest algorithm according to an IANA assignment.</p> <p>For more information, see <a href="https://www.iana.org/assignments/ds-rr-types/ds-rr-types.xhtml">IANA</a> for DNSSEC Delegation Signer (DS) Resource Record (RR) Type Digest Algorithms. </p>"""
    digest: NotRequired["capo_route_53_domains.types.string.String"]
    """<p> The delegation signer digest.</p> <p>Digest is calculated from the public key provided using specified digest algorithm and this digest is the actual value returned from the registry nameservers as the value of DS records. </p>"""
    key_tag: NotRequired["capo_route_53_domains.types.nullable_integer.NullableInteger"]
    """<p> A numeric identification of the DNSKEY record referred to by this DS record. </p>"""
    id: NotRequired["capo_route_53_domains.types.string.String"]
    """<p> An ID assigned to each DS record created by <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_AssociateDelegationSignerToDomain.html">AssociateDelegationSignerToDomain</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnssecKey) -> dict:
    out: dict = {}
    if "algorithm" in value:
        out["Algorithm"] = value["algorithm"]
    if "flags" in value:
        out["Flags"] = value["flags"]
    if "public_key" in value:
        out["PublicKey"] = value["public_key"]
    if "digest_type" in value:
        out["DigestType"] = value["digest_type"]
    if "digest" in value:
        out["Digest"] = value["digest"]
    if "key_tag" in value:
        out["KeyTag"] = value["key_tag"]
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DnssecKey:
    out: DnssecKey = {}  # type: ignore[typeddict-item]
    if data.get("Algorithm") is not None:
        out["algorithm"] = data["Algorithm"]
    if data.get("Flags") is not None:
        out["flags"] = data["Flags"]
    if data.get("PublicKey") is not None:
        out["public_key"] = data["PublicKey"]
    if data.get("DigestType") is not None:
        out["digest_type"] = data["DigestType"]
    if data.get("Digest") is not None:
        out["digest"] = data["Digest"]
    if data.get("KeyTag") is not None:
        out["key_tag"] = data["KeyTag"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    return out
