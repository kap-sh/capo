"""Generated from Smithy shape ``com.amazonaws.health#OrganizationEntityAggregateFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.organization_entity_aggregate_tag_filter


class OrganizationEntityAggregateFilter(TypedDict, closed=True):
    tags: NotRequired[
        "capo_health.types.organization_entity_aggregate_tag_filter.OrganizationEntityAggregateTagFilter"
    ]
    """<p>A map of tag keys to lists of tag values. A tag matches when its key is in the map and its value is one of the values listed for that key. Matching is case sensitive, and the filter matches when at least one key in the map matches.</p> <p>Only entities whose tags match are included in the aggregates.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationEntityAggregateFilter) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_health.types.organization_entity_aggregate_tag_filter

        out["tags"] = (
            capo_health.types.organization_entity_aggregate_tag_filter.serialize_aws_json_1_1(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OrganizationEntityAggregateFilter:
    out: OrganizationEntityAggregateFilter = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_health.types.organization_entity_aggregate_tag_filter

        out["tags"] = (
            capo_health.types.organization_entity_aggregate_tag_filter.deserialize_aws_json_1_1(
                data["tags"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OrganizationEntityAggregateFilter) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_health.types.organization_entity_aggregate_tag_filter

        out["tags"] = (
            capo_health.types.organization_entity_aggregate_tag_filter.serialize_cbor(
                value["tags"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> OrganizationEntityAggregateFilter:
    out: OrganizationEntityAggregateFilter = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_health.types.organization_entity_aggregate_tag_filter

        out["tags"] = (
            capo_health.types.organization_entity_aggregate_tag_filter.deserialize_cbor(
                data["tags"]
            )
        )
    return out
