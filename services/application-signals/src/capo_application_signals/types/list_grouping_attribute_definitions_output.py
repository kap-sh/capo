"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ListGroupingAttributeDefinitionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_application_signals.types.grouping_attribute_definitions
    import capo_application_signals.types.next_token


class ListGroupingAttributeDefinitionsOutput(TypedDict, closed=True):
    grouping_attribute_definitions: "capo_application_signals.types.grouping_attribute_definitions.GroupingAttributeDefinitions"
    """<p>An array of structures, where each structure contains information about one grouping attribute definition, including the grouping name, source keys, and default values.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the grouping configuration was last updated. When used in a raw HTTP Query API, it is formatted as epoch time in seconds.</p>"""
    next_token: NotRequired["capo_application_signals.types.next_token.NextToken"]
    """<p>Include this value in your next use of this API to get the next set of grouping attribute definitions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupingAttributeDefinitionsOutput) -> dict:
    out: dict = {}
    import capo_application_signals.types.grouping_attribute_definitions

    out["GroupingAttributeDefinitions"] = (
        capo_application_signals.types.grouping_attribute_definitions.serialize_json(
            value["grouping_attribute_definitions"]
        )
    )
    if "updated_at" in value:
        import capo_application_signals.types._prelude.timestamp

        out["UpdatedAt"] = (
            capo_application_signals.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGroupingAttributeDefinitionsOutput:
    out: ListGroupingAttributeDefinitionsOutput = {}  # type: ignore[typeddict-item]
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
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
