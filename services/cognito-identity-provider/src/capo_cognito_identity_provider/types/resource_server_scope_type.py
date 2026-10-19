"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ResourceServerScopeType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.resource_server_scope_description_type
    import capo_cognito_identity_provider.types.resource_server_scope_name_type


class ResourceServerScopeType(TypedDict, closed=True):
    scope_name: "capo_cognito_identity_provider.types.resource_server_scope_name_type.ResourceServerScopeNameType"
    """<p>The name of the scope. Amazon Cognito renders custom scopes in the format <code>resourceServerIdentifier/ScopeName</code>. For example, if this parameter is <code>exampleScope</code> in the resource server with the identifier <code>exampleResourceServer</code>, you request and receive the scope <code>exampleResourceServer/exampleScope</code>.</p>"""
    scope_description: "capo_cognito_identity_provider.types.resource_server_scope_description_type.ResourceServerScopeDescriptionType"
    """<p>A friendly description of a custom scope.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceServerScopeType) -> dict:
    out: dict = {}
    out["ScopeName"] = value["scope_name"]
    out["ScopeDescription"] = value["scope_description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceServerScopeType:
    out: ResourceServerScopeType = {}  # type: ignore[typeddict-item]
    if data.get("ScopeName") is not None:
        out["scope_name"] = data["ScopeName"]
    else:
        out["scope_name"] = ""
    if data.get("ScopeDescription") is not None:
        out["scope_description"] = data["ScopeDescription"]
    else:
        out["scope_description"] = ""
    return out
