"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribeChecklistEvent``."""

import json
from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_connecthealth._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_connecthealth.types.checklist_list


class MedicalScribeChecklistEvent(TypedDict, closed=True):
    snapshot_version: "int"
    """<p>The version of this snapshot. Versions increase within a session and can skip values. Keep the snapshot with the highest version and ignore any event whose version is not higher, including after you reconnect to the session. Versions of checklist events and periodontal chart events are independent.</p>"""
    checklists: "capo_connecthealth.types.checklist_list.ChecklistList"
    """<p>The checklists for the session. The list is empty when no checklist is active.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeChecklistEvent) -> dict:
    out: dict = {}
    out["snapshotVersion"] = value["snapshot_version"]
    import capo_connecthealth.types.checklist_list

    out["checklists"] = capo_connecthealth.types.checklist_list.serialize_json(
        value["checklists"]
    )
    return out


def deserialize_json(data: dict) -> MedicalScribeChecklistEvent:
    out: MedicalScribeChecklistEvent = {}  # type: ignore[typeddict-item]
    if data.get("snapshotVersion") is not None:
        out["snapshot_version"] = data["snapshotVersion"]
    else:
        out["snapshot_version"] = 0
    if data.get("checklists") is not None:
        import capo_connecthealth.types.checklist_list

        out["checklists"] = capo_connecthealth.types.checklist_list.deserialize_json(
            data["checklists"]
        )
    else:
        out["checklists"] = []
    return out


def serialize_event_json(value: MedicalScribeChecklistEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "checklistEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> MedicalScribeChecklistEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: MedicalScribeChecklistEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out


def redact_sensitive(value: MedicalScribeChecklistEvent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "checklists" in value:
        import capo_connecthealth.types.checklist_list

        out["checklists"] = capo_connecthealth.types.checklist_list.redact_sensitive(
            value["checklists"]
        )
    return out
