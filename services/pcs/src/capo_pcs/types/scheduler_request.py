"""Generated from Smithy shape ``com.amazonaws.pcs#SchedulerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pcs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pcs.types.scheduler_type


class SchedulerRequest(TypedDict, closed=True):
    type: "capo_pcs.types.scheduler_type.SchedulerType"
    """<p>The software PCS uses to manage cluster scaling and job scheduling.</p>"""
    version: "str"
    """<p>The version of the specified scheduling software that PCS uses to manage cluster scaling and job scheduling. For more information, see <a href="https://docs.aws.amazon.com/pcs/latest/userguide/slurm-versions.html">Slurm versions in PCS</a> in the <i>PCS User Guide</i>.</p> <p>Valid Values: <code>24.11 | 25.05 | 25.11 | 26.05</code> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SchedulerRequest) -> dict:
    out: dict = {}
    import capo_pcs.types.scheduler_type

    out["type"] = capo_pcs.types.scheduler_type.serialize_aws_json_1_0(value["type"])
    out["version"] = value["version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SchedulerRequest:
    out: SchedulerRequest = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_pcs.types.scheduler_type

        out["type"] = capo_pcs.types.scheduler_type.deserialize_aws_json_1_0(
            data["type"]
        )
    else:
        raise DeserializationError("SchedulerRequest.type required")
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        raise DeserializationError("SchedulerRequest.version required")
    return out
