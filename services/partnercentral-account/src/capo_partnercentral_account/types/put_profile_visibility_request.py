"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#PutProfileVisibilityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.partner_identifier
    import capo_partnercentral_account.types.profile_visibility


class PutProfileVisibilityRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier"
    """<p>The unique identifier of the partner account.</p>"""
    visibility: "capo_partnercentral_account.types.profile_visibility.ProfileVisibility"
    """<p>The visibility setting to apply to the partner profile.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutProfileVisibilityRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    import capo_partnercentral_account.types.profile_visibility

    out["Visibility"] = (
        capo_partnercentral_account.types.profile_visibility.serialize_aws_json_1_0(
            value["visibility"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> PutProfileVisibilityRequest:
    out: PutProfileVisibilityRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    if data.get("Visibility") is not None:
        import capo_partnercentral_account.types.profile_visibility

        out["visibility"] = (
            capo_partnercentral_account.types.profile_visibility.deserialize_aws_json_1_0(
                data["Visibility"]
            )
        )
    else:
        import typing

        out["visibility"] = typing.cast(
            "capo_partnercentral_account.types.profile_visibility.ProfileVisibility", ""
        )
    return out
