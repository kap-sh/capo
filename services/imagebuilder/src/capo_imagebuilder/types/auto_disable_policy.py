"""Generated from Smithy shape ``com.amazonaws.imagebuilder#AutoDisablePolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.auto_disable_failure_count


class AutoDisablePolicy(TypedDict, closed=True):
    failure_count: (
        "capo_imagebuilder.types.auto_disable_failure_count.AutoDisableFailureCount"
    )
    """<p>The number of consecutive scheduled image pipeline executions that must fail before Image Builder automatically disables the pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoDisablePolicy) -> dict:
    out: dict = {}
    out["failureCount"] = value["failure_count"]
    return out


def deserialize_json(data: dict) -> AutoDisablePolicy:
    out: AutoDisablePolicy = {}  # type: ignore[typeddict-item]
    if data.get("failureCount") is not None:
        out["failure_count"] = data["failureCount"]
    else:
        out["failure_count"] = 0
    return out
