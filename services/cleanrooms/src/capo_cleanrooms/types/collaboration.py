"""Generated from Smithy shape ``com.amazonaws.cleanrooms#Collaboration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.account_id
    import capo_cleanrooms.types.allowed_result_regions
    import capo_cleanrooms.types.analytics_engine
    import capo_cleanrooms.types.auto_approved_change_type_list
    import capo_cleanrooms.types.collaboration_arn
    import capo_cleanrooms.types.collaboration_description
    import capo_cleanrooms.types.collaboration_job_log_status
    import capo_cleanrooms.types.collaboration_name
    import capo_cleanrooms.types.collaboration_query_log_status
    import capo_cleanrooms.types.data_encryption_metadata
    import capo_cleanrooms.types.display_name
    import capo_cleanrooms.types.member_status
    import capo_cleanrooms.types.membership_arn
    import capo_cleanrooms.types.uuid


class Collaboration(TypedDict, closed=True):
    id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique ID for the collaboration.</p>"""
    arn: "capo_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The unique ARN for the collaboration.</p>"""
    name: "capo_cleanrooms.types.collaboration_name.CollaborationName"
    """<p>A human-readable identifier provided by the collaboration owner. Display names are not unique.</p>"""
    description: NotRequired[
        "capo_cleanrooms.types.collaboration_description.CollaborationDescription"
    ]
    """<p>A description of the collaboration provided by the collaboration owner.</p>"""
    creator_account_id: "capo_cleanrooms.types.account_id.AccountId"
    """<p>The identifier used to reference members of the collaboration. Currently only supports Amazon Web Services account ID.</p>"""
    creator_display_name: "capo_cleanrooms.types.display_name.DisplayName"
    """<p>A display name of the collaboration creator.</p>"""
    create_time: "datetime.datetime"
    """<p>The time when the collaboration was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time the collaboration metadata was last updated.</p>"""
    member_status: "capo_cleanrooms.types.member_status.MemberStatus"
    """<p>The status of a member in a collaboration.</p>"""
    membership_id: NotRequired["capo_cleanrooms.types.uuid.UUID"]
    """<p>The unique ID for your membership within the collaboration.</p>"""
    membership_arn: NotRequired["capo_cleanrooms.types.membership_arn.MembershipArn"]
    """<p>The unique ARN for your membership within the collaboration.</p>"""
    data_encryption_metadata: NotRequired[
        "capo_cleanrooms.types.data_encryption_metadata.DataEncryptionMetadata"
    ]
    """<p>The settings for client-side encryption for cryptographic computing.</p>"""
    query_log_status: "capo_cleanrooms.types.collaboration_query_log_status.CollaborationQueryLogStatus"
    """<p>An indicator as to whether query logging has been enabled or disabled for the collaboration.</p> <p>When <code>ENABLED</code>, Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>"""
    job_log_status: NotRequired[
        "capo_cleanrooms.types.collaboration_job_log_status.CollaborationJobLogStatus"
    ]
    """<p>An indicator as to whether job logging has been enabled or disabled for the collaboration. </p> <p>When <code>ENABLED</code>, Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>"""
    analytics_engine: NotRequired[
        "capo_cleanrooms.types.analytics_engine.AnalyticsEngine"
    ]
    """<p> The analytics engine for the collaboration.</p> <note> <p>After July 16, 2025, the <code>CLEAN_ROOMS_SQL</code> parameter will no longer be available. </p> </note>"""
    auto_approved_change_types: NotRequired[
        "capo_cleanrooms.types.auto_approved_change_type_list.AutoApprovedChangeTypeList"
    ]
    """<p>The types of change requests that are automatically approved for this collaboration.</p>"""
    allowed_result_regions: NotRequired[
        "capo_cleanrooms.types.allowed_result_regions.AllowedResultRegions"
    ]
    """<p>The Amazon Web Services Regions where collaboration query results can be stored. Returns the list of Region identifiers that were specified when the collaboration was created. This list is used to enforce regional storage policies and compliance requirements.</p>"""
    is_metrics_enabled: NotRequired["bool"]
    """<p>An indicator as to whether metrics are enabled for the collaboration.</p> <p>When <code>true</code>, collaboration members can opt in to Amazon CloudWatch metrics for their membership queries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Collaboration) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["creatorAccountId"] = value["creator_account_id"]
    out["creatorDisplayName"] = value["creator_display_name"]
    import capo_cleanrooms.types._prelude.timestamp

    out["createTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanrooms.types._prelude.timestamp

    out["updateTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["memberStatus"] = value["member_status"]
    if "membership_id" in value:
        out["membershipId"] = value["membership_id"]
    if "membership_arn" in value:
        out["membershipArn"] = value["membership_arn"]
    if "data_encryption_metadata" in value:
        import capo_cleanrooms.types.data_encryption_metadata

        out["dataEncryptionMetadata"] = (
            capo_cleanrooms.types.data_encryption_metadata.serialize_json(
                value["data_encryption_metadata"]
            )
        )
    import capo_cleanrooms.types.collaboration_query_log_status

    out["queryLogStatus"] = (
        capo_cleanrooms.types.collaboration_query_log_status.serialize_json(
            value["query_log_status"]
        )
    )
    if "job_log_status" in value:
        import capo_cleanrooms.types.collaboration_job_log_status

        out["jobLogStatus"] = (
            capo_cleanrooms.types.collaboration_job_log_status.serialize_json(
                value["job_log_status"]
            )
        )
    if "analytics_engine" in value:
        import capo_cleanrooms.types.analytics_engine

        out["analyticsEngine"] = capo_cleanrooms.types.analytics_engine.serialize_json(
            value["analytics_engine"]
        )
    if "auto_approved_change_types" in value:
        import capo_cleanrooms.types.auto_approved_change_type_list

        out["autoApprovedChangeTypes"] = (
            capo_cleanrooms.types.auto_approved_change_type_list.serialize_json(
                value["auto_approved_change_types"]
            )
        )
    if "allowed_result_regions" in value:
        import capo_cleanrooms.types.allowed_result_regions

        out["allowedResultRegions"] = (
            capo_cleanrooms.types.allowed_result_regions.serialize_json(
                value["allowed_result_regions"]
            )
        )
    if "is_metrics_enabled" in value:
        out["isMetricsEnabled"] = value["is_metrics_enabled"]
    return out


def deserialize_json(data: dict) -> Collaboration:
    out: Collaboration = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("creatorAccountId") is not None:
        out["creator_account_id"] = data["creatorAccountId"]
    else:
        out["creator_account_id"] = ""
    if data.get("creatorDisplayName") is not None:
        out["creator_display_name"] = data["creatorDisplayName"]
    else:
        out["creator_display_name"] = ""
    if data.get("createTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["create_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["createTime"]
        )
    else:
        import datetime

        out["create_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("updateTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["update_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["updateTime"]
        )
    else:
        import datetime

        out["update_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("memberStatus") is not None:
        out["member_status"] = data["memberStatus"]
    else:
        out["member_status"] = ""
    if data.get("membershipId") is not None:
        out["membership_id"] = data["membershipId"]
    if data.get("membershipArn") is not None:
        out["membership_arn"] = data["membershipArn"]
    if data.get("dataEncryptionMetadata") is not None:
        import capo_cleanrooms.types.data_encryption_metadata

        out["data_encryption_metadata"] = (
            capo_cleanrooms.types.data_encryption_metadata.deserialize_json(
                data["dataEncryptionMetadata"]
            )
        )
    if data.get("queryLogStatus") is not None:
        import capo_cleanrooms.types.collaboration_query_log_status

        out["query_log_status"] = (
            capo_cleanrooms.types.collaboration_query_log_status.deserialize_json(
                data["queryLogStatus"]
            )
        )
    else:
        import typing

        out["query_log_status"] = typing.cast(
            "capo_cleanrooms.types.collaboration_query_log_status.CollaborationQueryLogStatus",
            "",
        )
    if data.get("jobLogStatus") is not None:
        import capo_cleanrooms.types.collaboration_job_log_status

        out["job_log_status"] = (
            capo_cleanrooms.types.collaboration_job_log_status.deserialize_json(
                data["jobLogStatus"]
            )
        )
    if data.get("analyticsEngine") is not None:
        import capo_cleanrooms.types.analytics_engine

        out["analytics_engine"] = (
            capo_cleanrooms.types.analytics_engine.deserialize_json(
                data["analyticsEngine"]
            )
        )
    if data.get("autoApprovedChangeTypes") is not None:
        import capo_cleanrooms.types.auto_approved_change_type_list

        out["auto_approved_change_types"] = (
            capo_cleanrooms.types.auto_approved_change_type_list.deserialize_json(
                data["autoApprovedChangeTypes"]
            )
        )
    if data.get("allowedResultRegions") is not None:
        import capo_cleanrooms.types.allowed_result_regions

        out["allowed_result_regions"] = (
            capo_cleanrooms.types.allowed_result_regions.deserialize_json(
                data["allowedResultRegions"]
            )
        )
    if data.get("isMetricsEnabled") is not None:
        out["is_metrics_enabled"] = data["isMetricsEnabled"]
    return out
