"""Generated from Smithy shape ``com.amazonaws.codebuild#ListCommandExecutionsForSandboxInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.page_size
    import capo_codebuild.types.sensitive_string
    import capo_codebuild.types.sort_order_type


class ListCommandExecutionsForSandboxInput(TypedDict, closed=True):
    sandbox_id: "capo_codebuild.types.non_empty_string.NonEmptyString"
    """<p>A <code>sandboxId</code> or <code>sandboxArn</code>.</p>"""
    max_results: NotRequired["capo_codebuild.types.page_size.PageSize"]
    """<p>The maximum number of sandbox records to be retrieved.</p>"""
    sort_order: NotRequired["capo_codebuild.types.sort_order_type.SortOrderType"]
    """<p>The order in which sandbox records should be retrieved.</p>"""
    next_token: NotRequired["capo_codebuild.types.sensitive_string.SensitiveString"]
    """<p>The next token, if any, to get paginated results. You will get this value from previous execution of list sandboxes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCommandExecutionsForSandboxInput) -> dict:
    out: dict = {}
    out["sandboxId"] = value["sandbox_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "sort_order" in value:
        import capo_codebuild.types.sort_order_type

        out["sortOrder"] = capo_codebuild.types.sort_order_type.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCommandExecutionsForSandboxInput:
    out: ListCommandExecutionsForSandboxInput = {}  # type: ignore[typeddict-item]
    if data.get("sandboxId") is not None:
        out["sandbox_id"] = data["sandboxId"]
    else:
        out["sandbox_id"] = ""
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("sortOrder") is not None:
        import capo_codebuild.types.sort_order_type

        out["sort_order"] = (
            capo_codebuild.types.sort_order_type.deserialize_aws_json_1_1(
                data["sortOrder"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListCommandExecutionsForSandboxInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
