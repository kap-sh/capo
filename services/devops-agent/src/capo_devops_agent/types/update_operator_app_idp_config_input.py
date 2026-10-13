"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdateOperatorAppIdpConfigInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_id
    import capo_devops_agent.types.idp_client_secret


class UpdateOperatorAppIdpConfigInput(TypedDict, closed=True):
    agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the AgentSpace</p>"""
    idp_client_secret: NotRequired[
        "capo_devops_agent.types.idp_client_secret.IdpClientSecret"
    ]
    """<p>The OIDC client secret for the IdP application</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOperatorAppIdpConfigInput) -> dict:
    out: dict = {}
    if "idp_client_secret" in value:
        out["idpClientSecret"] = value["idp_client_secret"]
    return out


def deserialize_json(data: dict) -> UpdateOperatorAppIdpConfigInput:
    out: UpdateOperatorAppIdpConfigInput = {}  # type: ignore[typeddict-item]
    if data.get("idpClientSecret") is not None:
        out["idp_client_secret"] = data["idpClientSecret"]
    return out


def redact_sensitive(value: UpdateOperatorAppIdpConfigInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "idp_client_secret" in value:
        out["idp_client_secret"] = "*** Sensitive Data Redacted ***"
    return out
