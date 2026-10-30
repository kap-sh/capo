"""Generated from Smithy shape ``com.amazonaws.continuum#AssociateCollectorOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_continuum.errors import DeserializationError

if TYPE_CHECKING:
    import capo_continuum.types.associated_collector
    import capo_continuum.types.environment_arn
    import capo_continuum.types.environment_id


class AssociateCollectorOutput(TypedDict, closed=True):
    environment_id: "capo_continuum.types.environment_id.EnvironmentId"
    """The unique identifier of the Environment making the association."""
    environment_arn: "capo_continuum.types.environment_arn.EnvironmentArn"
    """The ARN of the Environment making the association."""
    associated_collector: (
        "capo_continuum.types.associated_collector.AssociatedCollector"
    )
    """The Collector identifier and ARN validated by this operation."""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateCollectorOutput) -> dict:
    out: dict = {}
    out["environmentId"] = value["environment_id"]
    out["environmentArn"] = value["environment_arn"]
    import capo_continuum.types.associated_collector

    out["associatedCollector"] = (
        capo_continuum.types.associated_collector.serialize_json(
            value["associated_collector"]
        )
    )
    return out


def deserialize_json(data: dict) -> AssociateCollectorOutput:
    out: AssociateCollectorOutput = {}  # type: ignore[typeddict-item]
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    if data.get("environmentArn") is not None:
        out["environment_arn"] = data["environmentArn"]
    else:
        out["environment_arn"] = ""
    if data.get("associatedCollector") is not None:
        import capo_continuum.types.associated_collector

        out["associated_collector"] = (
            capo_continuum.types.associated_collector.deserialize_json(
                data["associatedCollector"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateCollectorOutput.associated_collector required"
        )
    return out
