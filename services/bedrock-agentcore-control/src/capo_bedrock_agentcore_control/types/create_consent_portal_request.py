"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateConsentPortalRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.consent_portal_description_type
    import capo_bedrock_agentcore_control.types.consent_portal_idp_config
    import capo_bedrock_agentcore_control.types.consent_portal_name_type
    import capo_bedrock_agentcore_control.types.consent_portal_sources
    import capo_bedrock_agentcore_control.types.execution_role_arn_type
    import capo_bedrock_agentcore_control.types.tags_map


class CreateConsentPortalRequest(TypedDict, closed=True):
    execution_role_arn: "capo_bedrock_agentcore_control.types.execution_role_arn_type.ExecutionRoleArnType"
    """<p>The Amazon Resource Name (ARN) of the IAM role that the consent portal assumes to access the resources defined in its sources.</p>"""
    idp_config: "capo_bedrock_agentcore_control.types.consent_portal_idp_config.ConsentPortalIdpConfig"
    """<p>The identity provider configuration that the consent portal uses to authenticate end users.</p>"""
    name: "capo_bedrock_agentcore_control.types.consent_portal_name_type.ConsentPortalNameType"
    """<p>The name of the consent portal. The name must be unique within your account.</p>"""
    sources: "capo_bedrock_agentcore_control.types.consent_portal_sources.ConsentPortalSources"
    """<p>The resources served by the consent portal. Currently, we only support type <code>agentcore-gateway</code>.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.consent_portal_description_type.ConsentPortalDescriptionType"
    ]
    """<p>The description of the consent portal.</p>"""
    tags: NotRequired["capo_bedrock_agentcore_control.types.tags_map.TagsMap"]
    """<p>A map of tag keys and values to assign to the consent portal. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConsentPortalRequest) -> dict:
    out: dict = {}
    out["executionRoleArn"] = value["execution_role_arn"]
    import capo_bedrock_agentcore_control.types.consent_portal_idp_config

    out["idpConfig"] = (
        capo_bedrock_agentcore_control.types.consent_portal_idp_config.serialize_json(
            value["idp_config"]
        )
    )
    out["name"] = value["name"]
    import capo_bedrock_agentcore_control.types.consent_portal_sources

    out["sources"] = (
        capo_bedrock_agentcore_control.types.consent_portal_sources.serialize_json(
            value["sources"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_bedrock_agentcore_control.types.tags_map

        out["tags"] = capo_bedrock_agentcore_control.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateConsentPortalRequest:
    out: CreateConsentPortalRequest = {}  # type: ignore[typeddict-item]
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        out["execution_role_arn"] = ""
    if data.get("idpConfig") is not None:
        import capo_bedrock_agentcore_control.types.consent_portal_idp_config

        out["idp_config"] = (
            capo_bedrock_agentcore_control.types.consent_portal_idp_config.deserialize_json(
                data["idpConfig"]
            )
        )
    else:
        raise DeserializationError("CreateConsentPortalRequest.idp_config required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("sources") is not None:
        import capo_bedrock_agentcore_control.types.consent_portal_sources

        out["sources"] = (
            capo_bedrock_agentcore_control.types.consent_portal_sources.deserialize_json(
                data["sources"]
            )
        )
    else:
        out["sources"] = []
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_bedrock_agentcore_control.types.tags_map

        out["tags"] = capo_bedrock_agentcore_control.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out
