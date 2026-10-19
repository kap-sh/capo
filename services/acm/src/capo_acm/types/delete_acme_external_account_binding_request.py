"""Generated from Smithy shape ``com.amazonaws.acm#DeleteAcmeExternalAccountBindingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_acm.types.acme_external_account_binding_arn


class DeleteAcmeExternalAccountBindingRequest(TypedDict, closed=True):
    acme_external_account_binding_arn: (
        "capo_acm.types.acme_external_account_binding_arn.AcmeExternalAccountBindingArn"
    )
    """<p>The Amazon Resource Name (ARN) of the ACME external account binding to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAcmeExternalAccountBindingRequest) -> dict:
    out: dict = {}
    out["AcmeExternalAccountBindingArn"] = value["acme_external_account_binding_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAcmeExternalAccountBindingRequest:
    out: DeleteAcmeExternalAccountBindingRequest = {}  # type: ignore[typeddict-item]
    if data.get("AcmeExternalAccountBindingArn") is not None:
        out["acme_external_account_binding_arn"] = data["AcmeExternalAccountBindingArn"]
    else:
        out["acme_external_account_binding_arn"] = ""
    return out
