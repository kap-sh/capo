"""Generated from Smithy shape ``com.amazonaws.proton#RepositorySyncEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class RepositorySyncEvent(TypedDict, closed=True):
    type: "str"
    """<p>The type of event.</p>"""
    external_id: NotRequired["str"]
    """<p>The external ID of the sync event.</p>"""
    time: "datetime.datetime"
    """<p>The time that the sync event occurred.</p>"""
    event: "str"
    """<p>Event detail for a repository sync attempt.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RepositorySyncEvent) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    import capo_proton.types._prelude.timestamp

    out["time"] = capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["time"]
    )
    out["event"] = value["event"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RepositorySyncEvent:
    out: RepositorySyncEvent = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("time") is not None:
        import capo_proton.types._prelude.timestamp

        out["time"] = capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
            data["time"]
        )
    else:
        import datetime

        out["time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("event") is not None:
        out["event"] = data["event"]
    else:
        out["event"] = ""
    return out
