"""Generated from Smithy shape ``com.amazonaws.inspector#DescribeRulesPackagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.batch_describe_arn_list
    import capo_inspector.types.locale


class DescribeRulesPackagesRequest(TypedDict, closed=True):
    rules_package_arns: (
        "capo_inspector.types.batch_describe_arn_list.BatchDescribeArnList"
    )
    """<p>The ARN that specifies the rules package that you want to describe.</p>"""
    locale: NotRequired["capo_inspector.types.locale.Locale"]
    """<p>The locale that you want to translate a rules package description into.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRulesPackagesRequest) -> dict:
    out: dict = {}
    import capo_inspector.types.batch_describe_arn_list

    out["rulesPackageArns"] = (
        capo_inspector.types.batch_describe_arn_list.serialize_aws_json_1_1(
            value["rules_package_arns"]
        )
    )
    if "locale" in value:
        import capo_inspector.types.locale

        out["locale"] = capo_inspector.types.locale.serialize_aws_json_1_1(
            value["locale"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRulesPackagesRequest:
    out: DescribeRulesPackagesRequest = {}  # type: ignore[typeddict-item]
    if data.get("rulesPackageArns") is not None:
        import capo_inspector.types.batch_describe_arn_list

        out["rules_package_arns"] = (
            capo_inspector.types.batch_describe_arn_list.deserialize_aws_json_1_1(
                data["rulesPackageArns"]
            )
        )
    else:
        out["rules_package_arns"] = []
    if data.get("locale") is not None:
        import capo_inspector.types.locale

        out["locale"] = capo_inspector.types.locale.deserialize_aws_json_1_1(
            data["locale"]
        )
    return out
