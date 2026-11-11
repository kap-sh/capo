"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchUpdateCaseRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.batch_update_case_identifier_list
    import capo_connectcases.types.case_status
    import capo_connectcases.types.case_title
    import capo_connectcases.types.customer_profile_arn
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.field_value_input_list
    import capo_connectcases.types.user_union


class BatchUpdateCaseRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    cases: "capo_connectcases.types.batch_update_case_identifier_list.BatchUpdateCaseIdentifierList"
    """<p>The list of cases to update. All cases must belong to the same domain.</p>"""
    fields: "capo_connectcases.types.field_value_input_list.FieldValueInputList"
    """<p>An array of objects, each with a <code>fieldIdentifier</code> and a <code>value</code>. You can identify each field by its ID or by its name; identifying a field by name is supported only in <code>BatchUpdateCase</code>. The same field values are applied to every case in the request. This field must be present, but can be an empty list when you provide the top-level <code>title</code>, <code>status</code>, or <code>customerId</code> parameters. Do not include <code>title</code>, <code>status</code>, or <code>customerId</code> in this list; set those values only through their top-level parameters. Duplicating them in <code>fields</code> results in a validation error.</p>"""
    performed_by: NotRequired["capo_connectcases.types.user_union.UserUnion"]
    """<p>The entity that performed the action.</p>"""
    title: NotRequired["capo_connectcases.types.case_title.CaseTitle"]
    """<p>The title to apply to all cases in the request.</p>"""
    status: NotRequired["capo_connectcases.types.case_status.CaseStatus"]
    """<p>The status to apply to all cases in the request.</p>"""
    customer_id: NotRequired[
        "capo_connectcases.types.customer_profile_arn.CustomerProfileArn"
    ]
    """<p>The ARN of the customer profile to associate with all cases in the request.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p> <p>If you retry a request with the same client token, the service returns the original response instead of processing the request again. If you reuse a client token with different request parameters, the request fails with a <code>ConflictException</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateCaseRequest) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    import capo_connectcases.types.batch_update_case_identifier_list

    out["cases"] = (
        capo_connectcases.types.batch_update_case_identifier_list.serialize_json(
            value["cases"]
        )
    )
    import capo_connectcases.types.field_value_input_list

    out["fields"] = capo_connectcases.types.field_value_input_list.serialize_json(
        value["fields"]
    )
    if "performed_by" in value:
        import capo_connectcases.types.user_union

        out["performedBy"] = capo_connectcases.types.user_union.serialize_json(
            value["performed_by"]
        )
    if "title" in value:
        out["title"] = value["title"]
    if "status" in value:
        out["status"] = value["status"]
    if "customer_id" in value:
        out["customerId"] = value["customer_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> BatchUpdateCaseRequest:
    out: BatchUpdateCaseRequest = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("cases") is not None:
        import capo_connectcases.types.batch_update_case_identifier_list

        out["cases"] = (
            capo_connectcases.types.batch_update_case_identifier_list.deserialize_json(
                data["cases"]
            )
        )
    else:
        out["cases"] = []
    if data.get("fields") is not None:
        import capo_connectcases.types.field_value_input_list

        out["fields"] = capo_connectcases.types.field_value_input_list.deserialize_json(
            data["fields"]
        )
    else:
        out["fields"] = []
    if data.get("performedBy") is not None:
        import capo_connectcases.types.user_union

        out["performed_by"] = capo_connectcases.types.user_union.deserialize_json(
            data["performedBy"]
        )
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("customerId") is not None:
        out["customer_id"] = data["customerId"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: BatchUpdateCaseRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "performed_by" in value:
        import capo_connectcases.types.user_union

        out["performed_by"] = capo_connectcases.types.user_union.redact_sensitive(
            value["performed_by"]
        )
    if "title" in value:
        out["title"] = "*** Sensitive Data Redacted ***"
    return out
