"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateConsentPortalRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.consent_portal_description_type
    import capo_bedrock_agentcore_control.types.consent_portal_identifier
    import capo_bedrock_agentcore_control.types.consent_portal_idp_config
    import capo_bedrock_agentcore_control.types.execution_role_arn_type


class UpdateConsentPortalRequest(TypedDict, closed=True):
    consent_portal_identifier: "capo_bedrock_agentcore_control.types.consent_portal_identifier.ConsentPortalIdentifier"
    """<p>The identifier of the consent portal. You can specify either the consent portal ID or its Amazon Resource Name (ARN).</p>"""
    execution_role_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.execution_role_arn_type.ExecutionRoleArnType"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role that the consent portal assumes to access the resources defined in its sources.</p>"""
    idp_config: NotRequired[
        "capo_bedrock_agentcore_control.types.consent_portal_idp_config.ConsentPortalIdpConfig"
    ]
    """<p>The identity provider configuration that the consent portal uses to authenticate end users.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.consent_portal_description_type.ConsentPortalDescriptionType"
    ]
    """<p>The description of the consent portal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConsentPortalRequest) -> dict:
    out: dict = {}
    out["consentPortalIdentifier"] = value["consent_portal_identifier"]
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    if "idp_config" in value:
        import capo_bedrock_agentcore_control.types.consent_portal_idp_config

        out["idpConfig"] = (
            capo_bedrock_agentcore_control.types.consent_portal_idp_config.serialize_json(
                value["idp_config"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateConsentPortalRequest:
    out: UpdateConsentPortalRequest = {}  # type: ignore[typeddict-item]
    if data.get("consentPortalIdentifier") is not None:
        out["consent_portal_identifier"] = data["consentPortalIdentifier"]
    else:
        out["consent_portal_identifier"] = ""
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    if data.get("idpConfig") is not None:
        import capo_bedrock_agentcore_control.types.consent_portal_idp_config

        out["idp_config"] = (
            capo_bedrock_agentcore_control.types.consent_portal_idp_config.deserialize_json(
                data["idpConfig"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
