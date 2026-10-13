"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DocumentAccessControlList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.document_access_control_entry

DocumentAccessControlList: TypeAlias = list[
    "capo_bedrock_agent.types.document_access_control_entry.DocumentAccessControlEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAccessControlList) -> list:
    import capo_bedrock_agent.types.document_access_control_entry

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent.types.document_access_control_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DocumentAccessControlList:
    import capo_bedrock_agent.types.document_access_control_entry

    out: DocumentAccessControlList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent.types.document_access_control_entry.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: DocumentAccessControlList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
