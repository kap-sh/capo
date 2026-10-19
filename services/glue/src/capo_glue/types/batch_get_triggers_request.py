"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetTriggersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.trigger_name_list


class BatchGetTriggersRequest(TypedDict, closed=True):
    trigger_names: "capo_glue.types.trigger_name_list.TriggerNameList"
    """<p>A list of trigger names, which may be the names returned from the <code>ListTriggers</code> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetTriggersRequest) -> dict:
    out: dict = {}
    import capo_glue.types.trigger_name_list

    out["TriggerNames"] = capo_glue.types.trigger_name_list.serialize_aws_json_1_1(
        value["trigger_names"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetTriggersRequest:
    out: BatchGetTriggersRequest = {}  # type: ignore[typeddict-item]
    if data.get("TriggerNames") is not None:
        import capo_glue.types.trigger_name_list

        out["trigger_names"] = (
            capo_glue.types.trigger_name_list.deserialize_aws_json_1_1(
                data["TriggerNames"]
            )
        )
    else:
        out["trigger_names"] = []
    return out
