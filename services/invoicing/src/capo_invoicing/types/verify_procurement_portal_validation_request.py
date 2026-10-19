"""Generated from Smithy shape ``com.amazonaws.invoicing#VerifyProcurementPortalValidationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.basic_string_without_space
    import capo_invoicing.types.procurement_portal_preference_arn_string


class VerifyProcurementPortalValidationRequest(TypedDict, closed=True):
    procurement_portal_preference_arn: "capo_invoicing.types.procurement_portal_preference_arn_string.ProcurementPortalPreferenceArnString"
    """<p>The Amazon Resource Name (ARN) of the procurement portal preference to validate.</p>"""
    code: "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    """<p>The validation code received from the procurement portal in response to a previous <code>SendProcurementPortalValidation</code> request.</p>"""
    client_token: NotRequired[
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VerifyProcurementPortalValidationRequest) -> dict:
    out: dict = {}
    out["ProcurementPortalPreferenceArn"] = value["procurement_portal_preference_arn"]
    out["Code"] = value["code"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> VerifyProcurementPortalValidationRequest:
    out: VerifyProcurementPortalValidationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProcurementPortalPreferenceArn") is not None:
        out["procurement_portal_preference_arn"] = data[
            "ProcurementPortalPreferenceArn"
        ]
    else:
        out["procurement_portal_preference_arn"] = ""
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    else:
        out["code"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
