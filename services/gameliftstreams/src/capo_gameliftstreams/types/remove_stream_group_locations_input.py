"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#RemoveStreamGroupLocationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_gameliftstreams.types.identifier
    import capo_gameliftstreams.types.locations_list


class RemoveStreamGroupLocationsInput(TypedDict, closed=True):
    identifier: "capo_gameliftstreams.types.identifier.Identifier"
    """<p> A stream group to remove the specified locations from. </p> <p> This value is an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p>"""
    locations: "capo_gameliftstreams.types.locations_list.LocationsList"
    """<p> A set of locations to remove this stream group. For example, <code>us-east-1</code>.</p> <p> For a complete list of locations that Amazon GameLift Streams supports, refer to <a href="https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html">Regions, quotas, and limitations</a> in the <i>Amazon GameLift Streams Developer Guide</i>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveStreamGroupLocationsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemoveStreamGroupLocationsInput:
    out: RemoveStreamGroupLocationsInput = {}  # type: ignore[typeddict-item]
    return out
