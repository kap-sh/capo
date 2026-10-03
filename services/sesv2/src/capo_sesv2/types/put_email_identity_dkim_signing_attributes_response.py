"""Generated from Smithy shape ``com.amazonaws.sesv2#PutEmailIdentityDkimSigningAttributesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.dkim_status
    import capo_sesv2.types.dns_token_list
    import capo_sesv2.types.hosted_zone


class PutEmailIdentityDkimSigningAttributesResponse(TypedDict, closed=True):
    dkim_status: NotRequired["capo_sesv2.types.dkim_status.DkimStatus"]
    """<p>The DKIM authentication status of the identity. Amazon SES determines the authentication status by searching for specific records in the DNS configuration for your domain. If you used <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html">Easy DKIM</a> to set up DKIM authentication, Amazon SES tries to find three unique CNAME records in the DNS configuration for your domain.</p> <p>If you provided a public key to perform DKIM authentication, Amazon SES tries to find a TXT record that uses the selector that you specified. The value of the TXT record must be a public key that's paired with the private key that you specified in the process of creating the identity.</p> <p>The status can be one of the following:</p> <ul> <li> <p> <code>PENDING</code> – The verification process was initiated, but Amazon SES hasn't yet detected the DKIM records in the DNS configuration for the domain.</p> </li> <li> <p> <code>SUCCESS</code> – The verification process completed successfully.</p> </li> <li> <p> <code>FAILED</code> – The verification process failed. This typically occurs when Amazon SES fails to find the DKIM records in the DNS configuration of the domain.</p> </li> <li> <p> <code>TEMPORARY_FAILURE</code> – A temporary issue is preventing Amazon SES from determining the DKIM authentication status of the domain.</p> </li> <li> <p> <code>NOT_STARTED</code> – The DKIM verification process hasn't been initiated for the domain.</p> </li> </ul>"""
    dkim_tokens: NotRequired["capo_sesv2.types.dns_token_list.DnsTokenList"]
    """<p>If you used <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html">Easy DKIM</a> to configure DKIM authentication for the domain, then this object contains a set of unique strings that you use to create a set of CNAME records that you add to the DNS configuration for your domain. When Amazon SES detects these records in the DNS configuration for your domain, the DKIM authentication process is complete.</p> <p>If you configured DKIM authentication for the domain by providing your own public-private key pair, then this object contains the selector that's associated with your public key.</p> <p>Regardless of the DKIM authentication method you use, Amazon SES searches for the appropriate records in the DNS configuration of the domain for up to 72 hours.</p>"""
    signing_hosted_zone: NotRequired["capo_sesv2.types.hosted_zone.HostedZone"]
    """<p>The hosted zone where Amazon SES publishes the DKIM public key TXT records for this email identity. This value indicates the DNS zone that customers must reference when configuring their CNAME records for DKIM authentication.</p> <p>When configuring DKIM for your domain, create CNAME records in your DNS that point to the selectors in this hosted zone. For example:</p> <p> <code> selector1._domainkey.yourdomain.com CNAME selector1.<SigningHostedZone> </code> </p> <p> <code> selector2._domainkey.yourdomain.com CNAME selector2.<SigningHostedZone> </code> </p> <p> <code> selector3._domainkey.yourdomain.com CNAME selector3.<SigningHostedZone> </code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutEmailIdentityDkimSigningAttributesResponse) -> dict:
    out: dict = {}
    if "dkim_status" in value:
        import capo_sesv2.types.dkim_status

        out["DkimStatus"] = capo_sesv2.types.dkim_status.serialize_json(
            value["dkim_status"]
        )
    if "dkim_tokens" in value:
        import capo_sesv2.types.dns_token_list

        out["DkimTokens"] = capo_sesv2.types.dns_token_list.serialize_json(
            value["dkim_tokens"]
        )
    if "signing_hosted_zone" in value:
        out["SigningHostedZone"] = value["signing_hosted_zone"]
    return out


def deserialize_json(data: dict) -> PutEmailIdentityDkimSigningAttributesResponse:
    out: PutEmailIdentityDkimSigningAttributesResponse = {}  # type: ignore[typeddict-item]
    if data.get("DkimStatus") is not None:
        import capo_sesv2.types.dkim_status

        out["dkim_status"] = capo_sesv2.types.dkim_status.deserialize_json(
            data["DkimStatus"]
        )
    if data.get("DkimTokens") is not None:
        import capo_sesv2.types.dns_token_list

        out["dkim_tokens"] = capo_sesv2.types.dns_token_list.deserialize_json(
            data["DkimTokens"]
        )
    if data.get("SigningHostedZone") is not None:
        out["signing_hosted_zone"] = data["SigningHostedZone"]
    return out
