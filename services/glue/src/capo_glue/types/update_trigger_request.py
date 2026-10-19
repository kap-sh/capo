"""Generated from Smithy shape ``com.amazonaws.glue#UpdateTriggerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.name_string
    import capo_glue.types.trigger_update


class UpdateTriggerRequest(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>The name of the trigger to update.</p>"""
    trigger_update: "capo_glue.types.trigger_update.TriggerUpdate"
    """<p>The new values with which to update the trigger.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTriggerRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.trigger_update

    out["TriggerUpdate"] = capo_glue.types.trigger_update.serialize_aws_json_1_1(
        value["trigger_update"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTriggerRequest:
    out: UpdateTriggerRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("TriggerUpdate") is not None:
        import capo_glue.types.trigger_update

        out["trigger_update"] = capo_glue.types.trigger_update.deserialize_aws_json_1_1(
            data["TriggerUpdate"]
        )
    else:
        raise DeserializationError("UpdateTriggerRequest.trigger_update required")
    return out
