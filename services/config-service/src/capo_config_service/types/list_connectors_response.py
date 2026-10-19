"""Generated from Smithy shape ``com.amazonaws.configservice#ListConnectorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.connector_summaries
    import capo_config_service.types.string


class ListConnectorsResponse(TypedDict, closed=True):
    connector_summaries: (
        "capo_config_service.types.connector_summaries.ConnectorSummaries"
    )
    """<p>A list of <code>ConnectorSummary</code> objects.</p>"""
    next_token: NotRequired["capo_config_service.types.string.String"]
    """<p>The <code>NextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListConnectorsResponse) -> dict:
    out: dict = {}
    import capo_config_service.types.connector_summaries

    out["ConnectorSummaries"] = (
        capo_config_service.types.connector_summaries.serialize_aws_json_1_1(
            value["connector_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListConnectorsResponse:
    out: ListConnectorsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ConnectorSummaries") is not None:
        import capo_config_service.types.connector_summaries

        out["connector_summaries"] = (
            capo_config_service.types.connector_summaries.deserialize_aws_json_1_1(
                data["ConnectorSummaries"]
            )
        )
    else:
        out["connector_summaries"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
