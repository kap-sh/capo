"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CreateManagedLoginBrandingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.asset_list_type
    import capo_cognito_identity_provider.types.boolean_type
    import capo_cognito_identity_provider.types.client_id_type
    import capo_cognito_identity_provider.types.document
    import capo_cognito_identity_provider.types.user_pool_id_type


class CreateManagedLoginBrandingRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to create a new branding style.</p>"""
    client_id: "capo_cognito_identity_provider.types.client_id_type.ClientIdType"
    """<p>The app client that you want to create the branding style for. Each style is linked to an app client until you delete it.</p>"""
    use_cognito_provided_values: (
        "capo_cognito_identity_provider.types.boolean_type.BooleanType"
    )
    """<p>When true, applies the default branding style options. These default options are managed by Amazon Cognito. You can modify them later in the branding editor.</p> <p>When you specify <code>true</code> for this option, you must also omit values for <code>Settings</code> and <code>Assets</code> in the request.</p>"""
    settings: NotRequired["capo_cognito_identity_provider.types.document.Document"]
    """<p>A JSON file, encoded as a <code>Document</code> type, with the the settings that you want to apply to your style.</p> <p>The following components are not currently implemented and reserved for future use:</p> <ul> <li> <p> <code>signUp</code> </p> </li> <li> <p> <code>instructions</code> </p> </li> <li> <p> <code>sessionTimerDisplay</code> </p> </li> <li> <p> <code>languageSelector</code> (for localization, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html#managed-login-localization">Managed login localization)</a> </p> </li> </ul>"""
    assets: NotRequired[
        "capo_cognito_identity_provider.types.asset_list_type.AssetListType"
    ]
    """<p>An array of image files that you want to apply to functions like backgrounds, logos, and icons. Each object must also indicate whether it is for dark mode, light mode, or browser-adaptive mode.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateManagedLoginBrandingRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["ClientId"] = value["client_id"]
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


def deserialize_aws_json_1_1(data: dict) -> CreateManagedLoginBrandingRequest:
    out: CreateManagedLoginBrandingRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError(
            "CreateManagedLoginBrandingRequest.user_pool_id required"
        )
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    else:
        raise DeserializationError(
            "CreateManagedLoginBrandingRequest.client_id required"
        )
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
