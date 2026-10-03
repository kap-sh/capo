"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#AddStreamGroupLocationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_gameliftstreams.errors import DeserializationError

if TYPE_CHECKING:
    import capo_gameliftstreams.types.identifier
    import capo_gameliftstreams.types.location_states


class AddStreamGroupLocationsOutput(TypedDict, closed=True):
    identifier: "capo_gameliftstreams.types.identifier.Identifier"
    """<p>This value is an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p>"""
    locations: "capo_gameliftstreams.types.location_states.LocationStates"
    """<p>This value is set of locations, including their name, current status, and capacities. </p> <p>A location can be in one of the following states:</p> <ul> <li> <p> <code>ACTIVATING</code>: Amazon GameLift Streams is preparing the location. You cannot stream from, scale the capacity of, or remove this location yet.</p> </li> <li> <p> <code>ACTIVE</code>: The location is provisioned with initial capacity. You can now stream from, scale the capacity of, or remove this location.</p> </li> <li> <p> <code>ERROR</code>: Amazon GameLift Streams failed to set up this location. The <code>StatusReason</code> field describes the error. You can remove this location and try to add it again.</p> </li> <li> <p> <code>REMOVING</code>: Amazon GameLift Streams is working to remove this location. This will release all provisioned capacity for this location in this stream group.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddStreamGroupLocationsOutput) -> dict:
    out: dict = {}
    out["Identifier"] = value["identifier"]
    import capo_gameliftstreams.types.location_states

    out["Locations"] = capo_gameliftstreams.types.location_states.serialize_json(
        value["locations"]
    )
    return out


def deserialize_json(data: dict) -> AddStreamGroupLocationsOutput:
    out: AddStreamGroupLocationsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("AddStreamGroupLocationsOutput.identifier required")
    if data.get("Locations") is not None:
        import capo_gameliftstreams.types.location_states

        out["locations"] = capo_gameliftstreams.types.location_states.deserialize_json(
            data["Locations"]
        )
    else:
        raise DeserializationError("AddStreamGroupLocationsOutput.locations required")
    return out
