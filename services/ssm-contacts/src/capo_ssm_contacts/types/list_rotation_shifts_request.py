"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ListRotationShiftsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.date_time
    import capo_ssm_contacts.types.max_results
    import capo_ssm_contacts.types.pagination_token
    import capo_ssm_contacts.types.ssm_contacts_arn


class ListRotationShiftsRequest(TypedDict, closed=True):
    rotation_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the rotation to retrieve shift information about. </p>"""
    start_time: NotRequired["capo_ssm_contacts.types.date_time.DateTime"]
    """<p>The date and time for the beginning of the time range to list shifts for.</p>"""
    end_time: "capo_ssm_contacts.types.date_time.DateTime"
    """<p>The date and time for the end of the time range to list shifts for.</p>"""
    next_token: NotRequired["capo_ssm_contacts.types.pagination_token.PaginationToken"]
    """<p>A token to start the list. Use this token to get the next set of results.</p>"""
    max_results: NotRequired["capo_ssm_contacts.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRotationShiftsRequest) -> dict:
    out: dict = {}
    out["RotationId"] = value["rotation_id"]
    if "start_time" in value:
        import capo_ssm_contacts.types.date_time

        out["StartTime"] = capo_ssm_contacts.types.date_time.serialize_aws_json_1_1(
            value["start_time"]
        )
    import capo_ssm_contacts.types.date_time

    out["EndTime"] = capo_ssm_contacts.types.date_time.serialize_aws_json_1_1(
        value["end_time"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRotationShiftsRequest:
    out: ListRotationShiftsRequest = {}  # type: ignore[typeddict-item]
    if data.get("RotationId") is not None:
        out["rotation_id"] = data["RotationId"]
    else:
        out["rotation_id"] = ""
    if data.get("StartTime") is not None:
        import capo_ssm_contacts.types.date_time

        out["start_time"] = capo_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_ssm_contacts.types.date_time

        out["end_time"] = capo_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
