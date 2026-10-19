"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#SelfManageResources``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.self_manage_target_destinations


class SelfManageResources(TypedDict, closed=True):
    target_destination: "capo_migrationhubstrategy.types.self_manage_target_destinations.SelfManageTargetDestinations"
    """<p> Self-managed resources target destination. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelfManageResources) -> dict:
    out: dict = {}
    import capo_migrationhubstrategy.types.self_manage_target_destinations

    out["targetDestination"] = (
        capo_migrationhubstrategy.types.self_manage_target_destinations.serialize_json(
            value["target_destination"]
        )
    )
    return out


def deserialize_json(data: dict) -> SelfManageResources:
    out: SelfManageResources = {}  # type: ignore[typeddict-item]
    if data.get("targetDestination") is not None:
        import capo_migrationhubstrategy.types.self_manage_target_destinations

        out["target_destination"] = (
            capo_migrationhubstrategy.types.self_manage_target_destinations.deserialize_json(
                data["targetDestination"]
            )
        )
    else:
        out["target_destination"] = []
    return out
