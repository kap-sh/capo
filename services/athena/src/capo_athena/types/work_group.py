"""Generated from Smithy shape ``com.amazonaws.athena#WorkGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.date
    import capo_athena.types.identity_center_application_arn
    import capo_athena.types.work_group_configuration
    import capo_athena.types.work_group_description_string
    import capo_athena.types.work_group_name
    import capo_athena.types.work_group_state


class WorkGroup(TypedDict, closed=True):
    name: "capo_athena.types.work_group_name.WorkGroupName"
    """<p>The workgroup name.</p>"""
    state: NotRequired["capo_athena.types.work_group_state.WorkGroupState"]
    """<p>The state of the workgroup: ENABLED or DISABLED.</p>"""
    configuration: NotRequired[
        "capo_athena.types.work_group_configuration.WorkGroupConfiguration"
    ]
    """<p>The configuration of the workgroup, which includes the location in Amazon S3 where query and calculation results are stored, the encryption configuration, if any, used for query and calculation results; whether the Amazon CloudWatch Metrics are enabled for the workgroup; whether workgroup settings override client-side settings; and the data usage limits for the amount of data scanned per query or per workgroup. The workgroup settings override is specified in <code>EnforceWorkGroupConfiguration</code> (true/false) in the <code>WorkGroupConfiguration</code>. See <a>WorkGroupConfiguration$EnforceWorkGroupConfiguration</a>.</p>"""
    description: NotRequired[
        "capo_athena.types.work_group_description_string.WorkGroupDescriptionString"
    ]
    """<p>The workgroup description.</p>"""
    creation_time: NotRequired["capo_athena.types.date.Date"]
    """<p>The date and time the workgroup was created.</p>"""
    identity_center_application_arn: NotRequired[
        "capo_athena.types.identity_center_application_arn.IdentityCenterApplicationArn"
    ]
    """<p>The ARN of the IAM Identity Center enabled application associated with the workgroup.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkGroup) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "state" in value:
        import capo_athena.types.work_group_state

        out["State"] = capo_athena.types.work_group_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "configuration" in value:
        import capo_athena.types.work_group_configuration

        out["Configuration"] = (
            capo_athena.types.work_group_configuration.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "creation_time" in value:
        import capo_athena.types.date

        out["CreationTime"] = capo_athena.types.date.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "identity_center_application_arn" in value:
        out["IdentityCenterApplicationArn"] = value["identity_center_application_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkGroup:
    out: WorkGroup = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("State") is not None:
        import capo_athena.types.work_group_state

        out["state"] = capo_athena.types.work_group_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if data.get("Configuration") is not None:
        import capo_athena.types.work_group_configuration

        out["configuration"] = (
            capo_athena.types.work_group_configuration.deserialize_aws_json_1_1(
                data["Configuration"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CreationTime") is not None:
        import capo_athena.types.date

        out["creation_time"] = capo_athena.types.date.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("IdentityCenterApplicationArn") is not None:
        out["identity_center_application_arn"] = data["IdentityCenterApplicationArn"]
    return out
