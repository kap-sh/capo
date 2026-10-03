"""Generated from Smithy shape ``com.amazonaws.evs#VcfVersionInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_evs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_evs.types.instance_type_list
    import capo_evs.types.vcf_version


class VcfVersionInfo(TypedDict, closed=True):
    vcf_version: "capo_evs.types.vcf_version.VcfVersion"
    """<p>The VCF version number.</p>"""
    status: "str"
    """<p>The status for this VCF version. Valid values are:</p> <ul> <li> <p> <code>AVAILABLE</code> - This VCF version is available to you.</p> </li> <li> <p> <code>RESTRICTED</code> - This VCF version has limited availability.</p> </li> </ul> <note> <p> If the version you need shows RESTRICTED, and you require, check out <a href="https://docs.aws.amazon.com/evs/latest/userguide/versions-provided.html">VCF versions and EC2 instance types provided by Amazon EVS</a> for more information. </p> </note>"""
    default_esx_version: "str"
    """<p>The default ESX version for this VCF version. It is based on Broadcom's Bill Of Materials (BOM).</p>"""
    instance_types: "capo_evs.types.instance_type_list.InstanceTypeList"
    """<p>EC2 instance types provided by Amazon EVS for this VCF version for creating environments.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VcfVersionInfo) -> dict:
    out: dict = {}
    import capo_evs.types.vcf_version

    out["vcfVersion"] = capo_evs.types.vcf_version.serialize_aws_json_1_0(
        value["vcf_version"]
    )
    out["status"] = value["status"]
    out["defaultEsxVersion"] = value["default_esx_version"]
    import capo_evs.types.instance_type_list

    out["instanceTypes"] = capo_evs.types.instance_type_list.serialize_aws_json_1_0(
        value["instance_types"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> VcfVersionInfo:
    out: VcfVersionInfo = {}  # type: ignore[typeddict-item]
    if data.get("vcfVersion") is not None:
        import capo_evs.types.vcf_version

        out["vcf_version"] = capo_evs.types.vcf_version.deserialize_aws_json_1_0(
            data["vcfVersion"]
        )
    else:
        raise DeserializationError("VcfVersionInfo.vcf_version required")
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("VcfVersionInfo.status required")
    if data.get("defaultEsxVersion") is not None:
        out["default_esx_version"] = data["defaultEsxVersion"]
    else:
        raise DeserializationError("VcfVersionInfo.default_esx_version required")
    if data.get("instanceTypes") is not None:
        import capo_evs.types.instance_type_list

        out["instance_types"] = (
            capo_evs.types.instance_type_list.deserialize_aws_json_1_0(
                data["instanceTypes"]
            )
        )
    else:
        raise DeserializationError("VcfVersionInfo.instance_types required")
    return out
