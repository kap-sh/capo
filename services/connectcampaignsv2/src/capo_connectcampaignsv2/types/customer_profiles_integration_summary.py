"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#CustomerProfilesIntegrationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.arn
    import capo_connectcampaignsv2.types.object_type_names_map


class CustomerProfilesIntegrationSummary(TypedDict, closed=True):
    domain_arn: "capo_connectcampaignsv2.types.arn.Arn"
    object_type_names: (
        "capo_connectcampaignsv2.types.object_type_names_map.ObjectTypeNamesMap"
    )


# --- restJson1 ser/de ---
def serialize_json(value: CustomerProfilesIntegrationSummary) -> dict:
    out: dict = {}
    out["domainArn"] = value["domain_arn"]
    import capo_connectcampaignsv2.types.object_type_names_map

    out["objectTypeNames"] = (
        capo_connectcampaignsv2.types.object_type_names_map.serialize_json(
            value["object_type_names"]
        )
    )
    return out


def deserialize_json(data: dict) -> CustomerProfilesIntegrationSummary:
    out: CustomerProfilesIntegrationSummary = {}  # type: ignore[typeddict-item]
    if data.get("domainArn") is not None:
        out["domain_arn"] = data["domainArn"]
    else:
        out["domain_arn"] = ""
    if data.get("objectTypeNames") is not None:
        import capo_connectcampaignsv2.types.object_type_names_map

        out["object_type_names"] = (
            capo_connectcampaignsv2.types.object_type_names_map.deserialize_json(
                data["objectTypeNames"]
            )
        )
    else:
        out["object_type_names"] = {}
    return out
