"""Generated from Smithy shape ``com.amazonaws.sesv2#PutEmailIdentityDkimSigningAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sesv2.types.dkim_signing_attributes
    import capo_sesv2.types.dkim_signing_attributes_origin
    import capo_sesv2.types.identity


class PutEmailIdentityDkimSigningAttributesRequest(TypedDict, closed=True):
    email_identity: "capo_sesv2.types.identity.Identity"
    """<p>The email identity.</p>"""
    signing_attributes_origin: (
        "capo_sesv2.types.dkim_signing_attributes_origin.DkimSigningAttributesOrigin"
    )
    """<p>The method to use to configure DKIM for the identity. There are the following possible values:</p> <ul> <li> <p> <code>AWS_SES</code> – Configure DKIM for the identity by using <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html">Easy DKIM</a>.</p> </li> <li> <p> <code>EXTERNAL</code> – Configure DKIM for the identity by using Bring Your Own DKIM (BYODKIM).</p> </li> </ul>"""
    signing_attributes: NotRequired[
        "capo_sesv2.types.dkim_signing_attributes.DkimSigningAttributes"
    ]
    """<p>An object that contains information about the private key and selector that you want to use to configure DKIM for the identity for Bring Your Own DKIM (BYODKIM) for the identity, or, configures the key length to be used for <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html">Easy DKIM</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutEmailIdentityDkimSigningAttributesRequest) -> dict:
    out: dict = {}
    import capo_sesv2.types.dkim_signing_attributes_origin

    out["SigningAttributesOrigin"] = (
        capo_sesv2.types.dkim_signing_attributes_origin.serialize_json(
            value["signing_attributes_origin"]
        )
    )
    if "signing_attributes" in value:
        import capo_sesv2.types.dkim_signing_attributes

        out["SigningAttributes"] = (
            capo_sesv2.types.dkim_signing_attributes.serialize_json(
                value["signing_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutEmailIdentityDkimSigningAttributesRequest:
    out: PutEmailIdentityDkimSigningAttributesRequest = {}  # type: ignore[typeddict-item]
    if data.get("SigningAttributesOrigin") is not None:
        import capo_sesv2.types.dkim_signing_attributes_origin

        out["signing_attributes_origin"] = (
            capo_sesv2.types.dkim_signing_attributes_origin.deserialize_json(
                data["SigningAttributesOrigin"]
            )
        )
    else:
        raise DeserializationError(
            "PutEmailIdentityDkimSigningAttributesRequest.signing_attributes_origin required"
        )
    if data.get("SigningAttributes") is not None:
        import capo_sesv2.types.dkim_signing_attributes

        out["signing_attributes"] = (
            capo_sesv2.types.dkim_signing_attributes.deserialize_json(
                data["SigningAttributes"]
            )
        )
    return out
