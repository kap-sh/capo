"""Generated from Smithy shape ``com.amazonaws.applicationsignals#GroupingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_application_signals.types.grouping_attribute_definitions


class GroupingConfiguration(TypedDict, closed=True):
    grouping_attribute_definitions: "capo_application_signals.types.grouping_attribute_definitions.GroupingAttributeDefinitions"
    """<p>An array of grouping attribute definitions that specify how services should be grouped based on various attributes and source keys.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when this grouping configuration was last updated. When used in a raw HTTP Query API, it is formatted as epoch time in seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupingConfiguration) -> dict:
    out: dict = {}
    import capo_application_signals.types.grouping_attribute_definitions

    out["GroupingAttributeDefinitions"] = (
        capo_application_signals.types.grouping_attribute_definitions.serialize_json(
            value["grouping_attribute_definitions"]
        )
    )
    import capo_application_signals.types._prelude.timestamp

    out["UpdatedAt"] = capo_application_signals.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> GroupingConfiguration:
    out: GroupingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("GroupingAttributeDefinitions") is not None:
        import capo_application_signals.types.grouping_attribute_definitions

        out["grouping_attribute_definitions"] = (
            capo_application_signals.types.grouping_attribute_definitions.deserialize_json(
                data["GroupingAttributeDefinitions"]
            )
        )
    else:
        out["grouping_attribute_definitions"] = []
    if data.get("UpdatedAt") is not None:
        import capo_application_signals.types._prelude.timestamp

        out["updated_at"] = (
            capo_application_signals.types._prelude.timestamp.deserialize_json(
                data["UpdatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
