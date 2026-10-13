"""Generated from Smithy shape ``com.amazonaws.proton#DeleteEnvironmentOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.environment


class DeleteEnvironmentOutput(TypedDict, closed=True):
    environment: NotRequired["capo_proton.types.environment.Environment"]
    """<p>The detailed data of the environment being deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteEnvironmentOutput) -> dict:
    out: dict = {}
    if "environment" in value:
        import capo_proton.types.environment

        out["environment"] = capo_proton.types.environment.serialize_aws_json_1_0(
            value["environment"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteEnvironmentOutput:
    out: DeleteEnvironmentOutput = {}  # type: ignore[typeddict-item]
    if data.get("environment") is not None:
        import capo_proton.types.environment

        out["environment"] = capo_proton.types.environment.deserialize_aws_json_1_0(
            data["environment"]
        )
    return out


def redact_sensitive(value: DeleteEnvironmentOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "environment" in value:
        import capo_proton.types.environment

        out["environment"] = capo_proton.types.environment.redact_sensitive(
            value["environment"]
        )
    return out
