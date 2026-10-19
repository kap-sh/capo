"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetArchiveMessageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.archived_message_id


class GetArchiveMessageRequest(TypedDict, closed=True):
    archived_message_id: "capo_mailmanager.types.archived_message_id.ArchivedMessageId"
    """<p>The unique identifier of the archived email message.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetArchiveMessageRequest) -> dict:
    out: dict = {}
    out["ArchivedMessageId"] = value["archived_message_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetArchiveMessageRequest:
    out: GetArchiveMessageRequest = {}  # type: ignore[typeddict-item]
    if data.get("ArchivedMessageId") is not None:
        out["archived_message_id"] = data["ArchivedMessageId"]
    else:
        out["archived_message_id"] = ""
    return out
