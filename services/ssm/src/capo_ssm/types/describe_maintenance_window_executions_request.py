"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeMaintenanceWindowExecutionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_filter_list
    import capo_ssm.types.maintenance_window_id
    import capo_ssm.types.maintenance_window_max_results
    import capo_ssm.types.next_token


class DescribeMaintenanceWindowExecutionsRequest(TypedDict, closed=True):
    window_id: "capo_ssm.types.maintenance_window_id.MaintenanceWindowId"
    """<p>The ID of the maintenance window whose executions should be retrieved.</p>"""
    filters: NotRequired[
        "capo_ssm.types.maintenance_window_filter_list.MaintenanceWindowFilterList"
    ]
    """<p>Each entry in the array is a structure containing:</p> <ul> <li> <p>Key. A string between 1 and 128 characters. Supported keys include <code>ExecutedBefore</code> and <code>ExecutedAfter</code>.</p> </li> <li> <p>Values. An array of strings, each between 1 and 256 characters. Supported values are date/time strings in a valid ISO 8601 date/time format, such as <code>2024-11-04T05:00:00Z</code>.</p> </li> </ul>"""
    max_results: NotRequired[
        "capo_ssm.types.maintenance_window_max_results.MaintenanceWindowMaxResults"
    ]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMaintenanceWindowExecutionsRequest) -> dict:
    out: dict = {}
    out["WindowId"] = value["window_id"]
    if "filters" in value:
        import capo_ssm.types.maintenance_window_filter_list

        out["Filters"] = (
            capo_ssm.types.maintenance_window_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMaintenanceWindowExecutionsRequest:
    out: DescribeMaintenanceWindowExecutionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("WindowId") is not None:
        out["window_id"] = data["WindowId"]
    else:
        out["window_id"] = ""
    if data.get("Filters") is not None:
        import capo_ssm.types.maintenance_window_filter_list

        out["filters"] = (
            capo_ssm.types.maintenance_window_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
