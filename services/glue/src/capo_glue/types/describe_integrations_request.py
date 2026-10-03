"""Generated from Smithy shape ``com.amazonaws.glue#DescribeIntegrationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.integration_filter_list
    import capo_glue.types.integration_integer
    import capo_glue.types.string128


class DescribeIntegrationsRequest(TypedDict, closed=True):
    integration_identifier: NotRequired["capo_glue.types.string128.String128"]
    """<p>The Amazon Resource Name (ARN) for the integration.</p>"""
    marker: NotRequired["capo_glue.types.string128.String128"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request.</p>"""
    max_records: NotRequired["capo_glue.types.integration_integer.IntegrationInteger"]
    """<p>The total number of items to return in the output.</p>"""
    filters: NotRequired[
        "capo_glue.types.integration_filter_list.IntegrationFilterList"
    ]
    """<p>A list of key and values, to filter down the results. Supported keys are "Status", "IntegrationName", and "SourceArn". IntegrationName is limited to only one value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeIntegrationsRequest) -> dict:
    out: dict = {}
    if "integration_identifier" in value:
        out["IntegrationIdentifier"] = value["integration_identifier"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "max_records" in value:
        out["MaxRecords"] = value["max_records"]
    if "filters" in value:
        import capo_glue.types.integration_filter_list

        out["Filters"] = capo_glue.types.integration_filter_list.serialize_aws_json_1_1(
            value["filters"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeIntegrationsRequest:
    out: DescribeIntegrationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("IntegrationIdentifier") is not None:
        out["integration_identifier"] = data["IntegrationIdentifier"]
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    if data.get("MaxRecords") is not None:
        out["max_records"] = data["MaxRecords"]
    if data.get("Filters") is not None:
        import capo_glue.types.integration_filter_list

        out["filters"] = (
            capo_glue.types.integration_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    return out
