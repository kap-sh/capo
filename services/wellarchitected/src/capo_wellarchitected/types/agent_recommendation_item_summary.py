"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AgentRecommendationItemSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_wellarchitected.types.recommendation_arn
    import capo_wellarchitected.types.recommendation_item_type


class AgentRecommendationItemSummary(TypedDict, closed=True):
    id: "str"
    """<p>The unique identifier of the recommendation item.</p>"""
    recommendation_arn: (
        "capo_wellarchitected.types.recommendation_arn.RecommendationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the associated recommendation.</p>"""
    type: "capo_wellarchitected.types.recommendation_item_type.RecommendationItemType"
    """<p>The type of the recommendation item.</p>"""
    metadata: "object"
    """<p>Metadata containing a snapshot of the resource or recommendation at the time of generation.</p>"""
    created_by: "str"
    """<p>The identifier of the user or system that created this recommendation item.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the recommendation item was created.</p>"""
    last_modified_by: NotRequired["str"]
    """<p>The identifier of the user or system that last modified this recommendation item.</p>"""
    last_modified_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the recommendation item was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentRecommendationItemSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["recommendationArn"] = value["recommendation_arn"]
    import capo_wellarchitected.types.recommendation_item_type

    out["type"] = capo_wellarchitected.types.recommendation_item_type.serialize_json(
        value["type"]
    )
    out["metadata"] = value["metadata"]
    out["createdBy"] = value["created_by"]
    import capo_wellarchitected._protocol.serialize

    out["createdAt"] = capo_wellarchitected._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    if "last_modified_by" in value:
        out["lastModifiedBy"] = value["last_modified_by"]
    if "last_modified_at" in value:
        import capo_wellarchitected._protocol.serialize

        out["lastModifiedAt"] = capo_wellarchitected._protocol.serialize.fmt_date_time(
            value["last_modified_at"]
        )
    return out


def deserialize_json(data: dict) -> AgentRecommendationItemSummary:
    out: AgentRecommendationItemSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("recommendationArn") is not None:
        out["recommendation_arn"] = data["recommendationArn"]
    else:
        out["recommendation_arn"] = ""
    if data.get("type") is not None:
        import capo_wellarchitected.types.recommendation_item_type

        out["type"] = (
            capo_wellarchitected.types.recommendation_item_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_wellarchitected.types.recommendation_item_type.RecommendationItemType",
            "",
        )
    if data.get("metadata") is not None:
        out["metadata"] = data["metadata"]
    else:
        out["metadata"] = None
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("lastModifiedBy") is not None:
        out["last_modified_by"] = data["lastModifiedBy"]
    if data.get("lastModifiedAt") is not None:
        import datetime

        out["last_modified_at"] = datetime.datetime.fromisoformat(
            data["lastModifiedAt"].replace("Z", "+00:00")
        )
    return out
