"""Generated from Smithy shape ``com.amazonaws.lambdaweb#ScalingConfig``."""

from typing_extensions import NotRequired, TypedDict


class ScalingConfig(TypedDict, closed=True):
    max_environments: NotRequired["int"]
    """<p>The maximum number of concurrent execution environments for the endpoint. Minimum value of 2, maximum value of 10000. There is no default value. If you don't specify a value, the scaling configuration is absent from the response. On an update, omit <code>scalingConfig</code> to keep the current value, or specify an empty object to clear a previously set value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScalingConfig) -> dict:
    out: dict = {}
    if "max_environments" in value:
        out["maxEnvironments"] = value["max_environments"]
    return out


def deserialize_json(data: dict) -> ScalingConfig:
    out: ScalingConfig = {}  # type: ignore[typeddict-item]
    if data.get("maxEnvironments") is not None:
        out["max_environments"] = data["maxEnvironments"]
    return out
