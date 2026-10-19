"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#CreateEngagementContextRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.client_token
    import capo_partnercentral_selling.types.engagement_arn_or_identifier
    import capo_partnercentral_selling.types.engagement_context_payload
    import capo_partnercentral_selling.types.engagement_context_type


class CreateEngagementContextRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog associated with the engagement context request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the engagement context is created in. Use <code>AWS</code> to create contexts in the production environment, and <code>Sandbox</code> for testing in secure, isolated environments.</p>"""
    engagement_identifier: "capo_partnercentral_selling.types.engagement_arn_or_identifier.EngagementArnOrIdentifier"
    """<p>The unique identifier of the <code>Engagement</code> for which the context is being created. This parameter ensures the context is associated with the correct engagement and provides the necessary linkage between the engagement and its contextual information.</p>"""
    client_token: "capo_partnercentral_selling.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier provided by the client to ensure that the request is handled exactly once. This token helps prevent duplicate context creations and must not exceed sixty-four alphanumeric characters. Use a UUID or other unique string to ensure idempotency.</p>"""
    type: "capo_partnercentral_selling.types.engagement_context_type.EngagementContextType"
    """<p>Specifies the type of context being created for the engagement. This field determines the structure and content of the context payload. Valid values include <code>CustomerProject</code> for customer project-related contexts. The type field ensures that the context is properly categorized and processed according to its intended purpose.</p>"""
    payload: "capo_partnercentral_selling.types.engagement_context_payload.EngagementContextPayload"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateEngagementContextRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["EngagementIdentifier"] = value["engagement_identifier"]
    out["ClientToken"] = value["client_token"]
    import capo_partnercentral_selling.types.engagement_context_type

    out["Type"] = (
        capo_partnercentral_selling.types.engagement_context_type.serialize_aws_json_1_0(
            value["type"]
        )
    )
    import capo_partnercentral_selling.types.engagement_context_payload

    out["Payload"] = (
        capo_partnercentral_selling.types.engagement_context_payload.serialize_aws_json_1_0(
            value["payload"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateEngagementContextRequest:
    out: CreateEngagementContextRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("EngagementIdentifier") is not None:
        out["engagement_identifier"] = data["EngagementIdentifier"]
    else:
        out["engagement_identifier"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    if data.get("Type") is not None:
        import capo_partnercentral_selling.types.engagement_context_type

        out["type"] = (
            capo_partnercentral_selling.types.engagement_context_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_partnercentral_selling.types.engagement_context_type.EngagementContextType",
            "",
        )
    if data.get("Payload") is not None:
        import capo_partnercentral_selling.types.engagement_context_payload

        out["payload"] = (
            capo_partnercentral_selling.types.engagement_context_payload.deserialize_aws_json_1_0(
                data["Payload"]
            )
        )
    else:
        import capo_partnercentral_selling.types._unknown

        out["payload"] = capo_partnercentral_selling.types._unknown.UnknownUnionMember(
            ""
        )
    return out


def redact_sensitive(value: CreateEngagementContextRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payload" in value:
        import capo_partnercentral_selling.types.engagement_context_payload

        out["payload"] = (
            capo_partnercentral_selling.types.engagement_context_payload.redact_sensitive(
                value["payload"]
            )
        )
    return out
