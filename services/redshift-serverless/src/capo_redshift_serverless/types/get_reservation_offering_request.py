"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetReservationOfferingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.offering_id


class GetReservationOfferingRequest(TypedDict, closed=True):
    offering_id: "capo_redshift_serverless.types.offering_id.OfferingId"
    """<p>The identifier for the offering..</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetReservationOfferingRequest) -> dict:
    out: dict = {}
    out["offeringId"] = value["offering_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetReservationOfferingRequest:
    out: GetReservationOfferingRequest = {}  # type: ignore[typeddict-item]
    if data.get("offeringId") is not None:
        out["offering_id"] = data["offeringId"]
    else:
        out["offering_id"] = ""
    return out
