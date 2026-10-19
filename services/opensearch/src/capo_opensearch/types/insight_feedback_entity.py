"""Generated from Smithy shape ``com.amazonaws.opensearch#InsightFeedbackEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.insight_entity_value
    import capo_opensearch.types.insight_feedback_entity_type


class InsightFeedbackEntity(TypedDict, closed=True):
    type: "capo_opensearch.types.insight_feedback_entity_type.InsightFeedbackEntityType"
    """<p>The type of the entity. Possible values are <code>DomainName</code>.</p>"""
    value: "capo_opensearch.types.insight_entity_value.InsightEntityValue"
    """<p>The value of the entity, such as a domain name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightFeedbackEntity) -> dict:
    out: dict = {}
    import capo_opensearch.types.insight_feedback_entity_type

    out["Type"] = capo_opensearch.types.insight_feedback_entity_type.serialize_json(
        value["type"]
    )
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> InsightFeedbackEntity:
    out: InsightFeedbackEntity = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_opensearch.types.insight_feedback_entity_type

        out["type"] = (
            capo_opensearch.types.insight_feedback_entity_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_opensearch.types.insight_feedback_entity_type.InsightFeedbackEntityType",
            "",
        )
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
