"""Generated from Smithy shape ``com.amazonaws.inspector2#GetCodeSecurityIntegrationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_inspector2.types.authorization_url
    import capo_inspector2.types.code_security_integration_arn
    import capo_inspector2.types.integration_name
    import capo_inspector2.types.integration_status
    import capo_inspector2.types.integration_type
    import capo_inspector2.types.tag_map


class GetCodeSecurityIntegrationResponse(TypedDict, closed=True):
    integration_arn: (
        "capo_inspector2.types.code_security_integration_arn.CodeSecurityIntegrationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the code security integration.</p>"""
    name: "capo_inspector2.types.integration_name.IntegrationName"
    """<p>The name of the code security integration.</p>"""
    type: "capo_inspector2.types.integration_type.IntegrationType"
    """<p>The type of repository provider for the integration.</p>"""
    status: "capo_inspector2.types.integration_status.IntegrationStatus"
    """<p>The current status of the code security integration.</p>"""
    status_reason: "str"
    """<p>The reason for the current status of the code security integration.</p>"""
    created_on: "datetime.datetime"
    """<p>The timestamp when the code security integration was created.</p>"""
    last_update_on: "datetime.datetime"
    """<p>The timestamp when the code security integration was last updated.</p>"""
    authorization_url: NotRequired[
        "capo_inspector2.types.authorization_url.AuthorizationUrl"
    ]
    """<p>The URL used to authorize the integration with the repository provider. This is only returned if reauthorization is required to fix a connection issue. Otherwise, it is null.</p>"""
    tags: NotRequired["capo_inspector2.types.tag_map.TagMap"]
    """<p>The tags associated with the code security integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCodeSecurityIntegrationResponse) -> dict:
    out: dict = {}
    out["integrationArn"] = value["integration_arn"]
    out["name"] = value["name"]
    import capo_inspector2.types.integration_type

    out["type"] = capo_inspector2.types.integration_type.serialize_json(value["type"])
    import capo_inspector2.types.integration_status

    out["status"] = capo_inspector2.types.integration_status.serialize_json(
        value["status"]
    )
    out["statusReason"] = value["status_reason"]
    import capo_inspector2.types._prelude.timestamp

    out["createdOn"] = capo_inspector2.types._prelude.timestamp.serialize_json(
        value["created_on"]
    )
    import capo_inspector2.types._prelude.timestamp

    out["lastUpdateOn"] = capo_inspector2.types._prelude.timestamp.serialize_json(
        value["last_update_on"]
    )
    if "authorization_url" in value:
        out["authorizationUrl"] = value["authorization_url"]
    if "tags" in value:
        import capo_inspector2.types.tag_map

        out["tags"] = capo_inspector2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetCodeSecurityIntegrationResponse:
    out: GetCodeSecurityIntegrationResponse = {}  # type: ignore[typeddict-item]
    if data.get("integrationArn") is not None:
        out["integration_arn"] = data["integrationArn"]
    else:
        raise DeserializationError(
            "GetCodeSecurityIntegrationResponse.integration_arn required"
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetCodeSecurityIntegrationResponse.name required")
    if data.get("type") is not None:
        import capo_inspector2.types.integration_type

        out["type"] = capo_inspector2.types.integration_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("GetCodeSecurityIntegrationResponse.type required")
    if data.get("status") is not None:
        import capo_inspector2.types.integration_status

        out["status"] = capo_inspector2.types.integration_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetCodeSecurityIntegrationResponse.status required")
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    else:
        raise DeserializationError(
            "GetCodeSecurityIntegrationResponse.status_reason required"
        )
    if data.get("createdOn") is not None:
        import capo_inspector2.types._prelude.timestamp

        out["created_on"] = capo_inspector2.types._prelude.timestamp.deserialize_json(
            data["createdOn"]
        )
    else:
        raise DeserializationError(
            "GetCodeSecurityIntegrationResponse.created_on required"
        )
    if data.get("lastUpdateOn") is not None:
        import capo_inspector2.types._prelude.timestamp

        out["last_update_on"] = (
            capo_inspector2.types._prelude.timestamp.deserialize_json(
                data["lastUpdateOn"]
            )
        )
    else:
        raise DeserializationError(
            "GetCodeSecurityIntegrationResponse.last_update_on required"
        )
    if data.get("authorizationUrl") is not None:
        out["authorization_url"] = data["authorizationUrl"]
    if data.get("tags") is not None:
        import capo_inspector2.types.tag_map

        out["tags"] = capo_inspector2.types.tag_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: GetCodeSecurityIntegrationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authorization_url" in value:
        out["authorization_url"] = "*** Sensitive Data Redacted ***"
    return out
