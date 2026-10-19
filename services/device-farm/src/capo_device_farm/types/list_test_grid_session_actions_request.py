"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListTestGridSessionActionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.device_farm_arn
    import capo_device_farm.types.max_page_size
    import capo_device_farm.types.pagination_token


class ListTestGridSessionActionsRequest(TypedDict, closed=True):
    session_arn: "capo_device_farm.types.device_farm_arn.DeviceFarmArn"
    """<p>The ARN of the session to retrieve.</p>"""
    max_result: NotRequired["capo_device_farm.types.max_page_size.MaxPageSize"]
    """<p>The maximum number of sessions to return per response.</p>"""
    next_token: NotRequired["capo_device_farm.types.pagination_token.PaginationToken"]
    """<p>Pagination token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTestGridSessionActionsRequest) -> dict:
    out: dict = {}
    out["sessionArn"] = value["session_arn"]
    if "max_result" in value:
        out["maxResult"] = value["max_result"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTestGridSessionActionsRequest:
    out: ListTestGridSessionActionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("sessionArn") is not None:
        out["session_arn"] = data["sessionArn"]
    else:
        out["session_arn"] = ""
    if data.get("maxResult") is not None:
        out["max_result"] = data["maxResult"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
