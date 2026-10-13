"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityAnalyzerResults``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.data_quality_analyzer_result

DataQualityAnalyzerResults: TypeAlias = list[
    "capo_glue.types.data_quality_analyzer_result.DataQualityAnalyzerResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityAnalyzerResults) -> list:
    import capo_glue.types.data_quality_analyzer_result

    out: list = []
    for item in value:
        out.append(
            capo_glue.types.data_quality_analyzer_result.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DataQualityAnalyzerResults:
    import capo_glue.types.data_quality_analyzer_result

    out: DataQualityAnalyzerResults = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_glue.types.data_quality_analyzer_result.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: DataQualityAnalyzerResults) -> list[Any]:
    import capo_glue.types.data_quality_analyzer_result

    return [
        capo_glue.types.data_quality_analyzer_result.redact_sensitive(item)
        for item in value
    ]
