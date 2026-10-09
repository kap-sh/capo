"""Generated from Smithy shape ``com.amazonaws.sesv2#DkimSigningAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.dkim_signing_attributes_origin
    import capo_sesv2.types.dkim_signing_key_length
    import capo_sesv2.types.private_key
    import capo_sesv2.types.selector


class DkimSigningAttributes(TypedDict, closed=True):
    domain_signing_selector: NotRequired["capo_sesv2.types.selector.Selector"]
    """<p>[Bring Your Own DKIM] A string that's used to identify a public key in the DNS configuration for a domain.</p>"""
    domain_signing_private_key: NotRequired["capo_sesv2.types.private_key.PrivateKey"]
    """<p>[Bring Your Own DKIM] A private key that's used to generate a DKIM signature.</p> <p>The private key must use 1024 or 2048-bit RSA encryption, and must be encoded using base64 encoding.</p>"""
    next_signing_key_length: NotRequired[
        "capo_sesv2.types.dkim_signing_key_length.DkimSigningKeyLength"
    ]
    """<p>[Easy DKIM] The key length of the future DKIM key pair to be generated. This can be changed at most once per day.</p>"""
    domain_signing_attributes_origin: NotRequired[
        "capo_sesv2.types.dkim_signing_attributes_origin.DkimSigningAttributesOrigin"
    ]
    """<p>The attribute to use for configuring DKIM for the identity depends on the operation: </p> <ol> <li> <p>For <code>PutEmailIdentityDkimSigningAttributes</code>: </p> <ul> <li> <p>None of the values are allowed - use the <a href="https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutEmailIdentityDkimSigningAttributes.html#SES-PutEmailIdentityDkimSigningAttributes-request-SigningAttributesOrigin"> <code>SigningAttributesOrigin</code> </a> parameter instead </p> </li> </ul> </li> <li> <p>For <code>CreateEmailIdentity</code> when replicating a parent identity's DKIM configuration: </p> <ul> <li> <p>Allowed values: All values except <code>AWS_SES</code> and <code>EXTERNAL</code> </p> </li> </ul> </li> </ol> <ul> <li> <p> <code>AWS_SES</code> – Configure DKIM for the identity by using Easy DKIM. </p> </li> <li> <p> <code>EXTERNAL</code> – Configure DKIM for the identity by using Bring Your Own DKIM (BYODKIM). </p> </li> <li> <p> <code>AWS_SES_<REGION></code> – Configure DKIM for the identity by replicating the signing attributes of a parent identity in another Amazon Web Services Region, using <a href="https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-deed.html">Deterministic Easy-DKIM (DEED)</a>. Replace <code><REGION></code> with the Amazon Web Services Region of the parent identity, in uppercase with each hyphen replaced by an underscore. You can specify any Amazon Web Services Region in which Amazon SES supports DEED. For example, to replicate from a parent identity in <code>us-east-1</code>, specify <code>AWS_SES_US_EAST_1</code>.</p> <note> <p>The parent identity must already exist in the specified Amazon Web Services Region and have Easy DKIM configured.</p> </note> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: DkimSigningAttributes) -> dict:
    out: dict = {}
    if "domain_signing_selector" in value:
        out["DomainSigningSelector"] = value["domain_signing_selector"]
    if "domain_signing_private_key" in value:
        out["DomainSigningPrivateKey"] = value["domain_signing_private_key"]
    if "next_signing_key_length" in value:
        import capo_sesv2.types.dkim_signing_key_length

        out["NextSigningKeyLength"] = (
            capo_sesv2.types.dkim_signing_key_length.serialize_json(
                value["next_signing_key_length"]
            )
        )
    if "domain_signing_attributes_origin" in value:
        import capo_sesv2.types.dkim_signing_attributes_origin

        out["DomainSigningAttributesOrigin"] = (
            capo_sesv2.types.dkim_signing_attributes_origin.serialize_json(
                value["domain_signing_attributes_origin"]
            )
        )
    return out


def deserialize_json(data: dict) -> DkimSigningAttributes:
    out: DkimSigningAttributes = {}  # type: ignore[typeddict-item]
    if data.get("DomainSigningSelector") is not None:
        out["domain_signing_selector"] = data["DomainSigningSelector"]
    if data.get("DomainSigningPrivateKey") is not None:
        out["domain_signing_private_key"] = data["DomainSigningPrivateKey"]
    if data.get("NextSigningKeyLength") is not None:
        import capo_sesv2.types.dkim_signing_key_length

        out["next_signing_key_length"] = (
            capo_sesv2.types.dkim_signing_key_length.deserialize_json(
                data["NextSigningKeyLength"]
            )
        )
    if data.get("DomainSigningAttributesOrigin") is not None:
        import capo_sesv2.types.dkim_signing_attributes_origin

        out["domain_signing_attributes_origin"] = (
            capo_sesv2.types.dkim_signing_attributes_origin.deserialize_json(
                data["DomainSigningAttributesOrigin"]
            )
        )
    return out
