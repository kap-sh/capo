"""Generated from Smithy shape ``com.amazonaws.sagemaker#DestinationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.destination

DestinationList: TypeAlias = list["capo_sagemaker.types.destination.Destination"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DestinationList) -> list:
    import capo_sagemaker.types.destination

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.destination.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DestinationList:
    import capo_sagemaker.types.destination

    out: DestinationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_sagemaker.types.destination.deserialize_aws_json_1_1(item))
    return out
