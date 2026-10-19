"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#CreateLabelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.comments
    import capo_lookoutequipment.types.equipment
    import capo_lookoutequipment.types.fault_code
    import capo_lookoutequipment.types.idempotence_token
    import capo_lookoutequipment.types.label_group_name
    import capo_lookoutequipment.types.label_rating
    import capo_lookoutequipment.types.timestamp


class CreateLabelRequest(TypedDict, closed=True):
    label_group_name: "capo_lookoutequipment.types.label_group_name.LabelGroupName"
    """<p> The name of a group of labels. </p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data. </p>"""
    start_time: "capo_lookoutequipment.types.timestamp.Timestamp"
    """<p> The start time of the labeled event. </p>"""
    end_time: "capo_lookoutequipment.types.timestamp.Timestamp"
    """<p> The end time of the labeled event. </p>"""
    rating: "capo_lookoutequipment.types.label_rating.LabelRating"
    """<p> Indicates whether a labeled event represents an anomaly. </p>"""
    fault_code: NotRequired["capo_lookoutequipment.types.fault_code.FaultCode"]
    """<p> Provides additional information about the label. The fault code must be defined in the FaultCodes attribute of the label group.</p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data. </p>"""
    notes: NotRequired["capo_lookoutequipment.types.comments.Comments"]
    """<p> Metadata providing additional information about the label. </p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data.</p>"""
    equipment: NotRequired["capo_lookoutequipment.types.equipment.Equipment"]
    """<p> Indicates that a label pertains to a particular piece of equipment. </p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data.</p>"""
    client_token: "capo_lookoutequipment.types.idempotence_token.IdempotenceToken"
    """<p> A unique identifier for the request to create a label. If you do not set the client request token, Lookout for Equipment generates one. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateLabelRequest) -> dict:
    out: dict = {}
    out["LabelGroupName"] = value["label_group_name"]
    import capo_lookoutequipment.types.timestamp

    out["StartTime"] = capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
        value["start_time"]
    )
    import capo_lookoutequipment.types.timestamp

    out["EndTime"] = capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
        value["end_time"]
    )
    import capo_lookoutequipment.types.label_rating

    out["Rating"] = capo_lookoutequipment.types.label_rating.serialize_aws_json_1_0(
        value["rating"]
    )
    if "fault_code" in value:
        out["FaultCode"] = value["fault_code"]
    if "notes" in value:
        out["Notes"] = value["notes"]
    if "equipment" in value:
        out["Equipment"] = value["equipment"]
    out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateLabelRequest:
    out: CreateLabelRequest = {}  # type: ignore[typeddict-item]
    if data.get("LabelGroupName") is not None:
        out["label_group_name"] = data["LabelGroupName"]
    else:
        out["label_group_name"] = ""
    if data.get("StartTime") is not None:
        import capo_lookoutequipment.types.timestamp

        out["start_time"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["StartTime"]
            )
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("EndTime") is not None:
        import capo_lookoutequipment.types.timestamp

        out["end_time"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["EndTime"]
            )
        )
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("Rating") is not None:
        import capo_lookoutequipment.types.label_rating

        out["rating"] = (
            capo_lookoutequipment.types.label_rating.deserialize_aws_json_1_0(
                data["Rating"]
            )
        )
    else:
        import typing

        out["rating"] = typing.cast(
            "capo_lookoutequipment.types.label_rating.LabelRating", ""
        )
    if data.get("FaultCode") is not None:
        out["fault_code"] = data["FaultCode"]
    if data.get("Notes") is not None:
        out["notes"] = data["Notes"]
    if data.get("Equipment") is not None:
        out["equipment"] = data["Equipment"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    return out
