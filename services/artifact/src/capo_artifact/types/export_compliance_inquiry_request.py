"""Generated from Smithy shape ``com.amazonaws.artifact#ExportComplianceInquiryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_artifact.types.inquiry_id
    import capo_artifact.types.query_identifiers_list


class ExportComplianceInquiryRequest(TypedDict, closed=True):
    compliance_inquiry_id: "capo_artifact.types.inquiry_id.InquiryId"
    """<p>Unique resource ID for the compliance inquiry.</p>"""
    query_identifiers: NotRequired[
        "capo_artifact.types.query_identifiers_list.QueryIdentifiersList"
    ]
    """<p>List of query identifiers to include in the export.</p>"""
    include_citations: NotRequired["bool"]
    """<p>When true, include citations in the exported document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportComplianceInquiryRequest) -> dict:
    out: dict = {}
    out["complianceInquiryId"] = value["compliance_inquiry_id"]
    if "query_identifiers" in value:
        import capo_artifact.types.query_identifiers_list

        out["queryIdentifiers"] = (
            capo_artifact.types.query_identifiers_list.serialize_json(
                value["query_identifiers"]
            )
        )
    if "include_citations" in value:
        out["includeCitations"] = value["include_citations"]
    return out


def deserialize_json(data: dict) -> ExportComplianceInquiryRequest:
    out: ExportComplianceInquiryRequest = {}  # type: ignore[typeddict-item]
    if data.get("complianceInquiryId") is not None:
        out["compliance_inquiry_id"] = data["complianceInquiryId"]
    else:
        out["compliance_inquiry_id"] = ""
    if data.get("queryIdentifiers") is not None:
        import capo_artifact.types.query_identifiers_list

        out["query_identifiers"] = (
            capo_artifact.types.query_identifiers_list.deserialize_json(
                data["queryIdentifiers"]
            )
        )
    if data.get("includeCitations") is not None:
        out["include_citations"] = data["includeCitations"]
    return out
