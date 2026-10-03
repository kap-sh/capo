"""Generated from Smithy shape ``com.amazonaws.sesv2#CreateEmailIdentityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sesv2.types.configuration_set_name
    import capo_sesv2.types.dkim_signing_attributes
    import capo_sesv2.types.identity
    import capo_sesv2.types.tag_list


class CreateEmailIdentityRequest(TypedDict, closed=True):
    email_identity: "capo_sesv2.types.identity.Identity"
    """<p>The email address or domain to verify.</p>"""
    tags: NotRequired["capo_sesv2.types.tag_list.TagList"]
    """<p>An array of objects that define the tags (keys and values) to associate with the email identity.</p>"""
    dkim_signing_attributes: NotRequired[
        "capo_sesv2.types.dkim_signing_attributes.DkimSigningAttributes"
    ]
    """<p>If your request includes this object, Amazon SES configures the identity to use Bring Your Own DKIM (BYODKIM) for DKIM authentication purposes, or, configures the key length to be used for <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html">Easy DKIM</a>.</p> <p>You can only specify this object if the email identity is a domain, as opposed to an address.</p>"""
    configuration_set_name: NotRequired[
        "capo_sesv2.types.configuration_set_name.ConfigurationSetName"
    ]
    """<p>The configuration set to use by default when sending from this identity. Note that any configuration set defined in the email sending request takes precedence. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEmailIdentityRequest) -> dict:
    out: dict = {}
    out["EmailIdentity"] = value["email_identity"]
    if "tags" in value:
        import capo_sesv2.types.tag_list

        out["Tags"] = capo_sesv2.types.tag_list.serialize_json(value["tags"])
    if "dkim_signing_attributes" in value:
        import capo_sesv2.types.dkim_signing_attributes

        out["DkimSigningAttributes"] = (
            capo_sesv2.types.dkim_signing_attributes.serialize_json(
                value["dkim_signing_attributes"]
            )
        )
    if "configuration_set_name" in value:
        out["ConfigurationSetName"] = value["configuration_set_name"]
    return out


def deserialize_json(data: dict) -> CreateEmailIdentityRequest:
    out: CreateEmailIdentityRequest = {}  # type: ignore[typeddict-item]
    if data.get("EmailIdentity") is not None:
        out["email_identity"] = data["EmailIdentity"]
    else:
        raise DeserializationError("CreateEmailIdentityRequest.email_identity required")
    if data.get("Tags") is not None:
        import capo_sesv2.types.tag_list

        out["tags"] = capo_sesv2.types.tag_list.deserialize_json(data["Tags"])
    if data.get("DkimSigningAttributes") is not None:
        import capo_sesv2.types.dkim_signing_attributes

        out["dkim_signing_attributes"] = (
            capo_sesv2.types.dkim_signing_attributes.deserialize_json(
                data["DkimSigningAttributes"]
            )
        )
    if data.get("ConfigurationSetName") is not None:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    return out
