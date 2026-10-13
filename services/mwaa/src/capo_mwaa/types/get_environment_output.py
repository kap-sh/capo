"""Generated from Smithy shape ``com.amazonaws.mwaa#GetEnvironmentOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa.types.environment


class GetEnvironmentOutput(TypedDict, closed=True):
    environment: NotRequired["capo_mwaa.types.environment.Environment"]
    """<p>An object containing all available details about the environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnvironmentOutput) -> dict:
    out: dict = {}
    if "environment" in value:
        import capo_mwaa.types.environment

        out["Environment"] = capo_mwaa.types.environment.serialize_json(
            value["environment"]
        )
    return out


def deserialize_json(data: dict) -> GetEnvironmentOutput:
    out: GetEnvironmentOutput = {}  # type: ignore[typeddict-item]
    if data.get("Environment") is not None:
        import capo_mwaa.types.environment

        out["environment"] = capo_mwaa.types.environment.deserialize_json(
            data["Environment"]
        )
    return out


def redact_sensitive(value: GetEnvironmentOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "environment" in value:
        import capo_mwaa.types.environment

        out["environment"] = capo_mwaa.types.environment.redact_sensitive(
            value["environment"]
        )
    return out
