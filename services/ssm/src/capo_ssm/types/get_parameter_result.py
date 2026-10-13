"""Generated from Smithy shape ``com.amazonaws.ssm#GetParameterResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.parameter


class GetParameterResult(TypedDict, closed=True):
    parameter: NotRequired["capo_ssm.types.parameter.Parameter"]
    """<p>Information about a parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetParameterResult) -> dict:
    out: dict = {}
    if "parameter" in value:
        import capo_ssm.types.parameter

        out["Parameter"] = capo_ssm.types.parameter.serialize_aws_json_1_1(
            value["parameter"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetParameterResult:
    out: GetParameterResult = {}  # type: ignore[typeddict-item]
    if data.get("Parameter") is not None:
        import capo_ssm.types.parameter

        out["parameter"] = capo_ssm.types.parameter.deserialize_aws_json_1_1(
            data["Parameter"]
        )
    return out


def redact_sensitive(value: GetParameterResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "parameter" in value:
        import capo_ssm.types.parameter

        out["parameter"] = capo_ssm.types.parameter.redact_sensitive(value["parameter"])
    return out
