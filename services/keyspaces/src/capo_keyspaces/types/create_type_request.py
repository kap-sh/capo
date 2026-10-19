"""Generated from Smithy shape ``com.amazonaws.keyspaces#CreateTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.field_list
    import capo_keyspaces.types.keyspace_name
    import capo_keyspaces.types.type_name


class CreateTypeRequest(TypedDict, closed=True):
    keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName"
    """<p> The name of the keyspace. </p>"""
    type_name: "capo_keyspaces.types.type_name.TypeName"
    """<p> The name of the user-defined type. </p> <p>UDT names must contain 48 characters or less, must begin with an alphabetic character, and can only contain alpha-numeric characters and underscores. Amazon Keyspaces converts upper case characters automatically into lower case characters. </p> <p>Alternatively, you can declare a UDT name in double quotes. When declaring a UDT name inside double quotes, Amazon Keyspaces preserves upper casing and allows special characters.</p> <p>You can also use double quotes as part of the name when you create the UDT, but you must escape each double quote character with an additional double quote character.</p>"""
    field_definitions: "capo_keyspaces.types.field_list.FieldList"
    """<p> The field definitions, consisting of names and types, that define this type. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateTypeRequest) -> dict:
    out: dict = {}
    out["keyspaceName"] = value["keyspace_name"]
    out["typeName"] = value["type_name"]
    import capo_keyspaces.types.field_list

    out["fieldDefinitions"] = capo_keyspaces.types.field_list.serialize_aws_json_1_0(
        value["field_definitions"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateTypeRequest:
    out: CreateTypeRequest = {}  # type: ignore[typeddict-item]
    if data.get("keyspaceName") is not None:
        out["keyspace_name"] = data["keyspaceName"]
    else:
        out["keyspace_name"] = ""
    if data.get("typeName") is not None:
        out["type_name"] = data["typeName"]
    else:
        out["type_name"] = ""
    if data.get("fieldDefinitions") is not None:
        import capo_keyspaces.types.field_list

        out["field_definitions"] = (
            capo_keyspaces.types.field_list.deserialize_aws_json_1_0(
                data["fieldDefinitions"]
            )
        )
    else:
        out["field_definitions"] = []
    return out
