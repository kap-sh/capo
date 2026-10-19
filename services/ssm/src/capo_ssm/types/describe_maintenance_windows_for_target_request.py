"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeMaintenanceWindowsForTargetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_resource_type
    import capo_ssm.types.maintenance_window_search_max_results
    import capo_ssm.types.next_token
    import capo_ssm.types.targets


class DescribeMaintenanceWindowsForTargetRequest(TypedDict, closed=True):
    targets: "capo_ssm.types.targets.Targets"
    """<p>The managed node ID or key-value pair to retrieve information about.</p>"""
    resource_type: (
        "capo_ssm.types.maintenance_window_resource_type.MaintenanceWindowResourceType"
    )
    """<p>The type of resource you want to retrieve information about. For example, <code>INSTANCE</code>.</p>"""
    max_results: NotRequired[
        "capo_ssm.types.maintenance_window_search_max_results.MaintenanceWindowSearchMaxResults"
    ]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMaintenanceWindowsForTargetRequest) -> dict:
    out: dict = {}
    import capo_ssm.types.targets

    out["Targets"] = capo_ssm.types.targets.serialize_aws_json_1_1(value["targets"])
    import capo_ssm.types.maintenance_window_resource_type

    out["ResourceType"] = (
        capo_ssm.types.maintenance_window_resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMaintenanceWindowsForTargetRequest:
    out: DescribeMaintenanceWindowsForTargetRequest = {}  # type: ignore[typeddict-item]
    if data.get("Targets") is not None:
        import capo_ssm.types.targets

        out["targets"] = capo_ssm.types.targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    else:
        out["targets"] = []
    if data.get("ResourceType") is not None:
        import capo_ssm.types.maintenance_window_resource_type

        out["resource_type"] = (
            capo_ssm.types.maintenance_window_resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    else:
        import typing

        out["resource_type"] = typing.cast(
            "capo_ssm.types.maintenance_window_resource_type.MaintenanceWindowResourceType",
            "",
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
