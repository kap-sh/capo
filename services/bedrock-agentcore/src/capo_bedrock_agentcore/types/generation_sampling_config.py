"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GenerationSamplingConfig``."""

from typing_extensions import NotRequired, TypedDict


class GenerationSamplingConfig(TypedDict, closed=True):
    max_scenarios: NotRequired["int"]
    """<p>The maximum number of scenarios to generate, from 1 to 1,000. The default is 100. The generation produces at most one scenario for each selected session. The dataset's draft examples plus this value can't be more than 1,000.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerationSamplingConfig) -> dict:
    out: dict = {}
    if "max_scenarios" in value:
        out["maxScenarios"] = value["max_scenarios"]
    return out


def deserialize_json(data: dict) -> GenerationSamplingConfig:
    out: GenerationSamplingConfig = {}  # type: ignore[typeddict-item]
    if data.get("maxScenarios") is not None:
        out["max_scenarios"] = data["maxScenarios"]
    return out
