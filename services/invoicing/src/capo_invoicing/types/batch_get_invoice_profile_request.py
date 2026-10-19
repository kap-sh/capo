"""Generated from Smithy shape ``com.amazonaws.invoicing#BatchGetInvoiceProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.account_id_list


class BatchGetInvoiceProfileRequest(TypedDict, closed=True):
    account_ids: "capo_invoicing.types.account_id_list.AccountIdList"
    """<p>Retrieves the corresponding invoice profile data for these account IDs. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetInvoiceProfileRequest) -> dict:
    out: dict = {}
    import capo_invoicing.types.account_id_list

    out["AccountIds"] = capo_invoicing.types.account_id_list.serialize_aws_json_1_0(
        value["account_ids"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetInvoiceProfileRequest:
    out: BatchGetInvoiceProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccountIds") is not None:
        import capo_invoicing.types.account_id_list

        out["account_ids"] = (
            capo_invoicing.types.account_id_list.deserialize_aws_json_1_0(
                data["AccountIds"]
            )
        )
    else:
        out["account_ids"] = []
    return out
