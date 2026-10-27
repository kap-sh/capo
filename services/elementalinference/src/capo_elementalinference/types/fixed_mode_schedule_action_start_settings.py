"""Generated from Smithy shape ``com.amazonaws.elementalinference#FixedModeScheduleActionStartSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime


class FixedModeScheduleActionStartSettings(TypedDict, closed=True):
    scheduled_at: "datetime.datetime"
    """<p>The UTC time at which the action runs. Specify the time in whole seconds. For the range of times that you can specify, see the AWS Elemental Inference User Guide. </p> <p>This time is approximate. The change can take a few minutes to take effect on the media that the feed is processing. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FixedModeScheduleActionStartSettings) -> dict:
    out: dict = {}
    import capo_elementalinference.types._prelude.timestamp

    out["scheduledAt"] = (
        capo_elementalinference.types._prelude.timestamp.serialize_json(
            value["scheduled_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> FixedModeScheduleActionStartSettings:
    out: FixedModeScheduleActionStartSettings = {}  # type: ignore[typeddict-item]
    if data.get("scheduledAt") is not None:
        import capo_elementalinference.types._prelude.timestamp

        out["scheduled_at"] = (
            capo_elementalinference.types._prelude.timestamp.deserialize_json(
                data["scheduledAt"]
            )
        )
    else:
        import datetime

        out["scheduled_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
