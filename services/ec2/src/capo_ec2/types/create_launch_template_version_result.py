"""Generated from Smithy shape ``com.amazonaws.ec2#CreateLaunchTemplateVersionResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.launch_template_version
    import capo_ec2.types.validation_warning


class CreateLaunchTemplateVersionResult(TypedDict, closed=True):
    launch_template_version: NotRequired[
        "capo_ec2.types.launch_template_version.LaunchTemplateVersion"
    ]
    """<p>Information about the launch template version.</p>"""
    warning: NotRequired["capo_ec2.types.validation_warning.ValidationWarning"]
    """<p>If the new version of the launch template contains parameters or parameter combinations that are not valid, an error code and an error message are returned for each issue that's found.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateLaunchTemplateVersionResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "launch_template_version" in value:
        import capo_ec2.types.launch_template_version

        capo_ec2.types.launch_template_version.serialize_ec2_query(
            value["launch_template_version"],
            pairs,
            f"{key_prefix}LaunchTemplateVersion",
        )
    if "warning" in value:
        import capo_ec2.types.validation_warning

        capo_ec2.types.validation_warning.serialize_ec2_query(
            value["warning"], pairs, f"{key_prefix}Warning"
        )


def deserialize_ec2_query(el: Element) -> CreateLaunchTemplateVersionResult:
    out: CreateLaunchTemplateVersionResult = {}  # type: ignore[typeddict-item]
    child_launch_template_version = el.find("launchTemplateVersion")
    if child_launch_template_version is not None:
        import capo_ec2.types.launch_template_version

        out["launch_template_version"] = (
            capo_ec2.types.launch_template_version.deserialize_ec2_query(
                child_launch_template_version
            )
        )
    child_warning = el.find("warning")
    if child_warning is not None:
        import capo_ec2.types.validation_warning

        out["warning"] = capo_ec2.types.validation_warning.deserialize_ec2_query(
            child_warning
        )
    return out


def redact_sensitive(value: CreateLaunchTemplateVersionResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "launch_template_version" in value:
        import capo_ec2.types.launch_template_version

        out["launch_template_version"] = (
            capo_ec2.types.launch_template_version.redact_sensitive(
                value["launch_template_version"]
            )
        )
    return out
