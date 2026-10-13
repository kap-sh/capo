"""Generated from Smithy shape ``com.amazonaws.quicksight#CalculatedField``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.calculated_field_expression
    import capo_quicksight.types.column_name
    import capo_quicksight.types.data_set_identifier
    import capo_quicksight.types.topic_identifier


class CalculatedField(TypedDict, closed=True):
    data_set_identifier: "capo_quicksight.types.data_set_identifier.DataSetIdentifier"
    """<p>The data set that is used in this calculated field.</p>"""
    topic_identifier: NotRequired[
        "capo_quicksight.types.topic_identifier.TopicIdentifier"
    ]
    """<p>The topic that is used in this calculated field.</p>"""
    name: "capo_quicksight.types.column_name.ColumnName"
    """<p>The name of the calculated field.</p>"""
    expression: (
        "capo_quicksight.types.calculated_field_expression.CalculatedFieldExpression"
    )
    """<p>The expression of the calculated field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalculatedField) -> dict:
    out: dict = {}
    out["DataSetIdentifier"] = value.get("data_set_identifier", "")
    if "topic_identifier" in value:
        out["TopicIdentifier"] = value["topic_identifier"]
    out["Name"] = value["name"]
    out["Expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> CalculatedField:
    out: CalculatedField = {}  # type: ignore[typeddict-item]
    if data.get("DataSetIdentifier") is not None:
        out["data_set_identifier"] = data["DataSetIdentifier"]
    else:
        out["data_set_identifier"] = ""
    if data.get("TopicIdentifier") is not None:
        out["topic_identifier"] = data["TopicIdentifier"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CalculatedField.name required")
    if data.get("Expression") is not None:
        out["expression"] = data["Expression"]
    else:
        raise DeserializationError("CalculatedField.expression required")
    return out


def redact_sensitive(value: CalculatedField) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "expression" in value:
        out["expression"] = "*** Sensitive Data Redacted ***"
    return out
