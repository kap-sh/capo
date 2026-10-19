"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ListLabelsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.equipment
    import capo_lookoutequipment.types.fault_code
    import capo_lookoutequipment.types.label_group_name
    import capo_lookoutequipment.types.max_results
    import capo_lookoutequipment.types.next_token
    import capo_lookoutequipment.types.timestamp


class ListLabelsRequest(TypedDict, closed=True):
    label_group_name: "capo_lookoutequipment.types.label_group_name.LabelGroupName"
    """<p> Returns the name of the label group. </p>"""
    interval_start_time: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p> Returns all the labels with a end time equal to or later than the start time given. </p>"""
    interval_end_time: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p> Returns all labels with a start time earlier than the end time given. </p>"""
    fault_code: NotRequired["capo_lookoutequipment.types.fault_code.FaultCode"]
    """<p> Returns labels with a particular fault code. </p>"""
    equipment: NotRequired["capo_lookoutequipment.types.equipment.Equipment"]
    """<p> Lists the labels that pertain to a particular piece of equipment. </p>"""
    next_token: NotRequired["capo_lookoutequipment.types.next_token.NextToken"]
    """<p> An opaque pagination token indicating where to continue the listing of label groups. </p>"""
    max_results: NotRequired["capo_lookoutequipment.types.max_results.MaxResults"]
    """<p> Specifies the maximum number of labels to list. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListLabelsRequest) -> dict:
    out: dict = {}
    out["LabelGroupName"] = value["label_group_name"]
    if "interval_start_time" in value:
        import capo_lookoutequipment.types.timestamp

        out["IntervalStartTime"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["interval_start_time"]
            )
        )
    if "interval_end_time" in value:
        import capo_lookoutequipment.types.timestamp

        out["IntervalEndTime"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["interval_end_time"]
            )
        )
    if "fault_code" in value:
        out["FaultCode"] = value["fault_code"]
    if "equipment" in value:
        out["Equipment"] = value["equipment"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListLabelsRequest:
    out: ListLabelsRequest = {}  # type: ignore[typeddict-item]
    if data.get("LabelGroupName") is not None:
        out["label_group_name"] = data["LabelGroupName"]
    else:
        out["label_group_name"] = ""
    if data.get("IntervalStartTime") is not None:
        import capo_lookoutequipment.types.timestamp

        out["interval_start_time"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["IntervalStartTime"]
            )
        )
    if data.get("IntervalEndTime") is not None:
        import capo_lookoutequipment.types.timestamp

        out["interval_end_time"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["IntervalEndTime"]
            )
        )
    if data.get("FaultCode") is not None:
        out["fault_code"] = data["FaultCode"]
    if data.get("Equipment") is not None:
        out["equipment"] = data["Equipment"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
