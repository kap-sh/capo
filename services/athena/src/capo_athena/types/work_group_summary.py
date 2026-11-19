"""Generated from Smithy shape ``com.amazonaws.athena#WorkGroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.date
    import capo_athena.types.engine_version
    import capo_athena.types.identity_center_application_arn
    import capo_athena.types.work_group_description_string
    import capo_athena.types.work_group_name
    import capo_athena.types.work_group_state


class WorkGroupSummary(TypedDict, closed=True):
    name: NotRequired["capo_athena.types.work_group_name.WorkGroupName"]
    """<p>The name of the workgroup.</p>"""
    state: NotRequired["capo_athena.types.work_group_state.WorkGroupState"]
    """<p>The state of the workgroup.</p>"""
    description: NotRequired[
        "capo_athena.types.work_group_description_string.WorkGroupDescriptionString"
    ]
    """<p>The workgroup description.</p>"""
    creation_time: NotRequired["capo_athena.types.date.Date"]
    """<p>The workgroup creation date and time.</p>"""
    engine_version: NotRequired["capo_athena.types.engine_version.EngineVersion"]
    """<p>The engine version setting for all queries on the workgroup.</p>"""
    identity_center_application_arn: NotRequired[
        "capo_athena.types.identity_center_application_arn.IdentityCenterApplicationArn"
    ]
    """<p>The ARN of the IAM Identity Center enabled application associated with the workgroup.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkGroupSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "state" in value:
        import capo_athena.types.work_group_state

        out["State"] = capo_athena.types.work_group_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "creation_time" in value:
        import capo_athena.types.date

        out["CreationTime"] = capo_athena.types.date.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "engine_version" in value:
        import capo_athena.types.engine_version

        out["EngineVersion"] = capo_athena.types.engine_version.serialize_aws_json_1_1(
            value["engine_version"]
        )
    if "identity_center_application_arn" in value:
        out["IdentityCenterApplicationArn"] = value["identity_center_application_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkGroupSummary:
    out: WorkGroupSummary = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("State") is not None:
        import capo_athena.types.work_group_state

        out["state"] = capo_athena.types.work_group_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CreationTime") is not None:
        import capo_athena.types.date

        out["creation_time"] = capo_athena.types.date.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("EngineVersion") is not None:
        import capo_athena.types.engine_version

        out["engine_version"] = (
            capo_athena.types.engine_version.deserialize_aws_json_1_1(
                data["EngineVersion"]
            )
        )
    if data.get("IdentityCenterApplicationArn") is not None:
        out["identity_center_application_arn"] = data["IdentityCenterApplicationArn"]
    return out
