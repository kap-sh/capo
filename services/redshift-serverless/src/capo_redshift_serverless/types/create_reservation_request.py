"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#CreateReservationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_redshift_serverless.types.capacity
    import capo_redshift_serverless.types.offering_id


class CreateReservationRequest(TypedDict, closed=True):
    capacity: "capo_redshift_serverless.types.capacity.Capacity"
    """<p>The number of Redshift Processing Units (RPUs) to reserve.</p>"""
    offering_id: "capo_redshift_serverless.types.offering_id.OfferingId"
    """<p>The ID of the offering associated with the reservation. The offering determines the payment schedule for the reservation.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. This token must be a valid UUIDv4 value. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/"> Making retries safe with idempotent APIs </a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateReservationRequest) -> dict:
    out: dict = {}
    out["capacity"] = value.get("capacity", 0)
    out["offeringId"] = value["offering_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateReservationRequest:
    out: CreateReservationRequest = {}  # type: ignore[typeddict-item]
    if data.get("capacity") is not None:
        out["capacity"] = data["capacity"]
    else:
        out["capacity"] = 0
    if data.get("offeringId") is not None:
        out["offering_id"] = data["offeringId"]
    else:
        raise DeserializationError("CreateReservationRequest.offering_id required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
