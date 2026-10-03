"""Generated from Smithy shape ``com.amazonaws.health#EntityFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_health.errors import DeserializationError

if TYPE_CHECKING:
    import capo_health.types.date_time_range_list
    import capo_health.types.entity_arn_list
    import capo_health.types.entity_status_code_list
    import capo_health.types.entity_value_list
    import capo_health.types.event_arn_list
    import capo_health.types.tag_filter


class EntityFilter(TypedDict, closed=True):
    event_arns: "capo_health.types.event_arn_list.eventArnList"
    """<p>A list of event ARNs (unique identifiers). For example: <code>"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456", "arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"</code> </p>"""
    entity_arns: NotRequired["capo_health.types.entity_arn_list.entityArnList"]
    """<p>A list of entity ARNs (unique identifiers).</p>"""
    entity_values: NotRequired["capo_health.types.entity_value_list.entityValueList"]
    """<p>A list of IDs for affected entities.</p>"""
    last_updated_times: NotRequired[
        "capo_health.types.date_time_range_list.dateTimeRangeList"
    ]
    """<p>A list of the most recent dates and times that the entity was updated.</p>"""
    tags: NotRequired["capo_health.types.tag_filter.tagFilter"]
    """<p>A map of entity tags attached to the affected entity.</p> <note> <p>Currently, the <code>tags</code> property isn't supported.</p> </note>"""
    status_codes: NotRequired[
        "capo_health.types.entity_status_code_list.entityStatusCodeList"
    ]
    """<p>A list of entity status codes (<code>IMPAIRED</code>, <code>UNIMPAIRED</code>, or <code>UNKNOWN</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityFilter) -> dict:
    out: dict = {}
    import capo_health.types.event_arn_list

    out["eventArns"] = capo_health.types.event_arn_list.serialize_aws_json_1_1(
        value["event_arns"]
    )
    if "entity_arns" in value:
        import capo_health.types.entity_arn_list

        out["entityArns"] = capo_health.types.entity_arn_list.serialize_aws_json_1_1(
            value["entity_arns"]
        )
    if "entity_values" in value:
        import capo_health.types.entity_value_list

        out["entityValues"] = (
            capo_health.types.entity_value_list.serialize_aws_json_1_1(
                value["entity_values"]
            )
        )
    if "last_updated_times" in value:
        import capo_health.types.date_time_range_list

        out["lastUpdatedTimes"] = (
            capo_health.types.date_time_range_list.serialize_aws_json_1_1(
                value["last_updated_times"]
            )
        )
    if "tags" in value:
        import capo_health.types.tag_filter

        out["tags"] = capo_health.types.tag_filter.serialize_aws_json_1_1(value["tags"])
    if "status_codes" in value:
        import capo_health.types.entity_status_code_list

        out["statusCodes"] = (
            capo_health.types.entity_status_code_list.serialize_aws_json_1_1(
                value["status_codes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityFilter:
    out: EntityFilter = {}  # type: ignore[typeddict-item]
    if data.get("eventArns") is not None:
        import capo_health.types.event_arn_list

        out["event_arns"] = capo_health.types.event_arn_list.deserialize_aws_json_1_1(
            data["eventArns"]
        )
    else:
        raise DeserializationError("EntityFilter.event_arns required")
    if data.get("entityArns") is not None:
        import capo_health.types.entity_arn_list

        out["entity_arns"] = capo_health.types.entity_arn_list.deserialize_aws_json_1_1(
            data["entityArns"]
        )
    if data.get("entityValues") is not None:
        import capo_health.types.entity_value_list

        out["entity_values"] = (
            capo_health.types.entity_value_list.deserialize_aws_json_1_1(
                data["entityValues"]
            )
        )
    if data.get("lastUpdatedTimes") is not None:
        import capo_health.types.date_time_range_list

        out["last_updated_times"] = (
            capo_health.types.date_time_range_list.deserialize_aws_json_1_1(
                data["lastUpdatedTimes"]
            )
        )
    if data.get("tags") is not None:
        import capo_health.types.tag_filter

        out["tags"] = capo_health.types.tag_filter.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("statusCodes") is not None:
        import capo_health.types.entity_status_code_list

        out["status_codes"] = (
            capo_health.types.entity_status_code_list.deserialize_aws_json_1_1(
                data["statusCodes"]
            )
        )
    return out
