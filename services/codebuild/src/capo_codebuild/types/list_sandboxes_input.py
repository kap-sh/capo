"""Generated from Smithy shape ``com.amazonaws.codebuild#ListSandboxesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.page_size
    import capo_codebuild.types.sort_order_type
    import capo_codebuild.types.string


class ListSandboxesInput(TypedDict, closed=True):
    max_results: NotRequired["capo_codebuild.types.page_size.PageSize"]
    """<p>The maximum number of sandbox records to be retrieved.</p>"""
    sort_order: NotRequired["capo_codebuild.types.sort_order_type.SortOrderType"]
    """<p>The order in which sandbox records should be retrieved.</p>"""
    next_token: NotRequired["capo_codebuild.types.string.String"]
    """<p>The next token, if any, to get paginated results. You will get this value from previous execution of list sandboxes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSandboxesInput) -> dict:
    out: dict = {}
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


def deserialize_aws_json_1_1(data: dict) -> ListSandboxesInput:
    out: ListSandboxesInput = {}  # type: ignore[typeddict-item]
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


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListSandboxesInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "sort_order" in value:
        import capo_codebuild.types.sort_order_type

        out["sortOrder"] = capo_codebuild.types.sort_order_type.serialize_cbor(
            value["sort_order"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListSandboxesInput:
    out: ListSandboxesInput = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("sortOrder") is not None:
        import capo_codebuild.types.sort_order_type

        out["sort_order"] = capo_codebuild.types.sort_order_type.deserialize_cbor(
            data["sortOrder"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
