"""Generated from Smithy shape ``com.amazonaws.codebuild#LanguageType``."""

from typing import Literal, TypeAlias, cast

LanguageType: TypeAlias = Literal[
    "JAVA",
    "PYTHON",
    "NODE_JS",
    "RUBY",
    "GOLANG",
    "DOCKER",
    "ANDROID",
    "DOTNET",
    "BASE",
    "PHP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LanguageType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LanguageType:
    return cast(LanguageType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LanguageType) -> str:
    return value


def deserialize_cbor(data: str) -> LanguageType:
    return cast(LanguageType, data)
