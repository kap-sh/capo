"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeStatusItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.initialization_status_details
    import capo_ec2.types.operator_response
    import capo_ec2.types.string
    import capo_ec2.types.volume_status_actions_list
    import capo_ec2.types.volume_status_attachment_status_list
    import capo_ec2.types.volume_status_events_list
    import capo_ec2.types.volume_status_info


class VolumeStatusItem(TypedDict, closed=True):
    actions: NotRequired[
        "capo_ec2.types.volume_status_actions_list.VolumeStatusActionsList"
    ]
    """<p>The details of the operation.</p>"""
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone of the volume.</p>"""
    outpost_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Outpost.</p>"""
    events: NotRequired[
        "capo_ec2.types.volume_status_events_list.VolumeStatusEventsList"
    ]
    """<p>A list of events associated with the volume.</p>"""
    volume_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The volume ID.</p>"""
    volume_status: NotRequired["capo_ec2.types.volume_status_info.VolumeStatusInfo"]
    """<p>The volume status.</p>"""
    attachment_statuses: NotRequired[
        "capo_ec2.types.volume_status_attachment_status_list.VolumeStatusAttachmentStatusList"
    ]
    """<p>Information about the instances to which the volume is attached.</p>"""
    initialization_status_details: NotRequired[
        "capo_ec2.types.initialization_status_details.InitializationStatusDetails"
    ]
    """<p>Information about the volume initialization. It can take up to 5 minutes for the volume initialization information to be updated.</p> <p>Only available for volumes created from snapshots. Not available for empty volumes created without a snapshot.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/initalize-volume.html"> Initialize Amazon EBS volumes</a>.</p>"""
    availability_zone_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Availability Zone.</p>"""
    operator: NotRequired["capo_ec2.types.operator_response.OperatorResponse"]
    """<p>The service provider that manages the resource.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VolumeStatusItem, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "actions" in value:
        import capo_ec2.types.volume_status_actions_list

        capo_ec2.types.volume_status_actions_list.serialize_ec2_query(
            value["actions"], pairs, f"{key_prefix}ActionsSet"
        )
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "outpost_arn" in value:
        pairs.append((f"{key_prefix}OutpostArn", str(value["outpost_arn"])))
    if "events" in value:
        import capo_ec2.types.volume_status_events_list

        capo_ec2.types.volume_status_events_list.serialize_ec2_query(
            value["events"], pairs, f"{key_prefix}EventsSet"
        )
    if "volume_id" in value:
        pairs.append((f"{key_prefix}VolumeId", str(value["volume_id"])))
    if "volume_status" in value:
        import capo_ec2.types.volume_status_info

        capo_ec2.types.volume_status_info.serialize_ec2_query(
            value["volume_status"], pairs, f"{key_prefix}VolumeStatus"
        )
    if "attachment_statuses" in value:
        import capo_ec2.types.volume_status_attachment_status_list

        capo_ec2.types.volume_status_attachment_status_list.serialize_ec2_query(
            value["attachment_statuses"], pairs, f"{key_prefix}AttachmentStatuses"
        )
    if "initialization_status_details" in value:
        import capo_ec2.types.initialization_status_details

        capo_ec2.types.initialization_status_details.serialize_ec2_query(
            value["initialization_status_details"],
            pairs,
            f"{key_prefix}InitializationStatusDetails",
        )
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "operator" in value:
        import capo_ec2.types.operator_response

        capo_ec2.types.operator_response.serialize_ec2_query(
            value["operator"], pairs, f"{key_prefix}Operator"
        )


def deserialize_ec2_query(el: Element) -> VolumeStatusItem:
    out: VolumeStatusItem = {}  # type: ignore[typeddict-item]
    child_actions = el.find("actionsSet")
    if child_actions is not None:
        import capo_ec2.types.volume_status_actions_list

        out["actions"] = (
            capo_ec2.types.volume_status_actions_list.deserialize_ec2_query(
                child_actions
            )
        )
    child_availability_zone = el.find("availabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_outpost_arn = el.find("outpostArn")
    if child_outpost_arn is not None:
        out["outpost_arn"] = str(child_outpost_arn.text or "")
    child_events = el.find("eventsSet")
    if child_events is not None:
        import capo_ec2.types.volume_status_events_list

        out["events"] = capo_ec2.types.volume_status_events_list.deserialize_ec2_query(
            child_events
        )
    child_volume_id = el.find("volumeId")
    if child_volume_id is not None:
        out["volume_id"] = str(child_volume_id.text or "")
    child_volume_status = el.find("volumeStatus")
    if child_volume_status is not None:
        import capo_ec2.types.volume_status_info

        out["volume_status"] = capo_ec2.types.volume_status_info.deserialize_ec2_query(
            child_volume_status
        )
    child_attachment_statuses = el.find("attachmentStatuses")
    if child_attachment_statuses is not None:
        import capo_ec2.types.volume_status_attachment_status_list

        out["attachment_statuses"] = (
            capo_ec2.types.volume_status_attachment_status_list.deserialize_ec2_query(
                child_attachment_statuses
            )
        )
    child_initialization_status_details = el.find("initializationStatusDetails")
    if child_initialization_status_details is not None:
        import capo_ec2.types.initialization_status_details

        out["initialization_status_details"] = (
            capo_ec2.types.initialization_status_details.deserialize_ec2_query(
                child_initialization_status_details
            )
        )
    child_availability_zone_id = el.find("availabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_operator = el.find("operator")
    if child_operator is not None:
        import capo_ec2.types.operator_response

        out["operator"] = capo_ec2.types.operator_response.deserialize_ec2_query(
            child_operator
        )
    return out
