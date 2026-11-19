"""Generated from Smithy shape ``com.amazonaws.cloudwatch#MetricDataQueryDefinitionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.metric_data_query_definition_summary

MetricDataQueryDefinitionSummaries: TypeAlias = list[
    "capo_cloudwatch.types.metric_data_query_definition_summary.MetricDataQueryDefinitionSummary"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricDataQueryDefinitionSummaries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.metric_data_query_definition_summary

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.metric_data_query_definition_summary.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> MetricDataQueryDefinitionSummaries:
    import capo_cloudwatch.types.metric_data_query_definition_summary

    out: MetricDataQueryDefinitionSummaries = []
    for child in el.findall("member"):
        out.append(
            capo_cloudwatch.types.metric_data_query_definition_summary.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: MetricDataQueryDefinitionSummaries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.metric_data_query_definition_summary

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.metric_data_query_definition_summary.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> MetricDataQueryDefinitionSummaries:
    import capo_cloudwatch.types.metric_data_query_definition_summary

    out: MetricDataQueryDefinitionSummaries = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudwatch.types.metric_data_query_definition_summary.deserialize_query(
                child
            )
        )
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricDataQueryDefinitionSummaries) -> list:
    import capo_cloudwatch.types.metric_data_query_definition_summary

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch.types.metric_data_query_definition_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> MetricDataQueryDefinitionSummaries:
    import capo_cloudwatch.types.metric_data_query_definition_summary

    out: MetricDataQueryDefinitionSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch.types.metric_data_query_definition_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
