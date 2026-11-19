"""Generated from Smithy shape ``com.amazonaws.codebuild#ListProjectsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.project_sort_by_type
    import capo_codebuild.types.sort_order_type


class ListProjectsInput(TypedDict, closed=True):
    sort_by: NotRequired["capo_codebuild.types.project_sort_by_type.ProjectSortByType"]
    """<p>The criterion to be used to list build project names. Valid values include:</p> <ul> <li> <p> <code>CREATED_TIME</code>: List based on when each build project was created.</p> </li> <li> <p> <code>LAST_MODIFIED_TIME</code>: List based on when information about each build project was last changed.</p> </li> <li> <p> <code>NAME</code>: List based on each build project's name.</p> </li> </ul> <p>Use <code>sortOrder</code> to specify in what order to list the build project names based on the preceding criteria.</p>"""
    sort_order: NotRequired["capo_codebuild.types.sort_order_type.SortOrderType"]
    """<p>The order in which to list build projects. Valid values include:</p> <ul> <li> <p> <code>ASCENDING</code>: List in ascending order.</p> </li> <li> <p> <code>DESCENDING</code>: List in descending order.</p> </li> </ul> <p>Use <code>sortBy</code> to specify the criterion to be used to list build project names.</p>"""
    next_token: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>During a previous call, if there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a <i>nextToken</i>. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListProjectsInput) -> dict:
    out: dict = {}
    if "sort_by" in value:
        import capo_codebuild.types.project_sort_by_type

        out["sortBy"] = (
            capo_codebuild.types.project_sort_by_type.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_codebuild.types.sort_order_type

        out["sortOrder"] = capo_codebuild.types.sort_order_type.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListProjectsInput:
    out: ListProjectsInput = {}  # type: ignore[typeddict-item]
    if data.get("sortBy") is not None:
        import capo_codebuild.types.project_sort_by_type

        out["sort_by"] = (
            capo_codebuild.types.project_sort_by_type.deserialize_aws_json_1_1(
                data["sortBy"]
            )
        )
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
def serialize_cbor(value: ListProjectsInput) -> dict:
    out: dict = {}
    if "sort_by" in value:
        import capo_codebuild.types.project_sort_by_type

        out["sortBy"] = capo_codebuild.types.project_sort_by_type.serialize_cbor(
            value["sort_by"]
        )
    if "sort_order" in value:
        import capo_codebuild.types.sort_order_type

        out["sortOrder"] = capo_codebuild.types.sort_order_type.serialize_cbor(
            value["sort_order"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListProjectsInput:
    out: ListProjectsInput = {}  # type: ignore[typeddict-item]
    if data.get("sortBy") is not None:
        import capo_codebuild.types.project_sort_by_type

        out["sort_by"] = capo_codebuild.types.project_sort_by_type.deserialize_cbor(
            data["sortBy"]
        )
    if data.get("sortOrder") is not None:
        import capo_codebuild.types.sort_order_type

        out["sort_order"] = capo_codebuild.types.sort_order_type.deserialize_cbor(
            data["sortOrder"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
