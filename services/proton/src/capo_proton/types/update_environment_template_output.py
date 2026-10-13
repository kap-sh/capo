"""Generated from Smithy shape ``com.amazonaws.proton#UpdateEnvironmentTemplateOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.environment_template


class UpdateEnvironmentTemplateOutput(TypedDict, closed=True):
    environment_template: "capo_proton.types.environment_template.EnvironmentTemplate"
    """<p>The environment template detail data that's returned by Proton.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateEnvironmentTemplateOutput) -> dict:
    out: dict = {}
    import capo_proton.types.environment_template

    out["environmentTemplate"] = (
        capo_proton.types.environment_template.serialize_aws_json_1_0(
            value["environment_template"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateEnvironmentTemplateOutput:
    out: UpdateEnvironmentTemplateOutput = {}  # type: ignore[typeddict-item]
    if data.get("environmentTemplate") is not None:
        import capo_proton.types.environment_template

        out["environment_template"] = (
            capo_proton.types.environment_template.deserialize_aws_json_1_0(
                data["environmentTemplate"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateEnvironmentTemplateOutput.environment_template required"
        )
    return out


def redact_sensitive(value: UpdateEnvironmentTemplateOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "environment_template" in value:
        import capo_proton.types.environment_template

        out["environment_template"] = (
            capo_proton.types.environment_template.redact_sensitive(
                value["environment_template"]
            )
        )
    return out
