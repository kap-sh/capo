"""Generated from Smithy shape ``com.amazonaws.datazone#PutEnvironmentBlueprintConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.enabled_region_list
    import capo_datazone.types.environment_blueprint_id
    import capo_datazone.types.global_parameter_map
    import capo_datazone.types.policy_arn
    import capo_datazone.types.provisioning_configuration_list
    import capo_datazone.types.put_resource_configurations
    import capo_datazone.types.regional_parameter_map
    import capo_datazone.types.role_arn


class PutEnvironmentBlueprintConfigurationInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain.</p>"""
    environment_blueprint_identifier: (
        "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
    )
    """<p>The identifier of the environment blueprint.</p>"""
    provisioning_role_arn: NotRequired["capo_datazone.types.role_arn.RoleArn"]
    """<p>The ARN of the provisioning role.</p>"""
    manage_access_role_arn: NotRequired["capo_datazone.types.role_arn.RoleArn"]
    """<p>The ARN of the manage access role.</p>"""
    environment_role_permission_boundary: NotRequired[
        "capo_datazone.types.policy_arn.PolicyArn"
    ]
    """<p>The environment role permissions boundary.</p>"""
    enabled_regions: "capo_datazone.types.enabled_region_list.EnabledRegionList"
    """<p>Specifies the enabled Amazon Web Services Regions.</p>"""
    regional_parameters: NotRequired[
        "capo_datazone.types.regional_parameter_map.RegionalParameterMap"
    ]
    """<p>The regional parameters in the environment blueprint.</p>"""
    resource_configurations: NotRequired[
        "capo_datazone.types.put_resource_configurations.PutResourceConfigurations"
    ]
    """<p>The resource configurations of the environment blueprint.</p>"""
    allow_user_provided_configurations: NotRequired["bool"]
    """<p>Specifies whether user-provided resource configurations are allowed for the environment blueprint.</p>"""
    global_parameters: NotRequired[
        "capo_datazone.types.global_parameter_map.GlobalParameterMap"
    ]
    """<p>Region-agnostic environment blueprint parameters. </p>"""
    provisioning_configurations: NotRequired[
        "capo_datazone.types.provisioning_configuration_list.ProvisioningConfigurationList"
    ]
    """<p>The provisioning configuration of a blueprint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutEnvironmentBlueprintConfigurationInput) -> dict:
    out: dict = {}
    if "provisioning_role_arn" in value:
        out["provisioningRoleArn"] = value["provisioning_role_arn"]
    if "manage_access_role_arn" in value:
        out["manageAccessRoleArn"] = value["manage_access_role_arn"]
    if "environment_role_permission_boundary" in value:
        out["environmentRolePermissionBoundary"] = value[
            "environment_role_permission_boundary"
        ]
    import capo_datazone.types.enabled_region_list

    out["enabledRegions"] = capo_datazone.types.enabled_region_list.serialize_json(
        value["enabled_regions"]
    )
    if "regional_parameters" in value:
        import capo_datazone.types.regional_parameter_map

        out["regionalParameters"] = (
            capo_datazone.types.regional_parameter_map.serialize_json(
                value["regional_parameters"]
            )
        )
    if "resource_configurations" in value:
        import capo_datazone.types.put_resource_configurations

        out["resourceConfigurations"] = (
            capo_datazone.types.put_resource_configurations.serialize_json(
                value["resource_configurations"]
            )
        )
    if "allow_user_provided_configurations" in value:
        out["allowUserProvidedConfigurations"] = value[
            "allow_user_provided_configurations"
        ]
    if "global_parameters" in value:
        import capo_datazone.types.global_parameter_map

        out["globalParameters"] = (
            capo_datazone.types.global_parameter_map.serialize_json(
                value["global_parameters"]
            )
        )
    if "provisioning_configurations" in value:
        import capo_datazone.types.provisioning_configuration_list

        out["provisioningConfigurations"] = (
            capo_datazone.types.provisioning_configuration_list.serialize_json(
                value["provisioning_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutEnvironmentBlueprintConfigurationInput:
    out: PutEnvironmentBlueprintConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("provisioningRoleArn") is not None:
        out["provisioning_role_arn"] = data["provisioningRoleArn"]
    if data.get("manageAccessRoleArn") is not None:
        out["manage_access_role_arn"] = data["manageAccessRoleArn"]
    if data.get("environmentRolePermissionBoundary") is not None:
        out["environment_role_permission_boundary"] = data[
            "environmentRolePermissionBoundary"
        ]
    if data.get("enabledRegions") is not None:
        import capo_datazone.types.enabled_region_list

        out["enabled_regions"] = (
            capo_datazone.types.enabled_region_list.deserialize_json(
                data["enabledRegions"]
            )
        )
    else:
        out["enabled_regions"] = []
    if data.get("regionalParameters") is not None:
        import capo_datazone.types.regional_parameter_map

        out["regional_parameters"] = (
            capo_datazone.types.regional_parameter_map.deserialize_json(
                data["regionalParameters"]
            )
        )
    if data.get("resourceConfigurations") is not None:
        import capo_datazone.types.put_resource_configurations

        out["resource_configurations"] = (
            capo_datazone.types.put_resource_configurations.deserialize_json(
                data["resourceConfigurations"]
            )
        )
    if data.get("allowUserProvidedConfigurations") is not None:
        out["allow_user_provided_configurations"] = data[
            "allowUserProvidedConfigurations"
        ]
    if data.get("globalParameters") is not None:
        import capo_datazone.types.global_parameter_map

        out["global_parameters"] = (
            capo_datazone.types.global_parameter_map.deserialize_json(
                data["globalParameters"]
            )
        )
    if data.get("provisioningConfigurations") is not None:
        import capo_datazone.types.provisioning_configuration_list

        out["provisioning_configurations"] = (
            capo_datazone.types.provisioning_configuration_list.deserialize_json(
                data["provisioningConfigurations"]
            )
        )
    return out
