"""Generated from Smithy shape ``com.amazonaws.inspector#DescribeResourceGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.batch_describe_arn_list


class DescribeResourceGroupsRequest(TypedDict, closed=True):
    resource_group_arns: (
        "capo_inspector.types.batch_describe_arn_list.BatchDescribeArnList"
    )
    """<p>The ARN that specifies the resource group that you want to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeResourceGroupsRequest) -> dict:
    out: dict = {}
    import capo_inspector.types.batch_describe_arn_list

    out["resourceGroupArns"] = (
        capo_inspector.types.batch_describe_arn_list.serialize_aws_json_1_1(
            value["resource_group_arns"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeResourceGroupsRequest:
    out: DescribeResourceGroupsRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceGroupArns") is not None:
        import capo_inspector.types.batch_describe_arn_list

        out["resource_group_arns"] = (
            capo_inspector.types.batch_describe_arn_list.deserialize_aws_json_1_1(
                data["resourceGroupArns"]
            )
        )
    else:
        out["resource_group_arns"] = []
    return out
