"""Generated from Smithy shape ``com.amazonaws.keyspaces#ColumnDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_keyspaces.types.generic_string


class ColumnDefinition(TypedDict, closed=True):
    name: "capo_keyspaces.types.generic_string.GenericString"
    """<p>The name of the column.</p>"""
    type: "capo_keyspaces.types.generic_string.GenericString"
    """<p>The data type of the column. For a list of available data types, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.elements.html#cql.data-types">Data types</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ColumnDefinition) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["type"] = value["type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ColumnDefinition:
    out: ColumnDefinition = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ColumnDefinition.name required")
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError("ColumnDefinition.type required")
    return out
