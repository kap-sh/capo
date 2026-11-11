"""Generated from Smithy shape ``com.amazonaws.route53domains#RestoreDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.consent
    import capo_route_53_domains.types.domain_name


class RestoreDomainRequest(TypedDict, closed=True):
    domain_name: "capo_route_53_domains.types.domain_name.DomainName"
    """<p>The name of the domain that you want to restore. The domain must have been registered to the Amazon Web Services account that submits the request.</p>"""
    consent: NotRequired["capo_route_53_domains.types.consent.Consent"]
    """<p>Specifies the maximum price that you agree to pay to restore the domain name. This element is required if the domain has registry premium pricing, and optional if the domain is priced at the standard rate for its TLD. If you include it and the restoration price is more than <code>MaxPrice</code>, the request fails.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestoreDomainRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    if "consent" in value:
        import capo_route_53_domains.types.consent

        out["Consent"] = capo_route_53_domains.types.consent.serialize_aws_json_1_1(
            value["consent"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RestoreDomainRequest:
    out: RestoreDomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    if data.get("Consent") is not None:
        import capo_route_53_domains.types.consent

        out["consent"] = capo_route_53_domains.types.consent.deserialize_aws_json_1_1(
            data["Consent"]
        )
    return out
