"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateVersion``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.date_time
    import capo_ec2.types.launch_template_name
    import capo_ec2.types.long
    import capo_ec2.types.operator_response
    import capo_ec2.types.response_launch_template_data
    import capo_ec2.types.string
    import capo_ec2.types.version_description


class LaunchTemplateVersion(TypedDict, closed=True):
    launch_template_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the launch template.</p>"""
    launch_template_name: NotRequired[
        "capo_ec2.types.launch_template_name.LaunchTemplateName"
    ]
    """<p>The name of the launch template.</p>"""
    version_number: NotRequired["capo_ec2.types.long.Long"]
    """<p>The version number.</p>"""
    version_description: NotRequired[
        "capo_ec2.types.version_description.VersionDescription"
    ]
    """<p>The description for the version.</p>"""
    create_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The time the version was created.</p>"""
    created_by: NotRequired["capo_ec2.types.string.String"]
    """<p>The principal that created the version.</p>"""
    default_version: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the version is the default version.</p>"""
    launch_template_data: NotRequired[
        "capo_ec2.types.response_launch_template_data.ResponseLaunchTemplateData"
    ]
    """<p>Information about the launch template.</p>"""
    operator: NotRequired["capo_ec2.types.operator_response.OperatorResponse"]
    """<p>The entity that manages the launch template.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateVersion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "launch_template_id" in value:
        pairs.append(
            (f"{key_prefix}LaunchTemplateId", str(value["launch_template_id"]))
        )
    if "launch_template_name" in value:
        pairs.append(
            (f"{key_prefix}LaunchTemplateName", str(value["launch_template_name"]))
        )
    if "version_number" in value:
        pairs.append((f"{key_prefix}VersionNumber", str(value["version_number"])))
    if "version_description" in value:
        pairs.append(
            (f"{key_prefix}VersionDescription", str(value["version_description"]))
        )
    if "create_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["create_time"], pairs, f"{key_prefix}CreateTime"
        )
    if "created_by" in value:
        pairs.append((f"{key_prefix}CreatedBy", str(value["created_by"])))
    if "default_version" in value:
        pairs.append(
            (
                f"{key_prefix}DefaultVersion",
                "true" if value["default_version"] else "false",
            )
        )
    if "launch_template_data" in value:
        import capo_ec2.types.response_launch_template_data

        capo_ec2.types.response_launch_template_data.serialize_ec2_query(
            value["launch_template_data"], pairs, f"{key_prefix}LaunchTemplateData"
        )
    if "operator" in value:
        import capo_ec2.types.operator_response

        capo_ec2.types.operator_response.serialize_ec2_query(
            value["operator"], pairs, f"{key_prefix}Operator"
        )


def deserialize_ec2_query(el: Element) -> LaunchTemplateVersion:
    out: LaunchTemplateVersion = {}  # type: ignore[typeddict-item]
    child_launch_template_id = el.find("launchTemplateId")
    if child_launch_template_id is not None:
        out["launch_template_id"] = str(child_launch_template_id.text or "")
    child_launch_template_name = el.find("launchTemplateName")
    if child_launch_template_name is not None:
        out["launch_template_name"] = str(child_launch_template_name.text or "")
    child_version_number = el.find("versionNumber")
    if child_version_number is not None:
        out["version_number"] = int(child_version_number.text or "")
    child_version_description = el.find("versionDescription")
    if child_version_description is not None:
        out["version_description"] = str(child_version_description.text or "")
    child_create_time = el.find("createTime")
    if child_create_time is not None:
        import capo_ec2.types.date_time

        out["create_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_create_time
        )
    child_created_by = el.find("createdBy")
    if child_created_by is not None:
        out["created_by"] = str(child_created_by.text or "")
    child_default_version = el.find("defaultVersion")
    if child_default_version is not None:
        out["default_version"] = (child_default_version.text or "").lower() == "true"
    child_launch_template_data = el.find("launchTemplateData")
    if child_launch_template_data is not None:
        import capo_ec2.types.response_launch_template_data

        out["launch_template_data"] = (
            capo_ec2.types.response_launch_template_data.deserialize_ec2_query(
                child_launch_template_data
            )
        )
    child_operator = el.find("operator")
    if child_operator is not None:
        import capo_ec2.types.operator_response

        out["operator"] = capo_ec2.types.operator_response.deserialize_ec2_query(
            child_operator
        )
    return out


def redact_sensitive(value: LaunchTemplateVersion) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "launch_template_data" in value:
        import capo_ec2.types.response_launch_template_data

        out["launch_template_data"] = (
            capo_ec2.types.response_launch_template_data.redact_sensitive(
                value["launch_template_data"]
            )
        )
    return out
