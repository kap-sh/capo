"""Generated from Smithy shape ``com.amazonaws.forecast#AdditionalDataset``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import capo_forecast.types.configuration
    import capo_forecast.types.name


class AdditionalDataset(TypedDict, closed=True):
    name: "capo_forecast.types.name.Name"
    """<p>The name of the additional dataset. Valid names: <code>"holiday"</code> and <code>"weather"</code>.</p>"""
    configuration: NotRequired["capo_forecast.types.configuration.Configuration"]
    """<p> <b>Weather Index</b> </p> <p>To enable the Weather Index, do not specify a value for <code>Configuration</code>.</p> <p> <b>Holidays</b> </p> <p> <b>Holidays</b> </p> <p>To enable Holidays, set <code>CountryCode</code> to one of the following two-letter country codes:</p> <ul> <li> <p>"AL" - ALBANIA</p> </li> <li> <p>"AR" - ARGENTINA</p> </li> <li> <p>"AT" - AUSTRIA</p> </li> <li> <p>"AU" - AUSTRALIA</p> </li> <li> <p>"BA" - BOSNIA HERZEGOVINA</p> </li> <li> <p>"BE" - BELGIUM</p> </li> <li> <p>"BG" - BULGARIA</p> </li> <li> <p>"BO" - BOLIVIA</p> </li> <li> <p>"BR" - BRAZIL</p> </li> <li> <p>"BY" - BELARUS</p> </li> <li> <p>"CA" - CANADA</p> </li> <li> <p>"CL" - CHILE</p> </li> <li> <p>"CO" - COLOMBIA</p> </li> <li> <p>"CR" - COSTA RICA</p> </li> <li> <p>"HR" - CROATIA</p> </li> <li> <p>"CZ" - CZECH REPUBLIC</p> </li> <li> <p>"DK" - DENMARK</p> </li> <li> <p>"EC" - ECUADOR</p> </li> <li> <p>"EE" - ESTONIA</p> </li> <li> <p>"ET" - ETHIOPIA</p> </li> <li> <p>"FI" - FINLAND</p> </li> <li> <p>"FR" - FRANCE</p> </li> <li> <p>"DE" - GERMANY</p> </li> <li> <p>"GR" - GREECE</p> </li> <li> <p>"HU" - HUNGARY</p> </li> <li> <p>"IS" - ICELAND</p> </li> <li> <p>"IN" - INDIA</p> </li> <li> <p>"IE" - IRELAND</p> </li> <li> <p>"IT" - ITALY</p> </li> <li> <p>"JP" - JAPAN</p> </li> <li> <p>"KZ" - KAZAKHSTAN</p> </li> <li> <p>"KR" - KOREA</p> </li> <li> <p>"LV" - LATVIA</p> </li> <li> <p>"LI" - LIECHTENSTEIN</p> </li> <li> <p>"LT" - LITHUANIA</p> </li> <li> <p>"LU" - LUXEMBOURG</p> </li> <li> <p>"MK" - MACEDONIA</p> </li> <li> <p>"MT" - MALTA</p> </li> <li> <p>"MX" - MEXICO</p> </li> <li> <p>"MD" - MOLDOVA</p> </li> <li> <p>"ME" - MONTENEGRO</p> </li> <li> <p>"NL" - NETHERLANDS</p> </li> <li> <p>"NZ" - NEW ZEALAND</p> </li> <li> <p>"NI" - NICARAGUA</p> </li> <li> <p>"NG" - NIGERIA</p> </li> <li> <p>"NO" - NORWAY</p> </li> <li> <p>"PA" - PANAMA</p> </li> <li> <p>"PY" - PARAGUAY</p> </li> <li> <p>"PE" - PERU</p> </li> <li> <p>"PL" - POLAND</p> </li> <li> <p>"PT" - PORTUGAL</p> </li> <li> <p>"RO" - ROMANIA</p> </li> <li> <p>"RU" - RUSSIA</p> </li> <li> <p>"RS" - SERBIA</p> </li> <li> <p>"SK" - SLOVAKIA</p> </li> <li> <p>"SI" - SLOVENIA</p> </li> <li> <p>"ZA" - SOUTH AFRICA</p> </li> <li> <p>"ES" - SPAIN</p> </li> <li> <p>"SE" - SWEDEN</p> </li> <li> <p>"CH" - SWITZERLAND</p> </li> <li> <p>"UA" - UKRAINE</p> </li> <li> <p>"AE" - UNITED ARAB EMIRATES</p> </li> <li> <p>"US" - UNITED STATES</p> </li> <li> <p>"UK" - UNITED KINGDOM</p> </li> <li> <p>"UY" - URUGUAY</p> </li> <li> <p>"VE" - VENEZUELA</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdditionalDataset) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "configuration" in value:
        import capo_forecast.types.configuration

        out["Configuration"] = capo_forecast.types.configuration.serialize_aws_json_1_1(
            value["configuration"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdditionalDataset:
    out: AdditionalDataset = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("AdditionalDataset.name required")
    if data.get("Configuration") is not None:
        import capo_forecast.types.configuration

        out["configuration"] = (
            capo_forecast.types.configuration.deserialize_aws_json_1_1(
                data["Configuration"]
            )
        )
    return out
