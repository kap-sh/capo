"""Generated from Smithy shape ``com.amazonaws.snowball#UpdateJobShipmentStateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.job_id
    import capo_snowball.types.shipment_state


class UpdateJobShipmentStateRequest(TypedDict, closed=True):
    job_id: "capo_snowball.types.job_id.JobId"
    """<p>The job ID of the job whose shipment date you want to update, for example <code>JID123e4567-e89b-12d3-a456-426655440000</code>.</p>"""
    shipment_state: "capo_snowball.types.shipment_state.ShipmentState"
    """<p>The state of a device when it is being shipped. </p> <p>Set to <code>RECEIVED</code> when the device arrives at your location.</p> <p>Set to <code>RETURNED</code> when you have returned the device to Amazon Web Services.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateJobShipmentStateRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    import capo_snowball.types.shipment_state

    out["ShipmentState"] = capo_snowball.types.shipment_state.serialize_aws_json_1_1(
        value["shipment_state"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateJobShipmentStateRequest:
    out: UpdateJobShipmentStateRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    if data.get("ShipmentState") is not None:
        import capo_snowball.types.shipment_state

        out["shipment_state"] = (
            capo_snowball.types.shipment_state.deserialize_aws_json_1_1(
                data["ShipmentState"]
            )
        )
    else:
        import typing

        out["shipment_state"] = typing.cast(
            "capo_snowball.types.shipment_state.ShipmentState", ""
        )
    return out
