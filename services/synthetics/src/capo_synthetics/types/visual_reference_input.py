"""Generated from Smithy shape ``com.amazonaws.synthetics#VisualReferenceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_synthetics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_synthetics.types.base_screenshots
    import capo_synthetics.types.browser_type
    import capo_synthetics.types.string


class VisualReferenceInput(TypedDict, closed=True):
    base_screenshots: NotRequired[
        "capo_synthetics.types.base_screenshots.BaseScreenshots"
    ]
    """<p>An array of screenshots that will be used as the baseline for visual monitoring in future runs of this canary. If there is a screenshot that you don't want to be used for visual monitoring, remove it from this array.</p>"""
    base_canary_run_id: "capo_synthetics.types.string.String"
    """<p>Specifies which canary run to use the screenshots from as the baseline for future visual monitoring with this canary. Valid values are <code>nextrun</code> to use the screenshots from the next run after this update is made, <code>lastrun</code> to use the screenshots from the most recent run before this update was made, or the value of <code>Id</code> in the <a href="https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryRun.html"> CanaryRun</a> from a run of this a canary in the past 31 days. If you specify the <code>Id</code> of a canary run older than 31 days, the operation returns a 400 validation exception error..</p>"""
    browser_type: NotRequired["capo_synthetics.types.browser_type.BrowserType"]
    """<p>The browser type associated with this visual reference.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VisualReferenceInput) -> dict:
    out: dict = {}
    if "base_screenshots" in value:
        import capo_synthetics.types.base_screenshots

        out["BaseScreenshots"] = capo_synthetics.types.base_screenshots.serialize_json(
            value["base_screenshots"]
        )
    out["BaseCanaryRunId"] = value["base_canary_run_id"]
    if "browser_type" in value:
        import capo_synthetics.types.browser_type

        out["BrowserType"] = capo_synthetics.types.browser_type.serialize_json(
            value["browser_type"]
        )
    return out


def deserialize_json(data: dict) -> VisualReferenceInput:
    out: VisualReferenceInput = {}  # type: ignore[typeddict-item]
    if data.get("BaseScreenshots") is not None:
        import capo_synthetics.types.base_screenshots

        out["base_screenshots"] = (
            capo_synthetics.types.base_screenshots.deserialize_json(
                data["BaseScreenshots"]
            )
        )
    if data.get("BaseCanaryRunId") is not None:
        out["base_canary_run_id"] = data["BaseCanaryRunId"]
    else:
        raise DeserializationError("VisualReferenceInput.base_canary_run_id required")
    if data.get("BrowserType") is not None:
        import capo_synthetics.types.browser_type

        out["browser_type"] = capo_synthetics.types.browser_type.deserialize_json(
            data["BrowserType"]
        )
    return out
