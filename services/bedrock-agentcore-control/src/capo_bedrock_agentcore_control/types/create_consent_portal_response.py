"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateConsentPortalResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore_control.types.consent_portal_arn_type
    import capo_bedrock_agentcore_control.types.consent_portal_description_type
    import capo_bedrock_agentcore_control.types.consent_portal_id_type
    import capo_bedrock_agentcore_control.types.consent_portal_idp_config
    import capo_bedrock_agentcore_control.types.consent_portal_name_type
    import capo_bedrock_agentcore_control.types.consent_portal_sources
    import capo_bedrock_agentcore_control.types.consent_portal_status
    import capo_bedrock_agentcore_control.types.execution_role_arn_type
    import capo_bedrock_agentcore_control.types.portal_url_type
    import capo_bedrock_agentcore_control.types.status_reason_type


class CreateConsentPortalResponse(TypedDict, closed=True):
    sources: "capo_bedrock_agentcore_control.types.consent_portal_sources.ConsentPortalSources"
    """<p>The resources served by the consent portal.</p>"""
    consent_portal_arn: "capo_bedrock_agentcore_control.types.consent_portal_arn_type.ConsentPortalArnType"
    """<p>The Amazon Resource Name (ARN) of the consent portal.</p>"""
    consent_portal_id: "capo_bedrock_agentcore_control.types.consent_portal_id_type.ConsentPortalIdType"
    """<p>The unique identifier of the consent portal.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp for when the consent portal was created.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.consent_portal_description_type.ConsentPortalDescriptionType"
    ]
    """<p>The description of the consent portal.</p>"""
    execution_role_arn: "capo_bedrock_agentcore_control.types.execution_role_arn_type.ExecutionRoleArnType"
    """<p>The Amazon Resource Name (ARN) of the IAM role that the consent portal assumes to access the resources defined in its sources.</p>"""
    idp_config: "capo_bedrock_agentcore_control.types.consent_portal_idp_config.ConsentPortalIdpConfig"
    """<p>The identity provider configuration that the consent portal uses to authenticate end users.</p>"""
    name: "capo_bedrock_agentcore_control.types.consent_portal_name_type.ConsentPortalNameType"
    """<p>The name of the consent portal.</p>"""
    portal_url: NotRequired[
        "capo_bedrock_agentcore_control.types.portal_url_type.PortalUrlType"
    ]
    """<p>The URL used to access the consent portal.</p>"""
    status: (
        "capo_bedrock_agentcore_control.types.consent_portal_status.ConsentPortalStatus"
    )
    """<p>The current status of the consent portal.</p>"""
    status_reason: NotRequired[
        "capo_bedrock_agentcore_control.types.status_reason_type.StatusReasonType"
    ]
    """<p>A message that provides additional information about the current status of the consent portal.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp for when the consent portal was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConsentPortalResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.consent_portal_sources

    out["sources"] = (
        capo_bedrock_agentcore_control.types.consent_portal_sources.serialize_json(
            value["sources"]
        )
    )
    out["consentPortalArn"] = value["consent_portal_arn"]
    out["consentPortalId"] = value["consent_portal_id"]
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    out["executionRoleArn"] = value["execution_role_arn"]
    import capo_bedrock_agentcore_control.types.consent_portal_idp_config

    out["idpConfig"] = (
        capo_bedrock_agentcore_control.types.consent_portal_idp_config.serialize_json(
            value["idp_config"]
        )
    )
    out["name"] = value["name"]
    if "portal_url" in value:
        out["portalUrl"] = value["portal_url"]
    import capo_bedrock_agentcore_control.types.consent_portal_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.consent_portal_status.serialize_json(
            value["status"]
        )
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["updatedAt"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateConsentPortalResponse:
    out: CreateConsentPortalResponse = {}  # type: ignore[typeddict-item]
    if data.get("sources") is not None:
        import capo_bedrock_agentcore_control.types.consent_portal_sources

        out["sources"] = (
            capo_bedrock_agentcore_control.types.consent_portal_sources.deserialize_json(
                data["sources"]
            )
        )
    else:
        out["sources"] = []
    if data.get("consentPortalArn") is not None:
        out["consent_portal_arn"] = data["consentPortalArn"]
    else:
        out["consent_portal_arn"] = ""
    if data.get("consentPortalId") is not None:
        out["consent_portal_id"] = data["consentPortalId"]
    else:
        out["consent_portal_id"] = ""
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("description") is not None:
        out["description"] = data["description"]
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
        raise DeserializationError("CreateConsentPortalResponse.idp_config required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("portalUrl") is not None:
        out["portal_url"] = data["portalUrl"]
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.consent_portal_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.consent_portal_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.consent_portal_status.ConsentPortalStatus",
            "",
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("updatedAt") is not None:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
