"""Generated from Smithy shape ``com.amazonaws.sns#BatchResultErrorEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.boolean
    import capo_sns.types.string


class BatchResultErrorEntry(TypedDict, closed=True):
    id: "capo_sns.types.string.String"
    """<p>The <code>Id</code> of an entry in a batch request</p>"""
    code: "capo_sns.types.string.String"
    """<p>An error code representing why the action failed on this entry.</p>"""
    message: NotRequired["capo_sns.types.string.String"]
    """<p>A message explaining why the action failed on this entry.</p>"""
    sender_fault: "capo_sns.types.boolean.boolean"
    """<p>Specifies whether the error happened due to the caller of the batch API action.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: BatchResultErrorEntry, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Id", str(value["id"])))
    pairs.append((f"{key_prefix}Code", str(value["code"])))
    if "message" in value:
        pairs.append((f"{key_prefix}Message", str(value["message"])))
    pairs.append(
        (
            f"{key_prefix}SenderFault",
            "true" if value.get("sender_fault", False) else "false",
        )
    )


def deserialize_query(el: Element) -> BatchResultErrorEntry:
    out: BatchResultErrorEntry = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        out["id"] = ""
    child_code = el.find("Code")
    if child_code is not None:
        out["code"] = str(child_code.text or "")
    else:
        out["code"] = ""
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    child_sender_fault = el.find("SenderFault")
    if child_sender_fault is not None:
        out["sender_fault"] = (child_sender_fault.text or "").lower() == "true"
    else:
        out["sender_fault"] = False
    return out
