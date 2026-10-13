"""Generated from Smithy shape ``com.amazonaws.proton#GetEnvironmentTemplateVersionOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.environment_template_version


class GetEnvironmentTemplateVersionOutput(TypedDict, closed=True):
    environment_template_version: (
        "capo_proton.types.environment_template_version.EnvironmentTemplateVersion"
    )
    """<p>The detailed data of the requested environment template version.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEnvironmentTemplateVersionOutput) -> dict:
    out: dict = {}
    import capo_proton.types.environment_template_version

    out["environmentTemplateVersion"] = (
        capo_proton.types.environment_template_version.serialize_aws_json_1_0(
            value["environment_template_version"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEnvironmentTemplateVersionOutput:
    out: GetEnvironmentTemplateVersionOutput = {}  # type: ignore[typeddict-item]
    if data.get("environmentTemplateVersion") is not None:
        import capo_proton.types.environment_template_version

        out["environment_template_version"] = (
            capo_proton.types.environment_template_version.deserialize_aws_json_1_0(
                data["environmentTemplateVersion"]
            )
        )
    else:
        raise DeserializationError(
            "GetEnvironmentTemplateVersionOutput.environment_template_version required"
        )
    return out


def redact_sensitive(value: GetEnvironmentTemplateVersionOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "environment_template_version" in value:
        import capo_proton.types.environment_template_version

        out["environment_template_version"] = (
            capo_proton.types.environment_template_version.redact_sensitive(
                value["environment_template_version"]
            )
        )
    return out
