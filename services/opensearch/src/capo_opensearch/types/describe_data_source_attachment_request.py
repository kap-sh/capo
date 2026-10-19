"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeDataSourceAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.arn
    import capo_opensearch.types.id


class DescribeDataSourceAttachmentRequest(TypedDict, closed=True):
    id: "capo_opensearch.types.id.Id"
    """<p>The unique identifier or name of the OpenSearch application.</p>"""
    data_source_arn: "capo_opensearch.types.arn.ARN"


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDataSourceAttachmentRequest) -> dict:
    out: dict = {}
    out["dataSourceArn"] = value["data_source_arn"]
    return out


def deserialize_json(data: dict) -> DescribeDataSourceAttachmentRequest:
    out: DescribeDataSourceAttachmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("dataSourceArn") is not None:
        out["data_source_arn"] = data["dataSourceArn"]
    else:
        out["data_source_arn"] = ""
    return out
