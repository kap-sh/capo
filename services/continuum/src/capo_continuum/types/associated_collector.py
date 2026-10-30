"""Generated from Smithy shape ``com.amazonaws.continuum#AssociatedCollector``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.collector_arn
    import capo_continuum.types.collector_id


class AssociatedCollector(TypedDict, closed=True):
    collector_id: "capo_continuum.types.collector_id.CollectorId"
    """The unique identifier of the associated Collector."""
    collector_arn: "capo_continuum.types.collector_arn.CollectorArn"
    """The ARN of the associated Collector. The account and Region encoded in this ARN identify cross-account and cross-Region associations."""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedCollector) -> dict:
    out: dict = {}
    out["collectorId"] = value["collector_id"]
    out["collectorArn"] = value["collector_arn"]
    return out


def deserialize_json(data: dict) -> AssociatedCollector:
    out: AssociatedCollector = {}  # type: ignore[typeddict-item]
    if data.get("collectorId") is not None:
        out["collector_id"] = data["collectorId"]
    else:
        out["collector_id"] = ""
    if data.get("collectorArn") is not None:
        out["collector_arn"] = data["collectorArn"]
    else:
        out["collector_arn"] = ""
    return out
