"""Generated from Smithy shape ``com.amazonaws.codebuild#ProjectVisibilityType``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies the visibility of the project's builds. Possible values are:</p> <dl> <dt>PUBLIC_READ</dt> <dd> <p>The project builds are visible to the public.</p> </dd> <dt>PRIVATE</dt> <dd> <p>The project builds are not visible to the public.</p> </dd> </dl>"""
ProjectVisibilityType: TypeAlias = Literal[
    "PUBLIC_READ",
    "PRIVATE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectVisibilityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProjectVisibilityType:
    return cast(ProjectVisibilityType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProjectVisibilityType) -> str:
    return value


def deserialize_cbor(data: str) -> ProjectVisibilityType:
    return cast(ProjectVisibilityType, data)
