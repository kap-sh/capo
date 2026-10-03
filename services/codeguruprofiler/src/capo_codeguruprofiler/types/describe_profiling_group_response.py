"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#DescribeProfilingGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.profiling_group_description


class DescribeProfilingGroupResponse(TypedDict, closed=True):
    profiling_group: "capo_codeguruprofiler.types.profiling_group_description.ProfilingGroupDescription"
    """<p> The returned <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html"> <code>ProfilingGroupDescription</code> </a> object that contains information about the requested profiling group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeProfilingGroupResponse) -> dict:
    out: dict = {}
    import capo_codeguruprofiler.types.profiling_group_description

    out["profilingGroup"] = (
        capo_codeguruprofiler.types.profiling_group_description.serialize_json(
            value["profiling_group"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribeProfilingGroupResponse:
    out: DescribeProfilingGroupResponse = {}  # type: ignore[typeddict-item]
    if data.get("profilingGroup") is not None:
        import capo_codeguruprofiler.types.profiling_group_description

        out["profiling_group"] = (
            capo_codeguruprofiler.types.profiling_group_description.deserialize_json(
                data["profilingGroup"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeProfilingGroupResponse.profiling_group required"
        )
    return out
