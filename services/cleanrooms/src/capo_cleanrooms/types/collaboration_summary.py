"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.account_id
    import capo_cleanrooms.types.analytics_engine
    import capo_cleanrooms.types.collaboration_arn
    import capo_cleanrooms.types.collaboration_name
    import capo_cleanrooms.types.display_name
    import capo_cleanrooms.types.member_status
    import capo_cleanrooms.types.membership_arn
    import capo_cleanrooms.types.uuid


class CollaborationSummary(TypedDict, closed=True):
    id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The identifier for the collaboration.</p>"""
    arn: "capo_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The ARN of the collaboration.</p>"""
    name: "capo_cleanrooms.types.collaboration_name.CollaborationName"
    """<p>A human-readable identifier provided by the collaboration owner. Display names are not unique.</p>"""
    creator_account_id: "capo_cleanrooms.types.account_id.AccountId"
    """<p>The identifier used to reference members of the collaboration. Currently only supports Amazon Web Services account ID.</p>"""
    creator_display_name: "capo_cleanrooms.types.display_name.DisplayName"
    """<p>The display name of the collaboration creator.</p>"""
    create_time: "datetime.datetime"
    """<p>The time when the collaboration was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time the collaboration metadata was last updated.</p>"""
    member_status: "capo_cleanrooms.types.member_status.MemberStatus"
    """<p>The status of a member in a collaboration.</p>"""
    membership_id: NotRequired["capo_cleanrooms.types.uuid.UUID"]
    """<p>The identifier of a member in a collaboration.</p>"""
    membership_arn: NotRequired["capo_cleanrooms.types.membership_arn.MembershipArn"]
    """<p>The ARN of a member in a collaboration.</p>"""
    analytics_engine: NotRequired[
        "capo_cleanrooms.types.analytics_engine.AnalyticsEngine"
    ]
    """<p> The analytics engine.</p> <note> <p>After July 16, 2025, the <code>CLEAN_ROOMS_SQL</code> parameter will no longer be available. </p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
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
    if "analytics_engine" in value:
        import capo_cleanrooms.types.analytics_engine

        out["analyticsEngine"] = capo_cleanrooms.types.analytics_engine.serialize_json(
            value["analytics_engine"]
        )
    return out


def deserialize_json(data: dict) -> CollaborationSummary:
    out: CollaborationSummary = {}  # type: ignore[typeddict-item]
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
    if data.get("analyticsEngine") is not None:
        import capo_cleanrooms.types.analytics_engine

        out["analytics_engine"] = (
            capo_cleanrooms.types.analytics_engine.deserialize_json(
                data["analyticsEngine"]
            )
        )
    return out
