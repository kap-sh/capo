"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#UnlinkDeveloperIdentityInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity.types.developer_provider_name
    import capo_cognito_identity.types.developer_user_identifier
    import capo_cognito_identity.types.identity_id
    import capo_cognito_identity.types.identity_pool_id


class UnlinkDeveloperIdentityInput(TypedDict, closed=True):
    identity_id: "capo_cognito_identity.types.identity_id.IdentityId"
    """<p>A unique identifier in the format REGION:GUID.</p>"""
    identity_pool_id: "capo_cognito_identity.types.identity_pool_id.IdentityPoolId"
    """<p>An identity pool ID in the format REGION:GUID.</p>"""
    developer_provider_name: (
        "capo_cognito_identity.types.developer_provider_name.DeveloperProviderName"
    )
    """<p>The "domain" by which Cognito will refer to your users.</p>"""
    developer_user_identifier: (
        "capo_cognito_identity.types.developer_user_identifier.DeveloperUserIdentifier"
    )
    """<p>A unique ID used by your backend authentication process to identify a user.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnlinkDeveloperIdentityInput) -> dict:
    out: dict = {}
    out["IdentityId"] = value["identity_id"]
    out["IdentityPoolId"] = value["identity_pool_id"]
    out["DeveloperProviderName"] = value["developer_provider_name"]
    out["DeveloperUserIdentifier"] = value["developer_user_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnlinkDeveloperIdentityInput:
    out: UnlinkDeveloperIdentityInput = {}  # type: ignore[typeddict-item]
    if data.get("IdentityId") is not None:
        out["identity_id"] = data["IdentityId"]
    else:
        raise DeserializationError("UnlinkDeveloperIdentityInput.identity_id required")
    if data.get("IdentityPoolId") is not None:
        out["identity_pool_id"] = data["IdentityPoolId"]
    else:
        raise DeserializationError(
            "UnlinkDeveloperIdentityInput.identity_pool_id required"
        )
    if data.get("DeveloperProviderName") is not None:
        out["developer_provider_name"] = data["DeveloperProviderName"]
    else:
        raise DeserializationError(
            "UnlinkDeveloperIdentityInput.developer_provider_name required"
        )
    if data.get("DeveloperUserIdentifier") is not None:
        out["developer_user_identifier"] = data["DeveloperUserIdentifier"]
    else:
        raise DeserializationError(
            "UnlinkDeveloperIdentityInput.developer_user_identifier required"
        )
    return out
