"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateContainerFleetOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.container_fleet


class CreateContainerFleetOutput(TypedDict, closed=True):
    container_fleet: NotRequired["capo_gamelift.types.container_fleet.ContainerFleet"]
    """<p>The properties for the new container fleet, including current status. All fleets are initially placed in <code>PENDING</code> status. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateContainerFleetOutput) -> dict:
    out: dict = {}
    if "container_fleet" in value:
        import capo_gamelift.types.container_fleet

        out["ContainerFleet"] = (
            capo_gamelift.types.container_fleet.serialize_aws_json_1_1(
                value["container_fleet"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateContainerFleetOutput:
    out: CreateContainerFleetOutput = {}  # type: ignore[typeddict-item]
    if data.get("ContainerFleet") is not None:
        import capo_gamelift.types.container_fleet

        out["container_fleet"] = (
            capo_gamelift.types.container_fleet.deserialize_aws_json_1_1(
                data["ContainerFleet"]
            )
        )
    return out


def redact_sensitive(value: CreateContainerFleetOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "container_fleet" in value:
        import capo_gamelift.types.container_fleet

        out["container_fleet"] = capo_gamelift.types.container_fleet.redact_sensitive(
            value["container_fleet"]
        )
    return out
