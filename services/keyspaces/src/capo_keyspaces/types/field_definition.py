"""Generated from Smithy shape ``com.amazonaws.keyspaces#FieldDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_keyspaces.types.generic_string


class FieldDefinition(TypedDict, closed=True):
    name: "capo_keyspaces.types.generic_string.GenericString"
    """<p> The identifier. </p>"""
    type: "capo_keyspaces.types.generic_string.GenericString"
    """<p> Any supported Cassandra data type, including collections and other user-defined types that are contained in the same keyspace. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/cassandra-apis.html#cassandra-data-type">Cassandra data type support</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FieldDefinition) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["type"] = value["type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> FieldDefinition:
    out: FieldDefinition = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("FieldDefinition.name required")
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError("FieldDefinition.type required")
    return out
