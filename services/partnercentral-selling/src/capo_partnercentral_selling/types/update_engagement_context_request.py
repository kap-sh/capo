"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#UpdateEngagementContextRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.date_time
    import capo_partnercentral_selling.types.engagement_arn_or_identifier
    import capo_partnercentral_selling.types.engagement_context_identifier
    import capo_partnercentral_selling.types.engagement_context_type
    import capo_partnercentral_selling.types.update_engagement_context_payload


class UpdateEngagementContextRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog associated with the engagement context update request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the engagement context is updated in.</p>"""
    engagement_identifier: "capo_partnercentral_selling.types.engagement_arn_or_identifier.EngagementArnOrIdentifier"
    """<p>The unique identifier of the <code>Engagement</code> containing the context to be updated. This parameter ensures the context update is applied to the correct engagement.</p>"""
    context_identifier: "capo_partnercentral_selling.types.engagement_context_identifier.EngagementContextIdentifier"
    """<p>The unique identifier of the specific engagement context to be updated. This ensures that the correct context within the engagement is modified.</p>"""
    engagement_last_modified_at: "capo_partnercentral_selling.types.date_time.DateTime"
    """<p>The timestamp when the engagement was last modified, used for optimistic concurrency control. This helps prevent conflicts when multiple users attempt to update the same engagement simultaneously.</p>"""
    type: "capo_partnercentral_selling.types.engagement_context_type.EngagementContextType"
    """<p>Specifies the type of context being updated within the engagement. This field determines the structure and content of the context payload being modified.</p>"""
    payload: "capo_partnercentral_selling.types.update_engagement_context_payload.UpdateEngagementContextPayload"
    """<p>Contains the updated contextual information for the engagement. The structure of this payload varies based on the context type specified in the Type field.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateEngagementContextRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["EngagementIdentifier"] = value["engagement_identifier"]
    out["ContextIdentifier"] = value["context_identifier"]
    import capo_partnercentral_selling.types.date_time

    out["EngagementLastModifiedAt"] = (
        capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
            value["engagement_last_modified_at"]
        )
    )
    import capo_partnercentral_selling.types.engagement_context_type

    out["Type"] = (
        capo_partnercentral_selling.types.engagement_context_type.serialize_aws_json_1_0(
            value["type"]
        )
    )
    import capo_partnercentral_selling.types.update_engagement_context_payload

    out["Payload"] = (
        capo_partnercentral_selling.types.update_engagement_context_payload.serialize_aws_json_1_0(
            value["payload"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateEngagementContextRequest:
    out: UpdateEngagementContextRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("EngagementIdentifier") is not None:
        out["engagement_identifier"] = data["EngagementIdentifier"]
    else:
        out["engagement_identifier"] = ""
    if data.get("ContextIdentifier") is not None:
        out["context_identifier"] = data["ContextIdentifier"]
    else:
        out["context_identifier"] = ""
    if data.get("EngagementLastModifiedAt") is not None:
        import capo_partnercentral_selling.types.date_time

        out["engagement_last_modified_at"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["EngagementLastModifiedAt"]
            )
        )
    else:
        import datetime

        out["engagement_last_modified_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
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
        import capo_partnercentral_selling.types.update_engagement_context_payload

        out["payload"] = (
            capo_partnercentral_selling.types.update_engagement_context_payload.deserialize_aws_json_1_0(
                data["Payload"]
            )
        )
    else:
        import capo_partnercentral_selling.types._unknown

        out["payload"] = capo_partnercentral_selling.types._unknown.UnknownUnionMember(
            ""
        )
    return out


def redact_sensitive(value: UpdateEngagementContextRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payload" in value:
        import capo_partnercentral_selling.types.update_engagement_context_payload

        out["payload"] = (
            capo_partnercentral_selling.types.update_engagement_context_payload.redact_sensitive(
                value["payload"]
            )
        )
    return out
