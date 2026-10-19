"""Generated from Smithy shape ``com.amazonaws.artifact#CreateComplianceInquiryRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_artifact.types.idempotent_client_token
    import capo_artifact.types.inquiry_content
    import capo_artifact.types.inquiry_name
    import capo_artifact.types.inquiry_support_mode
    import capo_artifact.types.tags_map


class CreateComplianceInquiryRequest(TypedDict, closed=True):
    name: "capo_artifact.types.inquiry_name.InquiryName"
    """<p>Title of the inquiry.</p>"""
    inquiry_content: "capo_artifact.types.inquiry_content.InquiryContent"
    """<p>Content for creating a compliance inquiry - either a single query or file content.</p>"""
    client_token: NotRequired[
        "capo_artifact.types.idempotent_client_token.IdempotentClientToken"
    ]
    """<p>Idempotency token for the request.</p>"""
    support_mode: NotRequired[
        "capo_artifact.types.inquiry_support_mode.InquirySupportMode"
    ]
    """<p>Support mode for inquiry processing. Only supported for file upload mode. Defaults to AI_ONLY if not specified.</p>"""
    tags: NotRequired["capo_artifact.types.tags_map.TagsMap"]
    """<p>Tags to associate with the compliance inquiry resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateComplianceInquiryRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_artifact.types.inquiry_content

    out["inquiryContent"] = capo_artifact.types.inquiry_content.serialize_json(
        value["inquiry_content"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "support_mode" in value:
        import capo_artifact.types.inquiry_support_mode

        out["supportMode"] = capo_artifact.types.inquiry_support_mode.serialize_json(
            value["support_mode"]
        )
    if "tags" in value:
        import capo_artifact.types.tags_map

        out["tags"] = capo_artifact.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateComplianceInquiryRequest:
    out: CreateComplianceInquiryRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("inquiryContent") is not None:
        import capo_artifact.types.inquiry_content

        out["inquiry_content"] = capo_artifact.types.inquiry_content.deserialize_json(
            data["inquiryContent"]
        )
    else:
        import capo_artifact.types._unknown

        out["inquiry_content"] = capo_artifact.types._unknown.UnknownUnionMember("")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("supportMode") is not None:
        import capo_artifact.types.inquiry_support_mode

        out["support_mode"] = capo_artifact.types.inquiry_support_mode.deserialize_json(
            data["supportMode"]
        )
    if data.get("tags") is not None:
        import capo_artifact.types.tags_map

        out["tags"] = capo_artifact.types.tags_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: CreateComplianceInquiryRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "inquiry_content" in value:
        out["inquiry_content"] = "*** Sensitive Data Redacted ***"
    return out
