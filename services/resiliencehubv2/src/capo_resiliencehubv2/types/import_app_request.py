"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ImportAppRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.associated_system_list
    import capo_resiliencehubv2.types.client_token
    import capo_resiliencehubv2.types.kms_key_id
    import capo_resiliencehubv2.types.tag_map


class ImportAppRequest(TypedDict, closed=True):
    v1_app_arn: "capo_resiliencehubv2.types.arn.Arn"
    policy_arn: NotRequired["capo_resiliencehubv2.types.arn.Arn"]
    kms_key_id: NotRequired["capo_resiliencehubv2.types.kms_key_id.KmsKeyId"]
    skip_manually_added_resources: NotRequired["bool"]
    """<p>Whether to skip manually added resources during import.</p>"""
    associated_systems: NotRequired[
        "capo_resiliencehubv2.types.associated_system_list.AssociatedSystemList"
    ]
    """<p>The systems to associate with the imported service.</p>"""
    tags: NotRequired["capo_resiliencehubv2.types.tag_map.TagMap"]
    client_token: NotRequired["capo_resiliencehubv2.types.client_token.ClientToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ImportAppRequest) -> dict:
    out: dict = {}
    out["v1AppArn"] = value["v1_app_arn"]
    if "policy_arn" in value:
        out["policyArn"] = value["policy_arn"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "skip_manually_added_resources" in value:
        out["skipManuallyAddedResources"] = value["skip_manually_added_resources"]
    if "associated_systems" in value:
        import capo_resiliencehubv2.types.associated_system_list

        out["associatedSystems"] = (
            capo_resiliencehubv2.types.associated_system_list.serialize_json(
                value["associated_systems"]
            )
        )
    if "tags" in value:
        import capo_resiliencehubv2.types.tag_map

        out["tags"] = capo_resiliencehubv2.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> ImportAppRequest:
    out: ImportAppRequest = {}  # type: ignore[typeddict-item]
    if data.get("v1AppArn") is not None:
        out["v1_app_arn"] = data["v1AppArn"]
    else:
        out["v1_app_arn"] = ""
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("skipManuallyAddedResources") is not None:
        out["skip_manually_added_resources"] = data["skipManuallyAddedResources"]
    if data.get("associatedSystems") is not None:
        import capo_resiliencehubv2.types.associated_system_list

        out["associated_systems"] = (
            capo_resiliencehubv2.types.associated_system_list.deserialize_json(
                data["associatedSystems"]
            )
        )
    if data.get("tags") is not None:
        import capo_resiliencehubv2.types.tag_map

        out["tags"] = capo_resiliencehubv2.types.tag_map.deserialize_json(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: ImportAppRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
