"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DescribeManagedLoginBrandingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.boolean_type
    import capo_cognito_identity_provider.types.managed_login_branding_id_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class DescribeManagedLoginBrandingRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that contains the managed login branding style that you want to get information about.</p>"""
    managed_login_branding_id: "capo_cognito_identity_provider.types.managed_login_branding_id_type.ManagedLoginBrandingIdType"
    """<p>The ID of the managed login branding style that you want to get more information about.</p>"""
    return_merged_resources: NotRequired[
        "capo_cognito_identity_provider.types.boolean_type.BooleanType"
    ]
    """<p>When <code>true</code>, returns values for branding options that are unchanged from Amazon Cognito defaults. When <code>false</code> or when you omit this parameter, returns only values that you customized in your branding style.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeManagedLoginBrandingRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["ManagedLoginBrandingId"] = value["managed_login_branding_id"]
    if "return_merged_resources" in value:
        out["ReturnMergedResources"] = value["return_merged_resources"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeManagedLoginBrandingRequest:
    out: DescribeManagedLoginBrandingRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError(
            "DescribeManagedLoginBrandingRequest.user_pool_id required"
        )
    if data.get("ManagedLoginBrandingId") is not None:
        out["managed_login_branding_id"] = data["ManagedLoginBrandingId"]
    else:
        raise DeserializationError(
            "DescribeManagedLoginBrandingRequest.managed_login_branding_id required"
        )
    if data.get("ReturnMergedResources") is not None:
        out["return_merged_resources"] = data["ReturnMergedResources"]
    return out
