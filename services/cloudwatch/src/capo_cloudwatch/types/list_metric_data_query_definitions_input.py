"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ListMetricDataQueryDefinitionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.max_results
    import capo_cloudwatch.types.metric_data_query_definition_next_token


class ListMetricDataQueryDefinitionsInput(TypedDict, closed=True):
    max_results: NotRequired["capo_cloudwatch.types.max_results.MaxResults"]
    """<p>The maximum number of metric data query definitions to return in one call. The default is 100.</p>"""
    next_token: NotRequired[
        "capo_cloudwatch.types.metric_data_query_definition_next_token.MetricDataQueryDefinitionNextToken"
    ]
    """<p>The token returned by a previous call to indicate where to continue retrieving results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListMetricDataQueryDefinitionsInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListMetricDataQueryDefinitionsInput:
    out: ListMetricDataQueryDefinitionsInput = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: ListMetricDataQueryDefinitionsInput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListMetricDataQueryDefinitionsInput:
    out: ListMetricDataQueryDefinitionsInput = {}  # type: ignore[typeddict-item]
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListMetricDataQueryDefinitionsInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListMetricDataQueryDefinitionsInput:
    out: ListMetricDataQueryDefinitionsInput = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
