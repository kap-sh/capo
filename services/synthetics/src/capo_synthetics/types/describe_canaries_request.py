"""Generated from Smithy shape ``com.amazonaws.synthetics#DescribeCanariesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.describe_canaries_name_filter
    import capo_synthetics.types.max_canary_results
    import capo_synthetics.types.token


class DescribeCanariesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_synthetics.types.token.Token"]
    """<p>A token that indicates that there is more data available. You can use this token in a subsequent operation to retrieve the next set of results.</p>"""
    max_results: NotRequired[
        "capo_synthetics.types.max_canary_results.MaxCanaryResults"
    ]
    """<p>Specify this parameter to limit how many canaries are returned each time you use the <code>DescribeCanaries</code> operation. If you omit this parameter, the default of 20 is used.</p>"""
    names: NotRequired[
        "capo_synthetics.types.describe_canaries_name_filter.DescribeCanariesNameFilter"
    ]
    """<p>Use this parameter to return only canaries that match the names that you specify here. You can specify as many as five canary names.</p> <p>If you specify this parameter, the operation is successful only if you have authorization to view all the canaries that you specify in your request. If you do not have permission to view any of the canaries, the request fails with a 403 response.</p> <p>You are required to use this parameter if you are logged on to a user or role that has an IAM policy that restricts which canaries that you are allowed to view. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Restricted.html"> Limiting a user to viewing specific canaries</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCanariesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "names" in value:
        import capo_synthetics.types.describe_canaries_name_filter

        out["Names"] = (
            capo_synthetics.types.describe_canaries_name_filter.serialize_json(
                value["names"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeCanariesRequest:
    out: DescribeCanariesRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("Names") is not None:
        import capo_synthetics.types.describe_canaries_name_filter

        out["names"] = (
            capo_synthetics.types.describe_canaries_name_filter.deserialize_json(
                data["Names"]
            )
        )
    return out
