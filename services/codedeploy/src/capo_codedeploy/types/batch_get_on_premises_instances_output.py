"""Generated from Smithy shape ``com.amazonaws.codedeploy#BatchGetOnPremisesInstancesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.instance_info_list


class BatchGetOnPremisesInstancesOutput(TypedDict, closed=True):
    instance_infos: NotRequired[
        "capo_codedeploy.types.instance_info_list.InstanceInfoList"
    ]
    """<p>Information about the on-premises instances.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetOnPremisesInstancesOutput) -> dict:
    out: dict = {}
    if "instance_infos" in value:
        import capo_codedeploy.types.instance_info_list

        out["instanceInfos"] = (
            capo_codedeploy.types.instance_info_list.serialize_aws_json_1_1(
                value["instance_infos"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetOnPremisesInstancesOutput:
    out: BatchGetOnPremisesInstancesOutput = {}  # type: ignore[typeddict-item]
    if data.get("instanceInfos") is not None:
        import capo_codedeploy.types.instance_info_list

        out["instance_infos"] = (
            capo_codedeploy.types.instance_info_list.deserialize_aws_json_1_1(
                data["instanceInfos"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchGetOnPremisesInstancesOutput) -> dict:
    out: dict = {}
    if "instance_infos" in value:
        import capo_codedeploy.types.instance_info_list

        out["instanceInfos"] = capo_codedeploy.types.instance_info_list.serialize_cbor(
            value["instance_infos"]
        )
    return out


def deserialize_cbor(data: dict) -> BatchGetOnPremisesInstancesOutput:
    out: BatchGetOnPremisesInstancesOutput = {}  # type: ignore[typeddict-item]
    if data.get("instanceInfos") is not None:
        import capo_codedeploy.types.instance_info_list

        out["instance_infos"] = (
            capo_codedeploy.types.instance_info_list.deserialize_cbor(
                data["instanceInfos"]
            )
        )
    return out
