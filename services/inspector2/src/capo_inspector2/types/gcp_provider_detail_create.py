"""Generated from Smithy shape ``com.amazonaws.inspector2#GcpProviderDetailCreate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.aws_config_connector_arn
    import capo_inspector2.types.gcp_region_list
    import capo_inspector2.types.gcp_scope_configuration_input


class GcpProviderDetailCreate(TypedDict, closed=True):
    aws_config_connector_arn: (
        "capo_inspector2.types.aws_config_connector_arn.AwsConfigConnectorArn"
    )
    """<p>The ARN of the Amazon Web Services Config connector to associate with this connector.</p>"""
    scope_configuration: (
        "capo_inspector2.types.gcp_scope_configuration_input.GcpScopeConfigurationInput"
    )
    """<p>The scope configuration that defines which GCP resources to scan.</p>"""
    gcp_regions: "capo_inspector2.types.gcp_region_list.GcpRegionList"
    """<p>The GCP locations to scan, such as regions, zones, multi-regions, or dual-regions. Specify <code>ALL</code> to scan all locations.</p>"""
    auto_install_vm_scanner: "bool"
    """<p>Specifies whether to automatically install the VM scanner on connected GCP resources. Defaults to <code>true</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GcpProviderDetailCreate) -> dict:
    out: dict = {}
    out["awsConfigConnectorArn"] = value["aws_config_connector_arn"]
    import capo_inspector2.types.gcp_scope_configuration_input

    out["scopeConfiguration"] = (
        capo_inspector2.types.gcp_scope_configuration_input.serialize_json(
            value["scope_configuration"]
        )
    )
    import capo_inspector2.types.gcp_region_list

    out["gcpRegions"] = capo_inspector2.types.gcp_region_list.serialize_json(
        value["gcp_regions"]
    )
    out["autoInstallVMScanner"] = value.get("auto_install_vm_scanner", True)
    return out


def deserialize_json(data: dict) -> GcpProviderDetailCreate:
    out: GcpProviderDetailCreate = {}  # type: ignore[typeddict-item]
    if data.get("awsConfigConnectorArn") is not None:
        out["aws_config_connector_arn"] = data["awsConfigConnectorArn"]
    else:
        out["aws_config_connector_arn"] = ""
    if data.get("scopeConfiguration") is not None:
        import capo_inspector2.types.gcp_scope_configuration_input

        out["scope_configuration"] = (
            capo_inspector2.types.gcp_scope_configuration_input.deserialize_json(
                data["scopeConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "GcpProviderDetailCreate.scope_configuration required"
        )
    if data.get("gcpRegions") is not None:
        import capo_inspector2.types.gcp_region_list

        out["gcp_regions"] = capo_inspector2.types.gcp_region_list.deserialize_json(
            data["gcpRegions"]
        )
    else:
        out["gcp_regions"] = []
    if data.get("autoInstallVMScanner") is not None:
        out["auto_install_vm_scanner"] = data["autoInstallVMScanner"]
    else:
        out["auto_install_vm_scanner"] = True
    return out
