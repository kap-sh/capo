"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#CreateScopeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.date_timestamp
    import capo_network_security_manager.types.description
    import capo_network_security_manager.types.entity_status
    import capo_network_security_manager.types.entity_version
    import capo_network_security_manager.types.has_published_version
    import capo_network_security_manager.types.is_snapshot
    import capo_network_security_manager.types.scope_arn
    import capo_network_security_manager.types.scope_configuration
    import capo_network_security_manager.types.scope_id
    import capo_network_security_manager.types.scope_name
    import capo_network_security_manager.types.update_token


class CreateScopeOutput(TypedDict, closed=True):
    scope_id: "capo_network_security_manager.types.scope_id.ScopeId"
    """<p>The service-generated id of the scope.</p>"""
    scope_arn: "capo_network_security_manager.types.scope_arn.ScopeArn"
    """<p>The Amazon Resource Name (ARN) of the scope.</p>"""
    scope_name: "capo_network_security_manager.types.scope_name.ScopeName"
    """<p>The name of the scope.</p>"""
    scope_description: NotRequired[
        "capo_network_security_manager.types.description.Description"
    ]
    """<p>A description of the scope.</p>"""
    scope_configuration: NotRequired[
        "capo_network_security_manager.types.scope_configuration.ScopeConfiguration"
    ]
    """<p>The configuration that defines which accounts and resources are in scope.</p>"""
    status: "capo_network_security_manager.types.entity_status.EntityStatus"
    """<p>The current status of the resource: <code>DRAFT</code> (unpublished, editable) or <code>ACTIVE</code> (published, in use).</p>"""
    version: "capo_network_security_manager.types.entity_version.EntityVersion"
    """<p>The version of the resource.</p>"""
    update_token: NotRequired[
        "capo_network_security_manager.types.update_token.UpdateToken"
    ]
    """<p>A token used for optimistic concurrency control. Each read and write returns an <code>updateToken</code>. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.</p>"""
    is_snapshot: NotRequired[
        "capo_network_security_manager.types.is_snapshot.IsSnapshot"
    ]
    """<p>Specifies whether the resource is a snapshot of a published version.</p>"""
    has_published_version: NotRequired[
        "capo_network_security_manager.types.has_published_version.HasPublishedVersion"
    ]
    """<p>Specifies whether a published version of the resource exists.</p>"""
    updated_at: NotRequired[
        "capo_network_security_manager.types.date_timestamp.DateTimestamp"
    ]
    """<p>The time when the resource was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateScopeOutput) -> dict:
    out: dict = {}
    out["scopeId"] = value["scope_id"]
    out["scopeArn"] = value["scope_arn"]
    out["scopeName"] = value["scope_name"]
    if "scope_description" in value:
        out["scopeDescription"] = value["scope_description"]
    if "scope_configuration" in value:
        import capo_network_security_manager.types.scope_configuration

        out["scopeConfiguration"] = (
            capo_network_security_manager.types.scope_configuration.serialize_json(
                value["scope_configuration"]
            )
        )
    import capo_network_security_manager.types.entity_status

    out["status"] = capo_network_security_manager.types.entity_status.serialize_json(
        value["status"]
    )
    out["version"] = value["version"]
    if "update_token" in value:
        out["updateToken"] = value["update_token"]
    if "is_snapshot" in value:
        out["isSnapshot"] = value["is_snapshot"]
    if "has_published_version" in value:
        out["hasPublishedVersion"] = value["has_published_version"]
    if "updated_at" in value:
        import capo_network_security_manager.types.date_timestamp

        out["updatedAt"] = (
            capo_network_security_manager.types.date_timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateScopeOutput:
    out: CreateScopeOutput = {}  # type: ignore[typeddict-item]
    if data.get("scopeId") is not None:
        out["scope_id"] = data["scopeId"]
    else:
        raise DeserializationError("CreateScopeOutput.scope_id required")
    if data.get("scopeArn") is not None:
        out["scope_arn"] = data["scopeArn"]
    else:
        raise DeserializationError("CreateScopeOutput.scope_arn required")
    if data.get("scopeName") is not None:
        out["scope_name"] = data["scopeName"]
    else:
        raise DeserializationError("CreateScopeOutput.scope_name required")
    if data.get("scopeDescription") is not None:
        out["scope_description"] = data["scopeDescription"]
    if data.get("scopeConfiguration") is not None:
        import capo_network_security_manager.types.scope_configuration

        out["scope_configuration"] = (
            capo_network_security_manager.types.scope_configuration.deserialize_json(
                data["scopeConfiguration"]
            )
        )
    if data.get("status") is not None:
        import capo_network_security_manager.types.entity_status

        out["status"] = (
            capo_network_security_manager.types.entity_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CreateScopeOutput.status required")
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        raise DeserializationError("CreateScopeOutput.version required")
    if data.get("updateToken") is not None:
        out["update_token"] = data["updateToken"]
    if data.get("isSnapshot") is not None:
        out["is_snapshot"] = data["isSnapshot"]
    if data.get("hasPublishedVersion") is not None:
        out["has_published_version"] = data["hasPublishedVersion"]
    if data.get("updatedAt") is not None:
        import capo_network_security_manager.types.date_timestamp

        out["updated_at"] = (
            capo_network_security_manager.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
