"""Generated from Smithy shape ``com.amazonaws.qconnect#KnowledgeBaseList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.knowledge_base_summary

KnowledgeBaseList: TypeAlias = list[
    "capo_qconnect.types.knowledge_base_summary.KnowledgeBaseSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseList) -> list:
    import capo_qconnect.types.knowledge_base_summary

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.knowledge_base_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> KnowledgeBaseList:
    import capo_qconnect.types.knowledge_base_summary

    out: KnowledgeBaseList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_qconnect.types.knowledge_base_summary.deserialize_json(item))
    return out


def redact_sensitive(value: KnowledgeBaseList) -> list[Any]:
    import capo_qconnect.types.knowledge_base_summary

    return [
        capo_qconnect.types.knowledge_base_summary.redact_sensitive(item)
        for item in value
    ]
