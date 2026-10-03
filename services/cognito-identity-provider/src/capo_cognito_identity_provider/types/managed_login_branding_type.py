"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ManagedLoginBrandingType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.asset_list_type
    import capo_cognito_identity_provider.types.boolean_type
    import capo_cognito_identity_provider.types.date_type
    import capo_cognito_identity_provider.types.document
    import capo_cognito_identity_provider.types.managed_login_branding_id_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class ManagedLoginBrandingType(TypedDict, closed=True):
    managed_login_branding_id: NotRequired[
        "capo_cognito_identity_provider.types.managed_login_branding_id_type.ManagedLoginBrandingIdType"
    ]
    """<p>The ID of the managed login branding style.</p>"""
    user_pool_id: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    ]
    """<p>The user pool where the branding style is assigned.</p>"""
    use_cognito_provided_values: (
        "capo_cognito_identity_provider.types.boolean_type.BooleanType"
    )
    """<p>When true, applies the default branding style options. This option reverts to default style options that are managed by Amazon Cognito. You can modify them later in the branding editor.</p> <p>When you specify <code>true</code> for this option, you must also omit values for <code>Settings</code> and <code>Assets</code> in the request.</p>"""
    settings: NotRequired["capo_cognito_identity_provider.types.document.Document"]
    """<p>A JSON file, encoded as a <code>Document</code> type, with the the settings that you want to apply to your style.</p> <p>The following components are not currently implemented and reserved for future use:</p> <ul> <li> <p> <code>signUp</code> </p> </li> <li> <p> <code>instructions</code> </p> </li> <li> <p> <code>sessionTimerDisplay</code> </p> </li> <li> <p> <code>languageSelector</code> (for localization, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html#managed-login-localization">Managed login localization)</a> </p> </li> </ul>"""
    assets: NotRequired[
        "capo_cognito_identity_provider.types.asset_list_type.AssetListType"
    ]
    """<p>An array of image files that you want to apply to roles like backgrounds, logos, and icons. Each object must also indicate whether it is for dark mode, light mode, or browser-adaptive mode.</p>"""
    creation_date: NotRequired[
        "capo_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""
    last_modified_date: NotRequired[
        "capo_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedLoginBrandingType) -> dict:
    out: dict = {}
    if "managed_login_branding_id" in value:
        out["ManagedLoginBrandingId"] = value["managed_login_branding_id"]
    if "user_pool_id" in value:
        out["UserPoolId"] = value["user_pool_id"]
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
    if "creation_date" in value:
        import capo_cognito_identity_provider.types.date_type

        out["CreationDate"] = (
            capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["creation_date"]
            )
        )
    if "last_modified_date" in value:
        import capo_cognito_identity_provider.types.date_type

        out["LastModifiedDate"] = (
            capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["last_modified_date"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedLoginBrandingType:
    out: ManagedLoginBrandingType = {}  # type: ignore[typeddict-item]
    if data.get("ManagedLoginBrandingId") is not None:
        out["managed_login_branding_id"] = data["ManagedLoginBrandingId"]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
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
    if data.get("CreationDate") is not None:
        import capo_cognito_identity_provider.types.date_type

        out["creation_date"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["CreationDate"]
            )
        )
    if data.get("LastModifiedDate") is not None:
        import capo_cognito_identity_provider.types.date_type

        out["last_modified_date"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["LastModifiedDate"]
            )
        )
    return out
