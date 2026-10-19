"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListTestGridSessionArtifactsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.device_farm_arn
    import capo_device_farm.types.max_page_size
    import capo_device_farm.types.pagination_token
    import capo_device_farm.types.test_grid_session_artifact_category


class ListTestGridSessionArtifactsRequest(TypedDict, closed=True):
    session_arn: "capo_device_farm.types.device_farm_arn.DeviceFarmArn"
    """<p>The ARN of a <a>TestGridSession</a>. </p>"""
    type: NotRequired[
        "capo_device_farm.types.test_grid_session_artifact_category.TestGridSessionArtifactCategory"
    ]
    """<p>Limit results to a specified type of artifact.</p>"""
    max_result: NotRequired["capo_device_farm.types.max_page_size.MaxPageSize"]
    """<p>The maximum number of results to be returned by a request.</p>"""
    next_token: NotRequired["capo_device_farm.types.pagination_token.PaginationToken"]
    """<p>Pagination token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTestGridSessionArtifactsRequest) -> dict:
    out: dict = {}
    out["sessionArn"] = value["session_arn"]
    if "type" in value:
        import capo_device_farm.types.test_grid_session_artifact_category

        out["type"] = (
            capo_device_farm.types.test_grid_session_artifact_category.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "max_result" in value:
        out["maxResult"] = value["max_result"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTestGridSessionArtifactsRequest:
    out: ListTestGridSessionArtifactsRequest = {}  # type: ignore[typeddict-item]
    if data.get("sessionArn") is not None:
        out["session_arn"] = data["sessionArn"]
    else:
        out["session_arn"] = ""
    if data.get("type") is not None:
        import capo_device_farm.types.test_grid_session_artifact_category

        out["type"] = (
            capo_device_farm.types.test_grid_session_artifact_category.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    if data.get("maxResult") is not None:
        out["max_result"] = data["maxResult"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
