"""Generated from Smithy shape ``com.amazonaws.applicationsignals#GroupingAttributeDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_signals.types.grouping_source_key_string_list
    import capo_application_signals.types.grouping_string


class GroupingAttributeDefinition(TypedDict, closed=True):
    grouping_name: "capo_application_signals.types.grouping_string.GroupingString"
    """<p>The friendly name for this grouping attribute, such as <code>BusinessUnit</code> or <code>Environment</code>. This name is used to identify the grouping in the console and APIs.</p>"""
    grouping_source_keys: NotRequired[
        "capo_application_signals.types.grouping_source_key_string_list.GroupingSourceKeyStringList"
    ]
    """<p>An array of source keys used to derive the grouping attribute value from telemetry data, Amazon Web Services tags, or other sources. For example, ["business_unit", "team"] would look for values in those fields.</p>"""
    default_grouping_value: NotRequired[
        "capo_application_signals.types.grouping_string.GroupingString"
    ]
    """<p>The default value to use for this grouping attribute when no value can be derived from the source keys. This ensures all services have a grouping value even if the source data is missing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupingAttributeDefinition) -> dict:
    out: dict = {}
    out["GroupingName"] = value["grouping_name"]
    if "grouping_source_keys" in value:
        import capo_application_signals.types.grouping_source_key_string_list

        out["GroupingSourceKeys"] = (
            capo_application_signals.types.grouping_source_key_string_list.serialize_json(
                value["grouping_source_keys"]
            )
        )
    if "default_grouping_value" in value:
        out["DefaultGroupingValue"] = value["default_grouping_value"]
    return out


def deserialize_json(data: dict) -> GroupingAttributeDefinition:
    out: GroupingAttributeDefinition = {}  # type: ignore[typeddict-item]
    if data.get("GroupingName") is not None:
        out["grouping_name"] = data["GroupingName"]
    else:
        raise DeserializationError("GroupingAttributeDefinition.grouping_name required")
    if data.get("GroupingSourceKeys") is not None:
        import capo_application_signals.types.grouping_source_key_string_list

        out["grouping_source_keys"] = (
            capo_application_signals.types.grouping_source_key_string_list.deserialize_json(
                data["GroupingSourceKeys"]
            )
        )
    if data.get("DefaultGroupingValue") is not None:
        out["default_grouping_value"] = data["DefaultGroupingValue"]
    return out
