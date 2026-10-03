"""Generated from Smithy shape ``com.amazonaws.pcs#CgroupCustomSetting``."""

from typing_extensions import TypedDict

from capo_pcs.errors import DeserializationError


class CgroupCustomSetting(TypedDict, closed=True):
    parameter_name: "str"
    """<p>PCS supports custom Cgroup settings for clusters. For more information, see <a href="https://docs.aws.amazon.com/pcs/latest/userguide/cgroup-custom-settings.html">Configuring custom Cgroup settings in PCS</a> in the <i>PCS User Guide</i>.</p>"""
    parameter_value: "str"
    """<p>The values for the configured Cgroup settings.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CgroupCustomSetting) -> dict:
    out: dict = {}
    out["parameterName"] = value["parameter_name"]
    out["parameterValue"] = value["parameter_value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CgroupCustomSetting:
    out: CgroupCustomSetting = {}  # type: ignore[typeddict-item]
    if data.get("parameterName") is not None:
        out["parameter_name"] = data["parameterName"]
    else:
        raise DeserializationError("CgroupCustomSetting.parameter_name required")
    if data.get("parameterValue") is not None:
        out["parameter_value"] = data["parameterValue"]
    else:
        raise DeserializationError("CgroupCustomSetting.parameter_value required")
    return out
