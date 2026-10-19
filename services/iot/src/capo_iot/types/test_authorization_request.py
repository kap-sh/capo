"""Generated from Smithy shape ``com.amazonaws.iot#TestAuthorizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.auth_infos
    import capo_iot.types.client_id
    import capo_iot.types.cognito_identity_pool_id
    import capo_iot.types.policy_names
    import capo_iot.types.principal


class TestAuthorizationRequest(TypedDict, closed=True):
    principal: NotRequired["capo_iot.types.principal.Principal"]
    """<p>The principal. Valid principals are CertificateArn (arn:aws:iot:<i>region</i>:<i>accountId</i>:cert/<i>certificateId</i>) and CognitoId (<i>region</i>:<i>id</i>).</p>"""
    cognito_identity_pool_id: NotRequired[
        "capo_iot.types.cognito_identity_pool_id.CognitoIdentityPoolId"
    ]
    """<p>The Cognito identity pool ID.</p>"""
    auth_infos: "capo_iot.types.auth_infos.AuthInfos"
    """<p>A list of authorization info objects. Simulating authorization will create a response for each <code>authInfo</code> object in the list.</p>"""
    client_id: NotRequired["capo_iot.types.client_id.ClientId"]
    """<p>The MQTT client ID.</p>"""
    policy_names_to_add: NotRequired["capo_iot.types.policy_names.PolicyNames"]
    """<p>When testing custom authorization, the policies specified here are treated as if they are attached to the principal being authorized.</p>"""
    policy_names_to_skip: NotRequired["capo_iot.types.policy_names.PolicyNames"]
    """<p>When testing custom authorization, the policies specified here are treated as if they are not attached to the principal being authorized.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestAuthorizationRequest) -> dict:
    out: dict = {}
    if "principal" in value:
        out["principal"] = value["principal"]
    if "cognito_identity_pool_id" in value:
        out["cognitoIdentityPoolId"] = value["cognito_identity_pool_id"]
    import capo_iot.types.auth_infos

    out["authInfos"] = capo_iot.types.auth_infos.serialize_json(value["auth_infos"])
    if "policy_names_to_add" in value:
        import capo_iot.types.policy_names

        out["policyNamesToAdd"] = capo_iot.types.policy_names.serialize_json(
            value["policy_names_to_add"]
        )
    if "policy_names_to_skip" in value:
        import capo_iot.types.policy_names

        out["policyNamesToSkip"] = capo_iot.types.policy_names.serialize_json(
            value["policy_names_to_skip"]
        )
    return out


def deserialize_json(data: dict) -> TestAuthorizationRequest:
    out: TestAuthorizationRequest = {}  # type: ignore[typeddict-item]
    if data.get("principal") is not None:
        out["principal"] = data["principal"]
    if data.get("cognitoIdentityPoolId") is not None:
        out["cognito_identity_pool_id"] = data["cognitoIdentityPoolId"]
    if data.get("authInfos") is not None:
        import capo_iot.types.auth_infos

        out["auth_infos"] = capo_iot.types.auth_infos.deserialize_json(
            data["authInfos"]
        )
    else:
        out["auth_infos"] = []
    if data.get("policyNamesToAdd") is not None:
        import capo_iot.types.policy_names

        out["policy_names_to_add"] = capo_iot.types.policy_names.deserialize_json(
            data["policyNamesToAdd"]
        )
    if data.get("policyNamesToSkip") is not None:
        import capo_iot.types.policy_names

        out["policy_names_to_skip"] = capo_iot.types.policy_names.deserialize_json(
            data["policyNamesToSkip"]
        )
    return out
