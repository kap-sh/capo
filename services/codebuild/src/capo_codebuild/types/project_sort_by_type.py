"""Generated from Smithy shape ``com.amazonaws.codebuild#ProjectSortByType``."""

from typing import Literal, TypeAlias, cast

ProjectSortByType: TypeAlias = Literal[
    "NAME",
    "CREATED_TIME",
    "LAST_MODIFIED_TIME",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectSortByType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProjectSortByType:
    return cast(ProjectSortByType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProjectSortByType) -> str:
    return value


def deserialize_cbor(data: str) -> ProjectSortByType:
    return cast(ProjectSortByType, data)
