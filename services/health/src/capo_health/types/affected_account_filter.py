"""Generated from Smithy shape ``com.amazonaws.health#AffectedAccountFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.affected_accounts_for_organization_tag_filter
    import capo_health.types.event_arn


class AffectedAccountFilter(TypedDict, closed=True):
    event_arn: NotRequired["capo_health.types.event_arn.eventArn"]
    """<p>The unique identifier for the event. The event ARN has the <code>arn:aws:health:<i>event-region</i>::event/<i>SERVICE</i>/<i>EVENT_TYPE_CODE</i>/<i>EVENT_TYPE_PLUS_ID</i> </code> format.</p> <p>For example, an event ARN might look like the following:</p> <p> <code>arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456</code> </p>"""
    tags: NotRequired[
        "capo_health.types.affected_accounts_for_organization_tag_filter.AffectedAccountsForOrganizationTagFilter"
    ]
    """<p>A map of tag keys to lists of tag values. A tag matches when its key is in the map and its value is one of the values listed for that key. Matching is case sensitive, and the filter matches when at least one key in the map matches.</p> <p>An account is returned when its own tags, or the tags of one of its affected resources, match.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AffectedAccountFilter) -> dict:
    out: dict = {}
    if "event_arn" in value:
        out["eventArn"] = value["event_arn"]
    if "tags" in value:
        import capo_health.types.affected_accounts_for_organization_tag_filter

        out["tags"] = (
            capo_health.types.affected_accounts_for_organization_tag_filter.serialize_aws_json_1_1(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AffectedAccountFilter:
    out: AffectedAccountFilter = {}  # type: ignore[typeddict-item]
    if data.get("eventArn") is not None:
        out["event_arn"] = data["eventArn"]
    if data.get("tags") is not None:
        import capo_health.types.affected_accounts_for_organization_tag_filter

        out["tags"] = (
            capo_health.types.affected_accounts_for_organization_tag_filter.deserialize_aws_json_1_1(
                data["tags"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AffectedAccountFilter) -> dict:
    out: dict = {}
    if "event_arn" in value:
        out["eventArn"] = value["event_arn"]
    if "tags" in value:
        import capo_health.types.affected_accounts_for_organization_tag_filter

        out["tags"] = (
            capo_health.types.affected_accounts_for_organization_tag_filter.serialize_cbor(
                value["tags"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AffectedAccountFilter:
    out: AffectedAccountFilter = {}  # type: ignore[typeddict-item]
    if data.get("eventArn") is not None:
        out["event_arn"] = data["eventArn"]
    if data.get("tags") is not None:
        import capo_health.types.affected_accounts_for_organization_tag_filter

        out["tags"] = (
            capo_health.types.affected_accounts_for_organization_tag_filter.deserialize_cbor(
                data["tags"]
            )
        )
    return out
