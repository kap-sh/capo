"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribeServiceActionExecutionParametersInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.id


class DescribeServiceActionExecutionParametersInput(TypedDict, closed=True):
    provisioned_product_id: "capo_service_catalog.types.id.Id"
    """<p>The identifier of the provisioned product.</p>"""
    service_action_id: "capo_service_catalog.types.id.Id"
    """<p>The self-service action identifier.</p>"""
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeServiceActionExecutionParametersInput,
) -> dict:
    out: dict = {}
    out["ProvisionedProductId"] = value["provisioned_product_id"]
    out["ServiceActionId"] = value["service_action_id"]
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeServiceActionExecutionParametersInput:
    out: DescribeServiceActionExecutionParametersInput = {}  # type: ignore[typeddict-item]
    if data.get("ProvisionedProductId") is not None:
        out["provisioned_product_id"] = data["ProvisionedProductId"]
    else:
        out["provisioned_product_id"] = ""
    if data.get("ServiceActionId") is not None:
        out["service_action_id"] = data["ServiceActionId"]
    else:
        out["service_action_id"] = ""
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    return out
