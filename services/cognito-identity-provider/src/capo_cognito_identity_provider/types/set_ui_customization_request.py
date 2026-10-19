"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SetUICustomizationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.client_id_type
    import capo_cognito_identity_provider.types.css_type
    import capo_cognito_identity_provider.types.image_file_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class SetUICustomizationRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to apply branding to the classic hosted UI.</p>"""
    client_id: NotRequired[
        "capo_cognito_identity_provider.types.client_id_type.ClientIdType"
    ]
    """<p>The ID of the app client that you want to customize. To apply a default style to all app clients not configured with client-level branding, set this parameter value to <code>ALL</code>.</p>"""
    css: NotRequired["capo_cognito_identity_provider.types.css_type.CSSType"]
    """<p>A plaintext CSS file that contains the custom fields that you want to apply to your user pool or app client. To download a template, go to the Amazon Cognito console. Navigate to your user pool <i>App clients</i> tab, select <i>Login pages</i>, edit <i>Hosted UI (classic) style</i>, and select the link to <code>CSS template.css</code>.</p>"""
    image_file: NotRequired[
        "capo_cognito_identity_provider.types.image_file_type.ImageFileType"
    ]
    """<p>The image that you want to set as your login in the classic hosted UI, as a Base64-formatted binary object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetUICustomizationRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    if "client_id" in value:
        out["ClientId"] = value["client_id"]
    if "css" in value:
        out["CSS"] = value["css"]
    if "image_file" in value:
        import capo_cognito_identity_provider.types.image_file_type

        out["ImageFile"] = (
            capo_cognito_identity_provider.types.image_file_type.serialize_aws_json_1_1(
                value["image_file"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SetUICustomizationRequest:
    out: SetUICustomizationRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    if data.get("CSS") is not None:
        out["css"] = data["CSS"]
    if data.get("ImageFile") is not None:
        import capo_cognito_identity_provider.types.image_file_type

        out["image_file"] = (
            capo_cognito_identity_provider.types.image_file_type.deserialize_aws_json_1_1(
                data["ImageFile"]
            )
        )
    return out


def redact_sensitive(value: SetUICustomizationRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_id" in value:
        out["client_id"] = "*** Sensitive Data Redacted ***"
    return out
