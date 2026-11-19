"""Generated from Smithy shape ``com.amazonaws.workspaces#AccountModification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.dedicated_tenancy_management_cidr_range
    import capo_workspaces.types.dedicated_tenancy_modification_state_enum
    import capo_workspaces.types.dedicated_tenancy_support_result_enum
    import capo_workspaces.types.description
    import capo_workspaces.types.timestamp
    import capo_workspaces.types.workspace_error_code


class AccountModification(TypedDict, closed=True):
    modification_state: NotRequired[
        "capo_workspaces.types.dedicated_tenancy_modification_state_enum.DedicatedTenancyModificationStateEnum"
    ]
    """<p>The state of the modification to the configuration of BYOL.</p>"""
    dedicated_tenancy_support: NotRequired[
        "capo_workspaces.types.dedicated_tenancy_support_result_enum.DedicatedTenancySupportResultEnum"
    ]
    """<p>The status of BYOL (whether BYOL is being enabled or disabled).</p>"""
    dedicated_tenancy_management_cidr_range: NotRequired[
        "capo_workspaces.types.dedicated_tenancy_management_cidr_range.DedicatedTenancyManagementCidrRange"
    ]
    """<p>The IP address range, specified as an IPv4 CIDR block, for the management network interface used for the account.</p>"""
    start_time: NotRequired["capo_workspaces.types.timestamp.Timestamp"]
    """<p>The timestamp when the modification of the BYOL configuration was started.</p>"""
    error_code: NotRequired[
        "capo_workspaces.types.workspace_error_code.WorkspaceErrorCode"
    ]
    """<p>The error code that is returned if the configuration of BYOL cannot be modified.</p>"""
    error_message: NotRequired["capo_workspaces.types.description.Description"]
    """<p>The text of the error message that is returned if the configuration of BYOL cannot be modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountModification) -> dict:
    out: dict = {}
    if "modification_state" in value:
        import capo_workspaces.types.dedicated_tenancy_modification_state_enum

        out["ModificationState"] = (
            capo_workspaces.types.dedicated_tenancy_modification_state_enum.serialize_aws_json_1_1(
                value["modification_state"]
            )
        )
    if "dedicated_tenancy_support" in value:
        import capo_workspaces.types.dedicated_tenancy_support_result_enum

        out["DedicatedTenancySupport"] = (
            capo_workspaces.types.dedicated_tenancy_support_result_enum.serialize_aws_json_1_1(
                value["dedicated_tenancy_support"]
            )
        )
    if "dedicated_tenancy_management_cidr_range" in value:
        out["DedicatedTenancyManagementCidrRange"] = value[
            "dedicated_tenancy_management_cidr_range"
        ]
    if "start_time" in value:
        import capo_workspaces.types.timestamp

        out["StartTime"] = capo_workspaces.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AccountModification:
    out: AccountModification = {}  # type: ignore[typeddict-item]
    if data.get("ModificationState") is not None:
        import capo_workspaces.types.dedicated_tenancy_modification_state_enum

        out["modification_state"] = (
            capo_workspaces.types.dedicated_tenancy_modification_state_enum.deserialize_aws_json_1_1(
                data["ModificationState"]
            )
        )
    if data.get("DedicatedTenancySupport") is not None:
        import capo_workspaces.types.dedicated_tenancy_support_result_enum

        out["dedicated_tenancy_support"] = (
            capo_workspaces.types.dedicated_tenancy_support_result_enum.deserialize_aws_json_1_1(
                data["DedicatedTenancySupport"]
            )
        )
    if data.get("DedicatedTenancyManagementCidrRange") is not None:
        out["dedicated_tenancy_management_cidr_range"] = data[
            "DedicatedTenancyManagementCidrRange"
        ]
    if data.get("StartTime") is not None:
        import capo_workspaces.types.timestamp

        out["start_time"] = capo_workspaces.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccountModification) -> dict:
    out: dict = {}
    if "modification_state" in value:
        import capo_workspaces.types.dedicated_tenancy_modification_state_enum

        out["ModificationState"] = (
            capo_workspaces.types.dedicated_tenancy_modification_state_enum.serialize_cbor(
                value["modification_state"]
            )
        )
    if "dedicated_tenancy_support" in value:
        import capo_workspaces.types.dedicated_tenancy_support_result_enum

        out["DedicatedTenancySupport"] = (
            capo_workspaces.types.dedicated_tenancy_support_result_enum.serialize_cbor(
                value["dedicated_tenancy_support"]
            )
        )
    if "dedicated_tenancy_management_cidr_range" in value:
        out["DedicatedTenancyManagementCidrRange"] = value[
            "dedicated_tenancy_management_cidr_range"
        ]
    if "start_time" in value:
        import capo_workspaces.types.timestamp

        out["StartTime"] = capo_workspaces.types.timestamp.serialize_cbor(
            value["start_time"]
        )
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_cbor(data: dict) -> AccountModification:
    out: AccountModification = {}  # type: ignore[typeddict-item]
    if data.get("ModificationState") is not None:
        import capo_workspaces.types.dedicated_tenancy_modification_state_enum

        out["modification_state"] = (
            capo_workspaces.types.dedicated_tenancy_modification_state_enum.deserialize_cbor(
                data["ModificationState"]
            )
        )
    if data.get("DedicatedTenancySupport") is not None:
        import capo_workspaces.types.dedicated_tenancy_support_result_enum

        out["dedicated_tenancy_support"] = (
            capo_workspaces.types.dedicated_tenancy_support_result_enum.deserialize_cbor(
                data["DedicatedTenancySupport"]
            )
        )
    if data.get("DedicatedTenancyManagementCidrRange") is not None:
        out["dedicated_tenancy_management_cidr_range"] = data[
            "DedicatedTenancyManagementCidrRange"
        ]
    if data.get("StartTime") is not None:
        import capo_workspaces.types.timestamp

        out["start_time"] = capo_workspaces.types.timestamp.deserialize_cbor(
            data["StartTime"]
        )
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
