"""Generated from Smithy shape ``com.amazonaws.continuum#DisassociateCollectorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.collector_arn
    import capo_continuum.types.environment_id


class DisassociateCollectorInput(TypedDict, closed=True):
    environment_id: "capo_continuum.types.environment_id.EnvironmentId"
    """The unique identifier of the Environment whose associations are updated."""
    collector_arn: "capo_continuum.types.collector_arn.CollectorArn"
    """The ARN of the Collector to disassociate from this Environment."""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateCollectorInput) -> dict:
    out: dict = {}
    out["collectorArn"] = value["collector_arn"]
    return out


def deserialize_json(data: dict) -> DisassociateCollectorInput:
    out: DisassociateCollectorInput = {}  # type: ignore[typeddict-item]
    if data.get("collectorArn") is not None:
        out["collector_arn"] = data["collectorArn"]
    else:
        out["collector_arn"] = ""
    return out
