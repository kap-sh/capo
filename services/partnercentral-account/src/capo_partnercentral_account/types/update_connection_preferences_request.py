"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#UpdateConnectionPreferencesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_account.types.access_type
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.participant_identifier_list
    import capo_partnercentral_account.types.revision


class UpdateConnectionPreferencesRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    revision: "capo_partnercentral_account.types.revision.Revision"
    """<p>The revision number of the connection preferences for optimistic locking.</p>"""
    access_type: "capo_partnercentral_account.types.access_type.AccessType"
    """<p>The access type setting for connections (e.g., open, restricted, invitation-only).</p>"""
    excluded_participant_identifiers: NotRequired[
        "capo_partnercentral_account.types.participant_identifier_list.ParticipantIdentifierList"
    ]
    """<p>The updated list of participant identifiers to exclude from connections.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateConnectionPreferencesRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Revision"] = value["revision"]
    import capo_partnercentral_account.types.access_type

    out["AccessType"] = (
        capo_partnercentral_account.types.access_type.serialize_aws_json_1_0(
            value["access_type"]
        )
    )
    if "excluded_participant_identifiers" in value:
        import capo_partnercentral_account.types.participant_identifier_list

        out["ExcludedParticipantIdentifiers"] = (
            capo_partnercentral_account.types.participant_identifier_list.serialize_aws_json_1_0(
                value["excluded_participant_identifiers"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateConnectionPreferencesRequest:
    out: UpdateConnectionPreferencesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("Revision") is not None:
        out["revision"] = data["Revision"]
    else:
        out["revision"] = 0
    if data.get("AccessType") is not None:
        import capo_partnercentral_account.types.access_type

        out["access_type"] = (
            capo_partnercentral_account.types.access_type.deserialize_aws_json_1_0(
                data["AccessType"]
            )
        )
    else:
        import typing

        out["access_type"] = typing.cast(
            "capo_partnercentral_account.types.access_type.AccessType", ""
        )
    if data.get("ExcludedParticipantIdentifiers") is not None:
        import capo_partnercentral_account.types.participant_identifier_list

        out["excluded_participant_identifiers"] = (
            capo_partnercentral_account.types.participant_identifier_list.deserialize_aws_json_1_0(
                data["ExcludedParticipantIdentifiers"]
            )
        )
    return out
