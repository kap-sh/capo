"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DescribeExportConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.export_ids
    import capo_application_discovery_service.types.integer
    import capo_application_discovery_service.types.next_token


class DescribeExportConfigurationsRequest(TypedDict, closed=True):
    export_ids: NotRequired[
        "capo_application_discovery_service.types.export_ids.ExportIds"
    ]
    """<p>A list of continuous export IDs to search for.</p>"""
    max_results: NotRequired["capo_application_discovery_service.types.integer.Integer"]
    """<p>A number between 1 and 100 specifying the maximum number of continuous export descriptions returned.</p>"""
    next_token: NotRequired[
        "capo_application_discovery_service.types.next_token.NextToken"
    ]
    """<p>The token from the previous call to describe-export-tasks.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeExportConfigurationsRequest) -> dict:
    out: dict = {}
    if "export_ids" in value:
        import capo_application_discovery_service.types.export_ids

        out["exportIds"] = (
            capo_application_discovery_service.types.export_ids.serialize_aws_json_1_1(
                value["export_ids"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeExportConfigurationsRequest:
    out: DescribeExportConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("exportIds") is not None:
        import capo_application_discovery_service.types.export_ids

        out["export_ids"] = (
            capo_application_discovery_service.types.export_ids.deserialize_aws_json_1_1(
                data["exportIds"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
