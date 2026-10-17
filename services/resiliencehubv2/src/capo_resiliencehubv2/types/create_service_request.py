"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CreateServiceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.associated_system_list
    import capo_resiliencehubv2.types.client_token
    import capo_resiliencehubv2.types.dependency_discovery_input
    import capo_resiliencehubv2.types.entity_name
    import capo_resiliencehubv2.types.kms_key_id
    import capo_resiliencehubv2.types.long_description
    import capo_resiliencehubv2.types.permission_model
    import capo_resiliencehubv2.types.region_list
    import capo_resiliencehubv2.types.service_report_configuration
    import capo_resiliencehubv2.types.tag_map


class CreateServiceRequest(TypedDict, closed=True):
    name: "capo_resiliencehubv2.types.entity_name.EntityName"
    description: NotRequired[
        "capo_resiliencehubv2.types.long_description.LongDescription"
    ]
    associated_systems: NotRequired[
        "capo_resiliencehubv2.types.associated_system_list.AssociatedSystemList"
    ]
    """<p>The systems to associate with the service.</p>"""
    policy_arn: NotRequired["capo_resiliencehubv2.types.arn.Arn"]
    regions: "capo_resiliencehubv2.types.region_list.RegionList"
    """<p>The Regions where the service operates.</p>"""
    permission_model: "capo_resiliencehubv2.types.permission_model.PermissionModel"
    """<p>The permission model for the service.</p>"""
    dependency_discovery: NotRequired[
        "capo_resiliencehubv2.types.dependency_discovery_input.DependencyDiscoveryInput"
    ]
    report_configuration: NotRequired[
        "capo_resiliencehubv2.types.service_report_configuration.ServiceReportConfiguration"
    ]
    kms_key_id: NotRequired["capo_resiliencehubv2.types.kms_key_id.KmsKeyId"]
    tags: NotRequired["capo_resiliencehubv2.types.tag_map.TagMap"]
    client_token: NotRequired["capo_resiliencehubv2.types.client_token.ClientToken"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateServiceRequest) -> dict:
    out: dict = {}
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
    import capo_resiliencehubv2.types.region_list

    out["regions"] = capo_resiliencehubv2.types.region_list.serialize_json(
        value["regions"]
    )
    import capo_resiliencehubv2.types.permission_model

    out["permissionModel"] = capo_resiliencehubv2.types.permission_model.serialize_json(
        value["permission_model"]
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
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "tags" in value:
        import capo_resiliencehubv2.types.tag_map

        out["tags"] = capo_resiliencehubv2.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateServiceRequest:
    out: CreateServiceRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateServiceRequest.name required")
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
    else:
        raise DeserializationError("CreateServiceRequest.regions required")
    if data.get("permissionModel") is not None:
        import capo_resiliencehubv2.types.permission_model

        out["permission_model"] = (
            capo_resiliencehubv2.types.permission_model.deserialize_json(
                data["permissionModel"]
            )
        )
    else:
        raise DeserializationError("CreateServiceRequest.permission_model required")
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
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("tags") is not None:
        import capo_resiliencehubv2.types.tag_map

        out["tags"] = capo_resiliencehubv2.types.tag_map.deserialize_json(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: CreateServiceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
