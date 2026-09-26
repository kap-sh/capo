"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#DeploymentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.date_timestamp
    import capo_network_security_manager.types.deployment_arn
    import capo_network_security_manager.types.deployment_id
    import capo_network_security_manager.types.deployment_name
    import capo_network_security_manager.types.entity_status
    import capo_network_security_manager.types.entity_version
    import capo_network_security_manager.types.has_published_version


class DeploymentSummary(TypedDict, closed=True):
    deployment_id: "capo_network_security_manager.types.deployment_id.DeploymentId"
    """<p>The service-generated id of the deployment.</p>"""
    deployment_arn: "capo_network_security_manager.types.deployment_arn.DeploymentArn"
    """<p>The Amazon Resource Name (ARN) of the deployment.</p>"""
    deployment_name: NotRequired[
        "capo_network_security_manager.types.deployment_name.DeploymentName"
    ]
    """<p>The name of the deployment.</p>"""
    status: NotRequired[
        "capo_network_security_manager.types.entity_status.EntityStatus"
    ]
    """<p>The current status of the resource: <code>DRAFT</code> (unpublished, editable), <code>ACTIVE</code> (published, in use), or <code>DISABLED</code> (deactivated; changes cannot be published until the resource is re-enabled).</p>"""
    version: NotRequired[
        "capo_network_security_manager.types.entity_version.EntityVersion"
    ]
    """<p>The version of the resource.</p>"""
    has_published_version: NotRequired[
        "capo_network_security_manager.types.has_published_version.HasPublishedVersion"
    ]
    """<p>Specifies whether a published version of the resource exists.</p>"""
    updated_at: NotRequired[
        "capo_network_security_manager.types.date_timestamp.DateTimestamp"
    ]
    """<p>The time when the resource was last updated. For a snapshot, this is the time when the snapshot was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentSummary) -> dict:
    out: dict = {}
    out["deploymentId"] = value["deployment_id"]
    out["deploymentArn"] = value["deployment_arn"]
    if "deployment_name" in value:
        out["deploymentName"] = value["deployment_name"]
    if "status" in value:
        import capo_network_security_manager.types.entity_status

        out["status"] = (
            capo_network_security_manager.types.entity_status.serialize_json(
                value["status"]
            )
        )
    if "version" in value:
        out["version"] = value["version"]
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


def deserialize_json(data: dict) -> DeploymentSummary:
    out: DeploymentSummary = {}  # type: ignore[typeddict-item]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    else:
        raise DeserializationError("DeploymentSummary.deployment_id required")
    if data.get("deploymentArn") is not None:
        out["deployment_arn"] = data["deploymentArn"]
    else:
        raise DeserializationError("DeploymentSummary.deployment_arn required")
    if data.get("deploymentName") is not None:
        out["deployment_name"] = data["deploymentName"]
    if data.get("status") is not None:
        import capo_network_security_manager.types.entity_status

        out["status"] = (
            capo_network_security_manager.types.entity_status.deserialize_json(
                data["status"]
            )
        )
    if data.get("version") is not None:
        out["version"] = data["version"]
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
