"""Generated from Smithy shape ``com.amazonaws.applicationinsights#DescribeProblemResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.problem
    import capo_application_insights.types.sns_notification_arn


class DescribeProblemResponse(TypedDict, closed=True):
    problem: NotRequired["capo_application_insights.types.problem.Problem"]
    """<p>Information about the problem. </p>"""
    sns_notification_arn: NotRequired[
        "capo_application_insights.types.sns_notification_arn.SNSNotificationArn"
    ]
    """<p> The SNS notification topic ARN of the problem. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProblemResponse) -> dict:
    out: dict = {}
    if "problem" in value:
        import capo_application_insights.types.problem

        out["Problem"] = capo_application_insights.types.problem.serialize_aws_json_1_1(
            value["problem"]
        )
    if "sns_notification_arn" in value:
        out["SNSNotificationArn"] = value["sns_notification_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProblemResponse:
    out: DescribeProblemResponse = {}  # type: ignore[typeddict-item]
    if data.get("Problem") is not None:
        import capo_application_insights.types.problem

        out["problem"] = (
            capo_application_insights.types.problem.deserialize_aws_json_1_1(
                data["Problem"]
            )
        )
    if data.get("SNSNotificationArn") is not None:
        out["sns_notification_arn"] = data["SNSNotificationArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeProblemResponse) -> dict:
    out: dict = {}
    if "problem" in value:
        import capo_application_insights.types.problem

        out["Problem"] = capo_application_insights.types.problem.serialize_cbor(
            value["problem"]
        )
    if "sns_notification_arn" in value:
        out["SNSNotificationArn"] = value["sns_notification_arn"]
    return out


def deserialize_cbor(data: dict) -> DescribeProblemResponse:
    out: DescribeProblemResponse = {}  # type: ignore[typeddict-item]
    if data.get("Problem") is not None:
        import capo_application_insights.types.problem

        out["problem"] = capo_application_insights.types.problem.deserialize_cbor(
            data["Problem"]
        )
    if data.get("SNSNotificationArn") is not None:
        out["sns_notification_arn"] = data["SNSNotificationArn"]
    return out
