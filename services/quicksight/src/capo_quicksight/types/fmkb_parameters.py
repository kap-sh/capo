"""Generated from Smithy shape ``com.amazonaws.quicksight#FMKBParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.fmkb_knowledge_base_arn
    import capo_quicksight.types.linked_data_source_ids


class FMKBParameters(TypedDict, closed=True):
    knowledge_base_arn: (
        "capo_quicksight.types.fmkb_knowledge_base_arn.FMKBKnowledgeBaseArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Amazon Bedrock knowledge base.</p>"""
    linked_data_source_ids: NotRequired[
        "capo_quicksight.types.linked_data_source_ids.LinkedDataSourceIds"
    ]
    """<p>The IDs of the linked data sources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FMKBParameters) -> dict:
    out: dict = {}
    out["KnowledgeBaseArn"] = value["knowledge_base_arn"]
    if "linked_data_source_ids" in value:
        import capo_quicksight.types.linked_data_source_ids

        out["LinkedDataSourceIds"] = (
            capo_quicksight.types.linked_data_source_ids.serialize_json(
                value["linked_data_source_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> FMKBParameters:
    out: FMKBParameters = {}  # type: ignore[typeddict-item]
    if data.get("KnowledgeBaseArn") is not None:
        out["knowledge_base_arn"] = data["KnowledgeBaseArn"]
    else:
        out["knowledge_base_arn"] = ""
    if data.get("LinkedDataSourceIds") is not None:
        import capo_quicksight.types.linked_data_source_ids

        out["linked_data_source_ids"] = (
            capo_quicksight.types.linked_data_source_ids.deserialize_json(
                data["LinkedDataSourceIds"]
            )
        )
    return out
