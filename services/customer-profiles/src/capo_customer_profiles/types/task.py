"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Task``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.connector_operator
    import capo_customer_profiles.types.destination_field
    import capo_customer_profiles.types.source_fields
    import capo_customer_profiles.types.task_properties_map
    import capo_customer_profiles.types.task_type


class Task(TypedDict, closed=True):
    connector_operator: NotRequired[
        "capo_customer_profiles.types.connector_operator.ConnectorOperator"
    ]
    """<p>The operation to be performed on the provided source fields.</p>"""
    destination_field: NotRequired[
        "capo_customer_profiles.types.destination_field.DestinationField"
    ]
    """<p>A field in a destination connector, or a field value against which Amazon AppFlow validates a source field.</p>"""
    source_fields: "capo_customer_profiles.types.source_fields.SourceFields"
    """<p>The source fields to which a particular task is applied.</p>"""
    task_properties: NotRequired[
        "capo_customer_profiles.types.task_properties_map.TaskPropertiesMap"
    ]
    """<p>A map used to store task-related information. The service looks for particular information based on the TaskType.</p>"""
    task_type: "capo_customer_profiles.types.task_type.TaskType"
    """<p>Specifies the particular task implementation that Amazon AppFlow performs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Task) -> dict:
    out: dict = {}
    if "connector_operator" in value:
        import capo_customer_profiles.types.connector_operator

        out["ConnectorOperator"] = (
            capo_customer_profiles.types.connector_operator.serialize_json(
                value["connector_operator"]
            )
        )
    if "destination_field" in value:
        out["DestinationField"] = value["destination_field"]
    import capo_customer_profiles.types.source_fields

    out["SourceFields"] = capo_customer_profiles.types.source_fields.serialize_json(
        value["source_fields"]
    )
    if "task_properties" in value:
        import capo_customer_profiles.types.task_properties_map

        out["TaskProperties"] = (
            capo_customer_profiles.types.task_properties_map.serialize_json(
                value["task_properties"]
            )
        )
    import capo_customer_profiles.types.task_type

    out["TaskType"] = capo_customer_profiles.types.task_type.serialize_json(
        value["task_type"]
    )
    return out


def deserialize_json(data: dict) -> Task:
    out: Task = {}  # type: ignore[typeddict-item]
    if data.get("ConnectorOperator") is not None:
        import capo_customer_profiles.types.connector_operator

        out["connector_operator"] = (
            capo_customer_profiles.types.connector_operator.deserialize_json(
                data["ConnectorOperator"]
            )
        )
    if data.get("DestinationField") is not None:
        out["destination_field"] = data["DestinationField"]
    if data.get("SourceFields") is not None:
        import capo_customer_profiles.types.source_fields

        out["source_fields"] = (
            capo_customer_profiles.types.source_fields.deserialize_json(
                data["SourceFields"]
            )
        )
    else:
        out["source_fields"] = []
    if data.get("TaskProperties") is not None:
        import capo_customer_profiles.types.task_properties_map

        out["task_properties"] = (
            capo_customer_profiles.types.task_properties_map.deserialize_json(
                data["TaskProperties"]
            )
        )
    if data.get("TaskType") is not None:
        import capo_customer_profiles.types.task_type

        out["task_type"] = capo_customer_profiles.types.task_type.deserialize_json(
            data["TaskType"]
        )
    else:
        import typing

        out["task_type"] = typing.cast(
            "capo_customer_profiles.types.task_type.TaskType", ""
        )
    return out
