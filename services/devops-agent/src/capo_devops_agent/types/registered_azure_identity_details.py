"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisteredAzureIdentityDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.guid
    import capo_devops_agent.types.role_arn
    import capo_devops_agent.types.web_identity_token_audience_list


class RegisteredAzureIdentityDetails(TypedDict, closed=True):
    tenant_id: "capo_devops_agent.types.guid.Guid"
    """<p>The Azure Active Directory tenant ID for the identity.</p>"""
    client_id: "capo_devops_agent.types.guid.Guid"
    """<p>The client ID of the service principal or managed identity used for authentication.</p>"""
    web_identity_role_arn: "capo_devops_agent.types.role_arn.RoleArn"
    """<p>The role ARN to be assumed by DevOps Agent for requesting Web Identity Token.</p>"""
    web_identity_token_audiences: "capo_devops_agent.types.web_identity_token_audience_list.WebIdentityTokenAudienceList"
    """<p>The audiences for the Web Identity Token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredAzureIdentityDetails) -> dict:
    out: dict = {}
    out["tenantId"] = value["tenant_id"]
    out["clientId"] = value["client_id"]
    out["webIdentityRoleArn"] = value["web_identity_role_arn"]
    import capo_devops_agent.types.web_identity_token_audience_list

    out["webIdentityTokenAudiences"] = (
        capo_devops_agent.types.web_identity_token_audience_list.serialize_json(
            value["web_identity_token_audiences"]
        )
    )
    return out


def deserialize_json(data: dict) -> RegisteredAzureIdentityDetails:
    out: RegisteredAzureIdentityDetails = {}  # type: ignore[typeddict-item]
    if data.get("tenantId") is not None:
        out["tenant_id"] = data["tenantId"]
    else:
        out["tenant_id"] = ""
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    else:
        out["client_id"] = ""
    if data.get("webIdentityRoleArn") is not None:
        out["web_identity_role_arn"] = data["webIdentityRoleArn"]
    else:
        out["web_identity_role_arn"] = ""
    if data.get("webIdentityTokenAudiences") is not None:
        import capo_devops_agent.types.web_identity_token_audience_list

        out["web_identity_token_audiences"] = (
            capo_devops_agent.types.web_identity_token_audience_list.deserialize_json(
                data["webIdentityTokenAudiences"]
            )
        )
    else:
        out["web_identity_token_audiences"] = []
    return out
