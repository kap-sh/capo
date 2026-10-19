"""Generated from Smithy shape ``com.amazonaws.inspector#DescribeExclusionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.batch_describe_exclusions_arn_list
    import capo_inspector.types.locale


class DescribeExclusionsRequest(TypedDict, closed=True):
    exclusion_arns: "capo_inspector.types.batch_describe_exclusions_arn_list.BatchDescribeExclusionsArnList"
    """<p>The list of ARNs that specify the exclusions that you want to describe.</p>"""
    locale: NotRequired["capo_inspector.types.locale.Locale"]
    """<p>The locale into which you want to translate the exclusion's title, description, and recommendation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeExclusionsRequest) -> dict:
    out: dict = {}
    import capo_inspector.types.batch_describe_exclusions_arn_list

    out["exclusionArns"] = (
        capo_inspector.types.batch_describe_exclusions_arn_list.serialize_aws_json_1_1(
            value["exclusion_arns"]
        )
    )
    if "locale" in value:
        import capo_inspector.types.locale

        out["locale"] = capo_inspector.types.locale.serialize_aws_json_1_1(
            value["locale"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeExclusionsRequest:
    out: DescribeExclusionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("exclusionArns") is not None:
        import capo_inspector.types.batch_describe_exclusions_arn_list

        out["exclusion_arns"] = (
            capo_inspector.types.batch_describe_exclusions_arn_list.deserialize_aws_json_1_1(
                data["exclusionArns"]
            )
        )
    else:
        out["exclusion_arns"] = []
    if data.get("locale") is not None:
        import capo_inspector.types.locale

        out["locale"] = capo_inspector.types.locale.deserialize_aws_json_1_1(
            data["locale"]
        )
    return out
