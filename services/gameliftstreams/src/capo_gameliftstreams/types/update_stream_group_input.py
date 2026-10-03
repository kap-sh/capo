"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#UpdateStreamGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gameliftstreams.types.description
    import capo_gameliftstreams.types.identifier
    import capo_gameliftstreams.types.location_configurations


class UpdateStreamGroupInput(TypedDict, closed=True):
    identifier: "capo_gameliftstreams.types.identifier.Identifier"
    """<p>An <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p>"""
    location_configurations: NotRequired[
        "capo_gameliftstreams.types.location_configurations.LocationConfigurations"
    ]
    """<p> A set of one or more locations and the streaming capacity for each location. </p>"""
    description: NotRequired["capo_gameliftstreams.types.description.Description"]
    """<p>A descriptive label for the stream group.</p>"""
    default_application_identifier: NotRequired[
        "capo_gameliftstreams.types.identifier.Identifier"
    ]
    """<p>The unique identifier of the Amazon GameLift Streams application that you want to set as the default application in a stream group. The application that you specify must be in <code>READY</code> status. The default application is pre-cached on always-on compute resources, reducing stream startup times. Other applications are automatically cached as needed.</p> <p>Note that this parameter only sets the default application in a stream group. To associate a new application to an existing stream group, you must use <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_AssociateApplications.html">AssociateApplications</a>.</p> <p>When you switch default applications in a stream group, it can take up to a few hours for the new default application to be pre-cached.</p> <p>This value is an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the application resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. Example ID: <code>a-9ZY8X7Wv6</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateStreamGroupInput) -> dict:
    out: dict = {}
    if "location_configurations" in value:
        import capo_gameliftstreams.types.location_configurations

        out["LocationConfigurations"] = (
            capo_gameliftstreams.types.location_configurations.serialize_json(
                value["location_configurations"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "default_application_identifier" in value:
        out["DefaultApplicationIdentifier"] = value["default_application_identifier"]
    return out


def deserialize_json(data: dict) -> UpdateStreamGroupInput:
    out: UpdateStreamGroupInput = {}  # type: ignore[typeddict-item]
    if data.get("LocationConfigurations") is not None:
        import capo_gameliftstreams.types.location_configurations

        out["location_configurations"] = (
            capo_gameliftstreams.types.location_configurations.deserialize_json(
                data["LocationConfigurations"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DefaultApplicationIdentifier") is not None:
        out["default_application_identifier"] = data["DefaultApplicationIdentifier"]
    return out
