"""Generated from Smithy shape ``com.amazonaws.route53domains#AssociateDelegationSignerToDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53_domains.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53_domains.types.dnssec_signing_attributes
    import capo_route_53_domains.types.domain_name


class AssociateDelegationSignerToDomainRequest(TypedDict, closed=True):
    domain_name: "capo_route_53_domains.types.domain_name.DomainName"
    """<p>The name of the domain.</p>"""
    signing_attributes: (
        "capo_route_53_domains.types.dnssec_signing_attributes.DnssecSigningAttributes"
    )
    """<p>The information about a key, including the algorithm, public key-value, and flags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateDelegationSignerToDomainRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    import capo_route_53_domains.types.dnssec_signing_attributes

    out["SigningAttributes"] = (
        capo_route_53_domains.types.dnssec_signing_attributes.serialize_aws_json_1_1(
            value["signing_attributes"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateDelegationSignerToDomainRequest:
    out: AssociateDelegationSignerToDomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    if data.get("SigningAttributes") is not None:
        import capo_route_53_domains.types.dnssec_signing_attributes

        out["signing_attributes"] = (
            capo_route_53_domains.types.dnssec_signing_attributes.deserialize_aws_json_1_1(
                data["SigningAttributes"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateDelegationSignerToDomainRequest.signing_attributes required"
        )
    return out
