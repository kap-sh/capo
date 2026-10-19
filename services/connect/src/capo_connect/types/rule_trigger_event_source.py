"""Generated from Smithy shape ``com.amazonaws.connect#RuleTriggerEventSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.event_source_name
    import capo_connect.types.integration_association_id


class RuleTriggerEventSource(TypedDict, closed=True):
    event_source_name: "capo_connect.types.event_source_name.EventSourceName"
    """<p>The name of the event source.</p>"""
    integration_association_id: NotRequired[
        "capo_connect.types.integration_association_id.IntegrationAssociationId"
    ]
    """<p>The identifier for the integration association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleTriggerEventSource) -> dict:
    out: dict = {}
    import capo_connect.types.event_source_name

    out["EventSourceName"] = capo_connect.types.event_source_name.serialize_json(
        value["event_source_name"]
    )
    if "integration_association_id" in value:
        out["IntegrationAssociationId"] = value["integration_association_id"]
    return out


def deserialize_json(data: dict) -> RuleTriggerEventSource:
    out: RuleTriggerEventSource = {}  # type: ignore[typeddict-item]
    if data.get("EventSourceName") is not None:
        import capo_connect.types.event_source_name

        out["event_source_name"] = (
            capo_connect.types.event_source_name.deserialize_json(
                data["EventSourceName"]
            )
        )
    else:
        import typing

        out["event_source_name"] = typing.cast(
            "capo_connect.types.event_source_name.EventSourceName", ""
        )
    if data.get("IntegrationAssociationId") is not None:
        out["integration_association_id"] = data["IntegrationAssociationId"]
    return out
