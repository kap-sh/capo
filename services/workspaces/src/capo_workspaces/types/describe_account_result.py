"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeAccountResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.dedicated_tenancy_account_type
    import capo_workspaces.types.dedicated_tenancy_management_cidr_range
    import capo_workspaces.types.dedicated_tenancy_support_result_enum
    import capo_workspaces.types.message


class DescribeAccountResult(TypedDict, closed=True):
    dedicated_tenancy_support: NotRequired[
        "capo_workspaces.types.dedicated_tenancy_support_result_enum.DedicatedTenancySupportResultEnum"
    ]
    """<p>The status of BYOL (whether BYOL is enabled or disabled).</p>"""
    dedicated_tenancy_management_cidr_range: NotRequired[
        "capo_workspaces.types.dedicated_tenancy_management_cidr_range.DedicatedTenancyManagementCidrRange"
    ]
    """<p>The IP address range, specified as an IPv4 CIDR block, used for the management network interface.</p> <p>The management network interface is connected to a secure Amazon WorkSpaces management network. It is used for interactive streaming of the WorkSpace desktop to Amazon WorkSpaces clients, and to allow Amazon WorkSpaces to manage the WorkSpace.</p>"""
    dedicated_tenancy_account_type: NotRequired[
        "capo_workspaces.types.dedicated_tenancy_account_type.DedicatedTenancyAccountType"
    ]
    """<p>The type of linked account.</p>"""
    message: NotRequired["capo_workspaces.types.message.Message"]
    """<p>The text message to describe the status of BYOL.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAccountResult) -> dict:
    out: dict = {}
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
    if "dedicated_tenancy_account_type" in value:
        import capo_workspaces.types.dedicated_tenancy_account_type

        out["DedicatedTenancyAccountType"] = (
            capo_workspaces.types.dedicated_tenancy_account_type.serialize_aws_json_1_1(
                value["dedicated_tenancy_account_type"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAccountResult:
    out: DescribeAccountResult = {}  # type: ignore[typeddict-item]
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
    if data.get("DedicatedTenancyAccountType") is not None:
        import capo_workspaces.types.dedicated_tenancy_account_type

        out["dedicated_tenancy_account_type"] = (
            capo_workspaces.types.dedicated_tenancy_account_type.deserialize_aws_json_1_1(
                data["DedicatedTenancyAccountType"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeAccountResult) -> dict:
    out: dict = {}
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
    if "dedicated_tenancy_account_type" in value:
        import capo_workspaces.types.dedicated_tenancy_account_type

        out["DedicatedTenancyAccountType"] = (
            capo_workspaces.types.dedicated_tenancy_account_type.serialize_cbor(
                value["dedicated_tenancy_account_type"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_cbor(data: dict) -> DescribeAccountResult:
    out: DescribeAccountResult = {}  # type: ignore[typeddict-item]
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
    if data.get("DedicatedTenancyAccountType") is not None:
        import capo_workspaces.types.dedicated_tenancy_account_type

        out["dedicated_tenancy_account_type"] = (
            capo_workspaces.types.dedicated_tenancy_account_type.deserialize_cbor(
                data["DedicatedTenancyAccountType"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out
