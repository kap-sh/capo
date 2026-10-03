"""Generated from Smithy shape ``com.amazonaws.gamelift#LocationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.location_string_model


class LocationConfiguration(TypedDict, closed=True):
    location: NotRequired[
        "capo_gamelift.types.location_string_model.LocationStringModel"
    ]
    """<p>An Amazon Web Services Region code, such as <code>us-west-2</code>. For a list of supported Regions and Local Zones, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html"> Amazon GameLift Servers service locations</a> for managed hosting.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocationConfiguration) -> dict:
    out: dict = {}
    if "location" in value:
        out["Location"] = value["location"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LocationConfiguration:
    out: LocationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    return out
