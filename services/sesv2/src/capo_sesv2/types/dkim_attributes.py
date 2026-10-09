"""Generated from Smithy shape ``com.amazonaws.sesv2#DkimAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.dkim_signing_attributes_origin
    import capo_sesv2.types.dkim_signing_key_length
    import capo_sesv2.types.dkim_status
    import capo_sesv2.types.dns_token_list
    import capo_sesv2.types.enabled
    import capo_sesv2.types.hosted_zone
    import capo_sesv2.types.timestamp


class DkimAttributes(TypedDict, closed=True):
    signing_enabled: "capo_sesv2.types.enabled.Enabled"
    """<p>If the value is <code>true</code>, then the messages that you send from the identity are signed using DKIM. If the value is <code>false</code>, then the messages that you send from the identity aren't DKIM-signed.</p>"""
    status: NotRequired["capo_sesv2.types.dkim_status.DkimStatus"]
    """<p>Describes whether or not Amazon SES has successfully located the DKIM records in the DNS records for the domain. The status can be one of the following:</p> <ul> <li> <p> <code>PENDING</code> – The verification process was initiated, but Amazon SES hasn't yet detected the DKIM records in the DNS configuration for the domain.</p> </li> <li> <p> <code>SUCCESS</code> – The verification process completed successfully.</p> </li> <li> <p> <code>FAILED</code> – The verification process failed. This typically occurs when Amazon SES fails to find the DKIM records in the DNS configuration of the domain.</p> </li> <li> <p> <code>TEMPORARY_FAILURE</code> – A temporary issue is preventing Amazon SES from determining the DKIM authentication status of the domain.</p> </li> <li> <p> <code>NOT_STARTED</code> – The DKIM verification process hasn't been initiated for the domain.</p> </li> </ul>"""
    tokens: NotRequired["capo_sesv2.types.dns_token_list.DnsTokenList"]
    """<p>If you used <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html">Easy DKIM</a> to configure DKIM authentication for the domain, then this object contains a set of unique strings that you use to create a set of CNAME records that you add to the DNS configuration for your domain. When Amazon SES detects these records in the DNS configuration for your domain, the DKIM authentication process is complete.</p> <p>If you configured DKIM authentication for the domain by providing your own public-private key pair, then this object contains the selector for the public key.</p> <p>Regardless of the DKIM authentication method you use, Amazon SES searches for the appropriate records in the DNS configuration of the domain for up to 72 hours.</p>"""
    signing_hosted_zone: NotRequired["capo_sesv2.types.hosted_zone.HostedZone"]
    """<p>The hosted zone where Amazon SES publishes the DKIM public key TXT records for this email identity. This value indicates the DNS zone that customers must reference when configuring their CNAME records for DKIM authentication.</p> <p>When configuring DKIM for your domain, create CNAME records in your DNS that point to the selectors in this hosted zone. For example:</p> <p> <code> selector1._domainkey.yourdomain.com CNAME selector1.<SigningHostedZone> </code> </p> <p> <code> selector2._domainkey.yourdomain.com CNAME selector2.<SigningHostedZone> </code> </p> <p> <code> selector3._domainkey.yourdomain.com CNAME selector3.<SigningHostedZone> </code> </p>"""
    signing_attributes_origin: NotRequired[
        "capo_sesv2.types.dkim_signing_attributes_origin.DkimSigningAttributesOrigin"
    ]
    """<p>A string that indicates how DKIM was configured for the identity. These are the possible values:</p> <ul> <li> <p> <code>AWS_SES</code> – Indicates that DKIM was configured for the identity by using <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html">Easy DKIM</a>.</p> </li> <li> <p> <code>EXTERNAL</code> – Indicates that DKIM was configured for the identity by using Bring Your Own DKIM (BYODKIM).</p> </li> <li> <p> <code>AWS_SES_<REGION></code> – Indicates that DKIM was configured for the identity by replicating the signing attributes of a parent identity in another Amazon Web Services Region, using <a href="https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-deed.html">Deterministic Easy-DKIM (DEED)</a>. <code><REGION></code> is the Amazon Web Services Region of the parent identity, in uppercase with each hyphen replaced by an underscore. Amazon SES uses this format for every Amazon Web Services Region in which it supports DEED. For example, a parent identity in <code>us-east-1</code> is reported as <code>AWS_SES_US_EAST_1</code>.</p> </li> </ul>"""
    next_signing_key_length: NotRequired[
        "capo_sesv2.types.dkim_signing_key_length.DkimSigningKeyLength"
    ]
    """<p>[Easy DKIM] The key length of the future DKIM key pair to be generated. This can be changed at most once per day.</p>"""
    current_signing_key_length: NotRequired[
        "capo_sesv2.types.dkim_signing_key_length.DkimSigningKeyLength"
    ]
    """<p>[Easy DKIM] The key length of the DKIM key pair in use.</p>"""
    last_key_generation_timestamp: NotRequired["capo_sesv2.types.timestamp.Timestamp"]
    """<p>[Easy DKIM] The last time a key pair was generated for this identity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DkimAttributes) -> dict:
    out: dict = {}
    out["SigningEnabled"] = value.get("signing_enabled", False)
    if "status" in value:
        import capo_sesv2.types.dkim_status

        out["Status"] = capo_sesv2.types.dkim_status.serialize_json(value["status"])
    if "tokens" in value:
        import capo_sesv2.types.dns_token_list

        out["Tokens"] = capo_sesv2.types.dns_token_list.serialize_json(value["tokens"])
    if "signing_hosted_zone" in value:
        out["SigningHostedZone"] = value["signing_hosted_zone"]
    if "signing_attributes_origin" in value:
        import capo_sesv2.types.dkim_signing_attributes_origin

        out["SigningAttributesOrigin"] = (
            capo_sesv2.types.dkim_signing_attributes_origin.serialize_json(
                value["signing_attributes_origin"]
            )
        )
    if "next_signing_key_length" in value:
        import capo_sesv2.types.dkim_signing_key_length

        out["NextSigningKeyLength"] = (
            capo_sesv2.types.dkim_signing_key_length.serialize_json(
                value["next_signing_key_length"]
            )
        )
    if "current_signing_key_length" in value:
        import capo_sesv2.types.dkim_signing_key_length

        out["CurrentSigningKeyLength"] = (
            capo_sesv2.types.dkim_signing_key_length.serialize_json(
                value["current_signing_key_length"]
            )
        )
    if "last_key_generation_timestamp" in value:
        import capo_sesv2.types.timestamp

        out["LastKeyGenerationTimestamp"] = capo_sesv2.types.timestamp.serialize_json(
            value["last_key_generation_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> DkimAttributes:
    out: DkimAttributes = {}  # type: ignore[typeddict-item]
    if data.get("SigningEnabled") is not None:
        out["signing_enabled"] = data["SigningEnabled"]
    else:
        out["signing_enabled"] = False
    if data.get("Status") is not None:
        import capo_sesv2.types.dkim_status

        out["status"] = capo_sesv2.types.dkim_status.deserialize_json(data["Status"])
    if data.get("Tokens") is not None:
        import capo_sesv2.types.dns_token_list

        out["tokens"] = capo_sesv2.types.dns_token_list.deserialize_json(data["Tokens"])
    if data.get("SigningHostedZone") is not None:
        out["signing_hosted_zone"] = data["SigningHostedZone"]
    if data.get("SigningAttributesOrigin") is not None:
        import capo_sesv2.types.dkim_signing_attributes_origin

        out["signing_attributes_origin"] = (
            capo_sesv2.types.dkim_signing_attributes_origin.deserialize_json(
                data["SigningAttributesOrigin"]
            )
        )
    if data.get("NextSigningKeyLength") is not None:
        import capo_sesv2.types.dkim_signing_key_length

        out["next_signing_key_length"] = (
            capo_sesv2.types.dkim_signing_key_length.deserialize_json(
                data["NextSigningKeyLength"]
            )
        )
    if data.get("CurrentSigningKeyLength") is not None:
        import capo_sesv2.types.dkim_signing_key_length

        out["current_signing_key_length"] = (
            capo_sesv2.types.dkim_signing_key_length.deserialize_json(
                data["CurrentSigningKeyLength"]
            )
        )
    if data.get("LastKeyGenerationTimestamp") is not None:
        import capo_sesv2.types.timestamp

        out["last_key_generation_timestamp"] = (
            capo_sesv2.types.timestamp.deserialize_json(
                data["LastKeyGenerationTimestamp"]
            )
        )
    return out
