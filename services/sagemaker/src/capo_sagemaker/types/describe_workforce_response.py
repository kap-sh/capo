"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeWorkforceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.workforce


class DescribeWorkforceResponse(TypedDict, closed=True):
    workforce: NotRequired["capo_sagemaker.types.workforce.Workforce"]
    """<p>A single private workforce, which is automatically created when you create your first private work team. You can create one private work force in each Amazon Web Services Region. By default, any workforce-related API operation used in a specific region will apply to the workforce created in that region. To learn how to create a private workforce, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-create-private.html">Create a Private Workforce</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkforceResponse) -> dict:
    out: dict = {}
    if "workforce" in value:
        import capo_sagemaker.types.workforce

        out["Workforce"] = capo_sagemaker.types.workforce.serialize_aws_json_1_1(
            value["workforce"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkforceResponse:
    out: DescribeWorkforceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Workforce") is not None:
        import capo_sagemaker.types.workforce

        out["workforce"] = capo_sagemaker.types.workforce.deserialize_aws_json_1_1(
            data["Workforce"]
        )
    return out
