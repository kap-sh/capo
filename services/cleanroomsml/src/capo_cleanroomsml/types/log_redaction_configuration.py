"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#LogRedactionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.custom_entity_config
    import capo_cleanroomsml.types.entity_type_list


class LogRedactionConfiguration(TypedDict, closed=True):
    entities_to_redact: "capo_cleanroomsml.types.entity_type_list.EntityTypeList"
    """<p>Specifies the entities to be redacted from logs. Entities to redact are "ALL_PERSONALLY_IDENTIFIABLE_INFORMATION", "NUMBERS","CUSTOM". If CUSTOM is supplied or configured, custom patterns (customDataIdentifiers) should be provided, and the patterns will be redacted in logs or error messages.</p>"""
    custom_entity_config: NotRequired[
        "capo_cleanroomsml.types.custom_entity_config.CustomEntityConfig"
    ]
    """<p>Specifies the configuration for custom entities in the context of log redaction.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogRedactionConfiguration) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types.entity_type_list

    out["entitiesToRedact"] = capo_cleanroomsml.types.entity_type_list.serialize_json(
        value["entities_to_redact"]
    )
    if "custom_entity_config" in value:
        import capo_cleanroomsml.types.custom_entity_config

        out["customEntityConfig"] = (
            capo_cleanroomsml.types.custom_entity_config.serialize_json(
                value["custom_entity_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> LogRedactionConfiguration:
    out: LogRedactionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("entitiesToRedact") is not None:
        import capo_cleanroomsml.types.entity_type_list

        out["entities_to_redact"] = (
            capo_cleanroomsml.types.entity_type_list.deserialize_json(
                data["entitiesToRedact"]
            )
        )
    else:
        raise DeserializationError(
            "LogRedactionConfiguration.entities_to_redact required"
        )
    if data.get("customEntityConfig") is not None:
        import capo_cleanroomsml.types.custom_entity_config

        out["custom_entity_config"] = (
            capo_cleanroomsml.types.custom_entity_config.deserialize_json(
                data["customEntityConfig"]
            )
        )
    return out
