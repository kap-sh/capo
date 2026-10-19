"""Generated from Smithy shape ``com.amazonaws.devopsguru#DescribeOrganizationOverviewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.account_id_list
    import capo_devops_guru.types.organizational_unit_id_list
    import capo_devops_guru.types.timestamp


class DescribeOrganizationOverviewRequest(TypedDict, closed=True):
    from_time: "capo_devops_guru.types.timestamp.Timestamp"
    """<p> The start of the time range passed in. The start time granularity is at the day level. The floor of the start time is used. Returned information occurred after this day. </p>"""
    to_time: NotRequired["capo_devops_guru.types.timestamp.Timestamp"]
    """<p> The end of the time range passed in. The start time granularity is at the day level. The floor of the start time is used. Returned information occurred before this day. If this is not specified, then the current day is used. </p>"""
    account_ids: NotRequired["capo_devops_guru.types.account_id_list.AccountIdList"]
    """<p>The ID of the Amazon Web Services account.</p>"""
    organizational_unit_ids: NotRequired[
        "capo_devops_guru.types.organizational_unit_id_list.OrganizationalUnitIdList"
    ]
    """<p>The ID of the organizational unit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeOrganizationOverviewRequest) -> dict:
    out: dict = {}
    import capo_devops_guru.types.timestamp

    out["FromTime"] = capo_devops_guru.types.timestamp.serialize_json(
        value["from_time"]
    )
    if "to_time" in value:
        import capo_devops_guru.types.timestamp

        out["ToTime"] = capo_devops_guru.types.timestamp.serialize_json(
            value["to_time"]
        )
    if "account_ids" in value:
        import capo_devops_guru.types.account_id_list

        out["AccountIds"] = capo_devops_guru.types.account_id_list.serialize_json(
            value["account_ids"]
        )
    if "organizational_unit_ids" in value:
        import capo_devops_guru.types.organizational_unit_id_list

        out["OrganizationalUnitIds"] = (
            capo_devops_guru.types.organizational_unit_id_list.serialize_json(
                value["organizational_unit_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeOrganizationOverviewRequest:
    out: DescribeOrganizationOverviewRequest = {}  # type: ignore[typeddict-item]
    if data.get("FromTime") is not None:
        import capo_devops_guru.types.timestamp

        out["from_time"] = capo_devops_guru.types.timestamp.deserialize_json(
            data["FromTime"]
        )
    else:
        import datetime

        out["from_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("ToTime") is not None:
        import capo_devops_guru.types.timestamp

        out["to_time"] = capo_devops_guru.types.timestamp.deserialize_json(
            data["ToTime"]
        )
    if data.get("AccountIds") is not None:
        import capo_devops_guru.types.account_id_list

        out["account_ids"] = capo_devops_guru.types.account_id_list.deserialize_json(
            data["AccountIds"]
        )
    if data.get("OrganizationalUnitIds") is not None:
        import capo_devops_guru.types.organizational_unit_id_list

        out["organizational_unit_ids"] = (
            capo_devops_guru.types.organizational_unit_id_list.deserialize_json(
                data["OrganizationalUnitIds"]
            )
        )
    return out
