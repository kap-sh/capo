"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribePeriodontalChartEvent``."""

import json
from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_connecthealth._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_connecthealth.types.periodontal_review_list
    import capo_connecthealth.types.periodontal_tooth_list


class MedicalScribePeriodontalChartEvent(TypedDict, closed=True):
    snapshot_version: "int"
    """<p>The version of this snapshot. Versions increase within a session and can skip values. Keep the snapshot with the highest version and ignore any event whose version is not higher, including after you reconnect to the session. Versions of checklist events and periodontal chart events are independent.</p>"""
    teeth: "capo_connecthealth.types.periodontal_tooth_list.PeriodontalToothList"
    """<p>The teeth that have a recorded value or are marked missing, in ascending <code>toothNumber</code> order.</p>"""
    review_items: NotRequired[
        "capo_connecthealth.types.periodontal_review_list.PeriodontalReviewList"
    ]
    """<p>Items that need the clinician's confirmation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribePeriodontalChartEvent) -> dict:
    out: dict = {}
    out["snapshotVersion"] = value["snapshot_version"]
    import capo_connecthealth.types.periodontal_tooth_list

    out["teeth"] = capo_connecthealth.types.periodontal_tooth_list.serialize_json(
        value["teeth"]
    )
    if "review_items" in value:
        import capo_connecthealth.types.periodontal_review_list

        out["reviewItems"] = (
            capo_connecthealth.types.periodontal_review_list.serialize_json(
                value["review_items"]
            )
        )
    return out


def deserialize_json(data: dict) -> MedicalScribePeriodontalChartEvent:
    out: MedicalScribePeriodontalChartEvent = {}  # type: ignore[typeddict-item]
    if data.get("snapshotVersion") is not None:
        out["snapshot_version"] = data["snapshotVersion"]
    else:
        out["snapshot_version"] = 0
    if data.get("teeth") is not None:
        import capo_connecthealth.types.periodontal_tooth_list

        out["teeth"] = capo_connecthealth.types.periodontal_tooth_list.deserialize_json(
            data["teeth"]
        )
    else:
        out["teeth"] = []
    if data.get("reviewItems") is not None:
        import capo_connecthealth.types.periodontal_review_list

        out["review_items"] = (
            capo_connecthealth.types.periodontal_review_list.deserialize_json(
                data["reviewItems"]
            )
        )
    return out


def serialize_event_json(value: MedicalScribePeriodontalChartEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "periodontalChartEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> MedicalScribePeriodontalChartEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: MedicalScribePeriodontalChartEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out


def redact_sensitive(value: MedicalScribePeriodontalChartEvent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "teeth" in value:
        import capo_connecthealth.types.periodontal_tooth_list

        out["teeth"] = capo_connecthealth.types.periodontal_tooth_list.redact_sensitive(
            value["teeth"]
        )
    if "review_items" in value:
        import capo_connecthealth.types.periodontal_review_list

        out["review_items"] = (
            capo_connecthealth.types.periodontal_review_list.redact_sensitive(
                value["review_items"]
            )
        )
    return out
