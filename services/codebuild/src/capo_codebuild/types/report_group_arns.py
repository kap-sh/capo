"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportGroupArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string

ReportGroupArns: TypeAlias = list[
    "capo_codebuild.types.non_empty_string.NonEmptyString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportGroupArns) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ReportGroupArns:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReportGroupArns) -> list:
    return list(value)


def deserialize_cbor(data: list) -> ReportGroupArns:
    return [item for item in data if item is not None]
