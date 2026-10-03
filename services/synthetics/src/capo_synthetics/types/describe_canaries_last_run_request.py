"""Generated from Smithy shape ``com.amazonaws.synthetics#DescribeCanariesLastRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.browser_type
    import capo_synthetics.types.describe_canaries_last_run_name_filter
    import capo_synthetics.types.max_size100
    import capo_synthetics.types.token


class DescribeCanariesLastRunRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_synthetics.types.token.Token"]
    """<p>A token that indicates that there is more data available. You can use this token in a subsequent <code>DescribeCanariesLastRun</code> operation to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_synthetics.types.max_size100.MaxSize100"]
    """<p>Specify this parameter to limit how many runs are returned each time you use the <code>DescribeLastRun</code> operation. If you omit this parameter, the default of 100 is used.</p>"""
    names: NotRequired[
        "capo_synthetics.types.describe_canaries_last_run_name_filter.DescribeCanariesLastRunNameFilter"
    ]
    """<p>Use this parameter to return only canaries that match the names that you specify here. You can specify as many as five canary names.</p> <p>If you specify this parameter, the operation is successful only if you have authorization to view all the canaries that you specify in your request. If you do not have permission to view any of the canaries, the request fails with a 403 response.</p> <p>You are required to use the <code>Names</code> parameter if you are logged on to a user or role that has an IAM policy that restricts which canaries that you are allowed to view. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Restricted.html"> Limiting a user to viewing specific canaries</a>.</p>"""
    browser_type: NotRequired["capo_synthetics.types.browser_type.BrowserType"]
    """<p>The type of browser to use for the canary run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCanariesLastRunRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "names" in value:
        import capo_synthetics.types.describe_canaries_last_run_name_filter

        out["Names"] = (
            capo_synthetics.types.describe_canaries_last_run_name_filter.serialize_json(
                value["names"]
            )
        )
    if "browser_type" in value:
        import capo_synthetics.types.browser_type

        out["BrowserType"] = capo_synthetics.types.browser_type.serialize_json(
            value["browser_type"]
        )
    return out


def deserialize_json(data: dict) -> DescribeCanariesLastRunRequest:
    out: DescribeCanariesLastRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("Names") is not None:
        import capo_synthetics.types.describe_canaries_last_run_name_filter

        out["names"] = (
            capo_synthetics.types.describe_canaries_last_run_name_filter.deserialize_json(
                data["Names"]
            )
        )
    if data.get("BrowserType") is not None:
        import capo_synthetics.types.browser_type

        out["browser_type"] = capo_synthetics.types.browser_type.deserialize_json(
            data["BrowserType"]
        )
    return out
