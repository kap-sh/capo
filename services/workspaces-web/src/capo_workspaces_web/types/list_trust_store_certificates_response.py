"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ListTrustStoreCertificatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn
    import capo_workspaces_web.types.certificate_summary_list
    import capo_workspaces_web.types.pagination_token


class ListTrustStoreCertificatesResponse(TypedDict, closed=True):
    certificate_list: NotRequired[
        "capo_workspaces_web.types.certificate_summary_list.CertificateSummaryList"
    ]
    """<p>The certificate list.</p>"""
    trust_store_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the trust store.</p>"""
    next_token: NotRequired[
        "capo_workspaces_web.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token used to retrieve the next page of results for this operation.&gt;</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTrustStoreCertificatesResponse) -> dict:
    out: dict = {}
    if "certificate_list" in value:
        import capo_workspaces_web.types.certificate_summary_list

        out["certificateList"] = (
            capo_workspaces_web.types.certificate_summary_list.serialize_json(
                value["certificate_list"]
            )
        )
    out["trustStoreArn"] = value["trust_store_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTrustStoreCertificatesResponse:
    out: ListTrustStoreCertificatesResponse = {}  # type: ignore[typeddict-item]
    if data.get("certificateList") is not None:
        import capo_workspaces_web.types.certificate_summary_list

        out["certificate_list"] = (
            capo_workspaces_web.types.certificate_summary_list.deserialize_json(
                data["certificateList"]
            )
        )
    if data.get("trustStoreArn") is not None:
        out["trust_store_arn"] = data["trustStoreArn"]
    else:
        out["trust_store_arn"] = ""
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
