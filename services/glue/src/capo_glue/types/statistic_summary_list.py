"""Generated from Smithy shape ``com.amazonaws.glue#StatisticSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.statistic_summary

StatisticSummaryList: TypeAlias = list[
    "capo_glue.types.statistic_summary.StatisticSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatisticSummaryList) -> list:
    import capo_glue.types.statistic_summary

    out: list = []
    for item in value:
        out.append(capo_glue.types.statistic_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StatisticSummaryList:
    import capo_glue.types.statistic_summary

    out: StatisticSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_glue.types.statistic_summary.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: StatisticSummaryList) -> list[Any]:
    import capo_glue.types.statistic_summary

    return [capo_glue.types.statistic_summary.redact_sensitive(item) for item in value]
