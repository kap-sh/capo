"""Generated from Smithy shape ``com.amazonaws.personalize#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.date
    import capo_personalize.types.failure_reason
    import capo_personalize.types.filter_expression
    import capo_personalize.types.name
    import capo_personalize.types.status


class Filter(TypedDict, closed=True):
    name: NotRequired["capo_personalize.types.name.Name"]
    """<p>The name of the filter.</p>"""
    filter_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The ARN of the filter.</p>"""
    creation_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The time at which the filter was created.</p>"""
    last_updated_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The time at which the filter was last updated.</p>"""
    dataset_group_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The ARN of the dataset group to which the filter belongs.</p>"""
    failure_reason: NotRequired["capo_personalize.types.failure_reason.FailureReason"]
    """<p>If the filter failed, the reason for its failure.</p>"""
    filter_expression: NotRequired[
        "capo_personalize.types.filter_expression.FilterExpression"
    ]
    """<p>Specifies the type of item interactions to filter out of recommendation results. The filter expression must follow specific format rules. For information about filter expression structure and syntax, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/filter-expressions.html">Filter expressions</a>.</p>"""
    status: NotRequired["capo_personalize.types.status.Status"]
    """<p>The status of the filter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Filter) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "filter_arn" in value:
        out["filterArn"] = value["filter_arn"]
    if "creation_date_time" in value:
        import capo_personalize.types.date

        out["creationDateTime"] = capo_personalize.types.date.serialize_aws_json_1_1(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import capo_personalize.types.date

        out["lastUpdatedDateTime"] = capo_personalize.types.date.serialize_aws_json_1_1(
            value["last_updated_date_time"]
        )
    if "dataset_group_arn" in value:
        out["datasetGroupArn"] = value["dataset_group_arn"]
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "filter_expression" in value:
        out["filterExpression"] = value["filter_expression"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("filterArn") is not None:
        out["filter_arn"] = data["filterArn"]
    if data.get("creationDateTime") is not None:
        import capo_personalize.types.date

        out["creation_date_time"] = (
            capo_personalize.types.date.deserialize_aws_json_1_1(
                data["creationDateTime"]
            )
        )
    if data.get("lastUpdatedDateTime") is not None:
        import capo_personalize.types.date

        out["last_updated_date_time"] = (
            capo_personalize.types.date.deserialize_aws_json_1_1(
                data["lastUpdatedDateTime"]
            )
        )
    if data.get("datasetGroupArn") is not None:
        out["dataset_group_arn"] = data["datasetGroupArn"]
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
    if data.get("filterExpression") is not None:
        out["filter_expression"] = data["filterExpression"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    return out
