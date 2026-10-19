"""Generated from Smithy shape ``com.amazonaws.drs#CreateSourceNetworkRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.account_id
    import capo_drs.types.aws_region
    import capo_drs.types.tags_map
    import capo_drs.types.vpc_id


class CreateSourceNetworkRequest(TypedDict, closed=True):
    vpc_id: "capo_drs.types.vpc_id.VpcID"
    """<p>Which VPC ID to protect.</p>"""
    origin_account_id: "capo_drs.types.account_id.AccountID"
    """<p>Account containing the VPC to protect.</p>"""
    origin_region: "capo_drs.types.aws_region.AwsRegion"
    """<p>Region containing the VPC to protect.</p>"""
    tags: NotRequired["capo_drs.types.tags_map.TagsMap"]
    """<p>A set of tags to be associated with the Source Network resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSourceNetworkRequest) -> dict:
    out: dict = {}
    out["vpcID"] = value["vpc_id"]
    out["originAccountID"] = value["origin_account_id"]
    out["originRegion"] = value["origin_region"]
    if "tags" in value:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSourceNetworkRequest:
    out: CreateSourceNetworkRequest = {}  # type: ignore[typeddict-item]
    if data.get("vpcID") is not None:
        out["vpc_id"] = data["vpcID"]
    else:
        out["vpc_id"] = ""
    if data.get("originAccountID") is not None:
        out["origin_account_id"] = data["originAccountID"]
    else:
        out["origin_account_id"] = ""
    if data.get("originRegion") is not None:
        out["origin_region"] = data["originRegion"]
    else:
        out["origin_region"] = ""
    if data.get("tags") is not None:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: CreateSourceNetworkRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
