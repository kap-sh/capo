"""Generated from Smithy shape ``com.amazonaws.inspector2#AzureProviderDetailCreate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.aws_config_connector_arn
    import capo_inspector2.types.azure_region_list
    import capo_inspector2.types.azure_scope_configuration_input


class AzureProviderDetailCreate(TypedDict, closed=True):
    aws_config_connector_arn: (
        "capo_inspector2.types.aws_config_connector_arn.AwsConfigConnectorArn"
    )
    """<p>The ARN of the Amazon Web Services Config connector to associate with this connector.</p>"""
    scope_configuration: "capo_inspector2.types.azure_scope_configuration_input.AzureScopeConfigurationInput"
    """<p>The scope configuration that defines which Azure resources to scan.</p>"""
    azure_regions: "capo_inspector2.types.azure_region_list.AzureRegionList"
    """<p>The Azure regions to scan.</p>"""
    auto_install_vm_scanner: "bool"
    """<p>Specifies whether to automatically install the VM scanner on connected Azure resources. Defaults to <code>true</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureProviderDetailCreate) -> dict:
    out: dict = {}
    out["awsConfigConnectorArn"] = value["aws_config_connector_arn"]
    import capo_inspector2.types.azure_scope_configuration_input

    out["scopeConfiguration"] = (
        capo_inspector2.types.azure_scope_configuration_input.serialize_json(
            value["scope_configuration"]
        )
    )
    import capo_inspector2.types.azure_region_list

    out["azureRegions"] = capo_inspector2.types.azure_region_list.serialize_json(
        value["azure_regions"]
    )
    out["autoInstallVMScanner"] = value.get("auto_install_vm_scanner", True)
    return out


def deserialize_json(data: dict) -> AzureProviderDetailCreate:
    out: AzureProviderDetailCreate = {}  # type: ignore[typeddict-item]
    if data.get("awsConfigConnectorArn") is not None:
        out["aws_config_connector_arn"] = data["awsConfigConnectorArn"]
    else:
        out["aws_config_connector_arn"] = ""
    if data.get("scopeConfiguration") is not None:
        import capo_inspector2.types.azure_scope_configuration_input

        out["scope_configuration"] = (
            capo_inspector2.types.azure_scope_configuration_input.deserialize_json(
                data["scopeConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "AzureProviderDetailCreate.scope_configuration required"
        )
    if data.get("azureRegions") is not None:
        import capo_inspector2.types.azure_region_list

        out["azure_regions"] = capo_inspector2.types.azure_region_list.deserialize_json(
            data["azureRegions"]
        )
    else:
        out["azure_regions"] = []
    if data.get("autoInstallVMScanner") is not None:
        out["auto_install_vm_scanner"] = data["autoInstallVMScanner"]
    else:
        out["auto_install_vm_scanner"] = True
    return out
