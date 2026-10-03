"""Generated from Smithy shape ``com.amazonaws.synthetics#BaseScreenshot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_synthetics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_synthetics.types.base_screenshot_ignore_coordinates
    import capo_synthetics.types.string


class BaseScreenshot(TypedDict, closed=True):
    screenshot_name: "capo_synthetics.types.string.String"
    """<p>The name of the screenshot. This is generated the first time the canary is run after the <code>UpdateCanary</code> operation that specified for this canary to perform visual monitoring.</p>"""
    ignore_coordinates: NotRequired[
        "capo_synthetics.types.base_screenshot_ignore_coordinates.BaseScreenshotIgnoreCoordinates"
    ]
    """<p>Coordinates that define the part of a screen to ignore during screenshot comparisons. To obtain the coordinates to use here, use the CloudWatch console to draw the boundaries on the screen. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/synthetics_canaries_deletion.html"> Editing or deleting a canary</a> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BaseScreenshot) -> dict:
    out: dict = {}
    out["ScreenshotName"] = value["screenshot_name"]
    if "ignore_coordinates" in value:
        import capo_synthetics.types.base_screenshot_ignore_coordinates

        out["IgnoreCoordinates"] = (
            capo_synthetics.types.base_screenshot_ignore_coordinates.serialize_json(
                value["ignore_coordinates"]
            )
        )
    return out


def deserialize_json(data: dict) -> BaseScreenshot:
    out: BaseScreenshot = {}  # type: ignore[typeddict-item]
    if data.get("ScreenshotName") is not None:
        out["screenshot_name"] = data["ScreenshotName"]
    else:
        raise DeserializationError("BaseScreenshot.screenshot_name required")
    if data.get("IgnoreCoordinates") is not None:
        import capo_synthetics.types.base_screenshot_ignore_coordinates

        out["ignore_coordinates"] = (
            capo_synthetics.types.base_screenshot_ignore_coordinates.deserialize_json(
                data["IgnoreCoordinates"]
            )
        )
    return out
