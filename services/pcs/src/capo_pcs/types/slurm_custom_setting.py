"""Generated from Smithy shape ``com.amazonaws.pcs#SlurmCustomSetting``."""

from typing_extensions import TypedDict

from capo_pcs.errors import DeserializationError


class SlurmCustomSetting(TypedDict, closed=True):
    parameter_name: "str"
    """<p>PCS supports custom Slurm settings for clusters, compute node groups, and queues. For more information, see <a href="https://docs.aws.amazon.com/pcs/latest/userguide/slurm-custom-settings.html">Configuring custom Slurm settings in PCS</a> in the <i>PCS User Guide</i>.</p>"""
    parameter_value: "str"
    """<p>The values for the configured Slurm settings.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SlurmCustomSetting) -> dict:
    out: dict = {}
    out["parameterName"] = value["parameter_name"]
    out["parameterValue"] = value["parameter_value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SlurmCustomSetting:
    out: SlurmCustomSetting = {}  # type: ignore[typeddict-item]
    if data.get("parameterName") is not None:
        out["parameter_name"] = data["parameterName"]
    else:
        raise DeserializationError("SlurmCustomSetting.parameter_name required")
    if data.get("parameterValue") is not None:
        out["parameter_value"] = data["parameterValue"]
    else:
        raise DeserializationError("SlurmCustomSetting.parameter_value required")
    return out
