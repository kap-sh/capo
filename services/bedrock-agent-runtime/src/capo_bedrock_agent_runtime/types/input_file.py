"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InputFile``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.file_source
    import capo_bedrock_agent_runtime.types.file_use_case


class InputFile(TypedDict, closed=True):
    name: "str"
    """<p>The name of the source file.</p>"""
    source: "capo_bedrock_agent_runtime.types.file_source.FileSource"
    """<p>Specifies where the files are located.</p>"""
    use_case: "capo_bedrock_agent_runtime.types.file_use_case.FileUseCase"
    """<p>Specifies how the source files will be used by the code interpreter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputFile) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_bedrock_agent_runtime.types.file_source

    out["source"] = capo_bedrock_agent_runtime.types.file_source.serialize_json(
        value["source"]
    )
    import capo_bedrock_agent_runtime.types.file_use_case

    out["useCase"] = capo_bedrock_agent_runtime.types.file_use_case.serialize_json(
        value["use_case"]
    )
    return out


def deserialize_json(data: dict) -> InputFile:
    out: InputFile = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("source") is not None:
        import capo_bedrock_agent_runtime.types.file_source

        out["source"] = capo_bedrock_agent_runtime.types.file_source.deserialize_json(
            data["source"]
        )
    else:
        raise DeserializationError("InputFile.source required")
    if data.get("useCase") is not None:
        import capo_bedrock_agent_runtime.types.file_use_case

        out["use_case"] = (
            capo_bedrock_agent_runtime.types.file_use_case.deserialize_json(
                data["useCase"]
            )
        )
    else:
        import typing

        out["use_case"] = typing.cast(
            "capo_bedrock_agent_runtime.types.file_use_case.FileUseCase", ""
        )
    return out


def redact_sensitive(value: InputFile) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "source" in value:
        import capo_bedrock_agent_runtime.types.file_source

        out["source"] = capo_bedrock_agent_runtime.types.file_source.redact_sensitive(
            value["source"]
        )
    return out
