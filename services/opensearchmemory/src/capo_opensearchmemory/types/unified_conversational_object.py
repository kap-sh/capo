"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#UnifiedConversationalObject``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.message_list


class UnifiedConversationalObject(TypedDict, closed=True):
    messages: "capo_opensearchmemory.types.message_list.MessageList"
    """<p>The conversation turns, in order. The order matters for extraction.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UnifiedConversationalObject) -> dict:
    out: dict = {}
    import capo_opensearchmemory.types.message_list

    out["messages"] = capo_opensearchmemory.types.message_list.serialize_aws_json_1_0(
        value["messages"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UnifiedConversationalObject:
    out: UnifiedConversationalObject = {}  # type: ignore[typeddict-item]
    if data.get("messages") is not None:
        import capo_opensearchmemory.types.message_list

        out["messages"] = (
            capo_opensearchmemory.types.message_list.deserialize_aws_json_1_0(
                data["messages"]
            )
        )
    else:
        out["messages"] = []
    return out


def redact_sensitive(value: UnifiedConversationalObject) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "messages" in value:
        import capo_opensearchmemory.types.message_list

        out["messages"] = capo_opensearchmemory.types.message_list.redact_sensitive(
            value["messages"]
        )
    return out
