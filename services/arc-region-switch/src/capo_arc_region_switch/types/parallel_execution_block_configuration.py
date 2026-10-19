"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ParallelExecutionBlockConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.steps


class ParallelExecutionBlockConfiguration(TypedDict, closed=True):
    steps: "capo_arc_region_switch.types.steps.Steps"
    """<p>The steps for a parallel execution block.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ParallelExecutionBlockConfiguration) -> dict:
    out: dict = {}
    import capo_arc_region_switch.types.steps

    out["steps"] = capo_arc_region_switch.types.steps.serialize_aws_json_1_0(
        value["steps"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ParallelExecutionBlockConfiguration:
    out: ParallelExecutionBlockConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("steps") is not None:
        import capo_arc_region_switch.types.steps

        out["steps"] = capo_arc_region_switch.types.steps.deserialize_aws_json_1_0(
            data["steps"]
        )
    else:
        out["steps"] = []
    return out


def redact_sensitive(value: ParallelExecutionBlockConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "steps" in value:
        import capo_arc_region_switch.types.steps

        out["steps"] = capo_arc_region_switch.types.steps.redact_sensitive(
            value["steps"]
        )
    return out
