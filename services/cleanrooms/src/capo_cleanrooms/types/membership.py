"""Generated from Smithy shape ``com.amazonaws.cleanrooms#Membership``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.account_id
    import capo_cleanrooms.types.collaboration_arn
    import capo_cleanrooms.types.collaboration_name
    import capo_cleanrooms.types.display_name
    import capo_cleanrooms.types.member_abilities
    import capo_cleanrooms.types.membership_arn
    import capo_cleanrooms.types.membership_job_log_status
    import capo_cleanrooms.types.membership_payment_configuration
    import capo_cleanrooms.types.membership_protected_job_result_configuration
    import capo_cleanrooms.types.membership_protected_query_result_configuration
    import capo_cleanrooms.types.membership_query_log_status
    import capo_cleanrooms.types.membership_status
    import capo_cleanrooms.types.ml_member_abilities
    import capo_cleanrooms.types.uuid


class Membership(TypedDict, closed=True):
    id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique ID of the membership.</p>"""
    arn: "capo_cleanrooms.types.membership_arn.MembershipArn"
    """<p>The unique ARN for the membership.</p>"""
    collaboration_arn: "capo_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The unique ARN for the membership's associated collaboration.</p>"""
    collaboration_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique ID for the membership's collaboration.</p>"""
    collaboration_creator_account_id: "capo_cleanrooms.types.account_id.AccountId"
    """<p>The identifier used to reference members of the collaboration. Currently only supports Amazon Web Services account ID.</p>"""
    collaboration_creator_display_name: "capo_cleanrooms.types.display_name.DisplayName"
    """<p>The display name of the collaboration creator.</p>"""
    collaboration_name: "capo_cleanrooms.types.collaboration_name.CollaborationName"
    """<p>The name of the membership's collaboration.</p>"""
    create_time: "datetime.datetime"
    """<p>The time when the membership was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time the membership metadata was last updated.</p>"""
    status: "capo_cleanrooms.types.membership_status.MembershipStatus"
    """<p>The status of the membership.</p>"""
    member_abilities: "capo_cleanrooms.types.member_abilities.MemberAbilities"
    """<p>The abilities granted to the collaboration member.</p>"""
    ml_member_abilities: NotRequired[
        "capo_cleanrooms.types.ml_member_abilities.MLMemberAbilities"
    ]
    """<p>Specifies the ML member abilities that are granted to a collaboration member.</p>"""
    query_log_status: (
        "capo_cleanrooms.types.membership_query_log_status.MembershipQueryLogStatus"
    )
    """<p>An indicator as to whether query logging has been enabled or disabled for the membership.</p> <p>When <code>ENABLED</code>, Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>"""
    job_log_status: NotRequired[
        "capo_cleanrooms.types.membership_job_log_status.MembershipJobLogStatus"
    ]
    """<p>An indicator as to whether job logging has been enabled or disabled for the collaboration. </p> <p>When <code>ENABLED</code>, Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>"""
    default_result_configuration: NotRequired[
        "capo_cleanrooms.types.membership_protected_query_result_configuration.MembershipProtectedQueryResultConfiguration"
    ]
    """<p>The default protected query result configuration as specified by the member who can receive results.</p>"""
    default_job_result_configuration: NotRequired[
        "capo_cleanrooms.types.membership_protected_job_result_configuration.MembershipProtectedJobResultConfiguration"
    ]
    """<p> The default job result configuration for the membership.</p>"""
    payment_configuration: "capo_cleanrooms.types.membership_payment_configuration.MembershipPaymentConfiguration"
    """<p>The payment responsibilities accepted by the collaboration member.</p>"""
    is_metrics_enabled: NotRequired["bool"]
    """<p>An indicator as to whether Amazon CloudWatch metrics are enabled for the membership.</p> <p>When <code>true</code>, metrics about query execution are collected in Amazon CloudWatch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Membership) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["collaborationArn"] = value["collaboration_arn"]
    out["collaborationId"] = value["collaboration_id"]
    out["collaborationCreatorAccountId"] = value["collaboration_creator_account_id"]
    out["collaborationCreatorDisplayName"] = value["collaboration_creator_display_name"]
    out["collaborationName"] = value["collaboration_name"]
    import capo_cleanrooms.types._prelude.timestamp

    out["createTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanrooms.types._prelude.timestamp

    out["updateTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["status"] = value["status"]
    import capo_cleanrooms.types.member_abilities

    out["memberAbilities"] = capo_cleanrooms.types.member_abilities.serialize_json(
        value["member_abilities"]
    )
    if "ml_member_abilities" in value:
        import capo_cleanrooms.types.ml_member_abilities

        out["mlMemberAbilities"] = (
            capo_cleanrooms.types.ml_member_abilities.serialize_json(
                value["ml_member_abilities"]
            )
        )
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
    import capo_cleanrooms.types.membership_payment_configuration

    out["paymentConfiguration"] = (
        capo_cleanrooms.types.membership_payment_configuration.serialize_json(
            value["payment_configuration"]
        )
    )
    if "is_metrics_enabled" in value:
        out["isMetricsEnabled"] = value["is_metrics_enabled"]
    return out


def deserialize_json(data: dict) -> Membership:
    out: Membership = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("collaborationArn") is not None:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        out["collaboration_arn"] = ""
    if data.get("collaborationId") is not None:
        out["collaboration_id"] = data["collaborationId"]
    else:
        out["collaboration_id"] = ""
    if data.get("collaborationCreatorAccountId") is not None:
        out["collaboration_creator_account_id"] = data["collaborationCreatorAccountId"]
    else:
        out["collaboration_creator_account_id"] = ""
    if data.get("collaborationCreatorDisplayName") is not None:
        out["collaboration_creator_display_name"] = data[
            "collaborationCreatorDisplayName"
        ]
    else:
        out["collaboration_creator_display_name"] = ""
    if data.get("collaborationName") is not None:
        out["collaboration_name"] = data["collaborationName"]
    else:
        out["collaboration_name"] = ""
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
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("memberAbilities") is not None:
        import capo_cleanrooms.types.member_abilities

        out["member_abilities"] = (
            capo_cleanrooms.types.member_abilities.deserialize_json(
                data["memberAbilities"]
            )
        )
    else:
        out["member_abilities"] = []
    if data.get("mlMemberAbilities") is not None:
        import capo_cleanrooms.types.ml_member_abilities

        out["ml_member_abilities"] = (
            capo_cleanrooms.types.ml_member_abilities.deserialize_json(
                data["mlMemberAbilities"]
            )
        )
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
    else:
        raise DeserializationError("Membership.payment_configuration required")
    if data.get("isMetricsEnabled") is not None:
        out["is_metrics_enabled"] = data["isMetricsEnabled"]
    return out
