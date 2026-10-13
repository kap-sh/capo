"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateRegistryResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.approval_configuration
    import capo_bedrock_agentcore_control.types.authorizer_configuration
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.description
    import capo_bedrock_agentcore_control.types.registry_arn
    import capo_bedrock_agentcore_control.types.registry_authorizer_type
    import capo_bedrock_agentcore_control.types.registry_id
    import capo_bedrock_agentcore_control.types.registry_name
    import capo_bedrock_agentcore_control.types.registry_status


class UpdateRegistryResponse(TypedDict, closed=True):
    name: "capo_bedrock_agentcore_control.types.registry_name.RegistryName"
    """<p>The name of the updated registry.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The description of the updated registry.</p>"""
    registry_id: "capo_bedrock_agentcore_control.types.registry_id.RegistryId"
    """<p>The unique identifier of the updated registry.</p>"""
    registry_arn: "capo_bedrock_agentcore_control.types.registry_arn.RegistryArn"
    """<p>The Amazon Resource Name (ARN) of the updated registry.</p>"""
    authorizer_type: NotRequired[
        "capo_bedrock_agentcore_control.types.registry_authorizer_type.RegistryAuthorizerType"
    ]
    """<p>The type of authorizer used by the updated registry. This controls the authorization method for the Search and Invoke APIs used by consumers.</p> <ul> <li> <p> <code>CUSTOM_JWT</code> - Authorize with a bearer token.</p> </li> <li> <p> <code>AWS_IAM</code> - Authorize with your Amazon Web Services IAM credentials.</p> </li> </ul>"""
    authorizer_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
    ]
    """<p>The authorizer configuration for the updated registry. For details, see the <code>AuthorizerConfiguration</code> data type.</p>"""
    approval_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.approval_configuration.ApprovalConfiguration"
    ]
    """<p>The approval configuration for the updated registry. For details, see the <code>ApprovalConfiguration</code> data type.</p>"""
    status: "capo_bedrock_agentcore_control.types.registry_status.RegistryStatus"
    """<p>The current status of the updated registry. Possible values include <code>CREATING</code>, <code>READY</code>, <code>UPDATING</code>, <code>CREATE_FAILED</code>, <code>UPDATE_FAILED</code>, <code>DELETING</code>, and <code>DELETE_FAILED</code>.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the current status of the updated registry.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the registry was created.</p>"""
    updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the registry was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRegistryResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["registryId"] = value["registry_id"]
    out["registryArn"] = value["registry_arn"]
    if "authorizer_type" in value:
        import capo_bedrock_agentcore_control.types.registry_authorizer_type

        out["authorizerType"] = (
            capo_bedrock_agentcore_control.types.registry_authorizer_type.serialize_json(
                value["authorizer_type"]
            )
        )
    if "authorizer_configuration" in value:
        import capo_bedrock_agentcore_control.types.authorizer_configuration

        out["authorizerConfiguration"] = (
            capo_bedrock_agentcore_control.types.authorizer_configuration.serialize_json(
                value["authorizer_configuration"]
            )
        )
    if "approval_configuration" in value:
        import capo_bedrock_agentcore_control.types.approval_configuration

        out["approvalConfiguration"] = (
            capo_bedrock_agentcore_control.types.approval_configuration.serialize_json(
                value["approval_configuration"]
            )
        )
    import capo_bedrock_agentcore_control.types.registry_status

    out["status"] = capo_bedrock_agentcore_control.types.registry_status.serialize_json(
        value["status"]
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["updatedAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateRegistryResponse:
    out: UpdateRegistryResponse = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateRegistryResponse.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    else:
        raise DeserializationError("UpdateRegistryResponse.registry_id required")
    if data.get("registryArn") is not None:
        out["registry_arn"] = data["registryArn"]
    else:
        raise DeserializationError("UpdateRegistryResponse.registry_arn required")
    if data.get("authorizerType") is not None:
        import capo_bedrock_agentcore_control.types.registry_authorizer_type

        out["authorizer_type"] = (
            capo_bedrock_agentcore_control.types.registry_authorizer_type.deserialize_json(
                data["authorizerType"]
            )
        )
    if data.get("authorizerConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.authorizer_configuration

        out["authorizer_configuration"] = (
            capo_bedrock_agentcore_control.types.authorizer_configuration.deserialize_json(
                data["authorizerConfiguration"]
            )
        )
    if data.get("approvalConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.approval_configuration

        out["approval_configuration"] = (
            capo_bedrock_agentcore_control.types.approval_configuration.deserialize_json(
                data["approvalConfiguration"]
            )
        )
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.registry_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.registry_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("UpdateRegistryResponse.status required")
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("UpdateRegistryResponse.created_at required")
    if data.get("updatedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("UpdateRegistryResponse.updated_at required")
    return out


def redact_sensitive(value: UpdateRegistryResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
