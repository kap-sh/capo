"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#SupportedInstanceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.billing_mode
    import capo_workspaces_instances.types.instance_configuration_tenancy_enum
    import capo_workspaces_instances.types.platform_type_enum


class SupportedInstanceConfiguration(TypedDict, closed=True):
    billing_mode: NotRequired[
        "capo_workspaces_instances.types.billing_mode.BillingMode"
    ]
    """<p>Specifies the billing mode supported in this configuration combination.</p>"""
    platform_type: NotRequired[
        "capo_workspaces_instances.types.platform_type_enum.PlatformTypeEnum"
    ]
    """<p>Specifies the operating system platform supported in this configuration combination.</p>"""
    tenancy: NotRequired[
        "capo_workspaces_instances.types.instance_configuration_tenancy_enum.InstanceConfigurationTenancyEnum"
    ]
    """<p>Specifies the tenancy model supported in this configuration combination.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SupportedInstanceConfiguration) -> dict:
    out: dict = {}
    if "billing_mode" in value:
        import capo_workspaces_instances.types.billing_mode

        out["BillingMode"] = (
            capo_workspaces_instances.types.billing_mode.serialize_aws_json_1_0(
                value["billing_mode"]
            )
        )
    if "platform_type" in value:
        import capo_workspaces_instances.types.platform_type_enum

        out["PlatformType"] = (
            capo_workspaces_instances.types.platform_type_enum.serialize_aws_json_1_0(
                value["platform_type"]
            )
        )
    if "tenancy" in value:
        import capo_workspaces_instances.types.instance_configuration_tenancy_enum

        out["Tenancy"] = (
            capo_workspaces_instances.types.instance_configuration_tenancy_enum.serialize_aws_json_1_0(
                value["tenancy"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SupportedInstanceConfiguration:
    out: SupportedInstanceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("BillingMode") is not None:
        import capo_workspaces_instances.types.billing_mode

        out["billing_mode"] = (
            capo_workspaces_instances.types.billing_mode.deserialize_aws_json_1_0(
                data["BillingMode"]
            )
        )
    if data.get("PlatformType") is not None:
        import capo_workspaces_instances.types.platform_type_enum

        out["platform_type"] = (
            capo_workspaces_instances.types.platform_type_enum.deserialize_aws_json_1_0(
                data["PlatformType"]
            )
        )
    if data.get("Tenancy") is not None:
        import capo_workspaces_instances.types.instance_configuration_tenancy_enum

        out["tenancy"] = (
            capo_workspaces_instances.types.instance_configuration_tenancy_enum.deserialize_aws_json_1_0(
                data["Tenancy"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SupportedInstanceConfiguration) -> dict:
    out: dict = {}
    if "billing_mode" in value:
        import capo_workspaces_instances.types.billing_mode

        out["BillingMode"] = (
            capo_workspaces_instances.types.billing_mode.serialize_cbor(
                value["billing_mode"]
            )
        )
    if "platform_type" in value:
        import capo_workspaces_instances.types.platform_type_enum

        out["PlatformType"] = (
            capo_workspaces_instances.types.platform_type_enum.serialize_cbor(
                value["platform_type"]
            )
        )
    if "tenancy" in value:
        import capo_workspaces_instances.types.instance_configuration_tenancy_enum

        out["Tenancy"] = (
            capo_workspaces_instances.types.instance_configuration_tenancy_enum.serialize_cbor(
                value["tenancy"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> SupportedInstanceConfiguration:
    out: SupportedInstanceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("BillingMode") is not None:
        import capo_workspaces_instances.types.billing_mode

        out["billing_mode"] = (
            capo_workspaces_instances.types.billing_mode.deserialize_cbor(
                data["BillingMode"]
            )
        )
    if data.get("PlatformType") is not None:
        import capo_workspaces_instances.types.platform_type_enum

        out["platform_type"] = (
            capo_workspaces_instances.types.platform_type_enum.deserialize_cbor(
                data["PlatformType"]
            )
        )
    if data.get("Tenancy") is not None:
        import capo_workspaces_instances.types.instance_configuration_tenancy_enum

        out["tenancy"] = (
            capo_workspaces_instances.types.instance_configuration_tenancy_enum.deserialize_cbor(
                data["Tenancy"]
            )
        )
    return out
