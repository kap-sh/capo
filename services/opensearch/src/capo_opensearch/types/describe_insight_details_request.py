"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeInsightDetailsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.boolean
    import capo_opensearch.types.guid
    import capo_opensearch.types.insight_entity


class DescribeInsightDetailsRequest(TypedDict, closed=True):
    entity: "capo_opensearch.types.insight_entity.InsightEntity"
    """<p>The entity for which to retrieve insight details. Specifies the type and value of the entity, such as a domain name or Amazon Web Services account ID.</p>"""
    insight_id: "capo_opensearch.types.guid.GUID"
    """<p>The unique identifier of the insight to describe.</p>"""
    show_html_content: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>Specifies whether to show response with HTML content in response or not.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInsightDetailsRequest) -> dict:
    out: dict = {}
    import capo_opensearch.types.insight_entity

    out["Entity"] = capo_opensearch.types.insight_entity.serialize_json(value["entity"])
    out["InsightId"] = value["insight_id"]
    if "show_html_content" in value:
        out["ShowHtmlContent"] = value["show_html_content"]
    return out


def deserialize_json(data: dict) -> DescribeInsightDetailsRequest:
    out: DescribeInsightDetailsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Entity") is not None:
        import capo_opensearch.types.insight_entity

        out["entity"] = capo_opensearch.types.insight_entity.deserialize_json(
            data["Entity"]
        )
    else:
        raise DeserializationError("DescribeInsightDetailsRequest.entity required")
    if data.get("InsightId") is not None:
        out["insight_id"] = data["InsightId"]
    else:
        out["insight_id"] = ""
    if data.get("ShowHtmlContent") is not None:
        out["show_html_content"] = data["ShowHtmlContent"]
    return out
