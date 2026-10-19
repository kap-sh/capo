"""Generated from Smithy shape ``com.amazonaws.opensearch#InsightEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.insight_entity_type
    import capo_opensearch.types.insight_entity_value


class InsightEntity(TypedDict, closed=True):
    type: "capo_opensearch.types.insight_entity_type.InsightEntityType"
    """<p>The type of the entity. Possible values are <code>Account</code> and <code>DomainName</code>.</p>"""
    value: NotRequired["capo_opensearch.types.insight_entity_value.InsightEntityValue"]
    """<p>The value of the entity. For <code>DomainName</code>, this is the domain name. For <code>Account</code>, this is the Amazon Web Services account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightEntity) -> dict:
    out: dict = {}
    import capo_opensearch.types.insight_entity_type

    out["Type"] = capo_opensearch.types.insight_entity_type.serialize_json(
        value["type"]
    )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> InsightEntity:
    out: InsightEntity = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_opensearch.types.insight_entity_type

        out["type"] = capo_opensearch.types.insight_entity_type.deserialize_json(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_opensearch.types.insight_entity_type.InsightEntityType", ""
        )
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
