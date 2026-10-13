"""Generated from Smithy shape ``com.amazonaws.novaact#CallResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import capo_nova_act.types.call_id
    import capo_nova_act.types.call_result_contents


class CallResult(TypedDict, closed=True):
    call_id: NotRequired["capo_nova_act.types.call_id.CallId"]
    """<p>The identifier of the tool call that this result corresponds to.</p>"""
    content: "capo_nova_act.types.call_result_contents.CallResultContents"
    """<p>The content returned by the tool execution, which can include text or other media types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CallResult) -> dict:
    out: dict = {}
    if "call_id" in value:
        out["callId"] = value["call_id"]
    import capo_nova_act.types.call_result_contents

    out["content"] = capo_nova_act.types.call_result_contents.serialize_json(
        value["content"]
    )
    return out


def deserialize_json(data: dict) -> CallResult:
    out: CallResult = {}  # type: ignore[typeddict-item]
    if data.get("callId") is not None:
        out["call_id"] = data["callId"]
    if data.get("content") is not None:
        import capo_nova_act.types.call_result_contents

        out["content"] = capo_nova_act.types.call_result_contents.deserialize_json(
            data["content"]
        )
    else:
        raise DeserializationError("CallResult.content required")
    return out


def redact_sensitive(value: CallResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        import capo_nova_act.types.call_result_contents

        out["content"] = capo_nova_act.types.call_result_contents.redact_sensitive(
            value["content"]
        )
    return out
