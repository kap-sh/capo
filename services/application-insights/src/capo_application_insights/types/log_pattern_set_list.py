"""Generated from Smithy shape ``com.amazonaws.applicationinsights#LogPatternSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_insights.types.log_pattern_set_name

LogPatternSetList: TypeAlias = list[
    "capo_application_insights.types.log_pattern_set_name.LogPatternSetName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogPatternSetList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> LogPatternSetList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LogPatternSetList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> LogPatternSetList:
    return [item for item in data if item is not None]
