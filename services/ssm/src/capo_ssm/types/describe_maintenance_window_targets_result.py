"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeMaintenanceWindowTargetsResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_target_list
    import capo_ssm.types.next_token


class DescribeMaintenanceWindowTargetsResult(TypedDict, closed=True):
    targets: NotRequired[
        "capo_ssm.types.maintenance_window_target_list.MaintenanceWindowTargetList"
    ]
    """<p>Information about the targets in the maintenance window.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMaintenanceWindowTargetsResult) -> dict:
    out: dict = {}
    if "targets" in value:
        import capo_ssm.types.maintenance_window_target_list

        out["Targets"] = (
            capo_ssm.types.maintenance_window_target_list.serialize_aws_json_1_1(
                value["targets"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMaintenanceWindowTargetsResult:
    out: DescribeMaintenanceWindowTargetsResult = {}  # type: ignore[typeddict-item]
    if data.get("Targets") is not None:
        import capo_ssm.types.maintenance_window_target_list

        out["targets"] = (
            capo_ssm.types.maintenance_window_target_list.deserialize_aws_json_1_1(
                data["Targets"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: DescribeMaintenanceWindowTargetsResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "targets" in value:
        import capo_ssm.types.maintenance_window_target_list

        out["targets"] = capo_ssm.types.maintenance_window_target_list.redact_sensitive(
            value["targets"]
        )
    return out
