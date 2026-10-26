"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#DocumentBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.citations_config
    import capo_bedrock_runtime.types.document_format
    import capo_bedrock_runtime.types.document_source


class DocumentBlock(TypedDict, closed=True):
    format: "capo_bedrock_runtime.types.document_format.DocumentFormat"
    """<p>The format of a document, or its extension.</p>"""
    name: "str"
    """<p>A name for the document. The name can only contain the following characters:</p> <ul> <li> <p>Alphanumeric characters</p> </li> <li> <p>Whitespace characters (no more than one in a row)</p> </li> <li> <p>Hyphens</p> </li> <li> <p>Parentheses</p> </li> <li> <p>Square brackets</p> </li> </ul> <note> <p>This field is vulnerable to prompt injections, because the model might inadvertently interpret it as instructions. Therefore, we recommend that you specify a neutral name.</p> </note>"""
    source: "capo_bedrock_runtime.types.document_source.DocumentSource"
    """<p>Contains the content of the document.</p>"""
    context: NotRequired["str"]
    """<p>Contextual information about how the document should be processed or interpreted by the model when generating citations.</p>"""
    citations: NotRequired[
        "capo_bedrock_runtime.types.citations_config.CitationsConfig"
    ]
    """<p>Configuration settings that control how citations should be generated for this specific document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentBlock) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.document_format

    out["format"] = capo_bedrock_runtime.types.document_format.serialize_json(
        value.get("format", "txt")
    )
    out["name"] = value["name"]
    import capo_bedrock_runtime.types.document_source

    out["source"] = capo_bedrock_runtime.types.document_source.serialize_json(
        value["source"]
    )
    if "context" in value:
        out["context"] = value["context"]
    if "citations" in value:
        import capo_bedrock_runtime.types.citations_config

        out["citations"] = capo_bedrock_runtime.types.citations_config.serialize_json(
            value["citations"]
        )
    return out


def deserialize_json(data: dict) -> DocumentBlock:
    out: DocumentBlock = {}  # type: ignore[typeddict-item]
    if data.get("format") is not None:
        import capo_bedrock_runtime.types.document_format

        out["format"] = capo_bedrock_runtime.types.document_format.deserialize_json(
            data["format"]
        )
    else:
        out["format"] = "txt"
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("source") is not None:
        import capo_bedrock_runtime.types.document_source

        out["source"] = capo_bedrock_runtime.types.document_source.deserialize_json(
            data["source"]
        )
    else:
        out["source"] = {"$unknown": {"name": ""}}
    if data.get("context") is not None:
        out["context"] = data["context"]
    if data.get("citations") is not None:
        import capo_bedrock_runtime.types.citations_config

        out["citations"] = capo_bedrock_runtime.types.citations_config.deserialize_json(
            data["citations"]
        )
    return out
