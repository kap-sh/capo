"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormAIVersionLifecycle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_ai_version_status
    import capo_connect.types.timestamp


class EvaluationFormAIVersionLifecycle(TypedDict, closed=True):
    status: "capo_connect.types.evaluation_form_ai_version_status.EvaluationFormAIVersionStatus"
    """<p>The status of the AI version. Valid values:</p> <ul> <li> <p> <code>Latest</code> - The most recent AI version.</p> </li> <li> <p> <code>Preview</code> - An AI version available for preview.</p> </li> <li> <p> <code>Active</code> - An AI version that is currently available.</p> </li> <li> <p> <code>Deprecated</code> - An AI version that is no longer recommended for use.</p> </li> <li> <p> <code>Removed</code> - An AI version that is no longer available.</p> </li> </ul>"""
    start_of_life_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp for when this AI version became available.</p>"""
    end_of_life_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this AI version reaches or reached end of life.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormAIVersionLifecycle) -> dict:
    out: dict = {}
    import capo_connect.types.evaluation_form_ai_version_status

    out["Status"] = capo_connect.types.evaluation_form_ai_version_status.serialize_json(
        value["status"]
    )
    import capo_connect.types.timestamp

    out["StartOfLifeTime"] = capo_connect.types.timestamp.serialize_json(
        value["start_of_life_time"]
    )
    if "end_of_life_time" in value:
        import capo_connect.types.timestamp

        out["EndOfLifeTime"] = capo_connect.types.timestamp.serialize_json(
            value["end_of_life_time"]
        )
    return out


def deserialize_json(data: dict) -> EvaluationFormAIVersionLifecycle:
    out: EvaluationFormAIVersionLifecycle = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_connect.types.evaluation_form_ai_version_status

        out["status"] = (
            capo_connect.types.evaluation_form_ai_version_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_connect.types.evaluation_form_ai_version_status.EvaluationFormAIVersionStatus",
            "",
        )
    if data.get("StartOfLifeTime") is not None:
        import capo_connect.types.timestamp

        out["start_of_life_time"] = capo_connect.types.timestamp.deserialize_json(
            data["StartOfLifeTime"]
        )
    else:
        import datetime

        out["start_of_life_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("EndOfLifeTime") is not None:
        import capo_connect.types.timestamp

        out["end_of_life_time"] = capo_connect.types.timestamp.deserialize_json(
            data["EndOfLifeTime"]
        )
    return out
