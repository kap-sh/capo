"""Generated from Smithy shape ``com.amazonaws.inspector2#LambdaLayerAggregationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.account_id
    import capo_inspector2.types.non_empty_string
    import capo_inspector2.types.severity_counts


class LambdaLayerAggregationResponse(TypedDict, closed=True):
    function_name: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The names of the Amazon Web Services Lambda functions associated with the layers.</p>"""
    resource_id: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The Resource ID of the Amazon Web Services Lambda function layer.</p>"""
    layer_arn: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Lambda function layer.</p>"""
    account_id: "capo_inspector2.types.account_id.AccountId"
    """<p>The account ID of the Amazon Web Services Lambda function layer.</p>"""
    severity_counts: NotRequired["capo_inspector2.types.severity_counts.SeverityCounts"]
    """<p>An object that contains the counts of aggregated finding per severity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaLayerAggregationResponse) -> dict:
    out: dict = {}
    out["functionName"] = value["function_name"]
    out["resourceId"] = value["resource_id"]
    out["layerArn"] = value["layer_arn"]
    out["accountId"] = value["account_id"]
    if "severity_counts" in value:
        import capo_inspector2.types.severity_counts

        out["severityCounts"] = capo_inspector2.types.severity_counts.serialize_json(
            value["severity_counts"]
        )
    return out


def deserialize_json(data: dict) -> LambdaLayerAggregationResponse:
    out: LambdaLayerAggregationResponse = {}  # type: ignore[typeddict-item]
    if data.get("functionName") is not None:
        out["function_name"] = data["functionName"]
    else:
        out["function_name"] = ""
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        out["resource_id"] = ""
    if data.get("layerArn") is not None:
        out["layer_arn"] = data["layerArn"]
    else:
        out["layer_arn"] = ""
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("severityCounts") is not None:
        import capo_inspector2.types.severity_counts

        out["severity_counts"] = capo_inspector2.types.severity_counts.deserialize_json(
            data["severityCounts"]
        )
    return out
