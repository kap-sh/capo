"""Generated from Smithy shape ``com.amazonaws.proton#DeleteEnvironmentTemplateOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.environment_template


class DeleteEnvironmentTemplateOutput(TypedDict, closed=True):
    environment_template: NotRequired[
        "capo_proton.types.environment_template.EnvironmentTemplate"
    ]
    """<p>The detailed data of the environment template being deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteEnvironmentTemplateOutput) -> dict:
    out: dict = {}
    if "environment_template" in value:
        import capo_proton.types.environment_template

        out["environmentTemplate"] = (
            capo_proton.types.environment_template.serialize_aws_json_1_0(
                value["environment_template"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteEnvironmentTemplateOutput:
    out: DeleteEnvironmentTemplateOutput = {}  # type: ignore[typeddict-item]
    if data.get("environmentTemplate") is not None:
        import capo_proton.types.environment_template

        out["environment_template"] = (
            capo_proton.types.environment_template.deserialize_aws_json_1_0(
                data["environmentTemplate"]
            )
        )
    return out


def redact_sensitive(value: DeleteEnvironmentTemplateOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "environment_template" in value:
        import capo_proton.types.environment_template

        out["environment_template"] = (
            capo_proton.types.environment_template.redact_sensitive(
                value["environment_template"]
            )
        )
    return out
