"""Generated from Smithy shape ``com.amazonaws.inspector2#LambdaFunctionAggregationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.account_id
    import capo_inspector2.types.date_time_timestamp
    import capo_inspector2.types.non_empty_string
    import capo_inspector2.types.severity_counts
    import capo_inspector2.types.tag_map


class LambdaFunctionAggregationResponse(TypedDict, closed=True):
    resource_id: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The resource IDs included in the aggregation results.</p>"""
    function_name: NotRequired["str"]
    """<p>The Amazon Web Services Lambda function names included in the aggregation results.</p>"""
    runtime: NotRequired["str"]
    """<p>The runtimes included in the aggregation results.</p>"""
    lambda_tags: NotRequired["capo_inspector2.types.tag_map.TagMap"]
    """<p>The tags included in the aggregation results.</p>"""
    account_id: NotRequired["capo_inspector2.types.account_id.AccountId"]
    """<p>The ID of the Amazon Web Services account that owns the Amazon Web Services Lambda function. </p>"""
    severity_counts: NotRequired["capo_inspector2.types.severity_counts.SeverityCounts"]
    """<p>An object that contains the counts of aggregated finding per severity.</p>"""
    last_modified_at: NotRequired[
        "capo_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The date that the Amazon Web Services Lambda function included in the aggregation results was last changed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaFunctionAggregationResponse) -> dict:
    out: dict = {}
    out["resourceId"] = value["resource_id"]
    if "function_name" in value:
        out["functionName"] = value["function_name"]
    if "runtime" in value:
        out["runtime"] = value["runtime"]
    if "lambda_tags" in value:
        import capo_inspector2.types.tag_map

        out["lambdaTags"] = capo_inspector2.types.tag_map.serialize_json(
            value["lambda_tags"]
        )
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "severity_counts" in value:
        import capo_inspector2.types.severity_counts

        out["severityCounts"] = capo_inspector2.types.severity_counts.serialize_json(
            value["severity_counts"]
        )
    if "last_modified_at" in value:
        import capo_inspector2.types.date_time_timestamp

        out["lastModifiedAt"] = (
            capo_inspector2.types.date_time_timestamp.serialize_json(
                value["last_modified_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> LambdaFunctionAggregationResponse:
    out: LambdaFunctionAggregationResponse = {}  # type: ignore[typeddict-item]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        out["resource_id"] = ""
    if data.get("functionName") is not None:
        out["function_name"] = data["functionName"]
    if data.get("runtime") is not None:
        out["runtime"] = data["runtime"]
    if data.get("lambdaTags") is not None:
        import capo_inspector2.types.tag_map

        out["lambda_tags"] = capo_inspector2.types.tag_map.deserialize_json(
            data["lambdaTags"]
        )
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("severityCounts") is not None:
        import capo_inspector2.types.severity_counts

        out["severity_counts"] = capo_inspector2.types.severity_counts.deserialize_json(
            data["severityCounts"]
        )
    if data.get("lastModifiedAt") is not None:
        import capo_inspector2.types.date_time_timestamp

        out["last_modified_at"] = (
            capo_inspector2.types.date_time_timestamp.deserialize_json(
                data["lastModifiedAt"]
            )
        )
    return out
