"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CustomEntityConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.custom_data_identifier_list


class CustomEntityConfig(TypedDict, closed=True):
    custom_data_identifiers: (
        "capo_cleanroomsml.types.custom_data_identifier_list.CustomDataIdentifierList"
    )
    """<p>Defines data identifiers for the custom entity configuration. Provide this only if CUSTOM redaction is configured. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomEntityConfig) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types.custom_data_identifier_list

    out["customDataIdentifiers"] = (
        capo_cleanroomsml.types.custom_data_identifier_list.serialize_json(
            value["custom_data_identifiers"]
        )
    )
    return out


def deserialize_json(data: dict) -> CustomEntityConfig:
    out: CustomEntityConfig = {}  # type: ignore[typeddict-item]
    if data.get("customDataIdentifiers") is not None:
        import capo_cleanroomsml.types.custom_data_identifier_list

        out["custom_data_identifiers"] = (
            capo_cleanroomsml.types.custom_data_identifier_list.deserialize_json(
                data["customDataIdentifiers"]
            )
        )
    else:
        out["custom_data_identifiers"] = []
    return out
