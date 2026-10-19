"""Generated from Smithy shape ``com.amazonaws.appflow#Task``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.connector_operator
    import capo_appflow.types.destination_field
    import capo_appflow.types.source_fields
    import capo_appflow.types.task_properties_map
    import capo_appflow.types.task_type


class Task(TypedDict, closed=True):
    source_fields: "capo_appflow.types.source_fields.SourceFields"
    """<p> The source fields to which a particular task is applied. </p>"""
    connector_operator: NotRequired[
        "capo_appflow.types.connector_operator.ConnectorOperator"
    ]
    """<p> The operation to be performed on the provided source fields. </p>"""
    destination_field: NotRequired[
        "capo_appflow.types.destination_field.DestinationField"
    ]
    """<p> A field in a destination connector, or a field value against which Amazon AppFlow validates a source field. </p>"""
    task_type: "capo_appflow.types.task_type.TaskType"
    """<p> Specifies the particular task implementation that Amazon AppFlow performs. </p>"""
    task_properties: NotRequired[
        "capo_appflow.types.task_properties_map.TaskPropertiesMap"
    ]
    """<p> A map used to store task-related information. The execution service looks for particular information based on the <code>TaskType</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Task) -> dict:
    out: dict = {}
    import capo_appflow.types.source_fields

    out["sourceFields"] = capo_appflow.types.source_fields.serialize_json(
        value["source_fields"]
    )
    if "connector_operator" in value:
        import capo_appflow.types.connector_operator

        out["connectorOperator"] = capo_appflow.types.connector_operator.serialize_json(
            value["connector_operator"]
        )
    if "destination_field" in value:
        out["destinationField"] = value["destination_field"]
    import capo_appflow.types.task_type

    out["taskType"] = capo_appflow.types.task_type.serialize_json(value["task_type"])
    if "task_properties" in value:
        import capo_appflow.types.task_properties_map

        out["taskProperties"] = capo_appflow.types.task_properties_map.serialize_json(
            value["task_properties"]
        )
    return out


def deserialize_json(data: dict) -> Task:
    out: Task = {}  # type: ignore[typeddict-item]
    if data.get("sourceFields") is not None:
        import capo_appflow.types.source_fields

        out["source_fields"] = capo_appflow.types.source_fields.deserialize_json(
            data["sourceFields"]
        )
    else:
        out["source_fields"] = []
    if data.get("connectorOperator") is not None:
        import capo_appflow.types.connector_operator

        out["connector_operator"] = (
            capo_appflow.types.connector_operator.deserialize_json(
                data["connectorOperator"]
            )
        )
    if data.get("destinationField") is not None:
        out["destination_field"] = data["destinationField"]
    if data.get("taskType") is not None:
        import capo_appflow.types.task_type

        out["task_type"] = capo_appflow.types.task_type.deserialize_json(
            data["taskType"]
        )
    else:
        import typing

        out["task_type"] = typing.cast("capo_appflow.types.task_type.TaskType", "")
    if data.get("taskProperties") is not None:
        import capo_appflow.types.task_properties_map

        out["task_properties"] = (
            capo_appflow.types.task_properties_map.deserialize_json(
                data["taskProperties"]
            )
        )
    return out
