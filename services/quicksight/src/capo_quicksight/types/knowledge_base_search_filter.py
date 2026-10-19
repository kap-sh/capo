"""Generated from Smithy shape ``com.amazonaws.quicksight#KnowledgeBaseSearchFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.knowledge_base_search_filter_name
    import capo_quicksight.types.knowledge_base_search_operator


class KnowledgeBaseSearchFilter(TypedDict, closed=True):
    name: "capo_quicksight.types.knowledge_base_search_filter_name.KnowledgeBaseSearchFilterName"
    """<p>The name of the field to filter on.</p>"""
    operator: "capo_quicksight.types.knowledge_base_search_operator.KnowledgeBaseSearchOperator"
    """<p>The comparison operator to use for the filter.</p>"""
    value: "str"
    """<p>The value to filter on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseSearchFilter) -> dict:
    out: dict = {}
    import capo_quicksight.types.knowledge_base_search_filter_name

    out["name"] = (
        capo_quicksight.types.knowledge_base_search_filter_name.serialize_json(
            value["name"]
        )
    )
    import capo_quicksight.types.knowledge_base_search_operator

    out["operator"] = (
        capo_quicksight.types.knowledge_base_search_operator.serialize_json(
            value["operator"]
        )
    )
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> KnowledgeBaseSearchFilter:
    out: KnowledgeBaseSearchFilter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_quicksight.types.knowledge_base_search_filter_name

        out["name"] = (
            capo_quicksight.types.knowledge_base_search_filter_name.deserialize_json(
                data["name"]
            )
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_quicksight.types.knowledge_base_search_filter_name.KnowledgeBaseSearchFilterName",
            "",
        )
    if data.get("operator") is not None:
        import capo_quicksight.types.knowledge_base_search_operator

        out["operator"] = (
            capo_quicksight.types.knowledge_base_search_operator.deserialize_json(
                data["operator"]
            )
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_quicksight.types.knowledge_base_search_operator.KnowledgeBaseSearchOperator",
            "",
        )
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
