"""Generated from Smithy shape ``com.amazonaws.synthetics#StopCanaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.canary_name


class StopCanaryRequest(TypedDict, closed=True):
    name: "capo_synthetics.types.canary_name.CanaryName"
    """<p>The name of the canary that you want to stop. To find the names of your canaries, use <a href="https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html">ListCanaries</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopCanaryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopCanaryRequest:
    out: StopCanaryRequest = {}  # type: ignore[typeddict-item]
    return out
