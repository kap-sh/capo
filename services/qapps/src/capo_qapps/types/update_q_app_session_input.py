"""Generated from Smithy shape ``com.amazonaws.qapps#UpdateQAppSessionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.card_value_list
    import capo_qapps.types.instance_id
    import capo_qapps.types.uuid


class UpdateQAppSessionInput(TypedDict, closed=True):
    instance_id: "capo_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    session_id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Q App session to provide input for.</p>"""
    values: NotRequired["capo_qapps.types.card_value_list.CardValueList"]
    """<p>The input values to provide for the current state of the Q App session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQAppSessionInput) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    if "values" in value:
        import capo_qapps.types.card_value_list

        out["values"] = capo_qapps.types.card_value_list.serialize_json(value["values"])
    return out


def deserialize_json(data: dict) -> UpdateQAppSessionInput:
    out: UpdateQAppSessionInput = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("values") is not None:
        import capo_qapps.types.card_value_list

        out["values"] = capo_qapps.types.card_value_list.deserialize_json(
            data["values"]
        )
    return out
