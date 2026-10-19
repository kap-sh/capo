"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.evaluation_form_title
    import capo_connect.types.resource_id
    import capo_connect.types.timestamp
    import capo_connect.types.version_number


class EvaluationFormSummary(TypedDict, closed=True):
    evaluation_form_id: "capo_connect.types.resource_id.ResourceId"
    """<p>The unique identifier for the evaluation form.</p>"""
    evaluation_form_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) for the evaluation form resource.</p>"""
    title: "capo_connect.types.evaluation_form_title.EvaluationFormTitle"
    """<p>A title of the evaluation form.</p>"""
    created_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp for when the evaluation form was created.</p>"""
    created_by: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the user who created the evaluation form.</p>"""
    last_modified_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp for when the evaluation form was last updated.</p>"""
    last_modified_by: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the user who last updated the evaluation form.</p>"""
    last_activated_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp for when the evaluation form was last activated.</p>"""
    last_activated_by: NotRequired["capo_connect.types.arn.ARN"]
    """<p> The Amazon Resource Name (ARN) of the user who last activated the evaluation form.</p>"""
    latest_version: "capo_connect.types.version_number.VersionNumber"
    """<p>The version number of the latest evaluation form version.</p>"""
    active_version: NotRequired["capo_connect.types.version_number.VersionNumber"]
    """<p>The version of the active evaluation form version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormSummary) -> dict:
    out: dict = {}
    out["EvaluationFormId"] = value["evaluation_form_id"]
    out["EvaluationFormArn"] = value["evaluation_form_arn"]
    out["Title"] = value["title"]
    import capo_connect.types.timestamp

    out["CreatedTime"] = capo_connect.types.timestamp.serialize_json(
        value["created_time"]
    )
    out["CreatedBy"] = value["created_by"]
    import capo_connect.types.timestamp

    out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
        value["last_modified_time"]
    )
    out["LastModifiedBy"] = value["last_modified_by"]
    if "last_activated_time" in value:
        import capo_connect.types.timestamp

        out["LastActivatedTime"] = capo_connect.types.timestamp.serialize_json(
            value["last_activated_time"]
        )
    if "last_activated_by" in value:
        out["LastActivatedBy"] = value["last_activated_by"]
    out["LatestVersion"] = value.get("latest_version", 0)
    if "active_version" in value:
        out["ActiveVersion"] = value["active_version"]
    return out


def deserialize_json(data: dict) -> EvaluationFormSummary:
    out: EvaluationFormSummary = {}  # type: ignore[typeddict-item]
    if data.get("EvaluationFormId") is not None:
        out["evaluation_form_id"] = data["EvaluationFormId"]
    else:
        out["evaluation_form_id"] = ""
    if data.get("EvaluationFormArn") is not None:
        out["evaluation_form_arn"] = data["EvaluationFormArn"]
    else:
        out["evaluation_form_arn"] = ""
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    else:
        out["title"] = ""
    if data.get("CreatedTime") is not None:
        import capo_connect.types.timestamp

        out["created_time"] = capo_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        import datetime

        out["created_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("CreatedBy") is not None:
        out["created_by"] = data["CreatedBy"]
    else:
        out["created_by"] = ""
    if data.get("LastModifiedTime") is not None:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    else:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("LastModifiedBy") is not None:
        out["last_modified_by"] = data["LastModifiedBy"]
    else:
        out["last_modified_by"] = ""
    if data.get("LastActivatedTime") is not None:
        import capo_connect.types.timestamp

        out["last_activated_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastActivatedTime"]
        )
    if data.get("LastActivatedBy") is not None:
        out["last_activated_by"] = data["LastActivatedBy"]
    if data.get("LatestVersion") is not None:
        out["latest_version"] = data["LatestVersion"]
    else:
        out["latest_version"] = 0
    if data.get("ActiveVersion") is not None:
        out["active_version"] = data["ActiveVersion"]
    return out
