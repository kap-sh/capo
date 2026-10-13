"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeConversionTasksResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.describe_conversion_task_list


class DescribeConversionTasksResult(TypedDict, closed=True):
    conversion_tasks: NotRequired[
        "capo_ec2.types.describe_conversion_task_list.DescribeConversionTaskList"
    ]
    """<p>Information about the conversion tasks.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeConversionTasksResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "conversion_tasks" in value:
        import capo_ec2.types.describe_conversion_task_list

        capo_ec2.types.describe_conversion_task_list.serialize_ec2_query(
            value["conversion_tasks"], pairs, f"{key_prefix}ConversionTasks"
        )


def deserialize_ec2_query(el: Element) -> DescribeConversionTasksResult:
    out: DescribeConversionTasksResult = {}  # type: ignore[typeddict-item]
    child_conversion_tasks = el.find("conversionTasks")
    if child_conversion_tasks is not None:
        import capo_ec2.types.describe_conversion_task_list

        out["conversion_tasks"] = (
            capo_ec2.types.describe_conversion_task_list.deserialize_ec2_query(
                child_conversion_tasks
            )
        )
    return out


def redact_sensitive(value: DescribeConversionTasksResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "conversion_tasks" in value:
        import capo_ec2.types.describe_conversion_task_list

        out["conversion_tasks"] = (
            capo_ec2.types.describe_conversion_task_list.redact_sensitive(
                value["conversion_tasks"]
            )
        )
    return out
