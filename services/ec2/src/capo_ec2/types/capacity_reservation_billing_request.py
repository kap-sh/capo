"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationBillingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.account_id
    import capo_ec2.types.capacity_reservation_billing_request_status
    import capo_ec2.types.capacity_reservation_info
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class CapacityReservationBillingRequest(TypedDict, closed=True):
    capacity_reservation_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Capacity Reservation.</p>"""
    requested_by: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that initiated the request.</p>"""
    unused_reservation_billing_owner_id: NotRequired[
        "capo_ec2.types.account_id.AccountID"
    ]
    """<p>The ID of the Amazon Web Services account to which the request was sent.</p>"""
    last_update_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time, in UTC time format, at which the request was initiated.</p>"""
    status: NotRequired[
        "capo_ec2.types.capacity_reservation_billing_request_status.CapacityReservationBillingRequestStatus"
    ]
    """<p>The status of the request. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/view-billing-transfers.html"> View billing assignment requests for a shared Amazon EC2 Capacity Reservation</a>.</p>"""
    status_message: NotRequired["capo_ec2.types.string.String"]
    """<p>Information about the status.</p>"""
    capacity_reservation_info: NotRequired[
        "capo_ec2.types.capacity_reservation_info.CapacityReservationInfo"
    ]
    """<p>Information about the Capacity Reservation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityReservationBillingRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_reservation_id" in value:
        pairs.append(
            (
                f"{key_prefix}CapacityReservationId",
                str(value["capacity_reservation_id"]),
            )
        )
    if "requested_by" in value:
        pairs.append((f"{key_prefix}RequestedBy", str(value["requested_by"])))
    if "unused_reservation_billing_owner_id" in value:
        pairs.append(
            (
                f"{key_prefix}UnusedReservationBillingOwnerId",
                str(value["unused_reservation_billing_owner_id"]),
            )
        )
    if "last_update_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["last_update_time"], pairs, f"{key_prefix}LastUpdateTime"
        )
    if "status" in value:
        import capo_ec2.types.capacity_reservation_billing_request_status

        capo_ec2.types.capacity_reservation_billing_request_status.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "status_message" in value:
        pairs.append((f"{key_prefix}StatusMessage", str(value["status_message"])))
    if "capacity_reservation_info" in value:
        import capo_ec2.types.capacity_reservation_info

        capo_ec2.types.capacity_reservation_info.serialize_ec2_query(
            value["capacity_reservation_info"],
            pairs,
            f"{key_prefix}CapacityReservationInfo",
        )


def deserialize_ec2_query(el: Element) -> CapacityReservationBillingRequest:
    out: CapacityReservationBillingRequest = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_id = el.find("capacityReservationId")
    if child_capacity_reservation_id is not None:
        out["capacity_reservation_id"] = str(child_capacity_reservation_id.text or "")
    child_requested_by = el.find("requestedBy")
    if child_requested_by is not None:
        out["requested_by"] = str(child_requested_by.text or "")
    child_unused_reservation_billing_owner_id = el.find(
        "unusedReservationBillingOwnerId"
    )
    if child_unused_reservation_billing_owner_id is not None:
        out["unused_reservation_billing_owner_id"] = str(
            child_unused_reservation_billing_owner_id.text or ""
        )
    child_last_update_time = el.find("lastUpdateTime")
    if child_last_update_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["last_update_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_last_update_time
            )
        )
    child_status = el.find("status")
    if child_status is not None:
        import capo_ec2.types.capacity_reservation_billing_request_status

        out["status"] = (
            capo_ec2.types.capacity_reservation_billing_request_status.deserialize_ec2_query(
                child_status
            )
        )
    child_status_message = el.find("statusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    child_capacity_reservation_info = el.find("capacityReservationInfo")
    if child_capacity_reservation_info is not None:
        import capo_ec2.types.capacity_reservation_info

        out["capacity_reservation_info"] = (
            capo_ec2.types.capacity_reservation_info.deserialize_ec2_query(
                child_capacity_reservation_info
            )
        )
    return out
