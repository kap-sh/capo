"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DeleteMetricDataQueryDefinitionOutput``."""

from typing_extensions import TypedDict

from capo_cloudwatch._protocol.xml import Element


class DeleteMetricDataQueryDefinitionOutput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteMetricDataQueryDefinitionOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteMetricDataQueryDefinitionOutput:
    out: DeleteMetricDataQueryDefinitionOutput = {}  # type: ignore[typeddict-item]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteMetricDataQueryDefinitionOutput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pass


def deserialize_query(el: Element) -> DeleteMetricDataQueryDefinitionOutput:
    out: DeleteMetricDataQueryDefinitionOutput = {}  # type: ignore[typeddict-item]
    return out
