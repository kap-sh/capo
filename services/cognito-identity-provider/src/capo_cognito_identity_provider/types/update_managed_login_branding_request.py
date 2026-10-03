"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UpdateManagedLoginBrandingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.asset_list_type
    import capo_cognito_identity_provider.types.boolean_type
    import capo_cognito_identity_provider.types.document
    import capo_cognito_identity_provider.types.managed_login_branding_id_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class UpdateManagedLoginBrandingRequest(TypedDict, closed=True):
    user_pool_id: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    ]
    """<p>The ID of the user pool that contains the managed login branding style that you want to update.</p>"""
    managed_login_branding_id: NotRequired[
        "capo_cognito_identity_provider.types.managed_login_branding_id_type.ManagedLoginBrandingIdType"
    ]
    """<p>The ID of the managed login branding style that you want to update.</p>"""
    use_cognito_provided_values: (
        "capo_cognito_identity_provider.types.boolean_type.BooleanType"
    )
    """<p>When <code>true</code>, applies the default branding style options. This option reverts to default style options that are managed by Amazon Cognito. You can modify them later in the branding editor.</p> <p>When you specify <code>true</code> for this option, you must also omit values for <code>Settings</code> and <code>Assets</code> in the request.</p>"""
    settings: NotRequired["capo_cognito_identity_provider.types.document.Document"]
    """<p>A JSON file, encoded as a <code>Document</code> type, with the the settings that you want to apply to your style.</p> <p>The following components are not currently implemented and reserved for future use:</p> <ul> <li> <p> <code>signUp</code> </p> </li> <li> <p> <code>instructions</code> </p> </li> <li> <p> <code>sessionTimerDisplay</code> </p> </li> <li> <p> <code>languageSelector</code> (for localization, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html#managed-login-localization">Managed login localization)</a> </p> </li> </ul>"""
    assets: NotRequired[
        "capo_cognito_identity_provider.types.asset_list_type.AssetListType"
    ]
    """<p>An array of image files that you want to apply to roles like backgrounds, logos, and icons. Each object must also indicate whether it is for dark mode, light mode, or browser-adaptive mode.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateManagedLoginBrandingRequest) -> dict:
    out: dict = {}
    if "user_pool_id" in value:
        out["UserPoolId"] = value["user_pool_id"]
    if "managed_login_branding_id" in value:
        out["ManagedLoginBrandingId"] = value["managed_login_branding_id"]
    out["UseCognitoProvidedValues"] = value.get("use_cognito_provided_values", False)
    if "settings" in value:
        out["Settings"] = value["settings"]
    if "assets" in value:
        import capo_cognito_identity_provider.types.asset_list_type

        out["Assets"] = (
            capo_cognito_identity_provider.types.asset_list_type.serialize_aws_json_1_1(
                value["assets"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateManagedLoginBrandingRequest:
    out: UpdateManagedLoginBrandingRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    if data.get("ManagedLoginBrandingId") is not None:
        out["managed_login_branding_id"] = data["ManagedLoginBrandingId"]
    if data.get("UseCognitoProvidedValues") is not None:
        out["use_cognito_provided_values"] = data["UseCognitoProvidedValues"]
    else:
        out["use_cognito_provided_values"] = False
    if data.get("Settings") is not None:
        out["settings"] = data["Settings"]
    if data.get("Assets") is not None:
        import capo_cognito_identity_provider.types.asset_list_type

        out["assets"] = (
            capo_cognito_identity_provider.types.asset_list_type.deserialize_aws_json_1_1(
                data["Assets"]
            )
        )
    return out
