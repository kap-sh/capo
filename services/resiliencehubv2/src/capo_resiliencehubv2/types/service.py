"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#Service``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.account_id
    import capo_resiliencehubv2.types.achievability
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.assessment_cost
    import capo_resiliencehubv2.types.assessment_status
    import capo_resiliencehubv2.types.associated_system_list
    import capo_resiliencehubv2.types.dependency_discovery_config
    import capo_resiliencehubv2.types.dev_ops_agent_configuration_view
    import capo_resiliencehubv2.types.effective_policy_values
    import capo_resiliencehubv2.types.entity_name
    import capo_resiliencehubv2.types.kms_key_id
    import capo_resiliencehubv2.types.long_description
    import capo_resiliencehubv2.types.organization_id
    import capo_resiliencehubv2.types.ou_id
    import capo_resiliencehubv2.types.permission_model
    import capo_resiliencehubv2.types.region_list
    import capo_resiliencehubv2.types.resource_discovery_status
    import capo_resiliencehubv2.types.service_report_configuration
    import capo_resiliencehubv2.types.tag_map


class Service(TypedDict, closed=True):
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    name: "capo_resiliencehubv2.types.entity_name.EntityName"
    description: NotRequired[
        "capo_resiliencehubv2.types.long_description.LongDescription"
    ]
    associated_systems: NotRequired[
        "capo_resiliencehubv2.types.associated_system_list.AssociatedSystemList"
    ]
    """<p>The systems associated with the service.</p>"""
    policy_arn: NotRequired["capo_resiliencehubv2.types.arn.Arn"]
    regions: NotRequired["capo_resiliencehubv2.types.region_list.RegionList"]
    """<p>The Regions where the service operates.</p>"""
    permission_model: NotRequired[
        "capo_resiliencehubv2.types.permission_model.PermissionModel"
    ]
    """<p>The permission model for the service.</p>"""
    dependency_discovery: NotRequired[
        "capo_resiliencehubv2.types.dependency_discovery_config.DependencyDiscoveryConfig"
    ]
    """<p>The dependency discovery configuration for the service.</p>"""
    effective_policy_values: NotRequired[
        "capo_resiliencehubv2.types.effective_policy_values.EffectivePolicyValues"
    ]
    """<p>The effective policy values for the service.</p>"""
    achievability: NotRequired["capo_resiliencehubv2.types.achievability.Achievability"]
    """<p>The achievability status of the service's resilience targets.</p>"""
    report_configuration: NotRequired[
        "capo_resiliencehubv2.types.service_report_configuration.ServiceReportConfiguration"
    ]
    kms_key_id: NotRequired["capo_resiliencehubv2.types.kms_key_id.KmsKeyId"]
    tags: NotRequired["capo_resiliencehubv2.types.tag_map.TagMap"]
    estimated_assessment_cost: NotRequired[
        "capo_resiliencehubv2.types.assessment_cost.AssessmentCost"
    ]
    """<p>The estimated cost of running an assessment on the service.</p>"""
    resource_discovery: NotRequired[
        "capo_resiliencehubv2.types.resource_discovery_status.ResourceDiscoveryStatus"
    ]
    """<p>The resource discovery status for the service.</p>"""
    assessment_status: NotRequired[
        "capo_resiliencehubv2.types.assessment_status.AssessmentStatus"
    ]
    """<p>The current assessment status of the service.</p>"""
    rerun_assessment: NotRequired["bool"]
    """<p>Indicates whether the assessment should be rerun.</p>"""
    open_findings_count: NotRequired["int"]
    """<p>The number of open findings for the service.</p>"""
    resolved_findings_count: NotRequired["int"]
    """<p>The number of resolved findings for the service.</p>"""
    organization_id: NotRequired[
        "capo_resiliencehubv2.types.organization_id.OrganizationId"
    ]
    """<p>The AWS Organizations identifier for the service.</p>"""
    ou_id: NotRequired["capo_resiliencehubv2.types.ou_id.OuId"]
    """<p>The organizational unit (OU) identifier for the service.</p>"""
    account_id: NotRequired["capo_resiliencehubv2.types.account_id.AccountId"]
    """<p>The AWS account ID that owns the service.</p>"""
    dev_ops_agent_configuration: NotRequired[
        "capo_resiliencehubv2.types.dev_ops_agent_configuration_view.DevOpsAgentConfigurationView"
    ]
    """<p>The current DevOps Agent integration state for the service.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the service was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the service was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Service) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "associated_systems" in value:
        import capo_resiliencehubv2.types.associated_system_list

        out["associatedSystems"] = (
            capo_resiliencehubv2.types.associated_system_list.serialize_json(
                value["associated_systems"]
            )
        )
    if "policy_arn" in value:
        out["policyArn"] = value["policy_arn"]
    if "regions" in value:
        import capo_resiliencehubv2.types.region_list

        out["regions"] = capo_resiliencehubv2.types.region_list.serialize_json(
            value["regions"]
        )
    if "permission_model" in value:
        import capo_resiliencehubv2.types.permission_model

        out["permissionModel"] = (
            capo_resiliencehubv2.types.permission_model.serialize_json(
                value["permission_model"]
            )
        )
    if "dependency_discovery" in value:
        import capo_resiliencehubv2.types.dependency_discovery_config

        out["dependencyDiscovery"] = (
            capo_resiliencehubv2.types.dependency_discovery_config.serialize_json(
                value["dependency_discovery"]
            )
        )
    if "effective_policy_values" in value:
        import capo_resiliencehubv2.types.effective_policy_values

        out["effectivePolicyValues"] = (
            capo_resiliencehubv2.types.effective_policy_values.serialize_json(
                value["effective_policy_values"]
            )
        )
    if "achievability" in value:
        import capo_resiliencehubv2.types.achievability

        out["achievability"] = capo_resiliencehubv2.types.achievability.serialize_json(
            value["achievability"]
        )
    if "report_configuration" in value:
        import capo_resiliencehubv2.types.service_report_configuration

        out["reportConfiguration"] = (
            capo_resiliencehubv2.types.service_report_configuration.serialize_json(
                value["report_configuration"]
            )
        )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "tags" in value:
        import capo_resiliencehubv2.types.tag_map

        out["tags"] = capo_resiliencehubv2.types.tag_map.serialize_json(value["tags"])
    if "estimated_assessment_cost" in value:
        import capo_resiliencehubv2.types.assessment_cost

        out["estimatedAssessmentCost"] = (
            capo_resiliencehubv2.types.assessment_cost.serialize_json(
                value["estimated_assessment_cost"]
            )
        )
    if "resource_discovery" in value:
        import capo_resiliencehubv2.types.resource_discovery_status

        out["resourceDiscovery"] = (
            capo_resiliencehubv2.types.resource_discovery_status.serialize_json(
                value["resource_discovery"]
            )
        )
    if "assessment_status" in value:
        import capo_resiliencehubv2.types.assessment_status

        out["assessmentStatus"] = (
            capo_resiliencehubv2.types.assessment_status.serialize_json(
                value["assessment_status"]
            )
        )
    if "rerun_assessment" in value:
        out["rerunAssessment"] = value["rerun_assessment"]
    if "open_findings_count" in value:
        out["openFindingsCount"] = value["open_findings_count"]
    if "resolved_findings_count" in value:
        out["resolvedFindingsCount"] = value["resolved_findings_count"]
    if "organization_id" in value:
        out["organizationId"] = value["organization_id"]
    if "ou_id" in value:
        out["ouId"] = value["ou_id"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "dev_ops_agent_configuration" in value:
        import capo_resiliencehubv2.types.dev_ops_agent_configuration_view

        out["devOpsAgentConfiguration"] = (
            capo_resiliencehubv2.types.dev_ops_agent_configuration_view.serialize_json(
                value["dev_ops_agent_configuration"]
            )
        )
    if "created_at" in value:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["createdAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["updatedAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> Service:
    out: Service = {}  # type: ignore[typeddict-item]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    else:
        raise DeserializationError("Service.service_arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Service.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("associatedSystems") is not None:
        import capo_resiliencehubv2.types.associated_system_list

        out["associated_systems"] = (
            capo_resiliencehubv2.types.associated_system_list.deserialize_json(
                data["associatedSystems"]
            )
        )
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    if data.get("regions") is not None:
        import capo_resiliencehubv2.types.region_list

        out["regions"] = capo_resiliencehubv2.types.region_list.deserialize_json(
            data["regions"]
        )
    if data.get("permissionModel") is not None:
        import capo_resiliencehubv2.types.permission_model

        out["permission_model"] = (
            capo_resiliencehubv2.types.permission_model.deserialize_json(
                data["permissionModel"]
            )
        )
    if data.get("dependencyDiscovery") is not None:
        import capo_resiliencehubv2.types.dependency_discovery_config

        out["dependency_discovery"] = (
            capo_resiliencehubv2.types.dependency_discovery_config.deserialize_json(
                data["dependencyDiscovery"]
            )
        )
    if data.get("effectivePolicyValues") is not None:
        import capo_resiliencehubv2.types.effective_policy_values

        out["effective_policy_values"] = (
            capo_resiliencehubv2.types.effective_policy_values.deserialize_json(
                data["effectivePolicyValues"]
            )
        )
    if data.get("achievability") is not None:
        import capo_resiliencehubv2.types.achievability

        out["achievability"] = (
            capo_resiliencehubv2.types.achievability.deserialize_json(
                data["achievability"]
            )
        )
    if data.get("reportConfiguration") is not None:
        import capo_resiliencehubv2.types.service_report_configuration

        out["report_configuration"] = (
            capo_resiliencehubv2.types.service_report_configuration.deserialize_json(
                data["reportConfiguration"]
            )
        )
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("tags") is not None:
        import capo_resiliencehubv2.types.tag_map

        out["tags"] = capo_resiliencehubv2.types.tag_map.deserialize_json(data["tags"])
    if data.get("estimatedAssessmentCost") is not None:
        import capo_resiliencehubv2.types.assessment_cost

        out["estimated_assessment_cost"] = (
            capo_resiliencehubv2.types.assessment_cost.deserialize_json(
                data["estimatedAssessmentCost"]
            )
        )
    if data.get("resourceDiscovery") is not None:
        import capo_resiliencehubv2.types.resource_discovery_status

        out["resource_discovery"] = (
            capo_resiliencehubv2.types.resource_discovery_status.deserialize_json(
                data["resourceDiscovery"]
            )
        )
    if data.get("assessmentStatus") is not None:
        import capo_resiliencehubv2.types.assessment_status

        out["assessment_status"] = (
            capo_resiliencehubv2.types.assessment_status.deserialize_json(
                data["assessmentStatus"]
            )
        )
    if data.get("rerunAssessment") is not None:
        out["rerun_assessment"] = data["rerunAssessment"]
    if data.get("openFindingsCount") is not None:
        out["open_findings_count"] = data["openFindingsCount"]
    if data.get("resolvedFindingsCount") is not None:
        out["resolved_findings_count"] = data["resolvedFindingsCount"]
    if data.get("organizationId") is not None:
        out["organization_id"] = data["organizationId"]
    if data.get("ouId") is not None:
        out["ou_id"] = data["ouId"]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("devOpsAgentConfiguration") is not None:
        import capo_resiliencehubv2.types.dev_ops_agent_configuration_view

        out["dev_ops_agent_configuration"] = (
            capo_resiliencehubv2.types.dev_ops_agent_configuration_view.deserialize_json(
                data["devOpsAgentConfiguration"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["created_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if data.get("updatedAt") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["updated_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out


def redact_sensitive(value: Service) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
