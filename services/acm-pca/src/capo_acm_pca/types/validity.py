"""Generated from Smithy shape ``com.amazonaws.acmpca#Validity``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_acm_pca.types.positive_long
    import capo_acm_pca.types.validity_period_type


class Validity(TypedDict, closed=True):
    value: "capo_acm_pca.types.positive_long.PositiveLong"
    """<p>A long integer interpreted according to the value of <code>Type</code>, below.</p>"""
    type: "capo_acm_pca.types.validity_period_type.ValidityPeriodType"
    """<p>Determines how <i>Amazon Web Services Private CA</i> interprets the <code>Value</code> parameter, an integer. Supported validity types include those listed below. Type definitions with values include a sample input value and the resulting output. </p> <p> <code>END_DATE</code>: The specific date and time when the certificate will expire, expressed using UTCTime (YYMMDDHHMMSS) or GeneralizedTime (YYYYMMDDHHMMSS) format. When UTCTime is used, if the year field (YY) is greater than or equal to 50, the year is interpreted as 19YY. If the year field is less than 50, the year is interpreted as 20YY.</p> <ul> <li> <p>Sample input value: 491231235959 (UTCTime format)</p> </li> <li> <p>Output expiration date/time: 12/31/2049 23:59:59</p> </li> </ul> <p> <code>ABSOLUTE</code>: The specific date and time when the validity of a certificate will start or expire, expressed in seconds since the Unix Epoch. </p> <ul> <li> <p>Sample input value: 2524608000</p> </li> <li> <p>Output expiration date/time: 01/01/2050 00:00:00</p> </li> </ul> <p> <code>DAYS</code>, <code>MONTHS</code>, <code>YEARS</code>: The relative time from the moment of issuance until the certificate will expire, expressed in days, months, or years. </p> <p>Example if <code>DAYS</code>, issued on 10/12/2020 at 12:34:54 UTC:</p> <ul> <li> <p>Sample input value: 90</p> </li> <li> <p>Output expiration date: 01/10/2020 12:34:54 UTC</p> </li> </ul> <p>The minimum validity duration for a certificate using relative time (<code>DAYS</code>) is one day. The minimum validity for a certificate using absolute time (<code>ABSOLUTE</code> or <code>END_DATE</code>) is one second.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Validity) -> dict:
    out: dict = {}
    out["Value"] = value["value"]
    import capo_acm_pca.types.validity_period_type

    out["Type"] = capo_acm_pca.types.validity_period_type.serialize_aws_json_1_1(
        value["type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Validity:
    out: Validity = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = 0
    if data.get("Type") is not None:
        import capo_acm_pca.types.validity_period_type

        out["type"] = capo_acm_pca.types.validity_period_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_acm_pca.types.validity_period_type.ValidityPeriodType", ""
        )
    return out
