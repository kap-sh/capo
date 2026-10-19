"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetReservationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.reservation_id


class GetReservationRequest(TypedDict, closed=True):
    reservation_id: "capo_redshift_serverless.types.reservation_id.ReservationId"
    """<p>The ID of the reservation to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetReservationRequest) -> dict:
    out: dict = {}
    out["reservationId"] = value["reservation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetReservationRequest:
    out: GetReservationRequest = {}  # type: ignore[typeddict-item]
    if data.get("reservationId") is not None:
        out["reservation_id"] = data["reservationId"]
    else:
        out["reservation_id"] = ""
    return out
