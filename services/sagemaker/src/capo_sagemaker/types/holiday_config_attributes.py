"""Generated from Smithy shape ``com.amazonaws.sagemaker#HolidayConfigAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.country_code


class HolidayConfigAttributes(TypedDict, closed=True):
    country_code: NotRequired["capo_sagemaker.types.country_code.CountryCode"]
    """<p>The country code for the holiday calendar.</p> <p>For the list of public holiday calendars supported by AutoML job V2, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-timeseries-forecasting-holiday-calendars.html#holiday-country-codes">Country Codes</a>. Use the country code corresponding to the country of your choice.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HolidayConfigAttributes) -> dict:
    out: dict = {}
    if "country_code" in value:
        out["CountryCode"] = value["country_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HolidayConfigAttributes:
    out: HolidayConfigAttributes = {}  # type: ignore[typeddict-item]
    if data.get("CountryCode") is not None:
        out["country_code"] = data["CountryCode"]
    return out
