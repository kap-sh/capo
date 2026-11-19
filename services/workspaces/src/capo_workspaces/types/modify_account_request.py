"""Generated from Smithy shape ``com.amazonaws.workspaces#ModifyAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.dedicated_tenancy_management_cidr_range
    import capo_workspaces.types.dedicated_tenancy_support_enum


class ModifyAccountRequest(TypedDict, closed=True):
    dedicated_tenancy_support: NotRequired[
        "capo_workspaces.types.dedicated_tenancy_support_enum.DedicatedTenancySupportEnum"
    ]
    """<p>The status of BYOL.</p>"""
    dedicated_tenancy_management_cidr_range: NotRequired[
        "capo_workspaces.types.dedicated_tenancy_management_cidr_range.DedicatedTenancyManagementCidrRange"
    ]
    """<p>The IP address range, specified as an IPv4 CIDR block, for the management network interface. Specify an IP address range that is compatible with your network and in CIDR notation (that is, specify the range as an IPv4 CIDR block). The CIDR block size must be /16 (for example, 203.0.113.25/16). It must also be specified as available by the <code>ListAvailableManagementCidrRanges</code> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyAccountRequest) -> dict:
    out: dict = {}
    if "dedicated_tenancy_support" in value:
        import capo_workspaces.types.dedicated_tenancy_support_enum

        out["DedicatedTenancySupport"] = (
            capo_workspaces.types.dedicated_tenancy_support_enum.serialize_aws_json_1_1(
                value["dedicated_tenancy_support"]
            )
        )
    if "dedicated_tenancy_management_cidr_range" in value:
        out["DedicatedTenancyManagementCidrRange"] = value[
            "dedicated_tenancy_management_cidr_range"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyAccountRequest:
    out: ModifyAccountRequest = {}  # type: ignore[typeddict-item]
    if data.get("DedicatedTenancySupport") is not None:
        import capo_workspaces.types.dedicated_tenancy_support_enum

        out["dedicated_tenancy_support"] = (
            capo_workspaces.types.dedicated_tenancy_support_enum.deserialize_aws_json_1_1(
                data["DedicatedTenancySupport"]
            )
        )
    if data.get("DedicatedTenancyManagementCidrRange") is not None:
        out["dedicated_tenancy_management_cidr_range"] = data[
            "DedicatedTenancyManagementCidrRange"
        ]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ModifyAccountRequest) -> dict:
    out: dict = {}
    if "dedicated_tenancy_support" in value:
        import capo_workspaces.types.dedicated_tenancy_support_enum

        out["DedicatedTenancySupport"] = (
            capo_workspaces.types.dedicated_tenancy_support_enum.serialize_cbor(
                value["dedicated_tenancy_support"]
            )
        )
    if "dedicated_tenancy_management_cidr_range" in value:
        out["DedicatedTenancyManagementCidrRange"] = value[
            "dedicated_tenancy_management_cidr_range"
        ]
    return out


def deserialize_cbor(data: dict) -> ModifyAccountRequest:
    out: ModifyAccountRequest = {}  # type: ignore[typeddict-item]
    if data.get("DedicatedTenancySupport") is not None:
        import capo_workspaces.types.dedicated_tenancy_support_enum

        out["dedicated_tenancy_support"] = (
            capo_workspaces.types.dedicated_tenancy_support_enum.deserialize_cbor(
                data["DedicatedTenancySupport"]
            )
        )
    if data.get("DedicatedTenancyManagementCidrRange") is not None:
        out["dedicated_tenancy_management_cidr_range"] = data[
            "DedicatedTenancyManagementCidrRange"
        ]
    return out
