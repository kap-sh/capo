"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListTestGridSessionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.date_time
    import capo_device_farm.types.device_farm_arn
    import capo_device_farm.types.max_page_size
    import capo_device_farm.types.pagination_token
    import capo_device_farm.types.test_grid_session_status


class ListTestGridSessionsRequest(TypedDict, closed=True):
    project_arn: "capo_device_farm.types.device_farm_arn.DeviceFarmArn"
    """<p>ARN of a <a>TestGridProject</a>.</p>"""
    status: NotRequired[
        "capo_device_farm.types.test_grid_session_status.TestGridSessionStatus"
    ]
    """<p>Return only sessions in this state.</p>"""
    creation_time_after: NotRequired["capo_device_farm.types.date_time.DateTime"]
    """<p>Return only sessions created after this time.</p>"""
    creation_time_before: NotRequired["capo_device_farm.types.date_time.DateTime"]
    """<p>Return only sessions created before this time.</p>"""
    end_time_after: NotRequired["capo_device_farm.types.date_time.DateTime"]
    """<p>Return only sessions that ended after this time.</p>"""
    end_time_before: NotRequired["capo_device_farm.types.date_time.DateTime"]
    """<p>Return only sessions that ended before this time.</p>"""
    max_result: NotRequired["capo_device_farm.types.max_page_size.MaxPageSize"]
    """<p>Return only this many results at a time.</p>"""
    next_token: NotRequired["capo_device_farm.types.pagination_token.PaginationToken"]
    """<p>Pagination token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTestGridSessionsRequest) -> dict:
    out: dict = {}
    out["projectArn"] = value["project_arn"]
    if "status" in value:
        import capo_device_farm.types.test_grid_session_status

        out["status"] = (
            capo_device_farm.types.test_grid_session_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "creation_time_after" in value:
        import capo_device_farm.types.date_time

        out["creationTimeAfter"] = (
            capo_device_farm.types.date_time.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    if "creation_time_before" in value:
        import capo_device_farm.types.date_time

        out["creationTimeBefore"] = (
            capo_device_farm.types.date_time.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    if "end_time_after" in value:
        import capo_device_farm.types.date_time

        out["endTimeAfter"] = capo_device_farm.types.date_time.serialize_aws_json_1_1(
            value["end_time_after"]
        )
    if "end_time_before" in value:
        import capo_device_farm.types.date_time

        out["endTimeBefore"] = capo_device_farm.types.date_time.serialize_aws_json_1_1(
            value["end_time_before"]
        )
    if "max_result" in value:
        out["maxResult"] = value["max_result"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTestGridSessionsRequest:
    out: ListTestGridSessionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("projectArn") is not None:
        out["project_arn"] = data["projectArn"]
    else:
        out["project_arn"] = ""
    if data.get("status") is not None:
        import capo_device_farm.types.test_grid_session_status

        out["status"] = (
            capo_device_farm.types.test_grid_session_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("creationTimeAfter") is not None:
        import capo_device_farm.types.date_time

        out["creation_time_after"] = (
            capo_device_farm.types.date_time.deserialize_aws_json_1_1(
                data["creationTimeAfter"]
            )
        )
    if data.get("creationTimeBefore") is not None:
        import capo_device_farm.types.date_time

        out["creation_time_before"] = (
            capo_device_farm.types.date_time.deserialize_aws_json_1_1(
                data["creationTimeBefore"]
            )
        )
    if data.get("endTimeAfter") is not None:
        import capo_device_farm.types.date_time

        out["end_time_after"] = (
            capo_device_farm.types.date_time.deserialize_aws_json_1_1(
                data["endTimeAfter"]
            )
        )
    if data.get("endTimeBefore") is not None:
        import capo_device_farm.types.date_time

        out["end_time_before"] = (
            capo_device_farm.types.date_time.deserialize_aws_json_1_1(
                data["endTimeBefore"]
            )
        )
    if data.get("maxResult") is not None:
        out["max_result"] = data["maxResult"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
