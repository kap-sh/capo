"""Generated from Smithy shape ``com.amazonaws.ec2#SpotFleetRequestConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.activity_status
    import capo_ec2.types.batch_state
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.spot_fleet_request_config_data
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class SpotFleetRequestConfig(TypedDict, closed=True):
    activity_status: NotRequired["capo_ec2.types.activity_status.ActivityStatus"]
    """<p>The progress of the Spot Fleet request. If there is an error, the status is <code>error</code>. After all requests are placed, the status is <code>pending_fulfillment</code>. If the size of the fleet is equal to or greater than its target capacity, the status is <code>fulfilled</code>. If the size of the fleet is decreased, the status is <code>pending_termination</code> while Spot Instances are terminating.</p>"""
    create_time: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The creation date and time of the request.</p>"""
    spot_fleet_request_config: NotRequired[
        "capo_ec2.types.spot_fleet_request_config_data.SpotFleetRequestConfigData"
    ]
    """<p>The configuration of the Spot Fleet request.</p>"""
    spot_fleet_request_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Spot Fleet request.</p>"""
    spot_fleet_request_state: NotRequired["capo_ec2.types.batch_state.BatchState"]
    """<p>The state of the Spot Fleet request.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags for a Spot Fleet resource.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SpotFleetRequestConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "activity_status" in value:
        import capo_ec2.types.activity_status

        capo_ec2.types.activity_status.serialize_ec2_query(
            value["activity_status"], pairs, f"{key_prefix}ActivityStatus"
        )
    if "create_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["create_time"], pairs, f"{key_prefix}CreateTime"
        )
    if "spot_fleet_request_config" in value:
        import capo_ec2.types.spot_fleet_request_config_data

        capo_ec2.types.spot_fleet_request_config_data.serialize_ec2_query(
            value["spot_fleet_request_config"],
            pairs,
            f"{key_prefix}SpotFleetRequestConfig",
        )
    if "spot_fleet_request_id" in value:
        pairs.append(
            (f"{key_prefix}SpotFleetRequestId", str(value["spot_fleet_request_id"]))
        )
    if "spot_fleet_request_state" in value:
        import capo_ec2.types.batch_state

        capo_ec2.types.batch_state.serialize_ec2_query(
            value["spot_fleet_request_state"],
            pairs,
            f"{key_prefix}SpotFleetRequestState",
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> SpotFleetRequestConfig:
    out: SpotFleetRequestConfig = {}  # type: ignore[typeddict-item]
    child_activity_status = el.find("activityStatus")
    if child_activity_status is not None:
        import capo_ec2.types.activity_status

        out["activity_status"] = capo_ec2.types.activity_status.deserialize_ec2_query(
            child_activity_status
        )
    child_create_time = el.find("createTime")
    if child_create_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["create_time"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_create_time
        )
    child_spot_fleet_request_config = el.find("spotFleetRequestConfig")
    if child_spot_fleet_request_config is not None:
        import capo_ec2.types.spot_fleet_request_config_data

        out["spot_fleet_request_config"] = (
            capo_ec2.types.spot_fleet_request_config_data.deserialize_ec2_query(
                child_spot_fleet_request_config
            )
        )
    child_spot_fleet_request_id = el.find("spotFleetRequestId")
    if child_spot_fleet_request_id is not None:
        out["spot_fleet_request_id"] = str(child_spot_fleet_request_id.text or "")
    child_spot_fleet_request_state = el.find("spotFleetRequestState")
    if child_spot_fleet_request_state is not None:
        import capo_ec2.types.batch_state

        out["spot_fleet_request_state"] = (
            capo_ec2.types.batch_state.deserialize_ec2_query(
                child_spot_fleet_request_state
            )
        )
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    return out


def redact_sensitive(value: SpotFleetRequestConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "spot_fleet_request_config" in value:
        import capo_ec2.types.spot_fleet_request_config_data

        out["spot_fleet_request_config"] = (
            capo_ec2.types.spot_fleet_request_config_data.redact_sensitive(
                value["spot_fleet_request_config"]
            )
        )
    return out
