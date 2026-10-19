"""Generated from Smithy shape ``com.amazonaws.vpclattice#UpdateAccessLogSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.access_log_destination_arn
    import capo_vpc_lattice.types.access_log_subscription_identifier


class UpdateAccessLogSubscriptionRequest(TypedDict, closed=True):
    access_log_subscription_identifier: "capo_vpc_lattice.types.access_log_subscription_identifier.AccessLogSubscriptionIdentifier"
    """<p>The ID or ARN of the access log subscription.</p>"""
    destination_arn: (
        "capo_vpc_lattice.types.access_log_destination_arn.AccessLogDestinationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the access log destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccessLogSubscriptionRequest) -> dict:
    out: dict = {}
    out["destinationArn"] = value["destination_arn"]
    return out


def deserialize_json(data: dict) -> UpdateAccessLogSubscriptionRequest:
    out: UpdateAccessLogSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if data.get("destinationArn") is not None:
        out["destination_arn"] = data["destinationArn"]
    else:
        out["destination_arn"] = ""
    return out
