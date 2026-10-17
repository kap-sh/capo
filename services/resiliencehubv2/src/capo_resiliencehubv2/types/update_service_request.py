"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UpdateServiceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.associated_system_list
    import capo_resiliencehubv2.types.dependency_discovery_input
    import capo_resiliencehubv2.types.long_description
    import capo_resiliencehubv2.types.permission_model
    import capo_resiliencehubv2.types.region_list
    import capo_resiliencehubv2.types.service_report_configuration


class UpdateServiceRequest(TypedDict, closed=True):
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    description: NotRequired[
        "capo_resiliencehubv2.types.long_description.LongDescription"
    ]
    associated_systems: NotRequired[
        "capo_resiliencehubv2.types.associated_system_list.AssociatedSystemList"
    ]
    """<p>The updated systems to associate with the service.</p>"""
    policy_arn: NotRequired["capo_resiliencehubv2.types.arn.Arn"]
    regions: NotRequired["capo_resiliencehubv2.types.region_list.RegionList"]
    """<p>The updated AWS Regions where the service operates.</p>"""
    permission_model: NotRequired[
        "capo_resiliencehubv2.types.permission_model.PermissionModel"
    ]
    """<p>The updated permission model for the service.</p>"""
    dependency_discovery: NotRequired[
        "capo_resiliencehubv2.types.dependency_discovery_input.DependencyDiscoveryInput"
    ]
    report_configuration: NotRequired[
        "capo_resiliencehubv2.types.service_report_configuration.ServiceReportConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateServiceRequest) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
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
        import capo_resiliencehubv2.types.dependency_discovery_input

        out["dependencyDiscovery"] = (
            capo_resiliencehubv2.types.dependency_discovery_input.serialize_json(
                value["dependency_discovery"]
            )
        )
    if "report_configuration" in value:
        import capo_resiliencehubv2.types.service_report_configuration

        out["reportConfiguration"] = (
            capo_resiliencehubv2.types.service_report_configuration.serialize_json(
                value["report_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateServiceRequest:
    out: UpdateServiceRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    else:
        raise DeserializationError("UpdateServiceRequest.service_arn required")
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
        import capo_resiliencehubv2.types.dependency_discovery_input

        out["dependency_discovery"] = (
            capo_resiliencehubv2.types.dependency_discovery_input.deserialize_json(
                data["dependencyDiscovery"]
            )
        )
    if data.get("reportConfiguration") is not None:
        import capo_resiliencehubv2.types.service_report_configuration

        out["report_configuration"] = (
            capo_resiliencehubv2.types.service_report_configuration.deserialize_json(
                data["reportConfiguration"]
            )
        )
    return out
