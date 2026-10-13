"""Generated from Smithy shape ``com.amazonaws.proton#UpdateEnvironmentTemplateVersionOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.environment_template_version


class UpdateEnvironmentTemplateVersionOutput(TypedDict, closed=True):
    environment_template_version: (
        "capo_proton.types.environment_template_version.EnvironmentTemplateVersion"
    )
    """<p>The environment template version detail data that's returned by Proton.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateEnvironmentTemplateVersionOutput) -> dict:
    out: dict = {}
    import capo_proton.types.environment_template_version

    out["environmentTemplateVersion"] = (
        capo_proton.types.environment_template_version.serialize_aws_json_1_0(
            value["environment_template_version"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateEnvironmentTemplateVersionOutput:
    out: UpdateEnvironmentTemplateVersionOutput = {}  # type: ignore[typeddict-item]
    if data.get("environmentTemplateVersion") is not None:
        import capo_proton.types.environment_template_version

        out["environment_template_version"] = (
            capo_proton.types.environment_template_version.deserialize_aws_json_1_0(
                data["environmentTemplateVersion"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateEnvironmentTemplateVersionOutput.environment_template_version required"
        )
    return out


def redact_sensitive(value: UpdateEnvironmentTemplateVersionOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "environment_template_version" in value:
        import capo_proton.types.environment_template_version

        out["environment_template_version"] = (
            capo_proton.types.environment_template_version.redact_sensitive(
                value["environment_template_version"]
            )
        )
    return out
