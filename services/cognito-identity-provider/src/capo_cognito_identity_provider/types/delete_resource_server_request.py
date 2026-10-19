"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DeleteResourceServerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.resource_server_identifier_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class DeleteResourceServerRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to delete the resource server.</p>"""
    identifier: "capo_cognito_identity_provider.types.resource_server_identifier_type.ResourceServerIdentifierType"
    """<p>The identifier of the resource server that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteResourceServerRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteResourceServerRequest:
    out: DeleteResourceServerRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    return out
