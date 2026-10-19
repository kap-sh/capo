"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.association_status_name
    import capo_ssm.types.date_time
    import capo_ssm.types.status_additional_info
    import capo_ssm.types.status_message


class AssociationStatus(TypedDict, closed=True):
    date: "capo_ssm.types.date_time.DateTime"
    """<p>The date when the status changed.</p>"""
    name: "capo_ssm.types.association_status_name.AssociationStatusName"
    """<p>The status.</p>"""
    message: "capo_ssm.types.status_message.StatusMessage"
    """<p>The reason for the status.</p>"""
    additional_info: NotRequired[
        "capo_ssm.types.status_additional_info.StatusAdditionalInfo"
    ]
    """<p>A user-defined string.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationStatus) -> dict:
    out: dict = {}
    import capo_ssm.types.date_time

    out["Date"] = capo_ssm.types.date_time.serialize_aws_json_1_1(value["date"])
    import capo_ssm.types.association_status_name

    out["Name"] = capo_ssm.types.association_status_name.serialize_aws_json_1_1(
        value["name"]
    )
    out["Message"] = value["message"]
    if "additional_info" in value:
        out["AdditionalInfo"] = value["additional_info"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociationStatus:
    out: AssociationStatus = {}  # type: ignore[typeddict-item]
    if data.get("Date") is not None:
        import capo_ssm.types.date_time

        out["date"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(data["Date"])
    else:
        import datetime

        out["date"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("Name") is not None:
        import capo_ssm.types.association_status_name

        out["name"] = capo_ssm.types.association_status_name.deserialize_aws_json_1_1(
            data["Name"]
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_ssm.types.association_status_name.AssociationStatusName", ""
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("AdditionalInfo") is not None:
        out["additional_info"] = data["AdditionalInfo"]
    return out
