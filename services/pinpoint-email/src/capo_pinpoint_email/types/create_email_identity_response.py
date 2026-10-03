"""Generated from Smithy shape ``com.amazonaws.pinpointemail#CreateEmailIdentityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.dkim_attributes
    import capo_pinpoint_email.types.enabled
    import capo_pinpoint_email.types.identity_type


class CreateEmailIdentityResponse(TypedDict, closed=True):
    identity_type: NotRequired["capo_pinpoint_email.types.identity_type.IdentityType"]
    """<p>The email identity type.</p>"""
    verified_for_sending_status: "capo_pinpoint_email.types.enabled.Enabled"
    """<p>Specifies whether or not the identity is verified. In Amazon Pinpoint, you can only send email from verified email addresses or domains. For more information about verifying identities, see the <a href="https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-manage-verify.html">Amazon Pinpoint User Guide</a>.</p>"""
    dkim_attributes: NotRequired[
        "capo_pinpoint_email.types.dkim_attributes.DkimAttributes"
    ]
    """<p>An object that contains information about the DKIM attributes for the identity. This object includes the tokens that you use to create the CNAME records that are required to complete the DKIM verification process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEmailIdentityResponse) -> dict:
    out: dict = {}
    if "identity_type" in value:
        import capo_pinpoint_email.types.identity_type

        out["IdentityType"] = capo_pinpoint_email.types.identity_type.serialize_json(
            value["identity_type"]
        )
    out["VerifiedForSendingStatus"] = value.get("verified_for_sending_status", False)
    if "dkim_attributes" in value:
        import capo_pinpoint_email.types.dkim_attributes

        out["DkimAttributes"] = (
            capo_pinpoint_email.types.dkim_attributes.serialize_json(
                value["dkim_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateEmailIdentityResponse:
    out: CreateEmailIdentityResponse = {}  # type: ignore[typeddict-item]
    if data.get("IdentityType") is not None:
        import capo_pinpoint_email.types.identity_type

        out["identity_type"] = capo_pinpoint_email.types.identity_type.deserialize_json(
            data["IdentityType"]
        )
    if data.get("VerifiedForSendingStatus") is not None:
        out["verified_for_sending_status"] = data["VerifiedForSendingStatus"]
    else:
        out["verified_for_sending_status"] = False
    if data.get("DkimAttributes") is not None:
        import capo_pinpoint_email.types.dkim_attributes

        out["dkim_attributes"] = (
            capo_pinpoint_email.types.dkim_attributes.deserialize_json(
                data["DkimAttributes"]
            )
        )
    return out
