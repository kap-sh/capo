"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#OutputFormat``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.output_format_structure
    import capo_bedrock_runtime.types.output_format_type


class OutputFormat(TypedDict, closed=True):
    type: "capo_bedrock_runtime.types.output_format_type.OutputFormatType"
    """<p> The type of structured output format. </p>"""
    structure: (
        "capo_bedrock_runtime.types.output_format_structure.OutputFormatStructure"
    )
    """<p> The structure that the model's output must adhere to. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputFormat) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.output_format_type

    out["type"] = capo_bedrock_runtime.types.output_format_type.serialize_json(
        value["type"]
    )
    import capo_bedrock_runtime.types.output_format_structure

    out["structure"] = (
        capo_bedrock_runtime.types.output_format_structure.serialize_json(
            value["structure"]
        )
    )
    return out


def deserialize_json(data: dict) -> OutputFormat:
    out: OutputFormat = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_runtime.types.output_format_type

        out["type"] = capo_bedrock_runtime.types.output_format_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_runtime.types.output_format_type.OutputFormatType", ""
        )
    if data.get("structure") is not None:
        import capo_bedrock_runtime.types.output_format_structure

        out["structure"] = (
            capo_bedrock_runtime.types.output_format_structure.deserialize_json(
                data["structure"]
            )
        )
    else:
        import capo_bedrock_runtime.types._unknown

        out["structure"] = capo_bedrock_runtime.types._unknown.UnknownUnionMember("")
    return out


def redact_sensitive(value: OutputFormat) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "structure" in value:
        out["structure"] = "*** Sensitive Data Redacted ***"
    return out
