"""Generated from Smithy shape ``com.amazonaws.athena#CreateWorkGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.tag_list
    import capo_athena.types.work_group_configuration
    import capo_athena.types.work_group_description_string
    import capo_athena.types.work_group_name


class CreateWorkGroupInput(TypedDict, closed=True):
    name: "capo_athena.types.work_group_name.WorkGroupName"
    """<p>The workgroup name.</p>"""
    configuration: NotRequired[
        "capo_athena.types.work_group_configuration.WorkGroupConfiguration"
    ]
    """<p>Contains configuration information for creating an Athena SQL workgroup or Spark enabled Athena workgroup. Athena SQL workgroup configuration includes the location in Amazon S3 where query and calculation results are stored, the encryption configuration, if any, used for encrypting query results, whether the Amazon CloudWatch Metrics are enabled for the workgroup, the limit for the amount of bytes scanned (cutoff) per query, if it is specified, and whether workgroup's settings (specified with <code>EnforceWorkGroupConfiguration</code>) in the <code>WorkGroupConfiguration</code> override client-side settings. See <a>WorkGroupConfiguration$EnforceWorkGroupConfiguration</a>.</p>"""
    description: NotRequired[
        "capo_athena.types.work_group_description_string.WorkGroupDescriptionString"
    ]
    """<p>The workgroup description.</p>"""
    tags: NotRequired["capo_athena.types.tag_list.TagList"]
    """<p>A list of comma separated tags to add to the workgroup that is created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWorkGroupInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "configuration" in value:
        import capo_athena.types.work_group_configuration

        out["Configuration"] = (
            capo_athena.types.work_group_configuration.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_athena.types.tag_list

        out["Tags"] = capo_athena.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWorkGroupInput:
    out: CreateWorkGroupInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Configuration") is not None:
        import capo_athena.types.work_group_configuration

        out["configuration"] = (
            capo_athena.types.work_group_configuration.deserialize_aws_json_1_1(
                data["Configuration"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_athena.types.tag_list

        out["tags"] = capo_athena.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
