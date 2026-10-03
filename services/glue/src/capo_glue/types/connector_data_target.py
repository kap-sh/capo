"""Generated from Smithy shape ``com.amazonaws.glue#ConnectorDataTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.connector_options
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.node_name
    import capo_glue.types.one_input


class ConnectorDataTarget(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of this target node.</p>"""
    connection_type: (
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    )
    """<p>The <code>connectionType</code>, as provided to the underlying Glue library. This node type supports the following connection types: </p> <ul> <li> <p> <code>opensearch</code> </p> </li> <li> <p> <code>azuresql</code> </p> </li> <li> <p> <code>azurecosmos</code> </p> </li> <li> <p> <code>bigquery</code> </p> </li> <li> <p> <code>saphana</code> </p> </li> <li> <p> <code>teradata</code> </p> </li> <li> <p> <code>vertica</code> </p> </li> </ul>"""
    data: "capo_glue.types.connector_options.ConnectorOptions"
    """<p>A map specifying connection options for the node. You can find standard connection options for the corresponding connection type in the <a href="https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect.html"> Connection parameters</a> section of the Glue documentation.</p>"""
    inputs: NotRequired["capo_glue.types.one_input.OneInput"]
    """<p>The nodes that are inputs to the data target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectorDataTarget) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["ConnectionType"] = value["connection_type"]
    import capo_glue.types.connector_options

    out["Data"] = capo_glue.types.connector_options.serialize_aws_json_1_1(
        value["data"]
    )
    if "inputs" in value:
        import capo_glue.types.one_input

        out["Inputs"] = capo_glue.types.one_input.serialize_aws_json_1_1(
            value["inputs"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectorDataTarget:
    out: ConnectorDataTarget = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ConnectorDataTarget.name required")
    if data.get("ConnectionType") is not None:
        out["connection_type"] = data["ConnectionType"]
    else:
        raise DeserializationError("ConnectorDataTarget.connection_type required")
    if data.get("Data") is not None:
        import capo_glue.types.connector_options

        out["data"] = capo_glue.types.connector_options.deserialize_aws_json_1_1(
            data["Data"]
        )
    else:
        raise DeserializationError("ConnectorDataTarget.data required")
    if data.get("Inputs") is not None:
        import capo_glue.types.one_input

        out["inputs"] = capo_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    return out
