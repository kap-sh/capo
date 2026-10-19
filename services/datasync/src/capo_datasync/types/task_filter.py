"""Generated from Smithy shape ``com.amazonaws.datasync#TaskFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.filter_values
    import capo_datasync.types.operator
    import capo_datasync.types.task_filter_name


class TaskFilter(TypedDict, closed=True):
    name: "capo_datasync.types.task_filter_name.TaskFilterName"
    """<p>The name of the filter being used. Each API call supports a list of filters that are available for it. For example, <code>LocationId</code> for <code>ListTasks</code>.</p>"""
    values: "capo_datasync.types.filter_values.FilterValues"
    """<p>The values that you want to filter for. For example, you might want to display only tasks for a specific destination location.</p>"""
    operator: "capo_datasync.types.operator.Operator"
    """<p>The operator that is used to compare filter values (for example, <code>Equals</code> or <code>Contains</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskFilter) -> dict:
    out: dict = {}
    import capo_datasync.types.task_filter_name

    out["Name"] = capo_datasync.types.task_filter_name.serialize_aws_json_1_1(
        value["name"]
    )
    import capo_datasync.types.filter_values

    out["Values"] = capo_datasync.types.filter_values.serialize_aws_json_1_1(
        value["values"]
    )
    import capo_datasync.types.operator

    out["Operator"] = capo_datasync.types.operator.serialize_aws_json_1_1(
        value["operator"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskFilter:
    out: TaskFilter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        import capo_datasync.types.task_filter_name

        out["name"] = capo_datasync.types.task_filter_name.deserialize_aws_json_1_1(
            data["Name"]
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_datasync.types.task_filter_name.TaskFilterName", ""
        )
    if data.get("Values") is not None:
        import capo_datasync.types.filter_values

        out["values"] = capo_datasync.types.filter_values.deserialize_aws_json_1_1(
            data["Values"]
        )
    else:
        out["values"] = []
    if data.get("Operator") is not None:
        import capo_datasync.types.operator

        out["operator"] = capo_datasync.types.operator.deserialize_aws_json_1_1(
            data["Operator"]
        )
    else:
        import typing

        out["operator"] = typing.cast("capo_datasync.types.operator.Operator", "")
    return out
