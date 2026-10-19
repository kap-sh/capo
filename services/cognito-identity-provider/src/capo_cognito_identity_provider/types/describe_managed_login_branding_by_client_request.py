"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DescribeManagedLoginBrandingByClientRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.boolean_type
    import capo_cognito_identity_provider.types.client_id_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class DescribeManagedLoginBrandingByClientRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that contains the app client where you want more information about the managed login branding style.</p>"""
    client_id: "capo_cognito_identity_provider.types.client_id_type.ClientIdType"
    """<p>The app client that's assigned to the branding style that you want more information about.</p>"""
    return_merged_resources: NotRequired[
        "capo_cognito_identity_provider.types.boolean_type.BooleanType"
    ]
    """<p>When <code>true</code>, returns values for branding options that are unchanged from Amazon Cognito defaults. When <code>false</code> or when you omit this parameter, returns only values that you customized in your branding style.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeManagedLoginBrandingByClientRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["ClientId"] = value["client_id"]
    if "return_merged_resources" in value:
        out["ReturnMergedResources"] = value["return_merged_resources"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeManagedLoginBrandingByClientRequest:
    out: DescribeManagedLoginBrandingByClientRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    else:
        out["client_id"] = ""
    if data.get("ReturnMergedResources") is not None:
        out["return_merged_resources"] = data["ReturnMergedResources"]
    return out


def redact_sensitive(
    value: DescribeManagedLoginBrandingByClientRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_id" in value:
        out["client_id"] = "*** Sensitive Data Redacted ***"
    return out
