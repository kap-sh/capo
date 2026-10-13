"""Generated from Smithy shape ``com.amazonaws.ec2#GetLaunchTemplateDataResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.response_launch_template_data


class GetLaunchTemplateDataResult(TypedDict, closed=True):
    launch_template_data: NotRequired[
        "capo_ec2.types.response_launch_template_data.ResponseLaunchTemplateData"
    ]
    """<p>The instance data.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetLaunchTemplateDataResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "launch_template_data" in value:
        import capo_ec2.types.response_launch_template_data

        capo_ec2.types.response_launch_template_data.serialize_ec2_query(
            value["launch_template_data"], pairs, f"{key_prefix}LaunchTemplateData"
        )


def deserialize_ec2_query(el: Element) -> GetLaunchTemplateDataResult:
    out: GetLaunchTemplateDataResult = {}  # type: ignore[typeddict-item]
    child_launch_template_data = el.find("launchTemplateData")
    if child_launch_template_data is not None:
        import capo_ec2.types.response_launch_template_data

        out["launch_template_data"] = (
            capo_ec2.types.response_launch_template_data.deserialize_ec2_query(
                child_launch_template_data
            )
        )
    return out


def redact_sensitive(value: GetLaunchTemplateDataResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "launch_template_data" in value:
        import capo_ec2.types.response_launch_template_data

        out["launch_template_data"] = (
            capo_ec2.types.response_launch_template_data.redact_sensitive(
                value["launch_template_data"]
            )
        )
    return out
