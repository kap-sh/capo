"""Generated from Smithy shape ``com.amazonaws.bedrockagent#S3Prefixes``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.s3_prefix

S3Prefixes: TypeAlias = list["capo_bedrock_agent.types.s3_prefix.S3Prefix"]


# --- restJson1 ser/de ---
def serialize_json(value: S3Prefixes) -> list:
    return list(value)


def deserialize_json(data: list) -> S3Prefixes:
    return [item for item in data if item is not None]


def redact_sensitive(value: S3Prefixes) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
