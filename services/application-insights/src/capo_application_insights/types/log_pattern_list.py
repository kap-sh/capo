"""Generated from Smithy shape ``com.amazonaws.applicationinsights#LogPatternList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_insights.types.log_pattern

LogPatternList: TypeAlias = list[
    "capo_application_insights.types.log_pattern.LogPattern"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogPatternList) -> list:
    import capo_application_insights.types.log_pattern

    out: list = []
    for item in value:
        out.append(
            capo_application_insights.types.log_pattern.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LogPatternList:
    import capo_application_insights.types.log_pattern

    out: LogPatternList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_application_insights.types.log_pattern.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LogPatternList) -> list:
    import capo_application_insights.types.log_pattern

    out: list = []
    for item in value:
        out.append(capo_application_insights.types.log_pattern.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> LogPatternList:
    import capo_application_insights.types.log_pattern

    out: LogPatternList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_application_insights.types.log_pattern.deserialize_cbor(item))
    return out
