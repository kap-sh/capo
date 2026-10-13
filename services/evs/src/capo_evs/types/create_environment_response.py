"""Generated from Smithy shape ``com.amazonaws.evs#CreateEnvironmentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_evs.types.environment


class CreateEnvironmentResponse(TypedDict, closed=True):
    environment: NotRequired["capo_evs.types.environment.Environment"]
    """<p>A description of the created environment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateEnvironmentResponse) -> dict:
    out: dict = {}
    if "environment" in value:
        import capo_evs.types.environment

        out["environment"] = capo_evs.types.environment.serialize_aws_json_1_0(
            value["environment"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateEnvironmentResponse:
    out: CreateEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if data.get("environment") is not None:
        import capo_evs.types.environment

        out["environment"] = capo_evs.types.environment.deserialize_aws_json_1_0(
            data["environment"]
        )
    return out


def redact_sensitive(value: CreateEnvironmentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "environment" in value:
        import capo_evs.types.environment

        out["environment"] = capo_evs.types.environment.redact_sensitive(
            value["environment"]
        )
    return out
