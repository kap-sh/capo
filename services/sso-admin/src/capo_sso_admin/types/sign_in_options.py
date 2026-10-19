"""Generated from Smithy shape ``com.amazonaws.ssoadmin#SignInOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.application_url
    import capo_sso_admin.types.sign_in_origin


class SignInOptions(TypedDict, closed=True):
    origin: "capo_sso_admin.types.sign_in_origin.SignInOrigin"
    """<p>This determines how IAM Identity Center navigates the user to the target application. It can be one of the following values:</p> <ul> <li> <p> <code>APPLICATION</code>: IAM Identity Center redirects the customer to the configured <code>ApplicationUrl</code>.</p> </li> <li> <p> <code>IDENTITY_CENTER</code>: IAM Identity Center uses SAML identity-provider initiated authentication to sign the customer directly into a SAML-based application.</p> </li> </ul>"""
    application_url: NotRequired["capo_sso_admin.types.application_url.ApplicationUrl"]
    """<p>The URL that accepts authentication requests for an application. This is a required parameter if the <code>Origin</code> parameter is <code>APPLICATION</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SignInOptions) -> dict:
    out: dict = {}
    import capo_sso_admin.types.sign_in_origin

    out["Origin"] = capo_sso_admin.types.sign_in_origin.serialize_aws_json_1_1(
        value["origin"]
    )
    if "application_url" in value:
        out["ApplicationUrl"] = value["application_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SignInOptions:
    out: SignInOptions = {}  # type: ignore[typeddict-item]
    if data.get("Origin") is not None:
        import capo_sso_admin.types.sign_in_origin

        out["origin"] = capo_sso_admin.types.sign_in_origin.deserialize_aws_json_1_1(
            data["Origin"]
        )
    else:
        import typing

        out["origin"] = typing.cast(
            "capo_sso_admin.types.sign_in_origin.SignInOrigin", ""
        )
    if data.get("ApplicationUrl") is not None:
        out["application_url"] = data["ApplicationUrl"]
    return out
