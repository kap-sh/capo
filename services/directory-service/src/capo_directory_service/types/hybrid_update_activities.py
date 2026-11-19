"""Generated from Smithy shape ``com.amazonaws.directoryservice#HybridUpdateActivities``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.hybrid_update_info_entries


class HybridUpdateActivities(TypedDict, closed=True):
    self_managed_instances: NotRequired[
        "capo_directory_service.types.hybrid_update_info_entries.HybridUpdateInfoEntries"
    ]
    """<p>A list of update activities related to the self-managed instances with SSM in the self-managed instances with SSM hybrid directory configuration.</p>"""
    hybrid_administrator_account: NotRequired[
        "capo_directory_service.types.hybrid_update_info_entries.HybridUpdateInfoEntries"
    ]
    """<p>A list of update activities related to hybrid directory administrator account changes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HybridUpdateActivities) -> dict:
    out: dict = {}
    if "self_managed_instances" in value:
        import capo_directory_service.types.hybrid_update_info_entries

        out["SelfManagedInstances"] = (
            capo_directory_service.types.hybrid_update_info_entries.serialize_aws_json_1_1(
                value["self_managed_instances"]
            )
        )
    if "hybrid_administrator_account" in value:
        import capo_directory_service.types.hybrid_update_info_entries

        out["HybridAdministratorAccount"] = (
            capo_directory_service.types.hybrid_update_info_entries.serialize_aws_json_1_1(
                value["hybrid_administrator_account"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HybridUpdateActivities:
    out: HybridUpdateActivities = {}  # type: ignore[typeddict-item]
    if data.get("SelfManagedInstances") is not None:
        import capo_directory_service.types.hybrid_update_info_entries

        out["self_managed_instances"] = (
            capo_directory_service.types.hybrid_update_info_entries.deserialize_aws_json_1_1(
                data["SelfManagedInstances"]
            )
        )
    if data.get("HybridAdministratorAccount") is not None:
        import capo_directory_service.types.hybrid_update_info_entries

        out["hybrid_administrator_account"] = (
            capo_directory_service.types.hybrid_update_info_entries.deserialize_aws_json_1_1(
                data["HybridAdministratorAccount"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: HybridUpdateActivities) -> dict:
    out: dict = {}
    if "self_managed_instances" in value:
        import capo_directory_service.types.hybrid_update_info_entries

        out["SelfManagedInstances"] = (
            capo_directory_service.types.hybrid_update_info_entries.serialize_cbor(
                value["self_managed_instances"]
            )
        )
    if "hybrid_administrator_account" in value:
        import capo_directory_service.types.hybrid_update_info_entries

        out["HybridAdministratorAccount"] = (
            capo_directory_service.types.hybrid_update_info_entries.serialize_cbor(
                value["hybrid_administrator_account"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> HybridUpdateActivities:
    out: HybridUpdateActivities = {}  # type: ignore[typeddict-item]
    if data.get("SelfManagedInstances") is not None:
        import capo_directory_service.types.hybrid_update_info_entries

        out["self_managed_instances"] = (
            capo_directory_service.types.hybrid_update_info_entries.deserialize_cbor(
                data["SelfManagedInstances"]
            )
        )
    if data.get("HybridAdministratorAccount") is not None:
        import capo_directory_service.types.hybrid_update_info_entries

        out["hybrid_administrator_account"] = (
            capo_directory_service.types.hybrid_update_info_entries.deserialize_cbor(
                data["HybridAdministratorAccount"]
            )
        )
    return out
