"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#CreateDeploymentSnapshotOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.associated_policy_list
    import capo_network_security_manager.types.associated_scope_list
    import capo_network_security_manager.types.date_timestamp
    import capo_network_security_manager.types.deployment_arn
    import capo_network_security_manager.types.deployment_configuration
    import capo_network_security_manager.types.deployment_id
    import capo_network_security_manager.types.deployment_name
    import capo_network_security_manager.types.description
    import capo_network_security_manager.types.entity_status
    import capo_network_security_manager.types.entity_version
    import capo_network_security_manager.types.has_published_version
    import capo_network_security_manager.types.is_snapshot
    import capo_network_security_manager.types.update_token


class CreateDeploymentSnapshotOutput(TypedDict, closed=True):
    deployment_id: "capo_network_security_manager.types.deployment_id.DeploymentId"
    """<p>The service-generated id of the deployment.</p>"""
    deployment_arn: "capo_network_security_manager.types.deployment_arn.DeploymentArn"
    """<p>The Amazon Resource Name (ARN) of the deployment.</p>"""
    deployment_name: (
        "capo_network_security_manager.types.deployment_name.DeploymentName"
    )
    """<p>The name of the deployment.</p>"""
    deployment_description: NotRequired[
        "capo_network_security_manager.types.description.Description"
    ]
    """<p>A description of the deployment.</p>"""
    status: "capo_network_security_manager.types.entity_status.EntityStatus"
    """<p>The current status of the resource: <code>DRAFT</code> (unpublished, editable) or <code>ACTIVE</code> (published, in use).</p>"""
    deployment_configuration: NotRequired[
        "capo_network_security_manager.types.deployment_configuration.DeploymentConfiguration"
    ]
    """<p>The configuration settings for the deployment.</p>"""
    associated_policy_list: "capo_network_security_manager.types.associated_policy_list.AssociatedPolicyList"
    """<p>The policies associated with the deployment.</p>"""
    associated_scope_list: (
        "capo_network_security_manager.types.associated_scope_list.AssociatedScopeList"
    )
    """<p>The scope associated with the deployment. A deployment has exactly one scope.</p>"""
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
    """<p>The time when the snapshot was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDeploymentSnapshotOutput) -> dict:
    out: dict = {}
    out["deploymentId"] = value["deployment_id"]
    out["deploymentArn"] = value["deployment_arn"]
    out["deploymentName"] = value["deployment_name"]
    if "deployment_description" in value:
        out["deploymentDescription"] = value["deployment_description"]
    import capo_network_security_manager.types.entity_status

    out["status"] = capo_network_security_manager.types.entity_status.serialize_json(
        value["status"]
    )
    if "deployment_configuration" in value:
        import capo_network_security_manager.types.deployment_configuration

        out["deploymentConfiguration"] = (
            capo_network_security_manager.types.deployment_configuration.serialize_json(
                value["deployment_configuration"]
            )
        )
    import capo_network_security_manager.types.associated_policy_list

    out["associatedPolicyList"] = (
        capo_network_security_manager.types.associated_policy_list.serialize_json(
            value["associated_policy_list"]
        )
    )
    import capo_network_security_manager.types.associated_scope_list

    out["associatedScopeList"] = (
        capo_network_security_manager.types.associated_scope_list.serialize_json(
            value["associated_scope_list"]
        )
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


def deserialize_json(data: dict) -> CreateDeploymentSnapshotOutput:
    out: CreateDeploymentSnapshotOutput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    else:
        raise DeserializationError(
            "CreateDeploymentSnapshotOutput.deployment_id required"
        )
    if data.get("deploymentArn") is not None:
        out["deployment_arn"] = data["deploymentArn"]
    else:
        raise DeserializationError(
            "CreateDeploymentSnapshotOutput.deployment_arn required"
        )
    if data.get("deploymentName") is not None:
        out["deployment_name"] = data["deploymentName"]
    else:
        raise DeserializationError(
            "CreateDeploymentSnapshotOutput.deployment_name required"
        )
    if data.get("deploymentDescription") is not None:
        out["deployment_description"] = data["deploymentDescription"]
    if data.get("status") is not None:
        import capo_network_security_manager.types.entity_status

        out["status"] = (
            capo_network_security_manager.types.entity_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CreateDeploymentSnapshotOutput.status required")
    if data.get("deploymentConfiguration") is not None:
        import capo_network_security_manager.types.deployment_configuration

        out["deployment_configuration"] = (
            capo_network_security_manager.types.deployment_configuration.deserialize_json(
                data["deploymentConfiguration"]
            )
        )
    if data.get("associatedPolicyList") is not None:
        import capo_network_security_manager.types.associated_policy_list

        out["associated_policy_list"] = (
            capo_network_security_manager.types.associated_policy_list.deserialize_json(
                data["associatedPolicyList"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDeploymentSnapshotOutput.associated_policy_list required"
        )
    if data.get("associatedScopeList") is not None:
        import capo_network_security_manager.types.associated_scope_list

        out["associated_scope_list"] = (
            capo_network_security_manager.types.associated_scope_list.deserialize_json(
                data["associatedScopeList"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDeploymentSnapshotOutput.associated_scope_list required"
        )
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        raise DeserializationError("CreateDeploymentSnapshotOutput.version required")
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
