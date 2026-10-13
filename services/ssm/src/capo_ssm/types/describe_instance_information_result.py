"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeInstanceInformationResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.instance_information_list
    import capo_ssm.types.next_token


class DescribeInstanceInformationResult(TypedDict, closed=True):
    instance_information_list: NotRequired[
        "capo_ssm.types.instance_information_list.InstanceInformationList"
    ]
    """<p>The managed node information list.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInstanceInformationResult) -> dict:
    out: dict = {}
    if "instance_information_list" in value:
        import capo_ssm.types.instance_information_list

        out["InstanceInformationList"] = (
            capo_ssm.types.instance_information_list.serialize_aws_json_1_1(
                value["instance_information_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInstanceInformationResult:
    out: DescribeInstanceInformationResult = {}  # type: ignore[typeddict-item]
    if data.get("InstanceInformationList") is not None:
        import capo_ssm.types.instance_information_list

        out["instance_information_list"] = (
            capo_ssm.types.instance_information_list.deserialize_aws_json_1_1(
                data["InstanceInformationList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: DescribeInstanceInformationResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "instance_information_list" in value:
        import capo_ssm.types.instance_information_list

        out["instance_information_list"] = (
            capo_ssm.types.instance_information_list.redact_sensitive(
                value["instance_information_list"]
            )
        )
    return out
