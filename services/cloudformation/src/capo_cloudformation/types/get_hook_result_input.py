"""Generated from Smithy shape ``com.amazonaws.cloudformation#GetHookResultInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.hook_invocation_id


class GetHookResultInput(TypedDict, closed=True):
    hook_result_id: NotRequired[
        "capo_cloudformation.types.hook_invocation_id.HookInvocationId"
    ]
    """<p>The unique identifier (ID) of the Hook invocation result that you want details about. You can get the ID from the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListHookResults.html">ListHookResults</a> operation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetHookResultInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "hook_result_id" in value:
        pairs.append((f"{key_prefix}HookResultId", str(value["hook_result_id"])))


def deserialize_query(el: Element) -> GetHookResultInput:
    out: GetHookResultInput = {}  # type: ignore[typeddict-item]
    child_hook_result_id = el.find("HookResultId")
    if child_hook_result_id is not None:
        out["hook_result_id"] = str(child_hook_result_id.text or "")
    return out
