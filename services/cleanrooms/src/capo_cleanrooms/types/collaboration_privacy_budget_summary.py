"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationPrivacyBudgetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.account_id
    import capo_cleanrooms.types.collaboration_arn
    import capo_cleanrooms.types.privacy_budget
    import capo_cleanrooms.types.privacy_budget_template_arn
    import capo_cleanrooms.types.privacy_budget_template_identifier
    import capo_cleanrooms.types.privacy_budget_type
    import capo_cleanrooms.types.uuid


class CollaborationPrivacyBudgetSummary(TypedDict, closed=True):
    id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the collaboration privacy budget.</p>"""
    privacy_budget_template_id: "capo_cleanrooms.types.privacy_budget_template_identifier.PrivacyBudgetTemplateIdentifier"
    """<p>The unique identifier of the collaboration privacy budget template.</p>"""
    privacy_budget_template_arn: (
        "capo_cleanrooms.types.privacy_budget_template_arn.PrivacyBudgetTemplateArn"
    )
    """<p>The ARN of the collaboration privacy budget template.</p>"""
    collaboration_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the collaboration that includes this privacy budget.</p>"""
    collaboration_arn: "capo_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The ARN of the collaboration that includes this privacy budget.</p>"""
    creator_account_id: "capo_cleanrooms.types.account_id.AccountId"
    """<p>The unique identifier of the account that created this privacy budget.</p>"""
    type: "capo_cleanrooms.types.privacy_budget_type.PrivacyBudgetType"
    """<p>The type of privacy budget template.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which the privacy budget was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the privacy budget was updated.</p>"""
    budget: "capo_cleanrooms.types.privacy_budget.PrivacyBudget"
    """<p>The includes epsilon provided and utility in terms of aggregations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationPrivacyBudgetSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["privacyBudgetTemplateId"] = value["privacy_budget_template_id"]
    out["privacyBudgetTemplateArn"] = value["privacy_budget_template_arn"]
    out["collaborationId"] = value["collaboration_id"]
    out["collaborationArn"] = value["collaboration_arn"]
    out["creatorAccountId"] = value["creator_account_id"]
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


def deserialize_json(data: dict) -> CollaborationPrivacyBudgetSummary:
    out: CollaborationPrivacyBudgetSummary = {}  # type: ignore[typeddict-item]
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
    if data.get("collaborationId") is not None:
        out["collaboration_id"] = data["collaborationId"]
    else:
        out["collaboration_id"] = ""
    if data.get("collaborationArn") is not None:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        out["collaboration_arn"] = ""
    if data.get("creatorAccountId") is not None:
        out["creator_account_id"] = data["creatorAccountId"]
    else:
        out["creator_account_id"] = ""
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
        import capo_cleanrooms.types._unknown

        out["budget"] = capo_cleanrooms.types._unknown.UnknownUnionMember("")
    return out
