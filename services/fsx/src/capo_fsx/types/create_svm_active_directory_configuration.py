"""Generated from Smithy shape ``com.amazonaws.fsx#CreateSvmActiveDirectoryConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.net_bios_alias
    import capo_fsx.types.self_managed_active_directory_configuration


class CreateSvmActiveDirectoryConfiguration(TypedDict, closed=True):
    net_bios_name: NotRequired["capo_fsx.types.net_bios_alias.NetBiosAlias"]
    """<p>The NetBIOS name of the Active Directory computer object that will be created for your SVM.</p>"""
    self_managed_active_directory_configuration: NotRequired[
        "capo_fsx.types.self_managed_active_directory_configuration.SelfManagedActiveDirectoryConfiguration"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSvmActiveDirectoryConfiguration) -> dict:
    out: dict = {}
    if "net_bios_name" in value:
        out["NetBiosName"] = value["net_bios_name"]
    if "self_managed_active_directory_configuration" in value:
        import capo_fsx.types.self_managed_active_directory_configuration

        out["SelfManagedActiveDirectoryConfiguration"] = (
            capo_fsx.types.self_managed_active_directory_configuration.serialize_aws_json_1_1(
                value["self_managed_active_directory_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSvmActiveDirectoryConfiguration:
    out: CreateSvmActiveDirectoryConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("NetBiosName") is not None:
        out["net_bios_name"] = data["NetBiosName"]
    if data.get("SelfManagedActiveDirectoryConfiguration") is not None:
        import capo_fsx.types.self_managed_active_directory_configuration

        out["self_managed_active_directory_configuration"] = (
            capo_fsx.types.self_managed_active_directory_configuration.deserialize_aws_json_1_1(
                data["SelfManagedActiveDirectoryConfiguration"]
            )
        )
    return out


def redact_sensitive(value: CreateSvmActiveDirectoryConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "self_managed_active_directory_configuration" in value:
        import capo_fsx.types.self_managed_active_directory_configuration

        out["self_managed_active_directory_configuration"] = (
            capo_fsx.types.self_managed_active_directory_configuration.redact_sensitive(
                value["self_managed_active_directory_configuration"]
            )
        )
    return out
