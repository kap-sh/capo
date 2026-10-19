"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#StartServicePeriodPayload``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.date_time
    import capo_partnercentral_channel.types.minimum_notice_days
    import capo_partnercentral_channel.types.note
    import capo_partnercentral_channel.types.program_management_account_identifier
    import capo_partnercentral_channel.types.service_period_type


class StartServicePeriodPayload(TypedDict, closed=True):
    program_management_account_identifier: "capo_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier"
    """<p>The identifier of the program management account.</p>"""
    note: NotRequired["capo_partnercentral_channel.types.note.Note"]
    """<p>A note providing additional information about the service period.</p>"""
    service_period_type: (
        "capo_partnercentral_channel.types.service_period_type.ServicePeriodType"
    )
    """<p>The type of service period being started.</p>"""
    minimum_notice_days: NotRequired[
        "capo_partnercentral_channel.types.minimum_notice_days.MinimumNoticeDays"
    ]
    """<p>The minimum number of days notice required for changes.</p>"""
    end_date: NotRequired["capo_partnercentral_channel.types.date_time.DateTime"]
    """<p>The end date of the service period.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartServicePeriodPayload) -> dict:
    out: dict = {}
    out["programManagementAccountIdentifier"] = value[
        "program_management_account_identifier"
    ]
    if "note" in value:
        out["note"] = value["note"]
    import capo_partnercentral_channel.types.service_period_type

    out["servicePeriodType"] = (
        capo_partnercentral_channel.types.service_period_type.serialize_aws_json_1_0(
            value["service_period_type"]
        )
    )
    if "minimum_notice_days" in value:
        out["minimumNoticeDays"] = value["minimum_notice_days"]
    if "end_date" in value:
        import capo_partnercentral_channel.types.date_time

        out["endDate"] = (
            capo_partnercentral_channel.types.date_time.serialize_aws_json_1_0(
                value["end_date"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartServicePeriodPayload:
    out: StartServicePeriodPayload = {}  # type: ignore[typeddict-item]
    if data.get("programManagementAccountIdentifier") is not None:
        out["program_management_account_identifier"] = data[
            "programManagementAccountIdentifier"
        ]
    else:
        out["program_management_account_identifier"] = ""
    if data.get("note") is not None:
        out["note"] = data["note"]
    if data.get("servicePeriodType") is not None:
        import capo_partnercentral_channel.types.service_period_type

        out["service_period_type"] = (
            capo_partnercentral_channel.types.service_period_type.deserialize_aws_json_1_0(
                data["servicePeriodType"]
            )
        )
    else:
        import typing

        out["service_period_type"] = typing.cast(
            "capo_partnercentral_channel.types.service_period_type.ServicePeriodType",
            "",
        )
    if data.get("minimumNoticeDays") is not None:
        out["minimum_notice_days"] = data["minimumNoticeDays"]
    if data.get("endDate") is not None:
        import capo_partnercentral_channel.types.date_time

        out["end_date"] = (
            capo_partnercentral_channel.types.date_time.deserialize_aws_json_1_0(
                data["endDate"]
            )
        )
    return out
