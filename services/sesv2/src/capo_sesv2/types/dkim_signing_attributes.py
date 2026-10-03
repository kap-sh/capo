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
    """<p>The attribute to use for configuring DKIM for the identity depends on the operation: </p> <ol> <li> <p>For <code>PutEmailIdentityDkimSigningAttributes</code>: </p> <ul> <li> <p>None of the values are allowed - use the <a href="https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutEmailIdentityDkimSigningAttributes.html#SES-PutEmailIdentityDkimSigningAttributes-request-SigningAttributesOrigin"> <code>SigningAttributesOrigin</code> </a> parameter instead </p> </li> </ul> </li> <li> <p>For <code>CreateEmailIdentity</code> when replicating a parent identity's DKIM configuration: </p> <ul> <li> <p>Allowed values: All values except <code>AWS_SES</code> and <code>EXTERNAL</code> </p> </li> </ul> </li> </ol> <ul> <li> <p> <code>AWS_SES</code> – Configure DKIM for the identity by using Easy DKIM. </p> </li> <li> <p> <code>EXTERNAL</code> – Configure DKIM for the identity by using Bring Your Own DKIM (BYODKIM). </p> </li> <li> <p> <code>AWS_SES_AF_SOUTH_1</code> – Configure DKIM for the identity by replicating from a parent identity in Africa (Cape Town) region using Deterministic Easy-DKIM (DEED). </p> </li> <li> <p> <code>AWS_SES_EU_NORTH_1</code> – Configure DKIM for the identity by replicating from a parent identity in Europe (Stockholm) region using Deterministic Easy-DKIM (DEED). </p> </li> <li> <p> <code>AWS_SES_AP_SOUTH_1</code> – Configure DKIM for the identity by replicating from a parent identity in Asia Pacific (Mumbai) region using Deterministic Easy-DKIM (DEED). </p> </li> <li> <p> <code>AWS_SES_AP_SOUTH_2</code> – Configure DKIM for the identity by replicating from a parent identity in Asia Pacific (Hyderabad) region using Deterministic Easy-DKIM (DEED). </p> </li> <li> <p> <code>AWS_SES_EU_WEST_3</code> – Configure DKIM for the identity by replicating from a parent identity in Europe (Paris) region using Deterministic Easy-DKIM (DEED). </p> </li> <li> <p> <code>AWS_SES_EU_WEST_2</code> – Configure DKIM for the identity by replicating from a parent identity in Europe (London) region using Deterministic Easy-DKIM (DEED). </p> </li> <li> <p> <code>AWS_SES_EU_SOUTH_1</code> – Configure DKIM for the identity by replicating from a parent identity in Europe (Milan) region using Deterministic Easy-DKIM (DEED). </p> </li> <li> <p> <code>AWS_SES_EU_WEST_1</code> – Configure DKIM for the identity by replicating from a parent identity in Europe (Ireland) region using Deterministic Easy-DKIM (DEED). </p> </li> <li> <p> <code>AWS_SES_AP_NORTHEAST_3</code> – Configure DKIM for the identity by replicating from a parent identity in Asia Pacific (Osaka) region using Deterministic Easy-DKIM (DEED). </p> </li> <li> <p> <code>AWS_SES_AP_NORTHEAST_2</code> – Configure DKIM for the identity by replicating from a parent identity in Asia Pacific (Seoul) region using Deterministic Easy-DKIM (DEED). </p> </li> <li> <p> <code>AWS_SES_ME_CENTRAL_1</code> – Configure DKIM for the identity by replicating from a parent identity in Middle East (UAE) region using Deterministic Easy-DKIM (DEED). </p> </li> <li> <p> <code>AWS_SES_ME_SOUTH_1</code> – Configure DKIM for the identity by replicating from a parent identity in Middle East (Bahrain) region using Deterministic Easy-DKIM (DEED). </p> </li> <li> <p> <code>AWS_SES_AP_NORTHEAST_1</code> – Configure DKIM for the identity by replicating from a parent identity in Asia Pacific (Tokyo) region using Deterministic Easy-DKIM (DEED). </p> </li> <li> <p> <code>AWS_SES_IL_CENTRAL_1</code> – Configure DKIM for the identity by replicating from a parent identity in Israel (Tel Aviv) region using Deterministic Easy-DKIM (DEED). </p> </li> <li> <p> <code>AWS_SES_SA_EAST_1</code> – Configure DKIM for the identity by replicating from a parent identity in South America (São Paulo) region using Deterministic Easy-DKIM (DEED). </p> </li> <li> <p> <code>AWS_SES_CA_CENTRAL_1</code> – Configure DKIM for the identity by replicating from a parent identity in Canada (Central) region using Deterministic Easy-DKIM (DEED). </p> </li> <li> <p> <code>AWS_SES_CA_WEST_1</code> – Configure DKIM for the identity by replicating from a parent identity in Canada (Calgary) region using Deterministic Easy-DKIM (DEED). </p> </li> <li> <p> <code>AWS_SES_AP_SOUTHEAST_1</code> – Configure DKIM for the identity by replicating from a parent identity in Asia Pacific (Singapore) region using Deterministic Easy-DKIM (DEED). </p> </li> <li> <p> <code>AWS_SES_AP_SOUTHEAST_2</code> – Configure DKIM for the identity by replicating from a parent identity in Asia Pacific (Sydney) region using Deterministic Easy-DKIM (DEED). </p> </li> <li> <p> <code>AWS_SES_AP_SOUTHEAST_3</code> – Configure DKIM for the identity by replicating from a parent identity in Asia Pacific (Jakarta) region using Deterministic Easy-DKIM (DEED). </p> </li> <li> <p> <code>AWS_SES_AP_SOUTHEAST_5</code> – Configure DKIM for the identity by replicating from a parent identity in Asia Pacific (Malaysia) region using Deterministic Easy-DKIM (DEED). </p> </li> <li> <p> <code>AWS_SES_EU_CENTRAL_1</code> – Configure DKIM for the identity by replicating from a parent identity in Europe (Frankfurt) region using Deterministic Easy-DKIM (DEED). </p> </li> <li> <p> <code>AWS_SES_EU_CENTRAL_2</code> – Configure DKIM for the identity by replicating from a parent identity in Europe (Zurich) region using Deterministic Easy-DKIM (DEED). </p> </li> <li> <p> <code>AWS_SES_US_EAST_1</code> – Configure DKIM for the identity by replicating from a parent identity in US East (N. Virginia) region using Deterministic Easy-DKIM (DEED). </p> </li> <li> <p> <code>AWS_SES_US_EAST_2</code> – Configure DKIM for the identity by replicating from a parent identity in US East (Ohio) region using Deterministic Easy-DKIM (DEED). </p> </li> <li> <p> <code>AWS_SES_US_WEST_1</code> – Configure DKIM for the identity by replicating from a parent identity in US West (N. California) region using Deterministic Easy-DKIM (DEED). </p> </li> <li> <p> <code>AWS_SES_US_WEST_2</code> – Configure DKIM for the identity by replicating from a parent identity in US West (Oregon) region using Deterministic Easy-DKIM (DEED). </p> </li> <li> <p> <code>AWS_SES_US_GOV_EAST_1</code> – Configure DKIM for the identity by replicating from a parent identity in AWS GovCloud (US-East) region using Deterministic Easy-DKIM (DEED). </p> </li> <li> <p> <code>AWS_SES_US_GOV_WEST_1</code> – Configure DKIM for the identity by replicating from a parent identity in AWS GovCloud (US-West) region using Deterministic Easy-DKIM (DEED). </p> </li> </ul>"""


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
