"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UICustomizationType``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.client_id_type
    import capo_cognito_identity_provider.types.css_type
    import capo_cognito_identity_provider.types.css_version_type
    import capo_cognito_identity_provider.types.date_type
    import capo_cognito_identity_provider.types.image_url_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class UICustomizationType(TypedDict, closed=True):
    user_pool_id: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    ]
    """<p>The ID of the user pool with hosted UI customizations.</p>"""
    client_id: NotRequired[
        "capo_cognito_identity_provider.types.client_id_type.ClientIdType"
    ]
    """<p>The app client ID for your UI customization. When this value isn't present, the customization applies to all user pool app clients that don't have client-level settings..</p>"""
    image_url: NotRequired[
        "capo_cognito_identity_provider.types.image_url_type.ImageUrlType"
    ]
    """<p>A URL path to the hosted logo image of your UI customization.</p>"""
    css: NotRequired["capo_cognito_identity_provider.types.css_type.CSSType"]
    """<p>The CSS values in the UI customization.</p>"""
    css_version: NotRequired[
        "capo_cognito_identity_provider.types.css_version_type.CSSVersionType"
    ]
    """<p>The CSS version number.</p>"""
    last_modified_date: NotRequired[
        "capo_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""
    creation_date: NotRequired[
        "capo_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UICustomizationType) -> dict:
    out: dict = {}
    if "user_pool_id" in value:
        out["UserPoolId"] = value["user_pool_id"]
    if "client_id" in value:
        out["ClientId"] = value["client_id"]
    if "image_url" in value:
        out["ImageUrl"] = value["image_url"]
    if "css" in value:
        out["CSS"] = value["css"]
    if "css_version" in value:
        out["CSSVersion"] = value["css_version"]
    if "last_modified_date" in value:
        import capo_cognito_identity_provider.types.date_type

        out["LastModifiedDate"] = (
            capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["last_modified_date"]
            )
        )
    if "creation_date" in value:
        import capo_cognito_identity_provider.types.date_type

        out["CreationDate"] = (
            capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["creation_date"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UICustomizationType:
    out: UICustomizationType = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    if data.get("ImageUrl") is not None:
        out["image_url"] = data["ImageUrl"]
    if data.get("CSS") is not None:
        out["css"] = data["CSS"]
    if data.get("CSSVersion") is not None:
        out["css_version"] = data["CSSVersion"]
    if data.get("LastModifiedDate") is not None:
        import capo_cognito_identity_provider.types.date_type

        out["last_modified_date"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["LastModifiedDate"]
            )
        )
    if data.get("CreationDate") is not None:
        import capo_cognito_identity_provider.types.date_type

        out["creation_date"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["CreationDate"]
            )
        )
    return out


def redact_sensitive(value: UICustomizationType) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_id" in value:
        out["client_id"] = "*** Sensitive Data Redacted ***"
    return out
