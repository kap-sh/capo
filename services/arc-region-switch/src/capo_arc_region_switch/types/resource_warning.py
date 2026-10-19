"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ResourceWarning``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_arc_region_switch.types.minimal_workflow
    import capo_arc_region_switch.types.resource_arn
    import capo_arc_region_switch.types.resource_warning_status
    import capo_arc_region_switch.types.step_name


class ResourceWarning(TypedDict, closed=True):
    workflow: NotRequired[
        "capo_arc_region_switch.types.minimal_workflow.MinimalWorkflow"
    ]
    """<p>The workflow for the resource warning.</p>"""
    version: "str"
    """<p>The version for the resource warning.</p>"""
    step_name: NotRequired["capo_arc_region_switch.types.step_name.StepName"]
    """<p>The name of the step for the resource warning.</p>"""
    resource_arn: NotRequired["capo_arc_region_switch.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    warning_status: (
        "capo_arc_region_switch.types.resource_warning_status.ResourceWarningStatus"
    )
    """<p>The status of the resource warning.</p>"""
    warning_updated_time: "datetime.datetime"
    """<p>The timestamp when the warning was last updated.</p>"""
    warning_message: "str"
    """<p>The warning message about what needs to be corrected.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceWarning) -> dict:
    out: dict = {}
    if "workflow" in value:
        import capo_arc_region_switch.types.minimal_workflow

        out["workflow"] = (
            capo_arc_region_switch.types.minimal_workflow.serialize_aws_json_1_0(
                value["workflow"]
            )
        )
    out["version"] = value["version"]
    if "step_name" in value:
        out["stepName"] = value["step_name"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    import capo_arc_region_switch.types.resource_warning_status

    out["warningStatus"] = (
        capo_arc_region_switch.types.resource_warning_status.serialize_aws_json_1_0(
            value["warning_status"]
        )
    )
    import capo_arc_region_switch.types._prelude.timestamp

    out["warningUpdatedTime"] = (
        capo_arc_region_switch.types._prelude.timestamp.serialize_aws_json_1_0(
            value["warning_updated_time"]
        )
    )
    out["warningMessage"] = value["warning_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceWarning:
    out: ResourceWarning = {}  # type: ignore[typeddict-item]
    if data.get("workflow") is not None:
        import capo_arc_region_switch.types.minimal_workflow

        out["workflow"] = (
            capo_arc_region_switch.types.minimal_workflow.deserialize_aws_json_1_0(
                data["workflow"]
            )
        )
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = ""
    if data.get("stepName") is not None:
        out["step_name"] = data["stepName"]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    if data.get("warningStatus") is not None:
        import capo_arc_region_switch.types.resource_warning_status

        out["warning_status"] = (
            capo_arc_region_switch.types.resource_warning_status.deserialize_aws_json_1_0(
                data["warningStatus"]
            )
        )
    else:
        import typing

        out["warning_status"] = typing.cast(
            "capo_arc_region_switch.types.resource_warning_status.ResourceWarningStatus",
            "",
        )
    if data.get("warningUpdatedTime") is not None:
        import capo_arc_region_switch.types._prelude.timestamp

        out["warning_updated_time"] = (
            capo_arc_region_switch.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["warningUpdatedTime"]
            )
        )
    else:
        import datetime

        out["warning_updated_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("warningMessage") is not None:
        out["warning_message"] = data["warningMessage"]
    else:
        out["warning_message"] = ""
    return out
