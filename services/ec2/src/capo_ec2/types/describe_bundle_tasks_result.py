"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeBundleTasksResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.bundle_task_list


class DescribeBundleTasksResult(TypedDict, closed=True):
    bundle_tasks: NotRequired["capo_ec2.types.bundle_task_list.BundleTaskList"]
    """<p>Information about the bundle tasks.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeBundleTasksResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "bundle_tasks" in value:
        import capo_ec2.types.bundle_task_list

        capo_ec2.types.bundle_task_list.serialize_ec2_query(
            value["bundle_tasks"], pairs, f"{key_prefix}BundleInstanceTasksSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeBundleTasksResult:
    out: DescribeBundleTasksResult = {}  # type: ignore[typeddict-item]
    child_bundle_tasks = el.find("bundleInstanceTasksSet")
    if child_bundle_tasks is not None:
        import capo_ec2.types.bundle_task_list

        out["bundle_tasks"] = capo_ec2.types.bundle_task_list.deserialize_ec2_query(
            child_bundle_tasks
        )
    return out


def redact_sensitive(value: DescribeBundleTasksResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "bundle_tasks" in value:
        import capo_ec2.types.bundle_task_list

        out["bundle_tasks"] = capo_ec2.types.bundle_task_list.redact_sensitive(
            value["bundle_tasks"]
        )
    return out
