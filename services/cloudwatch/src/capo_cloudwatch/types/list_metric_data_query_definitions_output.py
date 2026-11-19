"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ListMetricDataQueryDefinitionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.metric_data_query_definition_next_token
    import capo_cloudwatch.types.metric_data_query_definition_summaries


class ListMetricDataQueryDefinitionsOutput(TypedDict, closed=True):
    items: NotRequired[
        "capo_cloudwatch.types.metric_data_query_definition_summaries.MetricDataQueryDefinitionSummaries"
    ]
    """<p>A list of metric data query definition summaries.</p>"""
    next_token: NotRequired[
        "capo_cloudwatch.types.metric_data_query_definition_next_token.MetricDataQueryDefinitionNextToken"
    ]
    """<p>The token to use when requesting the next set of results. If this field is absent, there are no more results to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListMetricDataQueryDefinitionsOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_cloudwatch.types.metric_data_query_definition_summaries

        out["Items"] = (
            capo_cloudwatch.types.metric_data_query_definition_summaries.serialize_aws_json_1_0(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListMetricDataQueryDefinitionsOutput:
    out: ListMetricDataQueryDefinitionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Items") is not None:
        import capo_cloudwatch.types.metric_data_query_definition_summaries

        out["items"] = (
            capo_cloudwatch.types.metric_data_query_definition_summaries.deserialize_aws_json_1_0(
                data["Items"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: ListMetricDataQueryDefinitionsOutput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "items" in value:
        import capo_cloudwatch.types.metric_data_query_definition_summaries

        capo_cloudwatch.types.metric_data_query_definition_summaries.serialize_query(
            value["items"], pairs, f"{key_prefix}Items"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListMetricDataQueryDefinitionsOutput:
    out: ListMetricDataQueryDefinitionsOutput = {}  # type: ignore[typeddict-item]
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudwatch.types.metric_data_query_definition_summaries

        out["items"] = (
            capo_cloudwatch.types.metric_data_query_definition_summaries.deserialize_query(
                child_items
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListMetricDataQueryDefinitionsOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_cloudwatch.types.metric_data_query_definition_summaries

        out["Items"] = (
            capo_cloudwatch.types.metric_data_query_definition_summaries.serialize_cbor(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListMetricDataQueryDefinitionsOutput:
    out: ListMetricDataQueryDefinitionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Items") is not None:
        import capo_cloudwatch.types.metric_data_query_definition_summaries

        out["items"] = (
            capo_cloudwatch.types.metric_data_query_definition_summaries.deserialize_cbor(
                data["Items"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
