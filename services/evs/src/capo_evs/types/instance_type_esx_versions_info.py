"""Generated from Smithy shape ``com.amazonaws.evs#InstanceTypeEsxVersionsInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_evs.types.esx_version_list
    import capo_evs.types.instance_type


class InstanceTypeEsxVersionsInfo(TypedDict, closed=True):
    instance_type: "capo_evs.types.instance_type.InstanceType"
    """<p>The EC2 instance type.</p>"""
    esx_versions: "capo_evs.types.esx_version_list.EsxVersionList"
    """<p>The list of ESX versions offered for this instance type.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceTypeEsxVersionsInfo) -> dict:
    out: dict = {}
    import capo_evs.types.instance_type

    out["instanceType"] = capo_evs.types.instance_type.serialize_aws_json_1_0(
        value["instance_type"]
    )
    import capo_evs.types.esx_version_list

    out["esxVersions"] = capo_evs.types.esx_version_list.serialize_aws_json_1_0(
        value["esx_versions"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> InstanceTypeEsxVersionsInfo:
    out: InstanceTypeEsxVersionsInfo = {}  # type: ignore[typeddict-item]
    if data.get("instanceType") is not None:
        import capo_evs.types.instance_type

        out["instance_type"] = capo_evs.types.instance_type.deserialize_aws_json_1_0(
            data["instanceType"]
        )
    else:
        import typing

        out["instance_type"] = typing.cast(
            "capo_evs.types.instance_type.InstanceType", ""
        )
    if data.get("esxVersions") is not None:
        import capo_evs.types.esx_version_list

        out["esx_versions"] = capo_evs.types.esx_version_list.deserialize_aws_json_1_0(
            data["esxVersions"]
        )
    else:
        out["esx_versions"] = []
    return out
