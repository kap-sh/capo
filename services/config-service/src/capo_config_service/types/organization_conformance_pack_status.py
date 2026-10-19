"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationConformancePackStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.date
    import capo_config_service.types.organization_conformance_pack_name
    import capo_config_service.types.organization_resource_status
    import capo_config_service.types.string


class OrganizationConformancePackStatus(TypedDict, closed=True):
    organization_conformance_pack_name: "capo_config_service.types.organization_conformance_pack_name.OrganizationConformancePackName"
    """<p>The name that you assign to organization conformance pack.</p>"""
    status: "capo_config_service.types.organization_resource_status.OrganizationResourceStatus"
    """<p>Indicates deployment status of an organization conformance pack. When management account calls PutOrganizationConformancePack for the first time, conformance pack status is created in all the member accounts. When management account calls PutOrganizationConformancePack for the second time, conformance pack status is updated in all the member accounts. Additionally, conformance pack status is updated when one or more member accounts join or leave an organization. Conformance pack status is deleted when the management account deletes OrganizationConformancePack in all the member accounts and disables service access for <code>config-multiaccountsetup.amazonaws.com</code>.</p> <p>Config sets the state of the conformance pack to:</p> <ul> <li> <p> <code>CREATE_SUCCESSFUL</code> when an organization conformance pack has been successfully created in all the member accounts. </p> </li> <li> <p> <code>CREATE_IN_PROGRESS</code> when an organization conformance pack creation is in progress.</p> </li> <li> <p> <code>CREATE_FAILED</code> when an organization conformance pack creation failed in one or more member accounts within that organization.</p> </li> <li> <p> <code>DELETE_FAILED</code> when an organization conformance pack deletion failed in one or more member accounts within that organization.</p> </li> <li> <p> <code>DELETE_IN_PROGRESS</code> when an organization conformance pack deletion is in progress.</p> </li> <li> <p> <code>DELETE_SUCCESSFUL</code> when an organization conformance pack has been successfully deleted from all the member accounts.</p> </li> <li> <p> <code>UPDATE_SUCCESSFUL</code> when an organization conformance pack has been successfully updated in all the member accounts.</p> </li> <li> <p> <code>UPDATE_IN_PROGRESS</code> when an organization conformance pack update is in progress.</p> </li> <li> <p> <code>UPDATE_FAILED</code> when an organization conformance pack update failed in one or more member accounts within that organization.</p> </li> </ul>"""
    error_code: NotRequired["capo_config_service.types.string.String"]
    """<p>An error code that is returned when organization conformance pack creation or deletion has failed in a member account. </p>"""
    error_message: NotRequired["capo_config_service.types.string.String"]
    """<p>An error message indicating that organization conformance pack creation or deletion failed due to an error. </p>"""
    last_update_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The timestamp of the last update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationConformancePackStatus) -> dict:
    out: dict = {}
    out["OrganizationConformancePackName"] = value["organization_conformance_pack_name"]
    import capo_config_service.types.organization_resource_status

    out["Status"] = (
        capo_config_service.types.organization_resource_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "last_update_time" in value:
        import capo_config_service.types.date

        out["LastUpdateTime"] = capo_config_service.types.date.serialize_aws_json_1_1(
            value["last_update_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OrganizationConformancePackStatus:
    out: OrganizationConformancePackStatus = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationConformancePackName") is not None:
        out["organization_conformance_pack_name"] = data[
            "OrganizationConformancePackName"
        ]
    else:
        out["organization_conformance_pack_name"] = ""
    if data.get("Status") is not None:
        import capo_config_service.types.organization_resource_status

        out["status"] = (
            capo_config_service.types.organization_resource_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_config_service.types.organization_resource_status.OrganizationResourceStatus",
            "",
        )
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("LastUpdateTime") is not None:
        import capo_config_service.types.date

        out["last_update_time"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["LastUpdateTime"]
            )
        )
    return out
