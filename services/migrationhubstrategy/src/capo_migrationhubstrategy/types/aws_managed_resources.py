"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#AwsManagedResources``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.aws_managed_target_destinations


class AwsManagedResources(TypedDict, closed=True):
    target_destination: "capo_migrationhubstrategy.types.aws_managed_target_destinations.AwsManagedTargetDestinations"
    """<p> The choice of application destination that you specify. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsManagedResources) -> dict:
    out: dict = {}
    import capo_migrationhubstrategy.types.aws_managed_target_destinations

    out["targetDestination"] = (
        capo_migrationhubstrategy.types.aws_managed_target_destinations.serialize_json(
            value["target_destination"]
        )
    )
    return out


def deserialize_json(data: dict) -> AwsManagedResources:
    out: AwsManagedResources = {}  # type: ignore[typeddict-item]
    if data.get("targetDestination") is not None:
        import capo_migrationhubstrategy.types.aws_managed_target_destinations

        out["target_destination"] = (
            capo_migrationhubstrategy.types.aws_managed_target_destinations.deserialize_json(
                data["targetDestination"]
            )
        )
    else:
        out["target_destination"] = []
    return out
