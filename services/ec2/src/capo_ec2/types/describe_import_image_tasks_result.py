"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeImportImageTasksResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.import_image_task_list
    import capo_ec2.types.string


class DescribeImportImageTasksResult(TypedDict, closed=True):
    import_image_tasks: NotRequired[
        "capo_ec2.types.import_image_task_list.ImportImageTaskList"
    ]
    """<p>A list of zero or more import image tasks that are currently active or were completed or canceled in the previous 7 days.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to get the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeImportImageTasksResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "import_image_tasks" in value:
        import capo_ec2.types.import_image_task_list

        capo_ec2.types.import_image_task_list.serialize_ec2_query(
            value["import_image_tasks"], pairs, f"{key_prefix}ImportImageTaskSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeImportImageTasksResult:
    out: DescribeImportImageTasksResult = {}  # type: ignore[typeddict-item]
    child_import_image_tasks = el.find("importImageTaskSet")
    if child_import_image_tasks is not None:
        import capo_ec2.types.import_image_task_list

        out["import_image_tasks"] = (
            capo_ec2.types.import_image_task_list.deserialize_ec2_query(
                child_import_image_tasks
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out


def redact_sensitive(value: DescribeImportImageTasksResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "import_image_tasks" in value:
        import capo_ec2.types.import_image_task_list

        out["import_image_tasks"] = (
            capo_ec2.types.import_image_task_list.redact_sensitive(
                value["import_image_tasks"]
            )
        )
    return out
