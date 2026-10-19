"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreateMembershipInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.collaboration_identifier
    import capo_cleanrooms.types.membership_job_log_status
    import capo_cleanrooms.types.membership_payment_configuration
    import capo_cleanrooms.types.membership_protected_job_result_configuration
    import capo_cleanrooms.types.membership_protected_query_result_configuration
    import capo_cleanrooms.types.membership_query_log_status
    import capo_cleanrooms.types.tag_map


class CreateMembershipInput(TypedDict, closed=True):
    collaboration_identifier: (
        "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>The unique ID for the associated collaboration.</p>"""
    query_log_status: (
        "capo_cleanrooms.types.membership_query_log_status.MembershipQueryLogStatus"
    )
    """<p>An indicator as to whether query logging has been enabled or disabled for the membership.</p> <p>When <code>ENABLED</code>, Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>"""
    job_log_status: NotRequired[
        "capo_cleanrooms.types.membership_job_log_status.MembershipJobLogStatus"
    ]
    """<p>An indicator as to whether job logging has been enabled or disabled for the collaboration. </p> <p>When <code>ENABLED</code>, Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>"""
    tags: NotRequired["capo_cleanrooms.types.tag_map.TagMap"]
    """<p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>"""
    default_result_configuration: NotRequired[
        "capo_cleanrooms.types.membership_protected_query_result_configuration.MembershipProtectedQueryResultConfiguration"
    ]
    """<p>The default protected query result configuration as specified by the member who can receive results.</p>"""
    default_job_result_configuration: NotRequired[
        "capo_cleanrooms.types.membership_protected_job_result_configuration.MembershipProtectedJobResultConfiguration"
    ]
    """<p>The default job result configuration that determines how job results are protected and managed within this membership. This configuration applies to all jobs.</p>"""
    payment_configuration: NotRequired[
        "capo_cleanrooms.types.membership_payment_configuration.MembershipPaymentConfiguration"
    ]
    """<p>The payment responsibilities accepted by the collaboration member.</p> <p>Not required if the collaboration member has the member ability to run queries. </p> <p>Required if the collaboration member doesn't have the member ability to run queries but is configured as a payer by the collaboration creator. </p>"""
    is_metrics_enabled: NotRequired["bool"]
    """<p>An indicator as to whether Amazon CloudWatch metrics have been enabled or disabled for the membership.</p> <p>Amazon CloudWatch metrics are only available when the collaboration has metrics enabled. This option can be set by collaboration members who have the ability to run queries (analysis runners) or by members who are configured as payers.</p> <p>When <code>true</code>, metrics about query execution are collected in Amazon CloudWatch. The default value is <code>false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMembershipInput) -> dict:
    out: dict = {}
    out["collaborationIdentifier"] = value["collaboration_identifier"]
    import capo_cleanrooms.types.membership_query_log_status

    out["queryLogStatus"] = (
        capo_cleanrooms.types.membership_query_log_status.serialize_json(
            value["query_log_status"]
        )
    )
    if "job_log_status" in value:
        import capo_cleanrooms.types.membership_job_log_status

        out["jobLogStatus"] = (
            capo_cleanrooms.types.membership_job_log_status.serialize_json(
                value["job_log_status"]
            )
        )
    if "tags" in value:
        import capo_cleanrooms.types.tag_map

        out["tags"] = capo_cleanrooms.types.tag_map.serialize_json(value["tags"])
    if "default_result_configuration" in value:
        import capo_cleanrooms.types.membership_protected_query_result_configuration

        out["defaultResultConfiguration"] = (
            capo_cleanrooms.types.membership_protected_query_result_configuration.serialize_json(
                value["default_result_configuration"]
            )
        )
    if "default_job_result_configuration" in value:
        import capo_cleanrooms.types.membership_protected_job_result_configuration

        out["defaultJobResultConfiguration"] = (
            capo_cleanrooms.types.membership_protected_job_result_configuration.serialize_json(
                value["default_job_result_configuration"]
            )
        )
    if "payment_configuration" in value:
        import capo_cleanrooms.types.membership_payment_configuration

        out["paymentConfiguration"] = (
            capo_cleanrooms.types.membership_payment_configuration.serialize_json(
                value["payment_configuration"]
            )
        )
    if "is_metrics_enabled" in value:
        out["isMetricsEnabled"] = value["is_metrics_enabled"]
    return out


def deserialize_json(data: dict) -> CreateMembershipInput:
    out: CreateMembershipInput = {}  # type: ignore[typeddict-item]
    if data.get("collaborationIdentifier") is not None:
        out["collaboration_identifier"] = data["collaborationIdentifier"]
    else:
        out["collaboration_identifier"] = ""
    if data.get("queryLogStatus") is not None:
        import capo_cleanrooms.types.membership_query_log_status

        out["query_log_status"] = (
            capo_cleanrooms.types.membership_query_log_status.deserialize_json(
                data["queryLogStatus"]
            )
        )
    else:
        import typing

        out["query_log_status"] = typing.cast(
            "capo_cleanrooms.types.membership_query_log_status.MembershipQueryLogStatus",
            "",
        )
    if data.get("jobLogStatus") is not None:
        import capo_cleanrooms.types.membership_job_log_status

        out["job_log_status"] = (
            capo_cleanrooms.types.membership_job_log_status.deserialize_json(
                data["jobLogStatus"]
            )
        )
    if data.get("tags") is not None:
        import capo_cleanrooms.types.tag_map

        out["tags"] = capo_cleanrooms.types.tag_map.deserialize_json(data["tags"])
    if data.get("defaultResultConfiguration") is not None:
        import capo_cleanrooms.types.membership_protected_query_result_configuration

        out["default_result_configuration"] = (
            capo_cleanrooms.types.membership_protected_query_result_configuration.deserialize_json(
                data["defaultResultConfiguration"]
            )
        )
    if data.get("defaultJobResultConfiguration") is not None:
        import capo_cleanrooms.types.membership_protected_job_result_configuration

        out["default_job_result_configuration"] = (
            capo_cleanrooms.types.membership_protected_job_result_configuration.deserialize_json(
                data["defaultJobResultConfiguration"]
            )
        )
    if data.get("paymentConfiguration") is not None:
        import capo_cleanrooms.types.membership_payment_configuration

        out["payment_configuration"] = (
            capo_cleanrooms.types.membership_payment_configuration.deserialize_json(
                data["paymentConfiguration"]
            )
        )
    if data.get("isMetricsEnabled") is not None:
        out["is_metrics_enabled"] = data["isMetricsEnabled"]
    return out
