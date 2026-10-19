"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DeleteManagedLoginBrandingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.managed_login_branding_id_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class DeleteManagedLoginBrandingRequest(TypedDict, closed=True):
    managed_login_branding_id: "capo_cognito_identity_provider.types.managed_login_branding_id_type.ManagedLoginBrandingIdType"
    """<p>The ID of the managed login branding style that you want to delete.</p>"""
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that contains the managed login branding style that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteManagedLoginBrandingRequest) -> dict:
    out: dict = {}
    out["ManagedLoginBrandingId"] = value["managed_login_branding_id"]
    out["UserPoolId"] = value["user_pool_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteManagedLoginBrandingRequest:
    out: DeleteManagedLoginBrandingRequest = {}  # type: ignore[typeddict-item]
    if data.get("ManagedLoginBrandingId") is not None:
        out["managed_login_branding_id"] = data["ManagedLoginBrandingId"]
    else:
        out["managed_login_branding_id"] = ""
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    return out
