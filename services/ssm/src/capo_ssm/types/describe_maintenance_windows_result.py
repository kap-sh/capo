"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeMaintenanceWindowsResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_identity_list
    import capo_ssm.types.next_token


class DescribeMaintenanceWindowsResult(TypedDict, closed=True):
    window_identities: NotRequired[
        "capo_ssm.types.maintenance_window_identity_list.MaintenanceWindowIdentityList"
    ]
    """<p>Information about the maintenance windows.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMaintenanceWindowsResult) -> dict:
    out: dict = {}
    if "window_identities" in value:
        import capo_ssm.types.maintenance_window_identity_list

        out["WindowIdentities"] = (
            capo_ssm.types.maintenance_window_identity_list.serialize_aws_json_1_1(
                value["window_identities"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMaintenanceWindowsResult:
    out: DescribeMaintenanceWindowsResult = {}  # type: ignore[typeddict-item]
    if data.get("WindowIdentities") is not None:
        import capo_ssm.types.maintenance_window_identity_list

        out["window_identities"] = (
            capo_ssm.types.maintenance_window_identity_list.deserialize_aws_json_1_1(
                data["WindowIdentities"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: DescribeMaintenanceWindowsResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "window_identities" in value:
        import capo_ssm.types.maintenance_window_identity_list

        out["window_identities"] = (
            capo_ssm.types.maintenance_window_identity_list.redact_sensitive(
                value["window_identities"]
            )
        )
    return out
