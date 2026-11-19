"""Generated from Smithy shape ``com.amazonaws.health#DescribeEntityAggregatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.entity_aggregate_list


class DescribeEntityAggregatesResponse(TypedDict, closed=True):
    entity_aggregates: NotRequired[
        "capo_health.types.entity_aggregate_list.EntityAggregateList"
    ]
    """<p>The number of entities that are affected by each of the specified events.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEntityAggregatesResponse) -> dict:
    out: dict = {}
    if "entity_aggregates" in value:
        import capo_health.types.entity_aggregate_list

        out["entityAggregates"] = (
            capo_health.types.entity_aggregate_list.serialize_aws_json_1_1(
                value["entity_aggregates"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEntityAggregatesResponse:
    out: DescribeEntityAggregatesResponse = {}  # type: ignore[typeddict-item]
    if data.get("entityAggregates") is not None:
        import capo_health.types.entity_aggregate_list

        out["entity_aggregates"] = (
            capo_health.types.entity_aggregate_list.deserialize_aws_json_1_1(
                data["entityAggregates"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeEntityAggregatesResponse) -> dict:
    out: dict = {}
    if "entity_aggregates" in value:
        import capo_health.types.entity_aggregate_list

        out["entityAggregates"] = (
            capo_health.types.entity_aggregate_list.serialize_cbor(
                value["entity_aggregates"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeEntityAggregatesResponse:
    out: DescribeEntityAggregatesResponse = {}  # type: ignore[typeddict-item]
    if data.get("entityAggregates") is not None:
        import capo_health.types.entity_aggregate_list

        out["entity_aggregates"] = (
            capo_health.types.entity_aggregate_list.deserialize_cbor(
                data["entityAggregates"]
            )
        )
    return out
