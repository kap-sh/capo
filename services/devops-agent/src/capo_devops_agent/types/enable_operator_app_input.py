"""Generated from Smithy shape ``com.amazonaws.devopsagent#EnableOperatorAppInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_id
    import capo_devops_agent.types.auth_flow
    import capo_devops_agent.types.idp_client_id
    import capo_devops_agent.types.idp_client_secret
    import capo_devops_agent.types.role_arn


class EnableOperatorAppInput(TypedDict, closed=True):
    agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the AgentSpace</p>"""
    auth_flow: "capo_devops_agent.types.auth_flow.AuthFlow"
    """<p>The authentication flow configured for the operator App. e.g. iam or idc</p>"""
    operator_app_role_arn: "capo_devops_agent.types.role_arn.RoleArn"
    """<p>The IAM role end users assume to access AIDevOps APIs</p>"""
    idc_instance_arn: NotRequired["str"]
    """<p>The IdC instance Arn used to create an IdC auth application</p>"""
    issuer_url: NotRequired["str"]
    """<p>The OIDC issuer URL of the external Identity Provider</p>"""
    idp_client_id: NotRequired["capo_devops_agent.types.idp_client_id.IdpClientId"]
    """<p>The OIDC client ID for the IdP application</p>"""
    idp_client_secret: NotRequired[
        "capo_devops_agent.types.idp_client_secret.IdpClientSecret"
    ]
    """<p>The OIDC client secret for the IdP application</p>"""
    provider: NotRequired["str"]
    """<p>The Identity Provider name (e.g., Entra, Okta, Google)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableOperatorAppInput) -> dict:
    out: dict = {}
    import capo_devops_agent.types.auth_flow

    out["authFlow"] = capo_devops_agent.types.auth_flow.serialize_json(
        value["auth_flow"]
    )
    out["operatorAppRoleArn"] = value["operator_app_role_arn"]
    if "idc_instance_arn" in value:
        out["idcInstanceArn"] = value["idc_instance_arn"]
    if "issuer_url" in value:
        out["issuerUrl"] = value["issuer_url"]
    if "idp_client_id" in value:
        out["idpClientId"] = value["idp_client_id"]
    if "idp_client_secret" in value:
        out["idpClientSecret"] = value["idp_client_secret"]
    if "provider" in value:
        out["provider"] = value["provider"]
    return out


def deserialize_json(data: dict) -> EnableOperatorAppInput:
    out: EnableOperatorAppInput = {}  # type: ignore[typeddict-item]
    if data.get("authFlow") is not None:
        import capo_devops_agent.types.auth_flow

        out["auth_flow"] = capo_devops_agent.types.auth_flow.deserialize_json(
            data["authFlow"]
        )
    else:
        raise DeserializationError("EnableOperatorAppInput.auth_flow required")
    if data.get("operatorAppRoleArn") is not None:
        out["operator_app_role_arn"] = data["operatorAppRoleArn"]
    else:
        raise DeserializationError(
            "EnableOperatorAppInput.operator_app_role_arn required"
        )
    if data.get("idcInstanceArn") is not None:
        out["idc_instance_arn"] = data["idcInstanceArn"]
    if data.get("issuerUrl") is not None:
        out["issuer_url"] = data["issuerUrl"]
    if data.get("idpClientId") is not None:
        out["idp_client_id"] = data["idpClientId"]
    if data.get("idpClientSecret") is not None:
        out["idp_client_secret"] = data["idpClientSecret"]
    if data.get("provider") is not None:
        out["provider"] = data["provider"]
    return out


def redact_sensitive(value: EnableOperatorAppInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "idp_client_secret" in value:
        out["idp_client_secret"] = "*** Sensitive Data Redacted ***"
    return out
