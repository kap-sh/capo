"""Generated from Smithy shape ``com.amazonaws.personalize#CreateFilterRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.filter_expression
    import capo_personalize.types.name
    import capo_personalize.types.tags


class CreateFilterRequest(TypedDict, closed=True):
    name: "capo_personalize.types.name.Name"
    """<p>The name of the filter to create.</p>"""
    dataset_group_arn: "capo_personalize.types.arn.Arn"
    """<p>The ARN of the dataset group that the filter will belong to.</p>"""
    filter_expression: "capo_personalize.types.filter_expression.FilterExpression"
    """<p>The filter expression defines which items are included or excluded from recommendations. Filter expression must follow specific format rules. For information about filter expression structure and syntax, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/filter-expressions.html">Filter expressions</a>.</p>"""
    tags: NotRequired["capo_personalize.types.tags.Tags"]
    """<p>A list of <a href="https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html">tags</a> to apply to the filter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFilterRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["datasetGroupArn"] = value["dataset_group_arn"]
    out["filterExpression"] = value["filter_expression"]
    if "tags" in value:
        import capo_personalize.types.tags

        out["tags"] = capo_personalize.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFilterRequest:
    out: CreateFilterRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("datasetGroupArn") is not None:
        out["dataset_group_arn"] = data["datasetGroupArn"]
    else:
        out["dataset_group_arn"] = ""
    if data.get("filterExpression") is not None:
        out["filter_expression"] = data["filterExpression"]
    else:
        out["filter_expression"] = ""
    if data.get("tags") is not None:
        import capo_personalize.types.tags

        out["tags"] = capo_personalize.types.tags.deserialize_aws_json_1_1(data["tags"])
    return out


def redact_sensitive(value: CreateFilterRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filter_expression" in value:
        out["filter_expression"] = "*** Sensitive Data Redacted ***"
    if "tags" in value:
        import capo_personalize.types.tags

        out["tags"] = capo_personalize.types.tags.redact_sensitive(value["tags"])
    return out
