"""Generated from Smithy shape ``com.amazonaws.securityir#GetFindingMetricsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_security_ir.types.membership_id


class GetFindingMetricsRequest(TypedDict, closed=True):
    membership_id: "capo_security_ir.types.membership_id.MembershipId"
    """The membership ID to retrieve metrics for."""
    start_date: "datetime.datetime"
    """The start of the day-aligned UTC window, inclusive."""
    end_date: "datetime.datetime"
    """The end of the day-aligned UTC window, inclusive."""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingMetricsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFindingMetricsRequest:
    out: GetFindingMetricsRequest = {}  # type: ignore[typeddict-item]
    return out
