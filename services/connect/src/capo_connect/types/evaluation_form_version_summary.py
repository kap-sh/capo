"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.evaluation_form_version_is_locked
    import capo_connect.types.evaluation_form_version_status
    import capo_connect.types.resource_id
    import capo_connect.types.timestamp
    import capo_connect.types.version_number


class EvaluationFormVersionSummary(TypedDict, closed=True):
    evaluation_form_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) for the evaluation form resource.</p>"""
    evaluation_form_id: "capo_connect.types.resource_id.ResourceId"
    """<p>The unique identifier for the evaluation form.</p>"""
    evaluation_form_version: "capo_connect.types.version_number.VersionNumber"
    """<p>A version of the evaluation form.</p>"""
    locked: "capo_connect.types.evaluation_form_version_is_locked.EvaluationFormVersionIsLocked"
    """<p>The flag indicating whether the evaluation form is locked for changes.</p>"""
    status: (
        "capo_connect.types.evaluation_form_version_status.EvaluationFormVersionStatus"
    )
    """<p>The status of the evaluation form.</p>"""
    created_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp for when the evaluation form was created.</p>"""
    created_by: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the user who created the evaluation form.</p>"""
    last_modified_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp for when the evaluation form was last updated.</p>"""
    last_modified_by: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the user who last updated the evaluation form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormVersionSummary) -> dict:
    out: dict = {}
    out["EvaluationFormArn"] = value["evaluation_form_arn"]
    out["EvaluationFormId"] = value["evaluation_form_id"]
    out["EvaluationFormVersion"] = value.get("evaluation_form_version", 0)
    out["Locked"] = value.get("locked", False)
    import capo_connect.types.evaluation_form_version_status

    out["Status"] = capo_connect.types.evaluation_form_version_status.serialize_json(
        value["status"]
    )
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
    return out


def deserialize_json(data: dict) -> EvaluationFormVersionSummary:
    out: EvaluationFormVersionSummary = {}  # type: ignore[typeddict-item]
    if data.get("EvaluationFormArn") is not None:
        out["evaluation_form_arn"] = data["EvaluationFormArn"]
    else:
        out["evaluation_form_arn"] = ""
    if data.get("EvaluationFormId") is not None:
        out["evaluation_form_id"] = data["EvaluationFormId"]
    else:
        out["evaluation_form_id"] = ""
    if data.get("EvaluationFormVersion") is not None:
        out["evaluation_form_version"] = data["EvaluationFormVersion"]
    else:
        out["evaluation_form_version"] = 0
    if data.get("Locked") is not None:
        out["locked"] = data["Locked"]
    else:
        out["locked"] = False
    if data.get("Status") is not None:
        import capo_connect.types.evaluation_form_version_status

        out["status"] = (
            capo_connect.types.evaluation_form_version_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_connect.types.evaluation_form_version_status.EvaluationFormVersionStatus",
            "",
        )
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
    return out
