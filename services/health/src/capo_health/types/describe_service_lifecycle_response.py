"""Generated from Smithy shape ``com.amazonaws.health#DescribeServiceLifecycleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.next_token
    import capo_health.types.service_lifecycle_list


class DescribeServiceLifecycleResponse(TypedDict, closed=True):
    service_lifecycles: NotRequired[
        "capo_health.types.service_lifecycle_list.ServiceLifecycleList"
    ]
    """<p>The list of service lifecycle entries matching the filter criteria.</p>"""
    next_token: NotRequired["capo_health.types.next_token.nextToken"]
    """<p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeServiceLifecycleResponse) -> dict:
    out: dict = {}
    if "service_lifecycles" in value:
        import capo_health.types.service_lifecycle_list

        out["serviceLifecycles"] = (
            capo_health.types.service_lifecycle_list.serialize_aws_json_1_1(
                value["service_lifecycles"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeServiceLifecycleResponse:
    out: DescribeServiceLifecycleResponse = {}  # type: ignore[typeddict-item]
    if data.get("serviceLifecycles") is not None:
        import capo_health.types.service_lifecycle_list

        out["service_lifecycles"] = (
            capo_health.types.service_lifecycle_list.deserialize_aws_json_1_1(
                data["serviceLifecycles"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
