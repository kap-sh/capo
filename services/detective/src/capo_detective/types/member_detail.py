"""Generated from Smithy shape ``com.amazonaws.detective#MemberDetail``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_detective.types.account_id
    import capo_detective.types.byte_value
    import capo_detective.types.datasource_package_ingest_states
    import capo_detective.types.email_address
    import capo_detective.types.graph_arn
    import capo_detective.types.invitation_type
    import capo_detective.types.member_disabled_reason
    import capo_detective.types.member_status
    import capo_detective.types.percentage
    import capo_detective.types.timestamp
    import capo_detective.types.volume_usage_by_datasource_package


class MemberDetail(TypedDict, closed=True):
    account_id: NotRequired["capo_detective.types.account_id.AccountId"]
    """<p>The Amazon Web Services account identifier for the member account.</p>"""
    email_address: NotRequired["capo_detective.types.email_address.EmailAddress"]
    """<p>The Amazon Web Services account root user email address for the member account.</p>"""
    graph_arn: NotRequired["capo_detective.types.graph_arn.GraphArn"]
    """<p>The ARN of the behavior graph.</p>"""
    master_id: NotRequired["capo_detective.types.account_id.AccountId"]
    """<p>The Amazon Web Services account identifier of the administrator account for the behavior graph.</p>"""
    administrator_id: NotRequired["capo_detective.types.account_id.AccountId"]
    """<p>The Amazon Web Services account identifier of the administrator account for the behavior graph.</p>"""
    status: NotRequired["capo_detective.types.member_status.MemberStatus"]
    """<p>The current membership status of the member account. The status can have one of the following values:</p> <ul> <li> <p> <code>INVITED</code> - For invited accounts only. Indicates that the member was sent an invitation but has not yet responded.</p> </li> <li> <p> <code>VERIFICATION_IN_PROGRESS</code> - For invited accounts only, indicates that Detective is verifying that the account identifier and email address provided for the member account match. If they do match, then Detective sends the invitation. If the email address and account identifier don't match, then the member cannot be added to the behavior graph.</p> <p>For organization accounts in the organization behavior graph, indicates that Detective is verifying that the account belongs to the organization.</p> </li> <li> <p> <code>VERIFICATION_FAILED</code> - For invited accounts only. Indicates that the account and email address provided for the member account do not match, and Detective did not send an invitation to the account.</p> </li> <li> <p> <code>ENABLED</code> - Indicates that the member account currently contributes data to the behavior graph. For invited accounts, the member account accepted the invitation. For organization accounts in the organization behavior graph, the Detective administrator account enabled the organization account as a member account.</p> </li> <li> <p> <code>ACCEPTED_BUT_DISABLED</code> - The account accepted the invitation, or was enabled by the Detective administrator account, but is prevented from contributing data to the behavior graph. <code>DisabledReason</code> provides the reason why the member account is not enabled.</p> </li> </ul> <p>Invited accounts that declined an invitation or that were removed from the behavior graph are not included. In the organization behavior graph, organization accounts that the Detective administrator account did not enable are not included.</p>"""
    disabled_reason: NotRequired[
        "capo_detective.types.member_disabled_reason.MemberDisabledReason"
    ]
    """<p>For member accounts with a status of <code>ACCEPTED_BUT_DISABLED</code>, the reason that the member account is not enabled.</p> <p>The reason can have one of the following values:</p> <ul> <li> <p> <code>VOLUME_TOO_HIGH</code> - Indicates that adding the member account would cause the data volume for the behavior graph to be too high.</p> </li> <li> <p> <code>VOLUME_UNKNOWN</code> - Indicates that Detective is unable to verify the data volume for the member account. This is usually because the member account is not enrolled in Amazon GuardDuty. </p> </li> </ul>"""
    invited_time: NotRequired["capo_detective.types.timestamp.Timestamp"]
    """<p>For invited accounts, the date and time that Detective sent the invitation to the account. The value is an ISO8601 formatted string. For example, <code>2021-08-18T16:35:56.284Z</code>.</p>"""
    updated_time: NotRequired["capo_detective.types.timestamp.Timestamp"]
    """<p>The date and time that the member account was last updated. The value is an ISO8601 formatted string. For example, <code>2021-08-18T16:35:56.284Z</code>.</p>"""
    volume_usage_in_bytes: NotRequired["capo_detective.types.byte_value.ByteValue"]
    """<p>The data volume in bytes per day for the member account.</p>"""
    volume_usage_updated_time: NotRequired["capo_detective.types.timestamp.Timestamp"]
    """<p>The data and time when the member account data volume was last updated. The value is an ISO8601 formatted string. For example, <code>2021-08-18T16:35:56.284Z</code>.</p>"""
    percent_of_graph_utilization: NotRequired[
        "capo_detective.types.percentage.Percentage"
    ]
    """<p>The member account data volume as a percentage of the maximum allowed data volume. 0 indicates 0 percent, and 100 indicates 100 percent.</p> <p>Note that this is not the percentage of the behavior graph data volume.</p> <p>For example, the data volume for the behavior graph is 80 GB per day. The maximum data volume is 160 GB per day. If the data volume for the member account is 40 GB per day, then <code>PercentOfGraphUtilization</code> is 25. It represents 25% of the maximum allowed data volume. </p>"""
    percent_of_graph_utilization_updated_time: NotRequired[
        "capo_detective.types.timestamp.Timestamp"
    ]
    """<p>The date and time when the graph utilization percentage was last updated. The value is an ISO8601 formatted string. For example, <code>2021-08-18T16:35:56.284Z</code>.</p>"""
    invitation_type: NotRequired["capo_detective.types.invitation_type.InvitationType"]
    """<p>The type of behavior graph membership.</p> <p>For an organization account in the organization behavior graph, the type is <code>ORGANIZATION</code>.</p> <p>For an account that was invited to a behavior graph, the type is <code>INVITATION</code>. </p>"""
    volume_usage_by_datasource_package: NotRequired[
        "capo_detective.types.volume_usage_by_datasource_package.VolumeUsageByDatasourcePackage"
    ]
    """<p>Details on the volume of usage for each data source package in a behavior graph.</p>"""
    datasource_package_ingest_states: NotRequired[
        "capo_detective.types.datasource_package_ingest_states.DatasourcePackageIngestStates"
    ]
    """<p>The state of a data source package for the behavior graph.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberDetail) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "email_address" in value:
        out["EmailAddress"] = value["email_address"]
    if "graph_arn" in value:
        out["GraphArn"] = value["graph_arn"]
    if "master_id" in value:
        out["MasterId"] = value["master_id"]
    if "administrator_id" in value:
        out["AdministratorId"] = value["administrator_id"]
    if "status" in value:
        import capo_detective.types.member_status

        out["Status"] = capo_detective.types.member_status.serialize_json(
            value["status"]
        )
    if "disabled_reason" in value:
        import capo_detective.types.member_disabled_reason

        out["DisabledReason"] = (
            capo_detective.types.member_disabled_reason.serialize_json(
                value["disabled_reason"]
            )
        )
    if "invited_time" in value:
        import capo_detective.types.timestamp

        out["InvitedTime"] = capo_detective.types.timestamp.serialize_json(
            value["invited_time"]
        )
    if "updated_time" in value:
        import capo_detective.types.timestamp

        out["UpdatedTime"] = capo_detective.types.timestamp.serialize_json(
            value["updated_time"]
        )
    if "volume_usage_in_bytes" in value:
        out["VolumeUsageInBytes"] = value["volume_usage_in_bytes"]
    if "volume_usage_updated_time" in value:
        import capo_detective.types.timestamp

        out["VolumeUsageUpdatedTime"] = capo_detective.types.timestamp.serialize_json(
            value["volume_usage_updated_time"]
        )
    if "percent_of_graph_utilization" in value:
        out["PercentOfGraphUtilization"] = (
            "NaN"
            if value["percent_of_graph_utilization"]
            != value["percent_of_graph_utilization"]
            else "Infinity"
            if value["percent_of_graph_utilization"] == float("inf")
            else "-Infinity"
            if value["percent_of_graph_utilization"] == float("-inf")
            else value["percent_of_graph_utilization"]
        )
    if "percent_of_graph_utilization_updated_time" in value:
        import capo_detective.types.timestamp

        out["PercentOfGraphUtilizationUpdatedTime"] = (
            capo_detective.types.timestamp.serialize_json(
                value["percent_of_graph_utilization_updated_time"]
            )
        )
    if "invitation_type" in value:
        import capo_detective.types.invitation_type

        out["InvitationType"] = capo_detective.types.invitation_type.serialize_json(
            value["invitation_type"]
        )
    if "volume_usage_by_datasource_package" in value:
        import capo_detective.types.volume_usage_by_datasource_package

        out["VolumeUsageByDatasourcePackage"] = (
            capo_detective.types.volume_usage_by_datasource_package.serialize_json(
                value["volume_usage_by_datasource_package"]
            )
        )
    if "datasource_package_ingest_states" in value:
        import capo_detective.types.datasource_package_ingest_states

        out["DatasourcePackageIngestStates"] = (
            capo_detective.types.datasource_package_ingest_states.serialize_json(
                value["datasource_package_ingest_states"]
            )
        )
    return out


def deserialize_json(data: dict) -> MemberDetail:
    out: MemberDetail = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("EmailAddress") is not None:
        out["email_address"] = data["EmailAddress"]
    if data.get("GraphArn") is not None:
        out["graph_arn"] = data["GraphArn"]
    if data.get("MasterId") is not None:
        out["master_id"] = data["MasterId"]
    if data.get("AdministratorId") is not None:
        out["administrator_id"] = data["AdministratorId"]
    if data.get("Status") is not None:
        import capo_detective.types.member_status

        out["status"] = capo_detective.types.member_status.deserialize_json(
            data["Status"]
        )
    if data.get("DisabledReason") is not None:
        import capo_detective.types.member_disabled_reason

        out["disabled_reason"] = (
            capo_detective.types.member_disabled_reason.deserialize_json(
                data["DisabledReason"]
            )
        )
    if data.get("InvitedTime") is not None:
        import capo_detective.types.timestamp

        out["invited_time"] = capo_detective.types.timestamp.deserialize_json(
            data["InvitedTime"]
        )
    if data.get("UpdatedTime") is not None:
        import capo_detective.types.timestamp

        out["updated_time"] = capo_detective.types.timestamp.deserialize_json(
            data["UpdatedTime"]
        )
    if data.get("VolumeUsageInBytes") is not None:
        out["volume_usage_in_bytes"] = data["VolumeUsageInBytes"]
    if data.get("VolumeUsageUpdatedTime") is not None:
        import capo_detective.types.timestamp

        out["volume_usage_updated_time"] = (
            capo_detective.types.timestamp.deserialize_json(
                data["VolumeUsageUpdatedTime"]
            )
        )
    if data.get("PercentOfGraphUtilization") is not None:
        out["percent_of_graph_utilization"] = float(data["PercentOfGraphUtilization"])
    if data.get("PercentOfGraphUtilizationUpdatedTime") is not None:
        import capo_detective.types.timestamp

        out["percent_of_graph_utilization_updated_time"] = (
            capo_detective.types.timestamp.deserialize_json(
                data["PercentOfGraphUtilizationUpdatedTime"]
            )
        )
    if data.get("InvitationType") is not None:
        import capo_detective.types.invitation_type

        out["invitation_type"] = capo_detective.types.invitation_type.deserialize_json(
            data["InvitationType"]
        )
    if data.get("VolumeUsageByDatasourcePackage") is not None:
        import capo_detective.types.volume_usage_by_datasource_package

        out["volume_usage_by_datasource_package"] = (
            capo_detective.types.volume_usage_by_datasource_package.deserialize_json(
                data["VolumeUsageByDatasourcePackage"]
            )
        )
    if data.get("DatasourcePackageIngestStates") is not None:
        import capo_detective.types.datasource_package_ingest_states

        out["datasource_package_ingest_states"] = (
            capo_detective.types.datasource_package_ingest_states.deserialize_json(
                data["DatasourcePackageIngestStates"]
            )
        )
    return out


def redact_sensitive(value: MemberDetail) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email_address" in value:
        out["email_address"] = "*** Sensitive Data Redacted ***"
    return out
