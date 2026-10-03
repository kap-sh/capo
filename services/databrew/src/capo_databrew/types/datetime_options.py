"""Generated from Smithy shape ``com.amazonaws.databrew#DatetimeOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import capo_databrew.types.datetime_format
    import capo_databrew.types.locale_code
    import capo_databrew.types.timezone_offset


class DatetimeOptions(TypedDict, closed=True):
    format: "capo_databrew.types.datetime_format.DatetimeFormat"
    """<p>Required option, that defines the datetime format used for a date parameter in the Amazon S3 path. Should use only supported datetime specifiers and separation characters, all literal a-z or A-Z characters should be escaped with single quotes. E.g. "MM.dd.yyyy-'at'-HH:mm".</p>"""
    timezone_offset: NotRequired["capo_databrew.types.timezone_offset.TimezoneOffset"]
    """<p>Optional value for a timezone offset of the datetime parameter value in the Amazon S3 path. Shouldn't be used if Format for this parameter includes timezone fields. If no offset specified, UTC is assumed.</p>"""
    locale_code: NotRequired["capo_databrew.types.locale_code.LocaleCode"]
    """<p>Optional value for a non-US locale code, needed for correct interpretation of some date formats.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatetimeOptions) -> dict:
    out: dict = {}
    out["Format"] = value["format"]
    if "timezone_offset" in value:
        out["TimezoneOffset"] = value["timezone_offset"]
    if "locale_code" in value:
        out["LocaleCode"] = value["locale_code"]
    return out


def deserialize_json(data: dict) -> DatetimeOptions:
    out: DatetimeOptions = {}  # type: ignore[typeddict-item]
    if data.get("Format") is not None:
        out["format"] = data["Format"]
    else:
        raise DeserializationError("DatetimeOptions.format required")
    if data.get("TimezoneOffset") is not None:
        out["timezone_offset"] = data["TimezoneOffset"]
    if data.get("LocaleCode") is not None:
        out["locale_code"] = data["LocaleCode"]
    return out
