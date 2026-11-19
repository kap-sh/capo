"""Generated from Smithy shape ``com.amazonaws.ssoadmin#VpcArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sso_admin.types.vpc_arn

VpcArnList: TypeAlias = list["capo_sso_admin.types.vpc_arn.VpcArn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcArnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> VpcArnList:
    return [item for item in data if item is not None]
