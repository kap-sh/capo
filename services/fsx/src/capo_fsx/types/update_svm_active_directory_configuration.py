"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateSvmActiveDirectoryConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.net_bios_alias
    import capo_fsx.types.self_managed_active_directory_configuration_updates


class UpdateSvmActiveDirectoryConfiguration(TypedDict, closed=True):
    self_managed_active_directory_configuration: NotRequired[
        "capo_fsx.types.self_managed_active_directory_configuration_updates.SelfManagedActiveDirectoryConfigurationUpdates"
    ]
    net_bios_name: NotRequired["capo_fsx.types.net_bios_alias.NetBiosAlias"]
    """<p>Specifies an updated NetBIOS name of the AD computer object <code>NetBiosName</code> to which an SVM is joined.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSvmActiveDirectoryConfiguration) -> dict:
    out: dict = {}
    if "self_managed_active_directory_configuration" in value:
        import capo_fsx.types.self_managed_active_directory_configuration_updates

        out["SelfManagedActiveDirectoryConfiguration"] = (
            capo_fsx.types.self_managed_active_directory_configuration_updates.serialize_aws_json_1_1(
                value["self_managed_active_directory_configuration"]
            )
        )
    if "net_bios_name" in value:
        out["NetBiosName"] = value["net_bios_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSvmActiveDirectoryConfiguration:
    out: UpdateSvmActiveDirectoryConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SelfManagedActiveDirectoryConfiguration") is not None:
        import capo_fsx.types.self_managed_active_directory_configuration_updates

        out["self_managed_active_directory_configuration"] = (
            capo_fsx.types.self_managed_active_directory_configuration_updates.deserialize_aws_json_1_1(
                data["SelfManagedActiveDirectoryConfiguration"]
            )
        )
    if data.get("NetBiosName") is not None:
        out["net_bios_name"] = data["NetBiosName"]
    return out


def redact_sensitive(value: UpdateSvmActiveDirectoryConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "self_managed_active_directory_configuration" in value:
        import capo_fsx.types.self_managed_active_directory_configuration_updates

        out["self_managed_active_directory_configuration"] = (
            capo_fsx.types.self_managed_active_directory_configuration_updates.redact_sensitive(
                value["self_managed_active_directory_configuration"]
            )
        )
    return out
