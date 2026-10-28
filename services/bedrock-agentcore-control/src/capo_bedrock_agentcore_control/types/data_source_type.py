"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DataSourceType``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.inline_examples_source
    import capo_bedrock_agentcore_control.types.s3_source


class DataSourceTypeInlineExamplesMember(TypedDict, closed=True):
    inlineExamples: "capo_bedrock_agentcore_control.types.inline_examples_source.InlineExamplesSource"


class DataSourceTypeS3SourceMember(TypedDict, closed=True):
    s3Source: "capo_bedrock_agentcore_control.types.s3_source.S3Source"


DataSourceType: TypeAlias = (
    DataSourceTypeInlineExamplesMember
    | DataSourceTypeS3SourceMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceType) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DataSourceType: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "inlineExamples" in value:
        import capo_bedrock_agentcore_control.types.inline_examples_source

        return {
            "inlineExamples": capo_bedrock_agentcore_control.types.inline_examples_source.serialize_json(
                value["inlineExamples"]
            )
        }
    elif "s3Source" in value:
        import capo_bedrock_agentcore_control.types.s3_source

        return {
            "s3Source": capo_bedrock_agentcore_control.types.s3_source.serialize_json(
                value["s3Source"]
            )
        }
    else:
        raise SerializationError("DataSourceType: no variant present")


def deserialize_json(data: dict) -> DataSourceType:
    if data.get("inlineExamples") is not None:
        import capo_bedrock_agentcore_control.types.inline_examples_source

        return {
            "inlineExamples": capo_bedrock_agentcore_control.types.inline_examples_source.deserialize_json(
                data["inlineExamples"]
            )
        }
    elif data.get("s3Source") is not None:
        import capo_bedrock_agentcore_control.types.s3_source

        return {
            "s3Source": capo_bedrock_agentcore_control.types.s3_source.deserialize_json(
                data["s3Source"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("DataSourceType: no recognized variant key")


def redact_sensitive(value: DataSourceType) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "inlineExamples" in value:
        import capo_bedrock_agentcore_control.types.inline_examples_source

        out["inlineExamples"] = (
            capo_bedrock_agentcore_control.types.inline_examples_source.redact_sensitive(
                value["inlineExamples"]
            )
        )
    return out
