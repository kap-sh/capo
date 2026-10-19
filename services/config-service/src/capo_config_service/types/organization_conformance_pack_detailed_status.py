"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationConformancePackDetailedStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.account_id
    import capo_config_service.types.date
    import capo_config_service.types.organization_resource_detailed_status
    import capo_config_service.types.string
    import capo_config_service.types.string_with_char_limit256


class OrganizationConformancePackDetailedStatus(TypedDict, closed=True):
    account_id: "capo_config_service.types.account_id.AccountId"
    """<p>The 12-digit account ID of a member account.</p>"""
    conformance_pack_name: (
        "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    )
    """<p>The name of conformance pack deployed in the member account.</p>"""
    status: "capo_config_service.types.organization_resource_detailed_status.OrganizationResourceDetailedStatus"
    """<p>Indicates deployment status for conformance pack in a member account. When management account calls <code>PutOrganizationConformancePack</code> action for the first time, conformance pack status is created in the member account. When management account calls <code>PutOrganizationConformancePack</code> action for the second time, conformance pack status is updated in the member account. Conformance pack status is deleted when the management account deletes <code>OrganizationConformancePack</code> and disables service access for <code>config-multiaccountsetup.amazonaws.com</code>. </p> <p> Config sets the state of the conformance pack to:</p> <ul> <li> <p> <code>CREATE_SUCCESSFUL</code> when conformance pack has been created in the member account. </p> </li> <li> <p> <code>CREATE_IN_PROGRESS</code> when conformance pack is being created in the member account.</p> </li> <li> <p> <code>CREATE_FAILED</code> when conformance pack creation has failed in the member account.</p> </li> <li> <p> <code>DELETE_FAILED</code> when conformance pack deletion has failed in the member account.</p> </li> <li> <p> <code>DELETE_IN_PROGRESS</code> when conformance pack is being deleted in the member account.</p> </li> <li> <p> <code>DELETE_SUCCESSFUL</code> when conformance pack has been deleted in the member account. </p> </li> <li> <p> <code>UPDATE_SUCCESSFUL</code> when conformance pack has been updated in the member account.</p> </li> <li> <p> <code>UPDATE_IN_PROGRESS</code> when conformance pack is being updated in the member account.</p> </li> <li> <p> <code>UPDATE_FAILED</code> when conformance pack deletion has failed in the member account.</p> </li> </ul>"""
    error_code: NotRequired["capo_config_service.types.string.String"]
    """<p>An error code that is returned when conformance pack creation or deletion failed in the member account. </p>"""
    error_message: NotRequired["capo_config_service.types.string.String"]
    """<p>An error message indicating that conformance pack account creation or deletion has failed due to an error in the member account. </p>"""
    last_update_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The timestamp of the last status update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationConformancePackDetailedStatus) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["ConformancePackName"] = value["conformance_pack_name"]
    import capo_config_service.types.organization_resource_detailed_status

    out["Status"] = (
        capo_config_service.types.organization_resource_detailed_status.serialize_aws_json_1_1(
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


def deserialize_aws_json_1_1(data: dict) -> OrganizationConformancePackDetailedStatus:
    out: OrganizationConformancePackDetailedStatus = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        out["account_id"] = ""
    if data.get("ConformancePackName") is not None:
        out["conformance_pack_name"] = data["ConformancePackName"]
    else:
        out["conformance_pack_name"] = ""
    if data.get("Status") is not None:
        import capo_config_service.types.organization_resource_detailed_status

        out["status"] = (
            capo_config_service.types.organization_resource_detailed_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_config_service.types.organization_resource_detailed_status.OrganizationResourceDetailedStatus",
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
