"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisTemplateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.analysis_template_arn
    import capo_cleanrooms.types.analysis_template_identifier
    import capo_cleanrooms.types.collaboration_arn
    import capo_cleanrooms.types.membership_arn
    import capo_cleanrooms.types.resource_alias
    import capo_cleanrooms.types.resource_description
    import capo_cleanrooms.types.uuid


class AnalysisTemplateSummary(TypedDict, closed=True):
    arn: "capo_cleanrooms.types.analysis_template_arn.AnalysisTemplateArn"
    """<p>The Amazon Resource Name (ARN) of the analysis template.</p>"""
    create_time: "datetime.datetime"
    """<p>The time that the analysis template summary was created.</p>"""
    id: "capo_cleanrooms.types.analysis_template_identifier.AnalysisTemplateIdentifier"
    """<p>The identifier of the analysis template.</p>"""
    name: "capo_cleanrooms.types.resource_alias.ResourceAlias"
    """<p>The name of the analysis template. </p>"""
    update_time: "datetime.datetime"
    """<p>The time that the analysis template summary was last updated.</p>"""
    membership_arn: "capo_cleanrooms.types.membership_arn.MembershipArn"
    """<p>The Amazon Resource Name (ARN) of the member who created the analysis template.</p>"""
    membership_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The identifier for a membership resource.</p>"""
    collaboration_arn: "capo_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The unique ARN for the analysis template summary’s associated collaboration.</p>"""
    collaboration_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>A unique identifier for the collaboration that the analysis template summary belongs to. Currently accepts collaboration ID.</p>"""
    description: NotRequired[
        "capo_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the analysis template.</p>"""
    is_synthetic_data: NotRequired["bool"]
    """<p>Indicates if this analysis template summary generated synthetic data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisTemplateSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import capo_cleanrooms.types._prelude.timestamp

    out["createTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    out["id"] = value["id"]
    out["name"] = value["name"]
    import capo_cleanrooms.types._prelude.timestamp

    out["updateTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["membershipArn"] = value["membership_arn"]
    out["membershipId"] = value["membership_id"]
    out["collaborationArn"] = value["collaboration_arn"]
    out["collaborationId"] = value["collaboration_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "is_synthetic_data" in value:
        out["isSyntheticData"] = value["is_synthetic_data"]
    return out


def deserialize_json(data: dict) -> AnalysisTemplateSummary:
    out: AnalysisTemplateSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
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
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
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
    if data.get("membershipArn") is not None:
        out["membership_arn"] = data["membershipArn"]
    else:
        out["membership_arn"] = ""
    if data.get("membershipId") is not None:
        out["membership_id"] = data["membershipId"]
    else:
        out["membership_id"] = ""
    if data.get("collaborationArn") is not None:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        out["collaboration_arn"] = ""
    if data.get("collaborationId") is not None:
        out["collaboration_id"] = data["collaborationId"]
    else:
        out["collaboration_id"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("isSyntheticData") is not None:
        out["is_synthetic_data"] = data["isSyntheticData"]
    return out
