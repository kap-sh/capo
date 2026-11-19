"""Generated from Smithy shape ``com.amazonaws.ssm#GcpProjectList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.gcp_project

GcpProjectList: TypeAlias = list["capo_ssm.types.gcp_project.GcpProject"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GcpProjectList) -> list:
    import capo_ssm.types.gcp_project

    out: list = []
    for item in value:
        out.append(capo_ssm.types.gcp_project.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GcpProjectList:
    import capo_ssm.types.gcp_project

    out: GcpProjectList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.gcp_project.deserialize_aws_json_1_1(item))
    return out
