"""Generated from Smithy shape ``com.amazonaws.connecthealth#WebAppConfiguration``."""

from typing_extensions import TypedDict


class WebAppConfiguration(TypedDict, closed=True):
    ehr_role: "str"
    """<p>ARN of the IAM role used for EHR operations.</p>"""
    idc_application_id: "str"
    """<p>The Identity Center application ID associated with this Domain.</p>"""
    idc_region: "str"
    """<p>The AWS region where Identity Center is configured.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WebAppConfiguration) -> dict:
    out: dict = {}
    out["ehrRole"] = value["ehr_role"]
    out["idcApplicationId"] = value["idc_application_id"]
    out["idcRegion"] = value["idc_region"]
    return out


def deserialize_json(data: dict) -> WebAppConfiguration:
    out: WebAppConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ehrRole") is not None:
        out["ehr_role"] = data["ehrRole"]
    else:
        out["ehr_role"] = ""
    if data.get("idcApplicationId") is not None:
        out["idc_application_id"] = data["idcApplicationId"]
    else:
        out["idc_application_id"] = ""
    if data.get("idcRegion") is not None:
        out["idc_region"] = data["idcRegion"]
    else:
        out["idc_region"] = ""
    return out
