"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListAppliedSchemaArnsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.next_token
    import capo_clouddirectory.types.number_results


class ListAppliedSchemaArnsRequest(TypedDict, closed=True):
    directory_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The ARN of the directory you are listing.</p>"""
    schema_arn: NotRequired["capo_clouddirectory.types.arn.Arn"]
    """<p>The response for <code>ListAppliedSchemaArns</code> when this parameter is used will list all minor version ARNs for a major version.</p>"""
    next_token: NotRequired["capo_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""
    max_results: NotRequired["capo_clouddirectory.types.number_results.NumberResults"]
    """<p>The maximum number of results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppliedSchemaArnsRequest) -> dict:
    out: dict = {}
    out["DirectoryArn"] = value["directory_arn"]
    if "schema_arn" in value:
        out["SchemaArn"] = value["schema_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListAppliedSchemaArnsRequest:
    out: ListAppliedSchemaArnsRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryArn") is not None:
        out["directory_arn"] = data["DirectoryArn"]
    else:
        out["directory_arn"] = ""
    if data.get("SchemaArn") is not None:
        out["schema_arn"] = data["SchemaArn"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
