"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DeleteProvisionedProductPlanInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.id
    import capo_service_catalog.types.ignore_errors


class DeleteProvisionedProductPlanInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    plan_id: "capo_service_catalog.types.id.Id"
    """<p>The plan identifier.</p>"""
    ignore_errors: NotRequired["capo_service_catalog.types.ignore_errors.IgnoreErrors"]
    """<p>If set to true, Service Catalog stops managing the specified provisioned product even if it cannot delete the underlying resources.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteProvisionedProductPlanInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["PlanId"] = value["plan_id"]
    if "ignore_errors" in value:
        out["IgnoreErrors"] = value["ignore_errors"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteProvisionedProductPlanInput:
    out: DeleteProvisionedProductPlanInput = {}  # type: ignore[typeddict-item]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    if data.get("PlanId") is not None:
        out["plan_id"] = data["PlanId"]
    else:
        out["plan_id"] = ""
    if data.get("IgnoreErrors") is not None:
        out["ignore_errors"] = data["IgnoreErrors"]
    return out
