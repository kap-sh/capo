"""Generated from Smithy shape ``com.amazonaws.gamelift#AnywhereConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.non_negative_limited_length_double


class AnywhereConfiguration(TypedDict, closed=True):
    cost: NotRequired[
        "capo_gamelift.types.non_negative_limited_length_double.NonNegativeLimitedLengthDouble"
    ]
    """<p>The cost to run your fleet per hour. Amazon GameLift Servers uses the provided cost of your fleet to balance usage in queues. For more information about queues, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-intro.html">Setting up queues</a> in the <i>Amazon GameLift Servers Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnywhereConfiguration) -> dict:
    out: dict = {}
    if "cost" in value:
        out["Cost"] = value["cost"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AnywhereConfiguration:
    out: AnywhereConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Cost") is not None:
        out["cost"] = data["Cost"]
    return out
