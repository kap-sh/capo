"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PrivacyBudgetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.collaboration_arn
    import capo_cleanrooms.types.membership_arn
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.privacy_budget
    import capo_cleanrooms.types.privacy_budget_template_arn
    import capo_cleanrooms.types.privacy_budget_template_identifier
    import capo_cleanrooms.types.privacy_budget_type
    import capo_cleanrooms.types.uuid


class PrivacyBudgetSummary(TypedDict, closed=True):
    id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the privacy budget.</p>"""
    privacy_budget_template_id: "capo_cleanrooms.types.privacy_budget_template_identifier.PrivacyBudgetTemplateIdentifier"
    """<p>The unique identifier of the privacy budget template.</p>"""
    privacy_budget_template_arn: (
        "capo_cleanrooms.types.privacy_budget_template_arn.PrivacyBudgetTemplateArn"
    )
    """<p>The ARN of the privacy budget template.</p>"""
    membership_id: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    """<p>The identifier for a membership resource.</p>"""
    membership_arn: "capo_cleanrooms.types.membership_arn.MembershipArn"
    """<p>The Amazon Resource Name (ARN) of the member who created the privacy budget summary.</p>"""
    collaboration_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the collaboration that contains this privacy budget.</p>"""
    collaboration_arn: "capo_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The ARN of the collaboration that contains this privacy budget.</p>"""
    type: "capo_cleanrooms.types.privacy_budget_type.PrivacyBudgetType"
    """<p>Specifies the type of the privacy budget.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which the privacy budget was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the privacy budget was updated.</p>"""
    budget: "capo_cleanrooms.types.privacy_budget.PrivacyBudget"
    """<p>The provided privacy budget.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrivacyBudgetSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["privacyBudgetTemplateId"] = value["privacy_budget_template_id"]
    out["privacyBudgetTemplateArn"] = value["privacy_budget_template_arn"]
    out["membershipId"] = value["membership_id"]
    out["membershipArn"] = value["membership_arn"]
    out["collaborationId"] = value["collaboration_id"]
    out["collaborationArn"] = value["collaboration_arn"]
    import capo_cleanrooms.types.privacy_budget_type

    out["type"] = capo_cleanrooms.types.privacy_budget_type.serialize_json(
        value["type"]
    )
    import capo_cleanrooms.types._prelude.timestamp

    out["createTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanrooms.types._prelude.timestamp

    out["updateTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    import capo_cleanrooms.types.privacy_budget

    out["budget"] = capo_cleanrooms.types.privacy_budget.serialize_json(value["budget"])
    return out


def deserialize_json(data: dict) -> PrivacyBudgetSummary:
    out: PrivacyBudgetSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("privacyBudgetTemplateId") is not None:
        out["privacy_budget_template_id"] = data["privacyBudgetTemplateId"]
    else:
        out["privacy_budget_template_id"] = ""
    if data.get("privacyBudgetTemplateArn") is not None:
        out["privacy_budget_template_arn"] = data["privacyBudgetTemplateArn"]
    else:
        out["privacy_budget_template_arn"] = ""
    if data.get("membershipId") is not None:
        out["membership_id"] = data["membershipId"]
    else:
        out["membership_id"] = ""
    if data.get("membershipArn") is not None:
        out["membership_arn"] = data["membershipArn"]
    else:
        out["membership_arn"] = ""
    if data.get("collaborationId") is not None:
        out["collaboration_id"] = data["collaborationId"]
    else:
        out["collaboration_id"] = ""
    if data.get("collaborationArn") is not None:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        out["collaboration_arn"] = ""
    if data.get("type") is not None:
        import capo_cleanrooms.types.privacy_budget_type

        out["type"] = capo_cleanrooms.types.privacy_budget_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_cleanrooms.types.privacy_budget_type.PrivacyBudgetType", ""
        )
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
    if data.get("budget") is not None:
        import capo_cleanrooms.types.privacy_budget

        out["budget"] = capo_cleanrooms.types.privacy_budget.deserialize_json(
            data["budget"]
        )
    else:
        out["budget"] = {"$unknown": {"name": ""}}
    return out
