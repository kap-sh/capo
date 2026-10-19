"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreateCollaborationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.allowed_result_regions
    import capo_cleanrooms.types.analytics_engine
    import capo_cleanrooms.types.auto_approved_change_type_list
    import capo_cleanrooms.types.collaboration_description
    import capo_cleanrooms.types.collaboration_job_log_status
    import capo_cleanrooms.types.collaboration_name
    import capo_cleanrooms.types.collaboration_query_log_status
    import capo_cleanrooms.types.data_encryption_metadata
    import capo_cleanrooms.types.display_name
    import capo_cleanrooms.types.member_abilities
    import capo_cleanrooms.types.member_list
    import capo_cleanrooms.types.ml_member_abilities
    import capo_cleanrooms.types.payment_configuration
    import capo_cleanrooms.types.tag_map


class CreateCollaborationInput(TypedDict, closed=True):
    members: "capo_cleanrooms.types.member_list.MemberList"
    """<p>A list of initial members, not including the creator. This list is immutable.</p>"""
    name: "capo_cleanrooms.types.collaboration_name.CollaborationName"
    """<p>The display name for a collaboration.</p>"""
    description: (
        "capo_cleanrooms.types.collaboration_description.CollaborationDescription"
    )
    """<p>A description of the collaboration provided by the collaboration owner.</p>"""
    creator_member_abilities: "capo_cleanrooms.types.member_abilities.MemberAbilities"
    """<p>The abilities granted to the collaboration creator.</p>"""
    creator_ml_member_abilities: NotRequired[
        "capo_cleanrooms.types.ml_member_abilities.MLMemberAbilities"
    ]
    """<p>The ML abilities granted to the collaboration creator.</p>"""
    creator_display_name: "capo_cleanrooms.types.display_name.DisplayName"
    """<p>The display name of the collaboration creator.</p>"""
    data_encryption_metadata: NotRequired[
        "capo_cleanrooms.types.data_encryption_metadata.DataEncryptionMetadata"
    ]
    """<p>The settings for client-side encryption with Cryptographic Computing for Clean Rooms.</p>"""
    query_log_status: "capo_cleanrooms.types.collaboration_query_log_status.CollaborationQueryLogStatus"
    """<p>An indicator as to whether query logging has been enabled or disabled for the collaboration.</p> <p>When <code>ENABLED</code>, Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>"""
    job_log_status: NotRequired[
        "capo_cleanrooms.types.collaboration_job_log_status.CollaborationJobLogStatus"
    ]
    """<p>Specifies whether job logs are enabled for this collaboration. </p> <p>When <code>ENABLED</code>, Clean Rooms logs details about jobs run within this collaboration; those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>"""
    tags: NotRequired["capo_cleanrooms.types.tag_map.TagMap"]
    """<p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>"""
    creator_payment_configuration: NotRequired[
        "capo_cleanrooms.types.payment_configuration.PaymentConfiguration"
    ]
    """<p>The collaboration creator's payment responsibilities set by the collaboration creator. </p> <p>If the collaboration creator hasn't specified anyone as the member paying for query compute costs, then the member who can query is the default payer.</p>"""
    analytics_engine: NotRequired[
        "capo_cleanrooms.types.analytics_engine.AnalyticsEngine"
    ]
    """<p> The analytics engine.</p> <note> <p>After July 16, 2025, the <code>CLEAN_ROOMS_SQL</code> parameter will no longer be available. </p> </note>"""
    auto_approved_change_request_types: NotRequired[
        "capo_cleanrooms.types.auto_approved_change_type_list.AutoApprovedChangeTypeList"
    ]
    """<p>The types of change requests that are automatically approved for this collaboration.</p>"""
    allowed_result_regions: NotRequired[
        "capo_cleanrooms.types.allowed_result_regions.AllowedResultRegions"
    ]
    """<p>The Amazon Web Services Regions where collaboration query results can be stored. When specified, results can only be written to these Regions. This parameter enables you to meet your compliance and data governance requirements, and implement regional data governance policies.</p>"""
    is_metrics_enabled: NotRequired["bool"]
    """<p>An indicator as to whether metrics have been enabled or disabled for the collaboration.</p> <p>When <code>true</code>, collaboration members can opt in to Amazon CloudWatch metrics for their membership queries. The default value is <code>false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCollaborationInput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.member_list

    out["members"] = capo_cleanrooms.types.member_list.serialize_json(value["members"])
    out["name"] = value["name"]
    out["description"] = value.get("description", "")
    import capo_cleanrooms.types.member_abilities

    out["creatorMemberAbilities"] = (
        capo_cleanrooms.types.member_abilities.serialize_json(
            value["creator_member_abilities"]
        )
    )
    if "creator_ml_member_abilities" in value:
        import capo_cleanrooms.types.ml_member_abilities

        out["creatorMLMemberAbilities"] = (
            capo_cleanrooms.types.ml_member_abilities.serialize_json(
                value["creator_ml_member_abilities"]
            )
        )
    out["creatorDisplayName"] = value["creator_display_name"]
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
    if "tags" in value:
        import capo_cleanrooms.types.tag_map

        out["tags"] = capo_cleanrooms.types.tag_map.serialize_json(value["tags"])
    if "creator_payment_configuration" in value:
        import capo_cleanrooms.types.payment_configuration

        out["creatorPaymentConfiguration"] = (
            capo_cleanrooms.types.payment_configuration.serialize_json(
                value["creator_payment_configuration"]
            )
        )
    if "analytics_engine" in value:
        import capo_cleanrooms.types.analytics_engine

        out["analyticsEngine"] = capo_cleanrooms.types.analytics_engine.serialize_json(
            value["analytics_engine"]
        )
    if "auto_approved_change_request_types" in value:
        import capo_cleanrooms.types.auto_approved_change_type_list

        out["autoApprovedChangeRequestTypes"] = (
            capo_cleanrooms.types.auto_approved_change_type_list.serialize_json(
                value["auto_approved_change_request_types"]
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


def deserialize_json(data: dict) -> CreateCollaborationInput:
    out: CreateCollaborationInput = {}  # type: ignore[typeddict-item]
    if data.get("members") is not None:
        import capo_cleanrooms.types.member_list

        out["members"] = capo_cleanrooms.types.member_list.deserialize_json(
            data["members"]
        )
    else:
        out["members"] = []
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("creatorMemberAbilities") is not None:
        import capo_cleanrooms.types.member_abilities

        out["creator_member_abilities"] = (
            capo_cleanrooms.types.member_abilities.deserialize_json(
                data["creatorMemberAbilities"]
            )
        )
    else:
        out["creator_member_abilities"] = []
    if data.get("creatorMLMemberAbilities") is not None:
        import capo_cleanrooms.types.ml_member_abilities

        out["creator_ml_member_abilities"] = (
            capo_cleanrooms.types.ml_member_abilities.deserialize_json(
                data["creatorMLMemberAbilities"]
            )
        )
    if data.get("creatorDisplayName") is not None:
        out["creator_display_name"] = data["creatorDisplayName"]
    else:
        out["creator_display_name"] = ""
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
    if data.get("tags") is not None:
        import capo_cleanrooms.types.tag_map

        out["tags"] = capo_cleanrooms.types.tag_map.deserialize_json(data["tags"])
    if data.get("creatorPaymentConfiguration") is not None:
        import capo_cleanrooms.types.payment_configuration

        out["creator_payment_configuration"] = (
            capo_cleanrooms.types.payment_configuration.deserialize_json(
                data["creatorPaymentConfiguration"]
            )
        )
    if data.get("analyticsEngine") is not None:
        import capo_cleanrooms.types.analytics_engine

        out["analytics_engine"] = (
            capo_cleanrooms.types.analytics_engine.deserialize_json(
                data["analyticsEngine"]
            )
        )
    if data.get("autoApprovedChangeRequestTypes") is not None:
        import capo_cleanrooms.types.auto_approved_change_type_list

        out["auto_approved_change_request_types"] = (
            capo_cleanrooms.types.auto_approved_change_type_list.deserialize_json(
                data["autoApprovedChangeRequestTypes"]
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
