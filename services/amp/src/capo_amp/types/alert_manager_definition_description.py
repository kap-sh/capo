"""Generated from Smithy shape ``com.amazonaws.amp#AlertManagerDefinitionDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_amp.types.alert_manager_definition_data
    import capo_amp.types.alert_manager_definition_status


class AlertManagerDefinitionDescription(TypedDict, closed=True):
    status: (
        "capo_amp.types.alert_manager_definition_status.AlertManagerDefinitionStatus"
    )
    """<p>A structure that displays the current status of the alert manager definition..</p>"""
    data: "capo_amp.types.alert_manager_definition_data.AlertManagerDefinitionData"
    """<p>The actual alert manager definition.</p> <p>For details about the alert manager definition, see <a href="https://docs.aws.amazon.com/prometheus/latest/APIReference/yaml-AlertManagerDefinitionData.html">AlertManagedDefinitionData</a>.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time that the alert manager definition was created.</p>"""
    modified_at: "datetime.datetime"
    """<p>The date and time that the alert manager definition was most recently changed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AlertManagerDefinitionDescription) -> dict:
    out: dict = {}
    import capo_amp.types.alert_manager_definition_status

    out["status"] = capo_amp.types.alert_manager_definition_status.serialize_json(
        value["status"]
    )
    import capo_amp.types.alert_manager_definition_data

    out["data"] = capo_amp.types.alert_manager_definition_data.serialize_json(
        value["data"]
    )
    import capo_amp.types._prelude.timestamp

    out["createdAt"] = capo_amp.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_amp.types._prelude.timestamp

    out["modifiedAt"] = capo_amp.types._prelude.timestamp.serialize_json(
        value["modified_at"]
    )
    return out


def deserialize_json(data: dict) -> AlertManagerDefinitionDescription:
    out: AlertManagerDefinitionDescription = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_amp.types.alert_manager_definition_status

        out["status"] = capo_amp.types.alert_manager_definition_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("AlertManagerDefinitionDescription.status required")
    if data.get("data") is not None:
        import capo_amp.types.alert_manager_definition_data

        out["data"] = capo_amp.types.alert_manager_definition_data.deserialize_json(
            data["data"]
        )
    else:
        raise DeserializationError("AlertManagerDefinitionDescription.data required")
    if data.get("createdAt") is not None:
        import capo_amp.types._prelude.timestamp

        out["created_at"] = capo_amp.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError(
            "AlertManagerDefinitionDescription.created_at required"
        )
    if data.get("modifiedAt") is not None:
        import capo_amp.types._prelude.timestamp

        out["modified_at"] = capo_amp.types._prelude.timestamp.deserialize_json(
            data["modifiedAt"]
        )
    else:
        raise DeserializationError(
            "AlertManagerDefinitionDescription.modified_at required"
        )
    return out
