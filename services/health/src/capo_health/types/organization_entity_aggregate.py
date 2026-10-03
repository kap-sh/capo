"""Generated from Smithy shape ``com.amazonaws.health#OrganizationEntityAggregate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.account_entity_aggregates_list
    import capo_health.types.count
    import capo_health.types.entity_statuses
    import capo_health.types.event_arn


class OrganizationEntityAggregate(TypedDict, closed=True):
    event_arn: NotRequired["capo_health.types.event_arn.eventArn"]
    """<p>A list of event ARNs (unique identifiers). For example: <code>"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456", "arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"</code> </p>"""
    count: "capo_health.types.count.count"
    """<p>The number of entities for the organization that match the filter criteria for the specified events.</p>"""
    statuses: NotRequired["capo_health.types.entity_statuses.entityStatuses"]
    """<p>The number of affected entities aggregated by the entitiy status codes.</p>"""
    accounts: NotRequired[
        "capo_health.types.account_entity_aggregates_list.AccountEntityAggregatesList"
    ]
    """<p>A list of entity aggregates for each of the specified accounts in your organization that are affected by a specific event. If there are no <code>awsAccountIds</code> provided in the request, this field will be empty in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationEntityAggregate) -> dict:
    out: dict = {}
    if "event_arn" in value:
        out["eventArn"] = value["event_arn"]
    out["count"] = value.get("count", 0)
    if "statuses" in value:
        import capo_health.types.entity_statuses

        out["statuses"] = capo_health.types.entity_statuses.serialize_aws_json_1_1(
            value["statuses"]
        )
    if "accounts" in value:
        import capo_health.types.account_entity_aggregates_list

        out["accounts"] = (
            capo_health.types.account_entity_aggregates_list.serialize_aws_json_1_1(
                value["accounts"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OrganizationEntityAggregate:
    out: OrganizationEntityAggregate = {}  # type: ignore[typeddict-item]
    if data.get("eventArn") is not None:
        out["event_arn"] = data["eventArn"]
    if data.get("count") is not None:
        out["count"] = data["count"]
    else:
        out["count"] = 0
    if data.get("statuses") is not None:
        import capo_health.types.entity_statuses

        out["statuses"] = capo_health.types.entity_statuses.deserialize_aws_json_1_1(
            data["statuses"]
        )
    if data.get("accounts") is not None:
        import capo_health.types.account_entity_aggregates_list

        out["accounts"] = (
            capo_health.types.account_entity_aggregates_list.deserialize_aws_json_1_1(
                data["accounts"]
            )
        )
    return out
