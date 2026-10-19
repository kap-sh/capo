"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationPrivacyBudgetTemplateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.account_id
    import capo_cleanrooms.types.collaboration_arn
    import capo_cleanrooms.types.privacy_budget_template_arn
    import capo_cleanrooms.types.privacy_budget_template_identifier
    import capo_cleanrooms.types.privacy_budget_type
    import capo_cleanrooms.types.uuid


class CollaborationPrivacyBudgetTemplateSummary(TypedDict, closed=True):
    id: "capo_cleanrooms.types.privacy_budget_template_identifier.PrivacyBudgetTemplateIdentifier"
    """<p>The unique identifier of the collaboration privacy budget template.</p>"""
    arn: "capo_cleanrooms.types.privacy_budget_template_arn.PrivacyBudgetTemplateArn"
    """<p>The ARN of the collaboration privacy budget template.</p>"""
    collaboration_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the collaboration that contains this collaboration privacy budget template.</p>"""
    collaboration_arn: "capo_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The ARN of the collaboration that contains this collaboration privacy budget template.</p>"""
    creator_account_id: "capo_cleanrooms.types.account_id.AccountId"
    """<p>The unique identifier of the account that created this collaboration privacy budget template.</p>"""
    privacy_budget_type: "capo_cleanrooms.types.privacy_budget_type.PrivacyBudgetType"
    """<p>The type of the privacy budget template.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which the collaboration privacy budget template was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the collaboration privacy budget template was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationPrivacyBudgetTemplateSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["collaborationId"] = value["collaboration_id"]
    out["collaborationArn"] = value["collaboration_arn"]
    out["creatorAccountId"] = value["creator_account_id"]
    import capo_cleanrooms.types.privacy_budget_type

    out["privacyBudgetType"] = capo_cleanrooms.types.privacy_budget_type.serialize_json(
        value["privacy_budget_type"]
    )
    import capo_cleanrooms.types._prelude.timestamp

    out["createTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanrooms.types._prelude.timestamp

    out["updateTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> CollaborationPrivacyBudgetTemplateSummary:
    out: CollaborationPrivacyBudgetTemplateSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
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
    if data.get("privacyBudgetType") is not None:
        import capo_cleanrooms.types.privacy_budget_type

        out["privacy_budget_type"] = (
            capo_cleanrooms.types.privacy_budget_type.deserialize_json(
                data["privacyBudgetType"]
            )
        )
    else:
        import typing

        out["privacy_budget_type"] = typing.cast(
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
    return out
