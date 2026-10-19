"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#InstanceConfigurationFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.billing_mode
    import capo_workspaces_instances.types.instance_configuration_tenancy_enum
    import capo_workspaces_instances.types.platform_type_enum


class InstanceConfigurationFilter(TypedDict, closed=True):
    billing_mode: "capo_workspaces_instances.types.billing_mode.BillingMode"
    """<p>Filters WorkSpace Instance types based on supported billing modes. Allows customers to search for instance types that support their preferred billing model, such as HOURLY or MONTHLY billing.</p>"""
    platform_type: "capo_workspaces_instances.types.platform_type_enum.PlatformTypeEnum"
    """<p>Filters WorkSpace Instance types by operating system platform. Allows customers to find instances that support their desired OS, such as Windows, Linux/UNIX, Ubuntu Pro, RHEL, or SUSE.</p>"""
    tenancy: "capo_workspaces_instances.types.instance_configuration_tenancy_enum.InstanceConfigurationTenancyEnum"
    """<p>Filters WorkSpace Instance types by tenancy model. Allows customers to find instances that match their tenancy requirements, such as SHARED or DEDICATED.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceConfigurationFilter) -> dict:
    out: dict = {}
    import capo_workspaces_instances.types.billing_mode

    out["BillingMode"] = (
        capo_workspaces_instances.types.billing_mode.serialize_aws_json_1_0(
            value["billing_mode"]
        )
    )
    import capo_workspaces_instances.types.platform_type_enum

    out["PlatformType"] = (
        capo_workspaces_instances.types.platform_type_enum.serialize_aws_json_1_0(
            value["platform_type"]
        )
    )
    import capo_workspaces_instances.types.instance_configuration_tenancy_enum

    out["Tenancy"] = (
        capo_workspaces_instances.types.instance_configuration_tenancy_enum.serialize_aws_json_1_0(
            value["tenancy"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> InstanceConfigurationFilter:
    out: InstanceConfigurationFilter = {}  # type: ignore[typeddict-item]
    if data.get("BillingMode") is not None:
        import capo_workspaces_instances.types.billing_mode

        out["billing_mode"] = (
            capo_workspaces_instances.types.billing_mode.deserialize_aws_json_1_0(
                data["BillingMode"]
            )
        )
    else:
        import typing

        out["billing_mode"] = typing.cast(
            "capo_workspaces_instances.types.billing_mode.BillingMode", ""
        )
    if data.get("PlatformType") is not None:
        import capo_workspaces_instances.types.platform_type_enum

        out["platform_type"] = (
            capo_workspaces_instances.types.platform_type_enum.deserialize_aws_json_1_0(
                data["PlatformType"]
            )
        )
    else:
        import typing

        out["platform_type"] = typing.cast(
            "capo_workspaces_instances.types.platform_type_enum.PlatformTypeEnum", ""
        )
    if data.get("Tenancy") is not None:
        import capo_workspaces_instances.types.instance_configuration_tenancy_enum

        out["tenancy"] = (
            capo_workspaces_instances.types.instance_configuration_tenancy_enum.deserialize_aws_json_1_0(
                data["Tenancy"]
            )
        )
    else:
        import typing

        out["tenancy"] = typing.cast(
            "capo_workspaces_instances.types.instance_configuration_tenancy_enum.InstanceConfigurationTenancyEnum",
            "",
        )
    return out
