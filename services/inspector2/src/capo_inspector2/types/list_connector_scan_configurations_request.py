"""Generated from Smithy shape ``com.amazonaws.inspector2#ListConnectorScanConfigurationsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.aws_config_connector_arn_list
    import capo_inspector2.types.connector_next_token
    import capo_inspector2.types.list_connector_scan_configurations_max_results


class ListConnectorScanConfigurationsRequest(TypedDict, closed=True):
    aws_config_connector_arns: NotRequired[
        "capo_inspector2.types.aws_config_connector_arn_list.AwsConfigConnectorArnList"
    ]
    """<p>The list of Amazon Web Services Config connector ARNs to filter results.</p>"""
    max_results: NotRequired[
        "capo_inspector2.types.list_connector_scan_configurations_max_results.ListConnectorScanConfigurationsMaxResults"
    ]
    """<p>The maximum number of results to return in a single call. Valid range is 1 to 50. To retrieve the remaining results, make another request with the <code>nextToken</code> value returned from this request.</p>"""
    next_token: NotRequired[
        "capo_inspector2.types.connector_next_token.ConnectorNextToken"
    ]
    """<p>A token to use for paginating results. Set this value to null for the first request. For subsequent calls, use the <code>nextToken</code> value returned from the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorScanConfigurationsRequest) -> dict:
    out: dict = {}
    if "aws_config_connector_arns" in value:
        import capo_inspector2.types.aws_config_connector_arn_list

        out["awsConfigConnectorArns"] = (
            capo_inspector2.types.aws_config_connector_arn_list.serialize_json(
                value["aws_config_connector_arns"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConnectorScanConfigurationsRequest:
    out: ListConnectorScanConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("awsConfigConnectorArns") is not None:
        import capo_inspector2.types.aws_config_connector_arn_list

        out["aws_config_connector_arns"] = (
            capo_inspector2.types.aws_config_connector_arn_list.deserialize_json(
                data["awsConfigConnectorArns"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListConnectorScanConfigurationsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
