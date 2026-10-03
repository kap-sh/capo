"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#MergeDeveloperIdentitiesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity.types.developer_provider_name
    import capo_cognito_identity.types.developer_user_identifier
    import capo_cognito_identity.types.identity_pool_id


class MergeDeveloperIdentitiesInput(TypedDict, closed=True):
    source_user_identifier: (
        "capo_cognito_identity.types.developer_user_identifier.DeveloperUserIdentifier"
    )
    """<p>User identifier for the source user. The value should be a <code>DeveloperUserIdentifier</code>.</p>"""
    destination_user_identifier: (
        "capo_cognito_identity.types.developer_user_identifier.DeveloperUserIdentifier"
    )
    """<p>User identifier for the destination user. The value should be a <code>DeveloperUserIdentifier</code>.</p>"""
    developer_provider_name: (
        "capo_cognito_identity.types.developer_provider_name.DeveloperProviderName"
    )
    """<p>The "domain" by which Cognito will refer to your users. This is a (pseudo) domain name that you provide while creating an identity pool. This name acts as a placeholder that allows your backend and the Cognito service to communicate about the developer provider. For the <code>DeveloperProviderName</code>, you can use letters as well as period (.), underscore (_), and dash (-).</p>"""
    identity_pool_id: "capo_cognito_identity.types.identity_pool_id.IdentityPoolId"
    """<p>An identity pool ID in the format REGION:GUID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MergeDeveloperIdentitiesInput) -> dict:
    out: dict = {}
    out["SourceUserIdentifier"] = value["source_user_identifier"]
    out["DestinationUserIdentifier"] = value["destination_user_identifier"]
    out["DeveloperProviderName"] = value["developer_provider_name"]
    out["IdentityPoolId"] = value["identity_pool_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MergeDeveloperIdentitiesInput:
    out: MergeDeveloperIdentitiesInput = {}  # type: ignore[typeddict-item]
    if data.get("SourceUserIdentifier") is not None:
        out["source_user_identifier"] = data["SourceUserIdentifier"]
    else:
        raise DeserializationError(
            "MergeDeveloperIdentitiesInput.source_user_identifier required"
        )
    if data.get("DestinationUserIdentifier") is not None:
        out["destination_user_identifier"] = data["DestinationUserIdentifier"]
    else:
        raise DeserializationError(
            "MergeDeveloperIdentitiesInput.destination_user_identifier required"
        )
    if data.get("DeveloperProviderName") is not None:
        out["developer_provider_name"] = data["DeveloperProviderName"]
    else:
        raise DeserializationError(
            "MergeDeveloperIdentitiesInput.developer_provider_name required"
        )
    if data.get("IdentityPoolId") is not None:
        out["identity_pool_id"] = data["IdentityPoolId"]
    else:
        raise DeserializationError(
            "MergeDeveloperIdentitiesInput.identity_pool_id required"
        )
    return out
