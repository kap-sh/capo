"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#LambdaFunctionSinkConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.arn


class LambdaFunctionSinkConfiguration(TypedDict, closed=True):
    insights_target: NotRequired["capo_chime_sdk_media_pipelines.types.arn.Arn"]
    """<p>The ARN of the sink.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaFunctionSinkConfiguration) -> dict:
    out: dict = {}
    if "insights_target" in value:
        out["InsightsTarget"] = value["insights_target"]
    return out


def deserialize_json(data: dict) -> LambdaFunctionSinkConfiguration:
    out: LambdaFunctionSinkConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("InsightsTarget") is not None:
        out["insights_target"] = data["InsightsTarget"]
    return out


def redact_sensitive(value: LambdaFunctionSinkConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "insights_target" in value:
        out["insights_target"] = "*** Sensitive Data Redacted ***"
    return out
