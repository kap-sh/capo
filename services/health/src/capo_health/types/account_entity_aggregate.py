"""Generated from Smithy shape ``com.amazonaws.health#AccountEntityAggregate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.count
    import capo_health.types.entity_statuses
    import capo_health.types.event_arn


class AccountEntityAggregate(TypedDict, closed=True):
    account_id: NotRequired["capo_health.types.event_arn.eventArn"]
    """<p>The 12-digit Amazon Web Services account numbers that contains the affected entities.</p>"""
    count: "capo_health.types.count.count"
    """<p>The number of entities that match the filter criteria for the specified events.</p>"""
    statuses: NotRequired["capo_health.types.entity_statuses.entityStatuses"]
    """<p>The number of affected entities aggregated by the entity status codes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountEntityAggregate) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    out["count"] = value.get("count", 0)
    if "statuses" in value:
        import capo_health.types.entity_statuses

        out["statuses"] = capo_health.types.entity_statuses.serialize_aws_json_1_1(
            value["statuses"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AccountEntityAggregate:
    out: AccountEntityAggregate = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("count") is not None:
        out["count"] = data["count"]
    else:
        out["count"] = 0
    if data.get("statuses") is not None:
        import capo_health.types.entity_statuses

        out["statuses"] = capo_health.types.entity_statuses.deserialize_aws_json_1_1(
            data["statuses"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccountEntityAggregate) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    out["count"] = value.get("count", 0)
    if "statuses" in value:
        import capo_health.types.entity_statuses

        out["statuses"] = capo_health.types.entity_statuses.serialize_cbor(
            value["statuses"]
        )
    return out


def deserialize_cbor(data: dict) -> AccountEntityAggregate:
    out: AccountEntityAggregate = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("count") is not None:
        out["count"] = data["count"]
    else:
        out["count"] = 0
    if data.get("statuses") is not None:
        import capo_health.types.entity_statuses

        out["statuses"] = capo_health.types.entity_statuses.deserialize_cbor(
            data["statuses"]
        )
    return out
