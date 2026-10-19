"""Generated from Smithy shape ``com.amazonaws.datazone#PostLineageEventInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.client_token
    import capo_datazone.types.domain_id
    import capo_datazone.types.lineage_event


class PostLineageEventInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to post a data lineage event.</p>"""
    event: "capo_datazone.types.lineage_event.LineageEvent"
    """<p>The data lineage event that you want to post. Only open-lineage run event are supported as events. </p>"""
    client_token: NotRequired["capo_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PostLineageEventInput) -> dict:
    out: dict = {}
    import capo_datazone.types.lineage_event

    out["event"] = capo_datazone.types.lineage_event.serialize_json(value["event"])
    return out


def deserialize_json(data: dict) -> PostLineageEventInput:
    out: PostLineageEventInput = {}  # type: ignore[typeddict-item]
    if data.get("event") is not None:
        import capo_datazone.types.lineage_event

        out["event"] = capo_datazone.types.lineage_event.deserialize_json(data["event"])
    else:
        out["event"] = b""
    return out


def redact_sensitive(value: PostLineageEventInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "event" in value:
        out["event"] = "*** Sensitive Data Redacted ***"
    return out
