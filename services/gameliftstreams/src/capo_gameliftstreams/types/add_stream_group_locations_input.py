"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#AddStreamGroupLocationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_gameliftstreams.errors import DeserializationError

if TYPE_CHECKING:
    import capo_gameliftstreams.types.identifier
    import capo_gameliftstreams.types.location_configurations


class AddStreamGroupLocationsInput(TypedDict, closed=True):
    identifier: "capo_gameliftstreams.types.identifier.Identifier"
    """<p> A stream group to add the specified locations to. </p> <p>This value is an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p>"""
    location_configurations: (
        "capo_gameliftstreams.types.location_configurations.LocationConfigurations"
    )
    """<p> A set of one or more locations and the streaming capacity for each location. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddStreamGroupLocationsInput) -> dict:
    out: dict = {}
    import capo_gameliftstreams.types.location_configurations

    out["LocationConfigurations"] = (
        capo_gameliftstreams.types.location_configurations.serialize_json(
            value["location_configurations"]
        )
    )
    return out


def deserialize_json(data: dict) -> AddStreamGroupLocationsInput:
    out: AddStreamGroupLocationsInput = {}  # type: ignore[typeddict-item]
    if data.get("LocationConfigurations") is not None:
        import capo_gameliftstreams.types.location_configurations

        out["location_configurations"] = (
            capo_gameliftstreams.types.location_configurations.deserialize_json(
                data["LocationConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "AddStreamGroupLocationsInput.location_configurations required"
        )
    return out
