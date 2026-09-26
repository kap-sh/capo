"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ResourceSynchronizationStatusSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.account_id
    import capo_network_security_manager.types.arn
    import capo_network_security_manager.types.date_timestamp
    import capo_network_security_manager.types.deployment_arn
    import capo_network_security_manager.types.out_of_sync_reasons_view
    import capo_network_security_manager.types.remediation_issues_view
    import capo_network_security_manager.types.resource_type
    import capo_network_security_manager.types.synchronization_status


class ResourceSynchronizationStatusSummary(TypedDict, closed=True):
    synchronization_status: "capo_network_security_manager.types.synchronization_status.SynchronizationStatus"
    """<p>The synchronization status of the resource, such as <code>IN_SYNC</code> or <code>OUT_OF_SYNC</code>.</p>"""
    account_id: "capo_network_security_manager.types.account_id.AccountId"
    """<p>The AWS account ID that owns the resource.</p>"""
    resource_arn: "capo_network_security_manager.types.arn.Arn"
    """<p>The ARN of the resource whose synchronization status is reported.</p>"""
    deployment_arn: NotRequired[
        "capo_network_security_manager.types.deployment_arn.DeploymentArn"
    ]
    """<p>The ARN of the deployment that the synchronization status is associated with. This is absent for aggregate (cross-deployment) statuses.</p>"""
    resource_type: NotRequired[
        "capo_network_security_manager.types.resource_type.ResourceType"
    ]
    """<p>The type of the resource, in AWS CloudFormation format.</p>"""
    updated_at: "capo_network_security_manager.types.date_timestamp.DateTimestamp"
    """<p>The time when the resource was last updated.</p>"""
    out_of_sync_reasons: NotRequired[
        "capo_network_security_manager.types.out_of_sync_reasons_view.OutOfSyncReasonsView"
    ]
    """<p>The reasons the resource is out of sync, keyed by firewall type. This is null when the resource is in sync.</p>"""
    remediation_issues: NotRequired[
        "capo_network_security_manager.types.remediation_issues_view.RemediationIssuesView"
    ]
    """<p>Details about remediation issues, keyed by firewall type. This is null when there are no remediation issues.</p>"""
    evaluated_at: NotRequired[
        "capo_network_security_manager.types.date_timestamp.DateTimestamp"
    ]
    """<p>The time when the synchronization status was last evaluated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceSynchronizationStatusSummary) -> dict:
    out: dict = {}
    import capo_network_security_manager.types.synchronization_status

    out["synchronizationStatus"] = (
        capo_network_security_manager.types.synchronization_status.serialize_json(
            value["synchronization_status"]
        )
    )
    out["accountId"] = value["account_id"]
    out["resourceArn"] = value["resource_arn"]
    if "deployment_arn" in value:
        out["deploymentArn"] = value["deployment_arn"]
    if "resource_type" in value:
        import capo_network_security_manager.types.resource_type

        out["resourceType"] = (
            capo_network_security_manager.types.resource_type.serialize_json(
                value["resource_type"]
            )
        )
    import capo_network_security_manager.types.date_timestamp

    out["updatedAt"] = (
        capo_network_security_manager.types.date_timestamp.serialize_json(
            value["updated_at"]
        )
    )
    if "out_of_sync_reasons" in value:
        import capo_network_security_manager.types.out_of_sync_reasons_view

        out["outOfSyncReasons"] = (
            capo_network_security_manager.types.out_of_sync_reasons_view.serialize_json(
                value["out_of_sync_reasons"]
            )
        )
    if "remediation_issues" in value:
        import capo_network_security_manager.types.remediation_issues_view

        out["remediationIssues"] = (
            capo_network_security_manager.types.remediation_issues_view.serialize_json(
                value["remediation_issues"]
            )
        )
    if "evaluated_at" in value:
        import capo_network_security_manager.types.date_timestamp

        out["evaluatedAt"] = (
            capo_network_security_manager.types.date_timestamp.serialize_json(
                value["evaluated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourceSynchronizationStatusSummary:
    out: ResourceSynchronizationStatusSummary = {}  # type: ignore[typeddict-item]
    if data.get("synchronizationStatus") is not None:
        import capo_network_security_manager.types.synchronization_status

        out["synchronization_status"] = (
            capo_network_security_manager.types.synchronization_status.deserialize_json(
                data["synchronizationStatus"]
            )
        )
    else:
        raise DeserializationError(
            "ResourceSynchronizationStatusSummary.synchronization_status required"
        )
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError(
            "ResourceSynchronizationStatusSummary.account_id required"
        )
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError(
            "ResourceSynchronizationStatusSummary.resource_arn required"
        )
    if data.get("deploymentArn") is not None:
        out["deployment_arn"] = data["deploymentArn"]
    if data.get("resourceType") is not None:
        import capo_network_security_manager.types.resource_type

        out["resource_type"] = (
            capo_network_security_manager.types.resource_type.deserialize_json(
                data["resourceType"]
            )
        )
    if data.get("updatedAt") is not None:
        import capo_network_security_manager.types.date_timestamp

        out["updated_at"] = (
            capo_network_security_manager.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "ResourceSynchronizationStatusSummary.updated_at required"
        )
    if data.get("outOfSyncReasons") is not None:
        import capo_network_security_manager.types.out_of_sync_reasons_view

        out["out_of_sync_reasons"] = (
            capo_network_security_manager.types.out_of_sync_reasons_view.deserialize_json(
                data["outOfSyncReasons"]
            )
        )
    if data.get("remediationIssues") is not None:
        import capo_network_security_manager.types.remediation_issues_view

        out["remediation_issues"] = (
            capo_network_security_manager.types.remediation_issues_view.deserialize_json(
                data["remediationIssues"]
            )
        )
    if data.get("evaluatedAt") is not None:
        import capo_network_security_manager.types.date_timestamp

        out["evaluated_at"] = (
            capo_network_security_manager.types.date_timestamp.deserialize_json(
                data["evaluatedAt"]
            )
        )
    return out
