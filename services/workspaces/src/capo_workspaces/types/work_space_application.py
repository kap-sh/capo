"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkSpaceApplication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.compute_list
    import capo_workspaces.types.non_empty_string
    import capo_workspaces.types.operating_system_name_list
    import capo_workspaces.types.string2048
    import capo_workspaces.types.timestamp
    import capo_workspaces.types.work_space_application_id
    import capo_workspaces.types.work_space_application_license_type
    import capo_workspaces.types.work_space_application_owner
    import capo_workspaces.types.work_space_application_state


class WorkSpaceApplication(TypedDict, closed=True):
    application_id: NotRequired[
        "capo_workspaces.types.work_space_application_id.WorkSpaceApplicationId"
    ]
    """<p>The identifier of the application.</p>"""
    created: NotRequired["capo_workspaces.types.timestamp.Timestamp"]
    """<p>The time the application is created.</p>"""
    description: NotRequired["capo_workspaces.types.string2048.String2048"]
    """<p>The description of the WorkSpace application.</p>"""
    license_type: NotRequired[
        "capo_workspaces.types.work_space_application_license_type.WorkSpaceApplicationLicenseType"
    ]
    """<p>The license availability for the applications.</p>"""
    name: NotRequired["capo_workspaces.types.non_empty_string.NonEmptyString"]
    """<p>The name of the WorkSpace application.</p>"""
    owner: NotRequired[
        "capo_workspaces.types.work_space_application_owner.WorkSpaceApplicationOwner"
    ]
    """<p>The owner of the WorkSpace application.</p>"""
    state: NotRequired[
        "capo_workspaces.types.work_space_application_state.WorkSpaceApplicationState"
    ]
    """<p>The status of WorkSpace application.</p>"""
    supported_compute_type_names: NotRequired[
        "capo_workspaces.types.compute_list.ComputeList"
    ]
    """<p>The supported compute types of the WorkSpace application.</p>"""
    supported_operating_system_names: NotRequired[
        "capo_workspaces.types.operating_system_name_list.OperatingSystemNameList"
    ]
    """<p>The supported operating systems of the WorkSpace application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkSpaceApplication) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "created" in value:
        import capo_workspaces.types.timestamp

        out["Created"] = capo_workspaces.types.timestamp.serialize_aws_json_1_1(
            value["created"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "license_type" in value:
        import capo_workspaces.types.work_space_application_license_type

        out["LicenseType"] = (
            capo_workspaces.types.work_space_application_license_type.serialize_aws_json_1_1(
                value["license_type"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "state" in value:
        import capo_workspaces.types.work_space_application_state

        out["State"] = (
            capo_workspaces.types.work_space_application_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "supported_compute_type_names" in value:
        import capo_workspaces.types.compute_list

        out["SupportedComputeTypeNames"] = (
            capo_workspaces.types.compute_list.serialize_aws_json_1_1(
                value["supported_compute_type_names"]
            )
        )
    if "supported_operating_system_names" in value:
        import capo_workspaces.types.operating_system_name_list

        out["SupportedOperatingSystemNames"] = (
            capo_workspaces.types.operating_system_name_list.serialize_aws_json_1_1(
                value["supported_operating_system_names"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkSpaceApplication:
    out: WorkSpaceApplication = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    if data.get("Created") is not None:
        import capo_workspaces.types.timestamp

        out["created"] = capo_workspaces.types.timestamp.deserialize_aws_json_1_1(
            data["Created"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("LicenseType") is not None:
        import capo_workspaces.types.work_space_application_license_type

        out["license_type"] = (
            capo_workspaces.types.work_space_application_license_type.deserialize_aws_json_1_1(
                data["LicenseType"]
            )
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    if data.get("State") is not None:
        import capo_workspaces.types.work_space_application_state

        out["state"] = (
            capo_workspaces.types.work_space_application_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if data.get("SupportedComputeTypeNames") is not None:
        import capo_workspaces.types.compute_list

        out["supported_compute_type_names"] = (
            capo_workspaces.types.compute_list.deserialize_aws_json_1_1(
                data["SupportedComputeTypeNames"]
            )
        )
    if data.get("SupportedOperatingSystemNames") is not None:
        import capo_workspaces.types.operating_system_name_list

        out["supported_operating_system_names"] = (
            capo_workspaces.types.operating_system_name_list.deserialize_aws_json_1_1(
                data["SupportedOperatingSystemNames"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WorkSpaceApplication) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "created" in value:
        import capo_workspaces.types.timestamp

        out["Created"] = capo_workspaces.types.timestamp.serialize_cbor(
            value["created"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "license_type" in value:
        import capo_workspaces.types.work_space_application_license_type

        out["LicenseType"] = (
            capo_workspaces.types.work_space_application_license_type.serialize_cbor(
                value["license_type"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "state" in value:
        import capo_workspaces.types.work_space_application_state

        out["State"] = (
            capo_workspaces.types.work_space_application_state.serialize_cbor(
                value["state"]
            )
        )
    if "supported_compute_type_names" in value:
        import capo_workspaces.types.compute_list

        out["SupportedComputeTypeNames"] = (
            capo_workspaces.types.compute_list.serialize_cbor(
                value["supported_compute_type_names"]
            )
        )
    if "supported_operating_system_names" in value:
        import capo_workspaces.types.operating_system_name_list

        out["SupportedOperatingSystemNames"] = (
            capo_workspaces.types.operating_system_name_list.serialize_cbor(
                value["supported_operating_system_names"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> WorkSpaceApplication:
    out: WorkSpaceApplication = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    if data.get("Created") is not None:
        import capo_workspaces.types.timestamp

        out["created"] = capo_workspaces.types.timestamp.deserialize_cbor(
            data["Created"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("LicenseType") is not None:
        import capo_workspaces.types.work_space_application_license_type

        out["license_type"] = (
            capo_workspaces.types.work_space_application_license_type.deserialize_cbor(
                data["LicenseType"]
            )
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    if data.get("State") is not None:
        import capo_workspaces.types.work_space_application_state

        out["state"] = (
            capo_workspaces.types.work_space_application_state.deserialize_cbor(
                data["State"]
            )
        )
    if data.get("SupportedComputeTypeNames") is not None:
        import capo_workspaces.types.compute_list

        out["supported_compute_type_names"] = (
            capo_workspaces.types.compute_list.deserialize_cbor(
                data["SupportedComputeTypeNames"]
            )
        )
    if data.get("SupportedOperatingSystemNames") is not None:
        import capo_workspaces.types.operating_system_name_list

        out["supported_operating_system_names"] = (
            capo_workspaces.types.operating_system_name_list.deserialize_cbor(
                data["SupportedOperatingSystemNames"]
            )
        )
    return out
